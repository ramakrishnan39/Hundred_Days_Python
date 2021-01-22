#Paint area calculator
import math as m
n_can=0
def paint_calc(height,width,cover):
    n_can=height * width / cover
    print(f"You'll need {int(m.ceil(n_can))} cans to paint your wall. ")

 #Starting point of execution :
test_h=int(input("Enter the height of wall : "))
test_w=int(input("Enter the width of the wall : "))
coverage= 5

paint_calc(height = test_h, width = test_w, cover = coverage)