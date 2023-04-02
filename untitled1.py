import tkinter as tk
import random as rd
import csv



 

def entry():
    root1.destroy()
            
    import menu_main
    menu_main.menu_launch()
def login():
    
    
    def passcheck():
        
        
        f1=open("PASS.csv","r")
        a=csv.reader(f1)
        k1=Usernameentry.get()
        k2=Passwordentry.get()
        for i in a:
            if len(i)==0:
                pass
            else:
                if len(k1)==0 or len(k2)==0:
                    pass
                else:
                    t1=i[0]
                    t2=i[1]
                    if k1==t1 and k2==t2:
                        root3.destroy()
                        entry()
                        break
                    
                
                
                
        else:
            if Label2["text"]=="":
                Label2["text"]+="Username or Password is invalid"
            
    root3=tk.Tk()
    root3.title("Login")
    root3.configure(bg="black")
    
    Label1=tk.Label(root3,bg="black")
    Label1.place(x=200,y=100,width=1000,height=1000)
    
    Usernamelabel=tk.Label(root3,text="USERNAME\t:",bg="black",fg="white",font="none 17",width=40)
    Usernamelabel.place(x=280,y=300)
    
    Usernameentry=tk.Entry(root3,borderwidth=4,width=40)
    Usernameentry.place(x=680,y=300)
    
    Passwordlabel=tk.Label(root3,text="PASSWORD\t:",bg="black",fg="white",font="none 17",width=40)
    Passwordlabel.place(x=280,y=450)
    
    Passwordentry=tk.Entry(root3,borderwidth=4,width=40)
    Passwordentry.place(x=680,y=450,)
    
    Label2=tk.Label(root3,text="",bg="black",fg="white")
    Label2.place(x=680,y=480)
    
    Submitbutton=tk.Button(root3,text="SUBMIT",command=passcheck,bg="grey",fg="white",width=35)
    Submitbutton.place(x=680,y=600)
        
    CancelButton=tk.Button(root3,text="Cancel",command=root3.destroy)
    CancelButton.place(x=0,y=0)
    root3.attributes('-fullscreen',True)
    
    root3.mainloop()
    
    
def signup():
    def passgen():
        import random 
        n=6
        p=""
        while len(p)!=n:
            x=random.randint(1,26)
            z=random.randint(1,26)
            y=str(random.randint(0,9))
            a=chr(64+x)
            b=chr(96+z)
            c=chr(64-x)
            d=str(y)
            l=[a,b,c,d]
            q=random.randint(0,3)
            p+=l[q]
        Repasswordentry.insert(0,p)
        Passwordentry.insert(0,p)
        

    def submit():
        f1=open("PASS.csv","a")
        a=csv.writer(f1)
        k1=Usernameentry.get()
        k2=Passwordentry.get()
        k4=Repasswordentry.get()
        k3=Nameentry.get()
        
        if len(k1)==0 or len(k2)==0 or len(k3)==0:
            Errorlabel["text"]="Please write proper details"
        elif k2==k4:
            l=[k1,k2,k3]
            a.writerow(l)
            root2.destroy()
            entry()
            
            
        else:
            Errorlabel["text"]="Passwords do not match"
            
    root2=tk.Tk()
    root2.configure(bg="white")
    root2.title("Sign Up")
    root2.attributes('-fullscreen',True)
    Label1=tk.Label(root2,bg="black")
    Label1.place(x=250,y=100,width=1000,height=1000)
    
    Errorlabel=tk.Label(root2,text="",bg="black",fg="white")
    Errorlabel.place(x=280,y=120)
    
    Usernamelabel=tk.Label(root2,text="USERNAME",bg="black",font="none 17",fg="white")
    Usernamelabel.place(x=280,y=150,width=400)
    
    Usernameentry=tk.Entry(root2,borderwidth=4)
    Usernameentry.place(x=680,y=150,width=400)
    
    Namelabel=tk.Label(root2,text="NAME",bg="black",font="none 17",fg="white")
    Namelabel.place(x=280,y=300,width=400)
    
    Nameentry=tk.Entry(root2,borderwidth=4)
    Nameentry.place(x=680,y=300,width=400)
    
    Passwordlabel=tk.Label(root2,text="PASSWORD",bg="black",font="none 17",fg="white")
    Passwordlabel.place(x=280,y=450,width=400)
    
    Passwordentry=tk.Entry(root2,borderwidth=4)
    Passwordentry.place(x=680,y=450,width=400)
    
    Repasswordlabel=tk.Label(root2,text="RE ENTER PASSWORD",bg="black",font="none 17",\
                             fg="white")
    Repasswordlabel.place(x=280,y=600,width=400)
    
    Repasswordentry=tk.Entry(root2,borderwidth=4)
    Repasswordentry.place(x=680,y=600,width=400)
    
    Submitbutton=tk.Button(root2,text="SUBMIT",command=submit,bg="grey")
    Submitbutton.place(x=680,y=700)
    
    Autopassbutton=tk.Button(root2,text="Generate Pass.",command=passgen,bg="grey")
    Autopassbutton.place(x=680,y=650)
    
    CancelButton=tk.Button(root2,text="Cancel",command=root2.destroy)
    CancelButton.place(x=0,y=0)
        
    root2.mainloop()
    
    
    
root1=tk.Tk()
root1.configure(background="black")
logo=tk.Canvas(root1,bg="black",width=231,height=231,highlightthickness=0)
logo.pack(pady=20)
img = tk.PhotoImage(file="Logo1.png",master=root1)
logo.create_image(0,0,anchor=tk.NW,image=img)
root1.title("PyOS")
root1.attributes("-fullscreen",True)

cross=tk.PhotoImage(file=r"D:\Computer Science Project Class XII-A\New Compile Fix\cross.png")

CancelButton=tk.Button(root1,text="Exit",command=root1.destroy,bg="black",image = cross,fg="red")

CancelButton.place(x=0,y=0)
heading=tk.Label(root1,text="PyOS",font="none 80",bg="black",fg="yellow")
heading.pack(pady=60)
Loginbutton=tk.Button(root1,text="LOG IN",bg="black",fg="white",width=20,borderwidth=5,font="none 17",\
                      command=login)
Loginbutton.pack(pady=20)

Signupbutton=tk.Button(root1,text="SIGN UP",bg="black",fg="white",width=20,borderwidth=5,font="none 17",command=\
                       signup)
Signupbutton.pack()
Skipbutton=tk.Button(root1,text="SKIP",bg="black",fg="white",borderwidth=0,font="none 10",\
                     command=entry)
                     
Skipbutton.pack(pady=5)
    

root1.mainloop()
        














