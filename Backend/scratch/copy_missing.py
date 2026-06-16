import shutil
import os

src_base = r'c:\Users\hp\Desktop\eqosy\Frontend\src'
dest_base = r'c:\Users\hp\Desktop\SuperFast\Frontend\src'

folders_to_copy = [
    'shared',
    'services',
    'modules/shared'
]

print("Copying missing directories from eqosy to SuperFast...")

for folder in folders_to_copy:
    src_folder = os.path.join(src_base, folder)
    dest_folder = os.path.join(dest_base, folder)
    
    if os.path.exists(src_folder):
        if os.path.exists(dest_folder):
            shutil.rmtree(dest_folder)
        shutil.copytree(src_folder, dest_folder)
        print(f"Successfully copied: {folder}")
    else:
        print(f"Source folder does not exist: {src_folder}")

print("Copy finished.")
