#Title - Love calculator
#Logic - Find the letters TRUE and LOVE in the names of two people.

fname=input("Hey Hi! tell me your name : ")
sname=input("Okay buddy. Now tell me your crush name : ")
full_name=fname+sname
cnt_T=full_name.lower().count("t")+full_name.lower().count("r")+full_name.lower().count("u")+full_name.lower().count("e")
cnt_L=full_name.lower().count("l")+full_name.lower().count("o")+full_name.lower().count("v")+full_name.lower().count("e")
l_per=int(str(cnt_T)+str(cnt_L))
print(str(l_per)+" "+str(cnt_T)+" "+str(cnt_L))