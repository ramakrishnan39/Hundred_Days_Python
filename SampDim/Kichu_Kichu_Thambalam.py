import random
p_flag = "yes"


def choose_plot():
    """This function is used to choose the plot in Kichu Kichu game"""
    star_plot = random.choice(range(0, plots - 1))
    all_plots[star_plot] = '*'
    user_guess = int(input("Guess where the star will be : "))
    str_plots = ' '.join(map(str, all_plots))
    print(str_plots)
    if star_plot == user_guess - 1:
        print("Yeah !!! You won  ")
    else:
        print("Ohhh you lose my dear! don't worry try again! ")


while p_flag.lower() == 'y' or p_flag.lower() == 'yes':
    all_plots = []
    str_plots = ""
    plots = int(input("Tell me how many sand parts to be included (between 5 to 13) : "))
    if 5 <= plots <= 13:
        for k in range(1,plots+1):
            all_plots.append('-')
        str_plots =' '.join(map(str,all_plots))
        print(str_plots)
        choose_plot()
    else:
        print("Sorry the limit is exceeded ! Please try again !")
    p_flag = input("Do you wish to continue ? (yes or no ) :")
else:
    print("You are leaving now...")