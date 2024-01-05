import os
import shutil

source_folder = "path/to/your/source/folder"  # Replace with the actual path to your source folder

destination_folders = {
    "images": "path/to/images/folder",
    "pdfs": "path/to/pdfs/folder",
    "videos": "path/to/videos/folder"
}

for folder_name, destination_folder in destination_folders.items():
    os.makedirs(destination_folder, exist_ok=True)  # Create folders if they don't exist

for filename in os.listdir(source_folder):
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in [".jpg", ".jpeg", ".png", ".gif"]:
        destination = destination_folders["images"]
    elif file_extension == ".pdf":
        destination = destination_folders["pdfs"]
    elif file_extension in [".mp4", ".mov", ".avi", ".wmv"]:
        destination = destination_folders["videos"]
    else:
        continue  # Skip other file types

    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination, filename)
    
    print(f"Moving '{source_file}' to '{destination_file}'")
    
    # Check if the source file exists before moving
    if os.path.exists(source_file):
        try:
            shutil.move(source_file, destination_file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
    else:
        print(f"Source file '{source_file}' does not exist. Skipping.")

print("Files separated successfully!")
