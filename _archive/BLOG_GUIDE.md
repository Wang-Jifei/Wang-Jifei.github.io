# Blog 修改指南

## 1. 文章在哪里
所有文章都在 `_posts/` 文件夹，一篇文章一个 `.md` 文件。2026 年新增的四篇：

| 文章 | 文件 | 图片文件夹 |
|---|---|---|
| AAG 2026（旧金山） | `_posts/2026-03-21-AAG-2026-Annual-Meeting-San-Francisco.md` | `img/post/aag2026/` |
| CUHK 3MT 2026 | `_posts/2026-05-19-CUHK-3MT-Competition-2026.md` | `img/post/3mt2026/` |
| ICPG 2026（南京） | `_posts/2026-06-25-ICPG-2026-Nanjing.md` | `img/post/icpg2026/` |
| Geoinformatics 2026 / CPGIS（新加坡） | `_posts/2026-07-20-Geoinformatics-2026-CPGIS-Singapore.md` | `img/post/cpgis2026/` |

文件名开头的日期（YYYY-MM-DD）决定文章网址和在 Blog 页的排序，改文件名会改网址。

## 2. 文章开头的设置（两行 `---` 之间）
```
title:      页面大标题
subtitle:   标题下方小字
date:       2026-03-21          # 显示的日期；未来日期的文章不会显示
header-img: img/post/aag2026/aag-presentation.jpg   # 顶部背景图（前面不要加 /）
header-mask: 0.4                # 背景图变暗程度，0 不变暗，0.6 很暗
tags:
    - Conference                # 标签，可写多个
```

## 3. 修改文字
直接改 `---` 以下的正文，用 Markdown 写法：
- `### 标题`、`#### 小标题`（会自动生成右侧目录 CATALOG）
- `**粗体**`、`*斜体*`
- `- 列表项`
- 链接：`[显示文字](https://网址)`

## 4. 更换或添加图片
1. 把图片放进对应的图片文件夹，例如 `img/post/aag2026/new-photo.jpg`
2. 在正文中需要的位置写两行：
   ```
   ![图片说明](/img/post/aag2026/new-photo.jpg)
   *图片下方的说明文字*
   ```
   注意：正文里的图片路径**以 `/` 开头**；而开头设置里的 `header-img` **不加 `/`**。
3. 删除某张图：删掉对应的这两行即可（图片文件可保留）。
4. 替换图片：用同名文件覆盖即可，正文不用改。
5. 建议：图片长边 1600px 左右、单张小于 500KB；文件名用英文小写和连字符，不要用空格和中文；GitHub 区分大小写（`.JPG` ≠ `.jpg`）。

缩小图片（Mac 自带命令）：
```
sips -Z 1600 原图.jpg --out img/post/aag2026/new-photo.jpg
```
iPhone 的 HEIC 照片先在“预览”里导出为 JPEG，或用：
```
sips -s format jpeg -Z 1600 照片.HEIC --out img/post/cpgis2026/photo.jpg
```

## 5. 3MT 视频
3MT 文章里的 `<iframe src=".../preview">` 是 Google Drive 视频播放器。换视频时，把两处链接中的文件 ID（`/d/` 和 `/preview` 之间那串字符）换成新的 ID。Google Drive 文件需设置为“知道链接的任何人可查看”，否则访客看不到。

## 6. 新增一篇文章
复制一篇现有文章，改文件名日期和标题，再改开头设置和正文；图片放进新建的 `img/post/<名称>/` 文件夹。

## 7. 推送前
```
python3 _archive/tools/site_tool.py check
```
显示 0 error 再 push；若提示 `local target not found`，说明图片路径或文件名写错了。
