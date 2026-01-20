from pathlib import Path

file_count = 0
folder_count = 0
total_size = 0
files_by_extension = {}
largest_files = []

def scan(path):
    global file_count, folder_count, total_size, files_by_extension
    
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
            
            # file size functionality
            try:
                size = item.stat().st_size
                total_size += size
            except OSError: # OSError used here because file may disappear, may be locked or OS refuses metadata access during scanning
                continue 
            
            # track largest files
            largest_files.append((item, size))
            
            # file extension functionality
            extension = item.suffix.lower()
            if extension == "":
                extension = "NO_EXTENSION"
            files_by_extension[extension] = files_by_extension.get(extension, 0) + 1
                
        elif item.is_dir():
            folder_count += 1
            scan(item)
            
start_path = Path("C:/Users/Admin/Desktop/Python/test_folder")
scan(start_path)

print("Files:", file_count)
print("Folders:", folder_count)
print("Total size (bytes):", total_size)
print("\nFiles by extension:")
for extension, count in files_by_extension.items():
    print(extension, "->", count)

# sort and get top 5
largest_files.sort(key=lambda x: x[1], reverse=True)
top5 = largest_files[:5]

print("\nLargest 5 files:")
for file, size in top5:
    print(f"{file} -> {size} bytes")

