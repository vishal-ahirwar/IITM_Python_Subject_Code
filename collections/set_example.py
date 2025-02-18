# s=set()#this is set
# s.add("hello")
# s.add("there")
# s.add("apple")
# s.add("apple")
# s.add("hello")
# for _s in s:
#     print(_s)
# s=sorted(s)
# for _s in s:
#     print(_s)

fruits=set(("apple","mango","graps","dunnoo","banana","guava","apple"))
for fruit in fruits:
    print(f"fruit : {fruit}")
    
def add5ToX():
    global x
    x+=5

x=0
for _ in range(5):
    add5ToX()
    print(f"x: {x}")