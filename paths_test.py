from pathlib import Path

p = Path(".")

for item in p.iterdir():
    if item.is_file():
        print(item, "-> FILE")
    else:
        print(item, "-> DIR")

