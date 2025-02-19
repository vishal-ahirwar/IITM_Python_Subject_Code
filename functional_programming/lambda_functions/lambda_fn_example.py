"""
def test(x,y):
    return x+y

test_lambda=lambda x,y:x+y

x=test(5,4)
print(x)#x=9
_x=test_lambda(5,3)
print(_x)#_x=8

"""
numbers=(2,3,4,5,6,4,2)
numbers=[i for i in map(lambda x:x*x,numbers)]#using lambda,map,tuple,loop all togather
print(numbers)
