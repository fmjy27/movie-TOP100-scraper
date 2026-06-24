#爬取高分电影-TOP100

🎬 TMDB 高分电影 TOP100 爬虫  一个基于 Python + lxml + XPath 的实战爬虫项目，从 The Movie Database（TMDB）抓取高分电影 TOP100 的完整信息。  本项目参考 B站黑马程序员涛哥 的爬虫课程设计，通过 requests 发送请求、lxml 解析 HTML、XPath 精准定位，将网页中散落的电影数据提取为结构化 CSV 文件，非常适合爬虫新手巩固“请求 → 解析 → 存储”的完整流程。
✨ 项目特点

· 🎯 目标明确：爬取 TMDB 评分最高的 100 部电影（Top Rated）
· 🔍 解析方式：全链路使用 XPath 定位元素，训练手写路径的能力
· 📦 数据丰富：电影名、年份、上映日期、类型、时长、评分、语言、导演、编剧、标语、简介……
· 💾 持久化存储：数据保存为 CSV，可直接用于数据分析
· 🧩 分页处理：支持多页爬取（前 5 页），每页 20 条，共 100 条
· 🛡️ 基础反爬：设置 User‑Agent 模拟浏览器，避免简单拦截

---
🛠️ 技术栈

库 用途
requests 发送 HTTP 请求，获取网页源码
lxml 解析 HTML，提供 XPath 支持
re（正则） 辅助提取日期、时长等字段中的特定格式
csv 将字典数据写入 CSV 文件
📁 项目结构

```
movie_top100_scraper/
├── scraper.py                # 主爬虫脚本（包含所有函数）
├── requirements.txt          # 依赖清单
├── CSV_data/                 # 数据存储目录（自动创建）
│   └── movie_list1.csv       # 爬取结果
└── README.md
```

---

🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/movie_top100_scraper.git
cd movie_top100_scraper

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行爬虫（请确保网络可访问 TMDB）
python scraper.py
```

爬取完成后，在 CSV_data/movie_list1.csv 中查看结果。

---

📊 数据字段说明

字段 说明
电影名 影片标题（中文/英文）
年份 上映年份（括号内年份）
上映时间 具体日期（YYYY-MM-DD）
类型 多个类型，以逗号分隔
时长 电影总时长（分钟）
评分 用户评分（百分制）
语言 原始语言代码（如 en）
导演 导演姓名
作者 编剧/作者姓名
slogan类型 电影宣传标语（tagline）
简介 剧情概述

---

🧠 学习收获（参考涛哥课程）

通过完成本项目，你可以：

· ✅ 掌握 requests 库的基本用法，包括 GET/POST 请求
· ✅ 熟悉 lxml.etree 和 XPath 语法，学会从复杂 HTML 中提取数据
· ✅ 了解如何处理动态分页（第一页为静态 HTML，后续页通过 POST 请求加载）
· ✅ 练习使用正则表达式从字符串中精准提取数值（如时长中的 h/m）
· ✅ 学会将爬取结果清洗后存储为 CSV 格式，便于后续分析

---

⚠️ 注意事项 & 免责声明

· 本爬虫仅用于学习交流，请勿对 TMDB 网站发起高频请求，以免影响其正常服务。
· 建议在请求间适当增加 time.sleep()，尊重网站 robots.txt 规则。
· 如果遇到页面结构变化，需自行调整 XPath 表达式（本项目路径基于 2026 年 TMDB 页面结构）。

---

📌 下一步改进方向

· 增加 代理 IP 和 随机 User‑Agent，降低被封风险
· 改用 TMDB 官方 API（无需解析 HTML，数据更规范）
· 将数据写入 MySQL 或 MongoDB，实现持久化存储
· 结合 数据分析（如 pandas + matplotlib）可视化评分分布、导演排名等

---

🌟 如果这个项目对你有所帮助，欢迎点个 Star 支持一下！
跟着涛哥学爬虫，从模仿到创新，我们一起进步！🐍

---
 # 🎬 TMDB Top Rated Movies – TOP 100 Scraper

**A Python-based web scraping project that extracts the top 100 highest-rated movies from The Movie Database (TMDB) using XPath and lxml.**

This project follows the practical scraping course by **Mr. Tao (黑马程序员)** on Bilibili. It demonstrates the complete workflow of **sending requests → parsing HTML → storing structured data**, making it a great hands-on exercise for beginners.

---

## ✨ Features

- 🎯 **Target**: TMDB's "Top Rated" movies (Top 100)
- 🔍 **Parsing**: Full XPath navigation – good practice for writing precise selectors
- 📦 **Rich Data**: Title, year, release date, genres, runtime, rating, language, director, writers, tagline, overview...
- 💾 **Storage**: Saves results to a **CSV** file for further analysis
- 📄 **Pagination**: Crawls first 5 pages (20 items per page) to collect 100 movies
- 🛡️ **Basic Anti‑blocking**: Custom User‑Agent header to mimic a real browser

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `requests` | Send HTTP GET/POST requests |
| `lxml` | Parse HTML and evaluate XPath expressions |
| `re` (regex) | Extract specific patterns (e.g., runtime in `h`/`m`) |
| `csv` | Write scraped data to CSV files |

---

## 📁 Project Structure

```

movie_top100_scraper/
├── scraper.py                # Main script (all functions)
├── requirements.txt          # Dependencies
├── CSV_data/                 # Auto‑created folder
│   └── movie_list1.csv       # Scraped results
└── README.md

```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourname/movie_top100_scraper.git
cd movie_top100_scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python scraper.py
```

After execution, check CSV_data/movie_list1.csv for the results.

---

📊 Data Fields

Field Description
电影名 Movie title (Chinese/English)
年份 Release year
上映时间 Exact release date (YYYY-MM-DD)
类型 Genres (comma‑separated)
时长 Runtime (in minutes)
评分 User score (percentage)
语言 Original language code (e.g., en)
导演 Director(s)
作者 Writer(s) / screenwriter(s)
slogan类型 Tagline / slogan
简介 Plot overview

---

🧠 What You'll Learn

By completing this project, you will:

· ✅ Master basic requests usage (GET/POST)
· ✅ Get familiar with lxml.etree and XPath syntax for extracting data from complex HTML
· ✅ Understand how to handle pagination (static first page, POST‑based subsequent pages)
· ✅ Practice using regular expressions to extract numeric values from strings
· ✅ Learn to clean and store scraped data in CSV format

---

⚠️ Disclaimer

· This scraper is intended for educational purposes only. Do not send high‑frequency requests to TMDB, as it may affect their service.
· Consider adding time.sleep() between requests to be polite and respect robots.txt.
· XPath expressions are based on the TMDB page structure as of 2026 – you may need to update them if the site changes.

---

📌 Future Improvements

· Add proxy rotation and random User‑Agent to reduce blocking risks
· Switch to the official TMDB API (cleaner data, no HTML parsing)
· Store data in MySQL or MongoDB for persistence
· Visualize rating distributions or director rankings with pandas + matplotlib

---

🌟 If this project helps you, feel free to give it a Star!
Learn scraping with Mr. Tao, and keep coding! 🐍

```
