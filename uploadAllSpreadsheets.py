import os
import ezsheets
def upload_all_spreadsheets():
        for filename in os.listdir('.'):
             if filename.endswith('.xlsx') or filename.endswith('.csv'):
                print(f"Uploading {filename} ...")
                ezsheets.upload(filename)
upload_all_spreadsheets()

