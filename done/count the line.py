with open("name.txt", "r") as f:
    lines=f.readlines()
lineno=1
for line in lines:
    if("researcher" in line):
        print(f"word found at line no:{lineno}")
        break
        lineno+=1
    else:
        print("not found")