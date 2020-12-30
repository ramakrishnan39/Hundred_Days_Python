weight=int(input("Enter your weight in Kilograms: "))
height=float(input("Enter your height in Meters : "))

bmi = weight / (height ** 2)
print(f"Your BMI is {int(bmi)}")