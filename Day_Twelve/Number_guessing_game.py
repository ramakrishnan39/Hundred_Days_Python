import random as r
logo= """
 _____                         _   _                                  _               
|  __ \                       | | | |                                | |              
| |  \/_   _  ___  ___ ___    | |_| |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | __| '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | |_| | | |  __/  | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/    \__|_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
                                                                                    
"""

print(logo)
q_num=0
q_num=r.randint(0,101)

level=input("Which lever you want 'easy' or 'hard' : ")
def detect(num_choice):
    while num_choice > 0 :
        print(f"You have {num_choice} choices.")
        a_num=int(input("Enter your number : "))
        if q_num == a_num:
            print("You won!!!!")
            return
        else :
            if q_num < a_num:
                if abs(a_num - q_num) <= 10:
                    print(f"You came near high.")
                else:
                    print("Too High !")
            elif q_num > a_num:
                if abs(q_num - a_num) <= 10:
                    print(f"You came near low.")
                else:
                    print("Too Low !")
            num_choice -= 1
    else:
        print(f"You Lose !! Try again . The answer is {q_num}")

if level == "easy":
    detect(10)

elif level == "hard":
    detect(5)