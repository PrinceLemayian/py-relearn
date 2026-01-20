from pathlib import Path

def scan(path):
    print("Scanning:", path)
    
    for item in path.iterdir():
        if item.is_dir():
            scan(item)
            
start_path = Path("C:/Users/Admin/Desktop/Python/test_folder")
scan(start_path)