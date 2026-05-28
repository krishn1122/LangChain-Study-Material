class chapter:
    a=1
class book(chapter):
    b=2
class index(book):
    c=3

o=index
print(o.a)
print(o.b)
print(o.c)