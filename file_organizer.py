import os
import shutil
import argparse

# قراءة المسار من سطر الأوامر
parser = argparse.ArgumentParser(description="Organize files by type.")
parser.add_argument("path", help="Path of the folder to organize")
args = parser.parse_args()

source_folder = args.path

file_types = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".docx", ".txt", ".doc"],
}

for folder in file_types:
    folder_path = os.path.join(source_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_folder, folder, filename))
                moved = True
                break

        if not moved:
            others_folder = os.path.join(source_folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

print("✅ Files organized successfully!")
