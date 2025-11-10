# MangaScraper

MangaPark Scraper 🐾

A Python-based MangaPark scraper with a GUI for easy downloading of manga chapters. Originally terminal-based, now upgraded with a Tkinter interface for selecting chapters and monitoring download progress.

Features

Fetch all chapters from a MangaPark manga URL.

GUI interface using Tkinter:

Input field for the manga URL.

List of available chapters for single or multiple selection.

Input field to download a range of chapters (supports fractional chapters like 34.5).

Progress bar showing real-time download progress.

Downloads chapters as PDFs.

Downloads are saved to a per-manga folder:
./downloads/<MANGA_TITLE>/

Supports async image downloading for faster downloads.

Handles chapters with fractional numbers (e.g., 34.5) correctly.

Optional debug logging.

Requirements

Python 3.11+

Dependencies:

pip install requests beautifulsoup4 playwright img2pdf aiohttp tqdm pyyaml pillow
playwright install  # if using Playwright fallback

Usage
Terminal Mode
python mangapark_scraper.py "https://mangapark.io/title/127529-en-the-lazy-lord-masters-the-sword"


Optional arguments:

-o, --output : Output directory (default: current folder)

-c, --chapters : Chapter selection (e.g., 1-3, 5, Black Wolf, all)

--no-async : Disable async downloads

--debug : Enable debug logging

GUI Mode

Run:

python mangapark_gui.py


Steps:

Paste the MangaPark URL in the URL field.

Click Fetch Chapters to load all chapters.

Option 1 – Download Selected Chapters:

Highlight chapters in the list.

Click Download Selected to download only those chapters.

Option 2 – Download Range:

Enter a chapter range (e.g., 1-5 or 12.5-14) in the Range field.

Click Download Range to download all chapters in that range.

Monitor progress with the progress bar and status label.

Downloads are saved in ./downloads/<MANGA_TITLE>/.

Notes

Fractional chapters (e.g., 34.5) are supported in both GUI range input and terminal selections.

Downloaded PDFs are named Chapter_001.pdf, Chapter_002.pdf, etc., with zero-padding.

GUI uses threading to keep the interface responsive during downloads.

Both single/multi selection and range download can be used simultaneously.

License

MIT License — free to use and modify.r-title folder.

Metadata saving is disabled by default
