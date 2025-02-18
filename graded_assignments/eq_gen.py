def poly(L, x_0):
    psum:str=""
    res=0
    n = len(L)
    for i in range(n):
        psum+= f"{L[i]}*{x_0}^{i}"
        res+=L[i]*x_0**i
        if(i!=n-1):
            psum+="+"
    psum+=f"={res}"
    return psum
eq=poly([1,2],5)
print(f"Generated Equation is : {eq}")