import os
import shutil


#folder pathe you want to organize
FOLDER_PATH = os.getcwd()  # Current working directory

#File type mapping to their respective folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Applications": [".exe", ".msi", ".apk"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".html", ".css", ".sql"],
}
#Create folders for each file type if they don't exist
for folder_name in FILE_TYPES:
    folder_path = os.path.join(FOLDER_PATH, folder_name)#
    if not os.path.exists(folder_path):
        os.makedirs(folder_path) 

#Organize files

for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

#Skip the folder
    if os.path.isdir(file_path):
        continue

    #get file extension
    #print(os.path.splitext(file))
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
           shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files have been organized successfully. ✅")