import tkinter as tk
import random,time
elements=['Rock','Paper','Seasors']
root=tk.Tk()
root.title("Stone Paper Seasors")
root.geometry("250x300")
points_Player=0
points_systems=0
label=tk.StringVar(root,"")
disp=tk.Label(root,text="Choose one of this :\n1 - Rock\n2 - Paper\n3 - Seasors\n")
disp.pack()
e=tk.Entry(root)
e.pack()
pp=tk.StringVar(root,f"Your points = {points_Player}")
point=tk.Label(root,textvariable=pp)
point.pack(side="top")
ps=tk.StringVar(root,f"System points = {points_systems}")
point=tk.Label(root,textvariable=ps)
point.pack(side="top")
flag=False
def c():
    global points_Player,label,points_systems,flag
    system=random.randint(0,2)
    if elements[int(e.get())-1]=='Rock':
        if elements[system]=='Seasors':
            label.set(f"Won \nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_Player+=1
        if elements[system]=="Paper":
            label.set(f"Loss\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_systems+=1
        if elements[system]==elements[int(e.get())-1]:
            label.set(f"draw\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
    elif elements[int(e.get())-1]=='Paper':
        if elements[system]=='Rock':
            label.set(f"Won\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_Player+=1
        if elements[system]=="Seasors":
            label.set(f"Loss\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_systems+=1
        if elements[system]==elements[int(e.get())-1]:label.set(f"draw\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
    elif elements[int(e.get())-1]=='Seasors':
        if elements[system]=='Paper':
            label.set(f"Won\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_Player+=1
        if elements[system]=="Rock":
            label.set(f"Loss\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
            points_systems+=1
        if elements[system]==elements[int(e.get())-1]:label.set(f"draw\nSystem :{elements[system]}\nYours :{elements[int(e.get())-1]}")
    else:
        label.set("Invalid Input")
    
    pp.set(f"Your points = {points_Player}")
    ps.set(f"System points = {points_systems}")

    if points_Player==3:
        label.set("Congrates your are the winner")
        b["state"]="disable"
    if points_systems==3:
        label.set("Systum wons")
        b["state"]="disable"
b=tk.Button(root,text="click",command=c)
b.pack()

lab=tk.Label(root,textvariable=label)
lab.pack()

root.mainloop()