# write hello python into a file, read it and print it

with open("example.txt", "w") as file :
    file.write("hello world")
    
with open("example.txt", "r") as file:
    content = file.read()

print(content)



