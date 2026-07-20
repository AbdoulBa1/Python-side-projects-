import os
import ezsheets
from pathlib import Path
def get_home_folder_size():
    filenames_and_sizes =[]
    for filename in os.listdir(Path.home()):
        absolute_file_path = Path.home() / filename

        if absolute_file_path.is_dir():
            continue
        try:
            file_size = absolute_file_path.stat().st_size
        except Exception:
            continue

    filenames_and_sizes.append((filename, file_size))
    filenames_and_sizes.sort(key=lambda item: item[1], reverse=True)
    filenames_and_sizes=filenames_and_sizes[:100]
    return filenames_and_sizes
def make_google_sheets_report(filenames_and_sizes):
    ss = ezsheets.createSpreadsheet('Home Files Report')
    sheet = ss[0]
    for row, (filename, size) in enumerate(filenames_and_sizes, start=1):
        sheet.updateRow(row, [filename, size])
    print(f"Google Sheets report created: {ss.url}")
make_google_sheets_report(get_home_folder_size())



    
