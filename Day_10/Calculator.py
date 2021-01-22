logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

oper_list = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
            }

print(logo)
num1=float(input("Enter the first number : "))
for k in oper_list:
    print(k)
def calc():

    continue_flag='y'
    while continue_flag == 'y' or continue_flag =='Y':
        oper_chosen=input("Please choose one operation from the above list. : ")
        num2=float(input("Enther the next number : "))
        func=oper_list[oper_chosen]
        result=func(num1,num2)
        print(f"{num1}{oper_chosen}{num2}={result}")

        if(input(f"Would you like to continue with {result}? options 'y' or 'n' : "))=='y':
            n1=result
        else:
            continue_flag='n'
            calc()

calc()

