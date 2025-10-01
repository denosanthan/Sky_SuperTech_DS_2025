
import sys
def mod(x, z):
    """ Return Remainder after integer division of x by z"""
    return float(x%z)

def power(x, z):
    """ Return the power od x to  z as a float"""

def sqrt(x, z):
    """ Return the square root of x to  z to 3 decimal places """
    return round(x**0.5, 3)

print("########### Adv Calc Examples ############")
print(f"4 % 3 = {mod(4, 3)}")
print(f"4 ** 3 = {power(4, 3)}")
print(f"\N{square root}99 = {sqrt(99)}")
print("###########################################")

sys.exit(0)
