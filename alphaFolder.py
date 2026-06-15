import os
import string
def make_alpha_folders(root_folder):
    for letter in string.ascii_uppercase:
        for letter2 in string.ascii_uppercase:
                print(letter + letter2) 
                sub_folder = os.makedirs(os.path.join(root_folder, letter, letter + letter2) , exist_ok=True)
root_folder = r'C:\Users\abdou\OneDrive\Desktop\Alpha Test File'
make_alpha_folders(root_folder)

