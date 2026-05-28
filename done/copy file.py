with open("name.txt")as f:
    content=f.read()

with open("copy_name.txt","w") as f:
    f.write(content)

