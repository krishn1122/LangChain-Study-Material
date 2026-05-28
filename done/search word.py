search="python"
with open("name.txt", "r") as f:
    content=f.read()
if(search in content):
    print("yes")
else:
    print("No")