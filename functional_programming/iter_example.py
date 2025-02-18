str_n:str="12345"
sum_str_n:int=0
itr_s:iter=iter(str_n)
x:int=int(next(itr_s,0))
while x:
    print(f"{x}")
    sum_str_n+=x
    x:int=int(next(itr_s,0))
print(f"sum of iter_s_n : {sum_str_n}")