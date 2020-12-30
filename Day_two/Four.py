print("Welcome to Tip calculator !")
bill_amt=float(input("Enter the bill amount to be paid : $" ))
pctg=int(input("Enter the percentage of Tip you want to give a.10 b.12 c.15 : "))
pctg_val=1 + (pctg /100)
ppl_num=int(input("How many of you came here ? : "))
pay_amt=float(round(( bill_amt * pctg_val ) / ppl_num,2))
print(f"Each person should pay ${pay_amt}")

