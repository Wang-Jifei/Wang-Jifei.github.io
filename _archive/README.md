# 网站结构与维护说明（_archive/README.md）

> `_archive/` 以下划线开头，Jekyll 不会发布它；这里只存放备份、变更日志和维护脚本，不影响线上网站。

## 1. 技术栈与构建流程
- 模板：Hux Blog → BY Blog → klovien 的 Fork（Jekyll 3 + Bootstrap 3 + jQuery）
- 托管：GitHub Pages，分支 `master`，push 后由 GitHub 自动执行 `jekyll build`（github-pages gem，Jekyll 3.x）
- 插件：`jekyll-paginate`（已停用分页：`paginate` 被注释）；Markdown：kramdown（GFM 输入）+ rouge 高亮
- 流程：`_config.yml` 全局变量 → 页面/文章 front matter 选择 layout → layout 套 `default.html` → `default.html` 拼接 `head.html` + `nav.html` + 内容 + `footer.html` → 输出 `_site/`
- 永久链接：`permalink: pretty` → `3-about.html` 发布为 `/3-about/`；文章发布为 `/YYYY/MM/DD/标题/`

## 2. 文件结构
| 路径 | 作用 |
|---|---|
| `_config.yml` | 站点标题、描述、头图、侧边栏头像与简介、Gitalk 评论、友情链接（friends）、分页等全局配置 |
| `index.html` | 网站主页 `/`：个人简介（原 About 内容）、教育、研究兴趣、论文、会议报告、CV 下载、Gitalk 评论 |
| `home.html` | 导航 “Home” → `/home/`：列出全部 `_posts` 文章 |
| `1-resources.html` | 导航 “Resources”：期刊/数据/工具链接 |
| `2-tags.html` | 标签归档页 `/2-tags/`（已从导航隐藏，仅供文章标签链接使用） |
| `3-about.html` | 跳转页：`/3-about/` → `/` |
| `404.html` / `offline.html` | 404 页与 PWA 离线页 |
| `feed.xml` | RSS（`RSS: false`，入口隐藏但文件仍生成） |
| `_layouts/default.html` | 根骨架：head + nav + content + footer |
| `_layouts/page.html` | 带头图的页面 + 右侧边栏（Featured Tags / About Me / More Sites） |
| `_layouts/post.html` | 文章页：头图、标签、上一篇/下一篇、Gitalk、目录（catalog） |
| `_layouts/keynote.html` | 幻灯片式文章布局（当前未使用） |
| `_includes/head.html` | `<head>`：SEO 标题、CSS、favicon、manifest、canonical |
| `_includes/nav.html` | 顶部导航：按 `_config.yml` 里的 `nav:` 列表生成（当前 About / Home / Resources） |
| `_includes/footer.html` | 页脚社交链接、版权；加载 jQuery/Bootstrap/hux-blog.js、Service Worker、标签云、目录、统计脚本 |
| `_posts/` | 文章（文件名须为 `YYYY-MM-DD-标题.md`） |
| `css/` `js/` `fonts/` | 编译后的静态资源（`hux-blog.min.css` 由 `less/` 经 Grunt 生成；直接改 css 需同时改 `.css` 和 `.min.css`） |
| `less/` `Gruntfile.js` `package.json` | 样式源文件与构建脚本（已在 exclude 中，不发布） |
| `img/` `img/post/` | 头图、头像、文章图片 |
| `files/` | CV 等 PDF（About 页当前链接 `files/CV_JF_Mar2026.pdf`） |
| `sw.js` `pwa/` | Service Worker 与 PWA manifest |

## 3. 修改规范（每次修改都遵循）
1. 修改前备份：`python3 _archive/tools/site_tool.py backup <标签> <文件...>` → 旧版本存到 `_archive/<时间戳>_<标签>/`
2. 修改文件（只改项目文件夹内的文件）
3. 推送前检查：`python3 _archive/tools/site_tool.py check`（YAML、layout、Liquid 闭合、本地链接/图片是否存在）
4. 在 `_archive/CHANGELOG.md` 记录本次改动
5. push 后在 GitHub 仓库 Actions 页查看 “pages build and deployment” 是否成功
