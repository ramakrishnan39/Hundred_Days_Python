#Prime checker:
import math
def prime_checker(number):
    sol="It's a Prime number"
    for i in range(2,int(math.floor(number/2))):
        if(number%i==0):
            sol="It's not a Prime number"
    print(sol)

n=int(input("Enter the number to check : "))
prime_checker(number=n)