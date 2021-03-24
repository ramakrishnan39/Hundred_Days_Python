PLACEHOLDER = "[name]"


with open("./Input/names.txt","r") as rf:
    l_names = rf.readlines()

with open("./Input/invitation.txt","r") as rf:
    letter = rf.read()
    for n in l_names:
        op = letter.replace(PLACEHOLDER,n.strip())
        with open(f"./Output/invitation_{n.strip()}.txt","w") as wf:
            wf.write(op)

