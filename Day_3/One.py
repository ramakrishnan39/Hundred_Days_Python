#First program
print("Welcome to Rollercoaster")
h=int(input("Enter your height : ")) #h - height
a=int(input("Enter your age : ")) # a-age
if h >=120:
    print("Great! You can ride in Rollercoaster")
    if a < 12:
        print("CHILD ticket costs $5")
    elif a >= 12 and a<=18:
        print("YOUTH ticket costs $7")
    else:
        print("ADULT ticket costs $12")
    c=input("Do you wanna take photo .. ? (Say Y or N respectively for Yes or No) : ") # c- Choice
    if c=='Y' or c=='y':
        print("Please pay additional $3 for permission.")
    elif c=='N' or c=='n':
        print("No problem. As you wish you don't need to pay any extra cost.")
else:
    print("OHH! You are still a kid. Grow buddy ! ")


"""#Second program
num=int(input("Enter the number to check : "))
if num%2==0:
    print("Its Even number")
else:
    print("Its Odd number")"""