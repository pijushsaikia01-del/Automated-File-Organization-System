import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"]
}

def organize_folder(source_folder):
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    total_files = len(files)

    if total_files == 0:
        return

    progress["maximum"] = total_files

    for i, file in enumerate(files, start=1):
        file_path = os.path.join(source_folder, file)

        moved = False

        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                move_file(file, file_path, source_folder, folder)
                moved = True
                break

        if not moved:
            move_file(file, file_path, source_folder, "Others")

        # Update progress bar
        progress["value"] = i
        root.update_idletasks()

def move_file(file, file_path, source_folder, category):
    file_time = os.path.getmtime(file_path)
    year = time.strftime("%Y", time.localtime(file_time))

    target_folder = os.path.join(source_folder, category, year)
    os.makedirs(target_folder, exist_ok=True)

    target_path = get_unique_name(target_folder, file)
    shutil.move(file_path, target_path)

def get_unique_name(folder, file):
    target_path = os.path.join(folder, file)

    if not os.path.exists(target_path):
        return target_path

    base, ext = os.path.splitext(file)
    count = 1

    while True:
        new_name = f"{base}_{count}{ext}"
        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        count += 1

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        try:
            organize_folder(folder)
            messagebox.showinfo("Success", "Files organized successfully!")
            progress["value"] = 0
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("350x200")

label = tk.Label(root, text="File Organizer", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(root, text="Select Folder", command=select_folder)
btn.pack(pady=10)


progress = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
progress.pack(pady=20)

root.mainloop()