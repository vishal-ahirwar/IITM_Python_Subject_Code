def odd_increment_even_decrement_no_modify(items) -> list:
    return [item + 1 if item % 2 else item - 1 for item in items]
def odd_square_even_double_modify(items:list) -> list:
    items= [item**2 if item%2 else item*2 for item in items]
print(odd_increment_even_decrement_no_modify([1,2,3,4,5,6,7,8,9]))
L=[1,2,3,4,5]
odd_square_even_double_modify(L)
print(L)