#!/usr/bin/env python3
"""Maintenance helper for this Jekyll / GitHub Pages site.

  python3 _archive/tools/site_tool.py backup <label> <file> [file ...]
      Copy the current version of each file into _archive/<YYYYMMDD-HHMMSS>_<label>/
      (paths preserved) BEFORE editing it.

  python3 _archive/tools/site_tool.py check
      Static pre-push check (no Jekyll needed): _config.yml YAML, front matter YAML,
      layouts exist, Liquid block balance, local asset/link targets exist.

Folders starting with "_" are never published by Jekyll, so _archive/ is safe.
"""
import os, re, sys, shutil, datetime
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP_DIRS = {".git", "_site", "_archive", "node_modules", ".jekyll-cache", ".claude", "less", "fonts"}
PAIRS = {"if": "endif", "unless": "endunless", "for": "endfor", "case": "endcase",
         "capture": "endcapture", "comment": "endcomment", "raw": "endraw", "highlight": "endhighlight"}
CLOSERS = {v: k for k, v in PAIRS.items()}


def backup(label, files):
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    dest_root = os.path.join(ROOT, "_archive", f"{stamp}_{label}")
    for f in files:
        src = os.path.join(ROOT, f)
        if not os.path.isfile(src):
            print(f"[new file, nothing to back up] {f}")
            continue
        dst = os.path.join(dest_root, f)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"[backed up] {f} -> _archive/{stamp}_{label}/{f}")
    print(dest_root)


def split_front_matter(text):
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        return "BROKEN", text
    return m.group(1), text[m.end():]


def site_files():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            if f.endswith((".html", ".md", ".xml")):
                yield os.path.join(d, f)


def check():
    errs, warns = [], []
    try:
        cfg = yaml.safe_load(open(os.path.join(ROOT, "_config.yml"), encoding="utf-8"))
    except Exception as e:
        print("ERROR _config.yml:", e); return 1
    layouts = {os.path.splitext(x)[0] for x in os.listdir(os.path.join(ROOT, "_layouts"))}
    includes = set(os.listdir(os.path.join(ROOT, "_includes")))
    for path in site_files():
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8", errors="replace").read()
        fm, body = split_front_matter(text)
        if fm == "BROKEN":
            errs.append(f"{rel}: front matter not closed with ---"); continue
        meta = {}
        if fm is not None:
            try:
                meta = yaml.safe_load(fm) or {}
            except Exception as e:
                errs.append(f"{rel}: front matter YAML error: {e}"); continue
            lay = meta.get("layout")
            if lay and lay not in ("null", None) and lay not in layouts:
                errs.append(f"{rel}: layout '{lay}' not found in _layouts/")
            hi = meta.get("header-img")
            if hi and not hi.startswith("http") and not os.path.exists(os.path.join(ROOT, hi.lstrip("/"))):
                errs.append(f"{rel}: header-img '{hi}' does not exist")
        if rel.startswith("_posts") and not re.match(r"_posts/\d{4}-\d{2}-\d{2}-", rel):
            errs.append(f"{rel}: post filename must start with YYYY-MM-DD-")
        # Liquid balance (skip inside raw)
        stack = []
        for m in re.finditer(r"{%-?\s*(\w+)", text):
            tag = m.group(1)
            if stack and stack[-1] in ("raw", "comment") and tag != PAIRS[stack[-1]]:
                continue
            if tag in PAIRS:
                stack.append(tag)
            elif tag in CLOSERS:
                if not stack or stack[-1] != CLOSERS[tag]:
                    errs.append(f"{rel}: unexpected {{% {tag} %}} (line {text[:m.start()].count(chr(10))+1})")
                else:
                    stack.pop()
            elif tag == "include":
                inc = re.match(r"{%-?\s*include\s+([\w.\-/]+)", text[m.start():])
                if inc and inc.group(1) not in includes:
                    errs.append(f"{rel}: include '{inc.group(1)}' not found")
        if stack:
            errs.append(f"{rel}: unclosed Liquid block(s): {stack}")
        # local link / asset targets
        plain = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        plain = re.sub(r"{{\s*site\.baseurl\s*}}", "", plain)
        cands = re.findall(r'(?:src|href)\s*=\s*["\'](/[^"\'#?{}]+)', plain)
        cands += re.findall(r'!\[[^\]]*\]\((/[^)\s#?]+)', plain)
        cands += re.findall(r'\{\{\s*["\'](/[^"\']+?)\s*["\']\s*\|\s*prepend', plain)
        for c in cands:
            c = c.strip()
            if c.startswith("//"):
                continue  # protocol-relative external URL
            p = os.path.join(ROOT, c.lstrip("/"))
            if os.path.exists(p) or os.path.exists(p.rstrip("/") + ".html") or os.path.exists(os.path.join(p, "index.html")):
                continue
            if re.match(r"^/\d-[\w-]+/?$", c) or c in ("/",):
                continue  # page permalinks (pretty)
            warns.append(f"{rel}: local target not found: {c}")
    for e in errs: print("ERROR  ", e)
    for w in warns: print("WARN   ", w)
    print(f"\n{len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "check":
        sys.exit(check())
    if len(sys.argv) >= 4 and sys.argv[1] == "backup":
        backup(sys.argv[2], sys.argv[3:]); sys.exit(0)
    print(__doc__); sys.exit(2)
