l=list()
l.append("hello")
l.append("there")
ll=l
l.append("world")
if "world" in l:
    l.remove("world")
else:
    print("world is not in list")
print(f"copy : {ll},count : {l.count("world") if "world" in l else -1}, {l.index("world") if "world" in l else -1}")
for msg in l:
    print(msg,end=" ")
print()
