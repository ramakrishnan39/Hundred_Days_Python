def greet():
    print("Hello !")
    print("Welcome to the function definitions")
    print("This will not use parameters!")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Its been a good thing you are here {name}")

def multi_input(name,country):
    print(f"Hey {name}! I think your country is {country} right?")

greet()
greet_with_name("Rama")
multi_input("Rama","India")