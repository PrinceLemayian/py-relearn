from pathlib import Path

file_count = 0
folder_count = 0

def scan(path):
    global file_count, folder_count
    
    for item in path.iterdir():
        if item.is_file():
            file_count += 1
        elif item.is_dir():
            folder_count += 1
            scan(item)
            
start_path = Path("C:/Users/Admin/Desktop/Python/test_folder")
scan(start_path)

print("Files:", file_count)
print("Folders:", folder_count)