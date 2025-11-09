# MangaScraper
MangaPark Scraper 🐾

A production-ready Python scraper for MangaPark
 that allows you to download manga chapters as PDFs with minimal setup. This scraper supports chapter selection by index, chapter number, range, or title substring, and can handle images with alpha channels.

Features

Fetch all chapters of a manga cleanly, removing misleading “Most Likes” or “Newly Added” entries.

Select chapters by:

Chapter number (e.g., 138)

Index (1..N)

Range (e.g., 1-5, 10-12)

Title substring (e.g., "Black Wolf")

Download images synchronously or asynchronously.

Convert downloaded chapters into PDF files.

Optional Playwright fallback for dynamic pages (requires extra setup).

Compatible with Python 3.11+.

Usage
# Download all chapters of a manga from its URL
python mangapark_scraper.py "https://mangapark.io/title/127529-en-the-lazy-lord-masters-the-sword"

# Download specific chapters
python mangapark_scraper.py "naruto" -c "138"        # By chapter number
python mangapark_scraper.py "naruto" -c "1-3,5"      # By index range
python mangapark_scraper.py "naruto"                 # Interactive selection

Dependencies
pip install requests beautifulsoup4 aiohttp img2pdf pillow tqdm pyyaml
# If using Playwright
pip install playwright
playwright install

Notes

PDFs are saved in a per-title folder.

Metadata saving is disabled by default
