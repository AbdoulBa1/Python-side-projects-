# Python-side-projects I am working  on over this summer -
A collection of Python scripts exploring various concepts — math, string manipulation, games, patterns, file utilities, and more.

---

## 🚀 How to Run

All scripts are standalone. No installs needed — they only use Python's built-in libraries.

**Option 1 – Run in terminal:**
```bash
python filename.py
```

**Option 2 – Copy & paste into VS Code**, then hit Run

**Option 3 – Call a function directly:**
```python
from arthemeticFuinctions import multiply
print(multiply(4, 5))  # Output: 20
```

> 💡 Scripts using `random` will produce different results each run — that's intentional!

---

## 📂 Categories

---

### 🔢 Math & Logic

| File | Description | Libraries |
|------|-------------|-----------|
| `arthemeticFuinctions.py` | Add and multiply positive numbers using only loops — no `+` or `*` operators | None |
| `fizzBuzzNumber.py` | Enter a number; prints Fizz, Buzz, FizzBuzz, or the number itself | None |
| `perimeterAreaCalculator.py` | Enter width and length to calculate a rectangle's area and perimeter | None |
| `total_sum.py` | Adds numbers 1–100 and prints the running total at each step | None |
| `Transaction_Tracker.py` | Checks if a bank transaction would bring the balance below zero before applying it | None |

---

### 🌡️ Weather & Data

| File | Description | Libraries |
|------|-------------|-----------|
| `avgTemp.py` | Generates 100 random weather readings and calculates the average temperature | `random` |
| `weatherDataGen.py` | Generates 100 random weather data entries (temp, humidity, pressure, feels-like) | `random` |
| `weather_information.py` | Prompts user to manually enter hourly weather data and stores it in a list | None |
| `SafeTemp.py` | Enter a temperature in C or F; tells you if it's a safe human body temperature | None |
| `safeTemp_Expr.py` | Same as SafeTemp but written with a single combined if-expression | None |

---

### 🎮 Games & Interactive

| File | Description | Libraries |
|------|-------------|-----------|
| `wordMatchGame.py` | Wordle-style game — guess a 5-letter word in 6 tries; get O/o/x hints | `random` |
| `coordinateDirections.py` | Enter N/S/E/W moves one at a time; outputs your final (x, y) coordinate | None |
| `restaurant_reservation.py` | Add a customer name and time to a reservation system; detects conflicts | None |

---

### 🔤 String & Text Tools

| File | Description | Libraries |
|------|-------------|-----------|
| `mockingSpongebob.py` | Converts any text to aLtErNaTiNg CaPs (mocking Spongebob meme) | None |
| `panagramDetector.py` | Checks if a sentence is a pangram (uses all 26 letters of the alphabet) | None |
| `laugh_Score.py` | Scores how long a laugh is — "hahaha" scores 6, "ha ha ha" scores 2 | `re` |
| `wordTwister.py` | Twists words by moving the last letter to the front using regex | `re` |

---

### 🔍 Regex Tools

| File | Description | Libraries |
|------|-------------|-----------|
| `hashtagRegex.py` | Extracts all hashtags from a sentence (e.g. `#python #code`) | `re` |
| `priceRegex.py` | Extracts all prices from a sentence (e.g. `$9.99`, `$100`) | `re` |

---

### ♟️ Chess

| File | Description | Libraries |
|------|-------------|-----------|
| `rookCapture.py` | Given a white rook's position and a board, returns all black pieces it can capture | None |

---

### 🎨 Patterns & Visuals

| File | Description | Libraries |
|------|-------------|-----------|
| `rectPrint.py` | Prints a rectangle of `0`s with a user-defined width | None |
| `diagStripe.py` | Animated diagonal stripe pattern that loops forever in the terminal | `time` |
| `Treeprint.py` | Prints an ASCII triangle tree with a trunk using a `for` loop | None |
| `Treeprint2.py` | Same tree as Treeprint but built with `while` loops | None |
| `xmasTreeprint.py` | Christmas tree with random `o` ornaments using a `for` loop | `random` |
| `xmasTreeprint2.py` | Same Christmas tree but built with `while` loops | `random` |

---

### 🗂️ File Utilities

| File | Description | Libraries |
|------|-------------|-----------|
| `dupFilename.py` | Scans a folder and all subfolders to find duplicate filenames | `os` |
| `alphaFolder.py` | Auto-generates an A–Z / AA–ZZ folder structure at a given path | `os`, `string` |

---

### 📦 Data Structures

| File | Description | Libraries |
|------|-------------|-----------|
| `Nested_dic_list.py` | Baseball score tracker using a nested dictionary (Home/Visitor by inning) | None |

---

### ⏱️ Timing

| File | Description | Libraries |
|------|-------------|-----------|
| `tickTock.py` | Prints "Tick" and "Tock" alternately every second for 10 seconds | `time` |

---
### 📊 Excel Automation

| File | Description | Libraries |
|------|-------------|-----------|
| `strike_test.py` | Creates a workbook and applies strikethrough font styling to a cell using `Font` | `openpyxl` |
| `findAllExcel.py` | Searches every `.xlsx` file in the current folder for a case-insensitive text match, returns matching cell addresses | `openpyxl`, `os` |
| `homeFilesReportExcel.py` | Scans the user's home folder and generates an Excel report listing every file and its size in bytes | `openpyxl`, `os`, `pathlib` |

---
## 📈 Google Sheets Automation

Automating Google Sheets with the `ezsheets` module — uploading, downloading, and syncing spreadsheet data via the Google Sheets and Drive APIs.

| Project | Description |
|---|---|
| `uploadAllSpreadsheets.py` | Searches the current working directory for all `.xlsx` and `.csv` files and uploads each one to Google Sheets, printing progress as it goes |
| `homeFilesReportGoogleSheets.py` | Scans the home folder, finds the 100 largest files by size, and writes a "Home Files Report" spreadsheet to Google Sheets with filenames in column A and file sizes in column B |

**Skills practiced:** OAuth2 authentication flow, Google Cloud Console API setup (Sheets + Drive APIs), `os.listdir()` file filtering, `Path.stat()` for file sizes, `.sort()` with `key=lambda` for custom sorting, list slicing, working directory vs. script location debugging, EZSheets object model (`Spreadsheet`, `Sheet`, `.title`, `.url`, `.sheets`), `sheet.updateRow()`, protecting OAuth credentials with `.gitignore`
## 🛠️ Requirements

- Python 3.x
- - `openpyxl` (install with `pip install openpyxl`) — required for the Excel Automation scripts
- No external packages needed — all libraries (`random`, `re`, `os`, `time`, `string`,`) are built into Python
