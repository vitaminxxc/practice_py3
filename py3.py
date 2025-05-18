#Task_1 : Calculate factorial
z = int(input("Enter a number:"))

def factorial(z):
    if z <=1:
        return z == 1
    else:
        return z * factorial(z-1)
    
factorial_ans = factorial(z)
print(factorial_ans)





#Task 2: Using math module for calculations
import math

x = int(input("Enter a number:"))

#square root of x
a = math.sqrt(x)

# Log of the number
b = math.log(x)

# sine of number in radians
c = math.sin(x)

print(a)
print(b)
print(c)