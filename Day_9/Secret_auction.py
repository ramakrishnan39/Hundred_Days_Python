
##Below is my effort

import os
logo=    """
 \/___________--
 /\           |-|
|_|              """

print(logo)
chk_bidder="Yes"
dict={}
while chk_bidder == "Yes" or chk_bidder == "yes":
    name=input("Enter the bidder name : ")
    amount=float(input("Enter the bid amount : $"))
    dict[name]=amount
    chk_bidder=input("Is there any other person to Bid")
    if(chk_bidder == "Yes" or chk_bidder == "yes"):
        os.system('cls')

amt_li =[]
for key in dict:
    amt_li.append(dict[key])

amt_li.sort(reverse=True)
print(amt_li)
