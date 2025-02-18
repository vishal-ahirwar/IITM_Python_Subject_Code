d={}
d["hello"]="there"
d["there"]="hello"
d[1]="one"
d[0]="zero"
d[2]="two"

for key in d:
    print(f"key : {key}, value : {d[key]}")