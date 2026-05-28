with open("name.txt","r") as f1:
    c1=f1.read()
with open("copy_name.txt","r") as f2:
    c2=f2.read()
if(c1==c2):
    print("Both file have same content!")
else:
    print("Both files are different.")