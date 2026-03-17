Automated File Organization System

Description

A Python-based desktop application that automatically organizes files into structured folders based on file type and modification date. The application provides a graphical user interface and real-time progress tracking for efficient file management.

---

Features

* Automatic file sorting by type (Images, Documents, Videos, Music, etc.)
* Organization based on modification year
* Graphical user interface using Tkinter
* Real-time progress bar for tracking operations
* Duplicate file handling to prevent overwriting
* Standalone executable (.exe) support

---

Technologies Used

* Python
* Tkinter (GUI)
* OS and Shutil (File Handling)
* PyInstaller (Executable creation)

---

How to Run

Option 1: Run using Python

python organizer.py


Option 2: Run as Application
Open the executable file from the `dist` folder

---

Project Structure

```
FileOrganizer/
│── organizer.py
│── screenshot.png
│── dist/
│   └── organizer.exe
```

---

How It Works

1. Select a folder using the graphical interface
2. The program scans all files in the selected directory
3. Files are categorized based on type
4. Files are further organized into folders by year
5. Progress bar updates during execution

---

Screenshots
1. Test Folder.png
2. GUI.png
3. Output 1.png
4. Output 2.png
5. Output 3.png

---

Future Improvements

* Drag and drop support
* Dark mode interface
* File preview before organizing
* AI-based file classification

---

Author

Developed as part of an internship project demonstrating automation, GUI development, and file handling using Python.
