
def generator(limit):
    x=0
    print("Output from generator :")
    while x<limit:
        yield x+1
        yield x+2
        yield x+3
        x+=1

x:int=generator(10)

out:int=next(x,0)
while out:
    print(f"{out}",end=" ",sep=",")
    out=next(x,0)
print()
