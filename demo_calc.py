"""
    Basic Calculator App with add, multiply and divide features
"""


print(menu)
def add(*args):
    """Return the sum of all arguments as a float"""
    sum = 0
    for num in args:
        sum += num
    return sum

def mul(*args):
    """Return the product of all arguments as a float"""
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """Return the quotient of x divided by z to 2 to 3 decimal places"""
    return round(x/z, 3)

print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

l_div = lambda x, z: round(x/z, 3)
print(f"5 / 4 = {l_div(5, 4)}")