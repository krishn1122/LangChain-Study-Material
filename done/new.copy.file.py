
with open("name.txt","r") as f1:
    lines=f1.readlines()
lineno=1
for line in lines:
        if("research" in line):
            print("Word found at",lineno)
            break
            lineno+=1
            
        else:
            print("Word not found")



