import random,time
points=0
sp=0
elements=['Rock','Paper','Seasors']

while True:
    aponent=int(input("Choose one of this :\n1 - Rock\n2 - Paper\n3 - Seasors\n"))
    system=random.randint(0,2)
    if elements[aponent-1]=='Rock':
        if elements[system]=='Seasors':
            print(f"Won",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            points+=1
        if elements[system]=="Paper":
            print(f"Loss",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            sp+=1
        if elements[system]==elements[aponent-1]:
            print("draw",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
    elif elements[aponent-1]=='Paper':
        if elements[system]=='Rock':
            print(f"Won",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            points+=1
        if elements[system]=="Seasors":
            print(f"Loss",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            sp+=1
        if elements[system]==elements[aponent-1]:print("draw",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
    elif elements[aponent-1]=='Seasors':
        if elements[system]=='Paper':
            print(f"Won",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            points+=1
        if elements[system]=="Rock":
            print(f"Loss",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
            sp+=1
        if elements[system]==elements[aponent-1]:print("draw",f"System :{elements[system]}",f"Yours :{elements[aponent-1]}",sep="\n")
    else:
        print("Invalid Input")
    print("System points = ",sp)
    print("Your points = ",points,"\n--------------------------------------")
    if points==3:
        print("Congrajulations Your are the winner")
        break
    if sp==3:
        print("System wins")
        break
    time.sleep(1)