import os
def find_dup_filenames(folder):
    tracked_files = {}
    for dirpath, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fullpath = os.path.join(dirpath, filename)
            if filename in tracked_files:
               tracked_files[filename].append(fullpath)
            else:
              tracked_files[filename]=[fullpath]
    return tracked_files
results = find_dup_filenames(r'C:\Users\abdou\OneDrive\Desktop\TestFolder')
for filename, paths in results.items():
    if len(paths) > 1:
        print(filename)
        for path in paths:
            print("    " + path)

