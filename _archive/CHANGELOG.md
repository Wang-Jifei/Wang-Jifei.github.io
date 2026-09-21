# 变更日志

格式：日期 | 改动文件 | 内容 | 备份位置

## 2026-09-21 — 初始化维护机制
- 新增 `_archive/README.md`：网站结构与构建流程说明
- 新增 `_archive/CHANGELOG.md`：本变更日志
- 新增 `_archive/tools/site_tool.py`：修改前备份 + 推送前静态检查
- 网站本身文件：**未改动**（`_archive/` 不会被 Jekyll 发布）
- 基线检查：0 error；3 warning（`_layouts/keynote.html` 指向不存在的 `/tags/`，该布局未被使用）

## 2026-09-21 — About 设为主页 + 修复已发现问题
备份位置：`_archive/20260921-131307_about-as-homepage/`（含所有被修改/删除文件的旧版本）

**结构调整**
- `index.html`：内容换成原 About 页（网址 `/` 打开即个人简介），保留 Gitalk 评论（id 仍为 `about`，旧评论不丢）
- `home.html`（新增）：原首页的文章列表，网址 `/home/`（改用 `site.posts`，不再分页）
- `3-about.html`：改为跳转页，旧链接 `/3-about/` 自动跳到 `/`
- `_includes/nav.html` + `_config.yml` 新增 `nav:`：导航只显示 About / Home / Resources（顺序在 `_config.yml` 的 `nav` 中调整）
- `2-tags.html`（Blog）：不再出现在导航，但页面保留，文章里的标签链接仍可用
- `_config.yml`：`featured-tags: false`（隐藏侧边栏标签区）；注释掉 `paginate`（首页不再是文章列表）
- `_layouts/page.html`：侧边栏 “ABOUT ME” 和头像链接改指向 `/`

**问题修复**
- `_config.yml`：`url` 改为 `https://wang-jifei.github.io`；`gems:` → `plugins:`；侧边栏简介 PhD student → PhD Candidate
- About 内容：NUS 硕士日期改为 08/2020 - 08/2022（依据 CV_JF_Mar2026.pdf）；PhD student → PhD candidate；修正 “Social Meida Data Mininig” 拼写；修复未闭合的 `<p>`；论文列表改为规范的列表；按 CV 新增 Conference Presentations
- `1-resources.html`、原 About：删除失效的中英切换脚本（下拉框已被注释，该脚本每次打开都会报 JS 错误）
- Gitalk：`index.html`、`1-resources.html`、`_layouts/post.html`、`_layouts/keynote.html` 固定为 `gitalk@1.8.0`（原为 `@latest`）
- `_layouts/keynote.html`：`/tags/` 链接改为 `/2-tags/`
- `pwa/manifest.json`：名称 “BY Blog” → “Wang Jifei”
- `CNAME`：删除空文件（未使用自定义域名）
- 检查结果：0 error，0 warning

## 2026-09-21 — 导航改名：About → Home，Home → Blog
备份位置：`_archive/20260921-132040_rename-nav-home-blog/`
- `_config.yml`：`nav` 改为 Home（`/`）/ Blog（`/blog/`）/ Resources（`/1-resources/`）
- `index.html`：页面标题 About → Home（内容不变，仍是个人简介）
- `blog.html`（新增）：文章列表，网址 `/blog/`，标题 Blog
- `home.html`：改为跳转页，已上线的 `/home/` 自动跳到 `/blog/`

## 2026-09-21 — 新增 4 篇会议/活动博客
（均为新增文件，没有修改已有文件，因此无需备份）
- `_posts/2026-03-21-AAG-2026-Annual-Meeting-San-Francisco.md` + `img/post/aag2026/`（标题页、报告照片）
- `_posts/2026-05-19-CUHK-3MT-Competition-2026.md` + `img/post/3mt2026/`（海报、3MT 幻灯片、4 张照片、Google Drive 录像嵌入）
- `_posts/2026-06-25-ICPG-2026-Nanjing.md` + `img/post/icpg2026/`（标题页、会场、合影）
- `_posts/2026-07-20-Geoinformatics-2026-CPGIS-Singapore.md` + `img/post/cpgis2026/`（标题页、报告照片、NUS 照片）
- 图片处理：由 PPT 首页导出 1600px JPG；照片缩至长边 1600px（NUS 竖图 1200px），HEIC 转 JPG，并去除 EXIF（含定位信息）
- 新增 `_archive/BLOG_GUIDE.md`：修改文字/图片/视频的指南
- 新标签：Conference、Competition
- 检查结果：0 error，0 warning

## 2026-09-21 — 更换 4 篇会议博客的顶部背景图
备份位置：`_archive/20260921-151452_header-images/`（4 篇文章旧版）
- 新增背景图（长边 1920px，去除 EXIF）：`img/post/3mt2026/3mt-header.jpg`（3MT-all00）、`img/post/aag2026/aag-header.jpg`（AAG-scene）、`img/post/icpg2026/icpg-header.jpg`（ICPG-NJU）、`img/post/cpgis2026/cpgis-header.jpg`（CPGIS-SCENE）
- 4 篇文章的 `header-img` 改为上述图片；背景图不出现在正文中
- CPGIS 文章正文末尾新增与硕士导师合影 `img/post/cpgis2026/cpgis-master-supervisor.jpg`
- 检查结果：0 error，0 warning
