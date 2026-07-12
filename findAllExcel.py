import os 
import openpyxl
def find_in_excel(search_text):
    results = {}
    for filename in os.listdir('.'):
        if filename.endswith('.xlsx'):
            wb = openpyxl.load_workbook(filename, data_only=True)
            ws= wb.active
            for rowOfCellObjects in ws.rows:
                for cellObj in rowOfCellObjects:
                    if search_text.lower() in str(cellObj.value).lower():
                        if filename not in results:
                            results[filename] =[]
                        results[filename].append(cellObj.coordinate)
    return results
print(find_in_excel("name"))
