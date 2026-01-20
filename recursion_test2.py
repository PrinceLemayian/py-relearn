from pathlib import Path

file_count = 0
folder_count = 0
total_size = 0

def scan(path):
    global file_count, folder_count, total_size
    
# since path.iterdir talks directly to the OS, if the folder is protected,
# is a system directory or is locked/you don't have permissions the OS throws an error
    try:
        items = list(path.iterdir())
    except PermissionError:
        print("Permission denied:", path)
        return
    
    for item in items:
        if item.is_file():
            file_count += 1
            try:
                total_size += item.stat().st_size
            except OSError: # OSError used here because file may disappear, may be locked or OS refuses metadata access during scanning
                pass  
        elif item.is_dir():
            folder_count += 1
            scan(item)
            
start_path = Path("C:/Users/Admin/Desktop/Python/test_folder")
scan(start_path)

print("Files:", file_count)
print("Folders:", folder_count)
print("Total size (bytes):", total_size)