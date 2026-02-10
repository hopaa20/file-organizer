import os
import shutil

# ضع هنا مسار المجلد اللي عايز ترتب الملفات فيه
source_folder = "C:/Users/Ehab/Downloads"

# أنواع الملفات والمجلدات الخاصة بها
file_types = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".docx", ".txt", ".doc"],
}

# إنشاء المجلدات لو مش موجودة
for folder in file_types:
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# نقل الملفات حسب النوع
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
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))

print("✅ Files organized successfully!")
