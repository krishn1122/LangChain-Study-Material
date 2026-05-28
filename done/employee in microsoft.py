class employee:
    company="microsoft"

    def __init__(self, name,age):
        self.name=name
        self.age=age
        
p=employee("krishn", 17)
q=employee("yash", 16)
r=employee("chetan", 18)
s=employee("Aditya", 20)
print(p.name,p.age)
print(q.name,q.age)
print(r.name,r.age)
print(s.name,s.age)