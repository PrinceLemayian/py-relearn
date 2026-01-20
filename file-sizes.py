# Every file has metadata including size, modified time and permissions
# in pathlib, you get this using -> item.stat.st_size


from pathlib import Path

p = Path("recursion_test1.py")
print(p.stat().st_size)

# 259
# -> means 259 bytes