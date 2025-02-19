l=[2,3,4,5]
d={"name":"vishal ahirwar","hm":"wth dunno what to type"}
x=zip(l,d)
# print(dict(x))#{2: 'name', 3: 'hm'}
x_dict=dict(x)
#don't ask my why I did this :)
for key in x_dict:
    print(f"{x_dict[key]} : {d[x_dict[key]]}")
