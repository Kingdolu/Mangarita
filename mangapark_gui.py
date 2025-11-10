import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os
from mangapark_scraper import MangaParkScraper, Config
from mangapark_scraper import MangaParkScraper, Config, sanitize_filename


# --- Initialize scraper ---
scraper = MangaParkScraper(Config())
chapters = []
manga_title = ""

# --- Functions ---
def fetch_chapters():
    global chapters, manga_title
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input error", "Paste a manga URL first!")
        return
    try:
        manga_title, chapters = scraper.fetch_all_chapters(url)
        listbox.delete(0, tk.END)
        for c in chapters:
            ch_num = c.chapter_number if c.chapter_number is not None else c.index
            listbox.insert(tk.END, f"{ch_num}: {c.title}")
        messagebox.showinfo("Success", f"Found {len(chapters)} chapters for {manga_title}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_selected_thread():
    threading.Thread(target=download_selected, daemon=True).start()

def download_selected():
    global chapters, manga_title
    if not chapters:
        messagebox.showwarning("No chapters", "Fetch chapters first!")
        return

    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("No selection", "Select chapters from the list first.")
        return

    selected = [chapters[i] for i in selected_indices]

    # Prepare output directory
    safe_title = sanitize_filename(manga_title)
    output_dir = os.path.join("./downloads", safe_title)
    os.makedirs(output_dir, exist_ok=True)

    total = len(selected)
    progress_bar["maximum"] = total
    progress_bar["value"] = 0

    messagebox.showinfo("Download started", f"Downloading {total} chapter(s)...")

    for i, ch in enumerate(selected, start=1):
        try:
            scraper.chapter_to_pdf(ch, output_dir)
        except Exception as e:
            print(f"Failed to download {ch.title}: {e}")
        progress_bar["value"] = i
        progress_label.config(text=f"Downloading {i}/{total}")
        root.update_idletasks()

    messagebox.showinfo("Done", f"Downloaded {total} chapter(s) successfully!")

def download_range_thread():
    threading.Thread(target=download_range, daemon=True).start()

def download_range():
    global chapters, manga_title
    if not chapters:
        messagebox.showwarning("No chapters", "Fetch chapters first!")
        return

    range_text = range_entry.get().strip()
    if not range_text:
        messagebox.showwarning("Input error", "Enter a chapter range (e.g. 1-5)")
        return

    try:
        start, end = [float(x.strip()) for x in range_text.split('-')]
    except:
        messagebox.showerror("Error", "Invalid range format. Use e.g. 1-5 or 12.5-14")
        return

    selected = []
    for ch in chapters:
        ch_num = ch.chapter_number if ch.chapter_number is not None else ch.index
        if start <= float(ch_num) <= end:
            selected.append(ch)

    if not selected:
        messagebox.showinfo("No match", "No chapters found in that range.")
        return

    # Prepare output directory
    safe_title = sanitize_filename(manga_title)
    output_dir = os.path.join("./downloads", safe_title)
    os.makedirs(output_dir, exist_ok=True)

    total = len(selected)
    progress_bar["maximum"] = total
    progress_bar["value"] = 0

    messagebox.showinfo("Download started", f"Downloading {total} chapters...")

    for i, ch in enumerate(selected, start=1):
        try:
            scraper.chapter_to_pdf(ch, output_dir)
        except Exception as e:
            print(f"Failed to download {ch.title}: {e}")
        progress_bar["value"] = i
        progress_label.config(text=f"Downloading {i}/{total}")
        root.update_idletasks()

    messagebox.showinfo("Done", f"Downloaded {total} chapters successfully!")

# --- Tkinter UI ---
root = tk.Tk()
root.title("MangaPark Downloader")

tk.Label(root, text="Manga URL:").pack(pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack()

tk.Button(root, text="Fetch Chapters", command=fetch_chapters).pack(pady=5)

tk.Label(root, text="Available Chapters:").pack()
listbox = tk.Listbox(root, width=70, height=12, selectmode=tk.MULTIPLE)
listbox.pack()

tk.Button(root, text="Download Selected", command=download_selected_thread).pack(pady=5)

tk.Label(root, text="Chapter Range (e.g. 1-5):").pack(pady=5)
range_entry = tk.Entry(root, width=20)
range_entry.pack()

tk.Button(root, text="Download Range", command=download_range_thread).pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)
progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
