import tkinter as tk
import os

def tax(menu):
    root=tk.Tk()
    root.title("Tax Calculator")
    root.configure(background="white")
    exit_but=tk.Button(root,text="EXIT",bg="black",fg="white",font=80,command=root.destroy).pack()
    root.attributes("-fullscreen",True)
    Heading=tk.Label(root,borderwidth=0,relief="solid",\
                  text=" Income\nTax\n Calculator",font="none 23",foreground="black",background="white")
    Heading.place(x=195)
    Instructions=tk.Label(root,text="*In numerical figures per annum",background="white")
    Instructions.place(y=150)
    Agelabel=tk.Label(root,text="Age and Gender:",background="white",foreground="black",font="none 15")
    Agelabel.place(y=200)
    originalvalue=tk.StringVar(root)
    originalvalue.set("Age and Gender")
    Agelist=["under 60 male","under 60 female","60 or more male","60 or more female"]
    Agemenu=tk.OptionMenu(root,originalvalue,*Agelist)
    Agemenu.place(x=200,y=200,width=200)
    Incomelabel=tk.Label(root,text="Basic Salary* :",background="white",\
                         foreground="black",font="none 15")
    Incomelabel.place(y=300)
    Incomeentry=tk.Entry(root,background="white",border=2)
    Incomeentry.place(y=300,x=200,width=200)
    Healthlabel=tk.Label(root,text="Health Allowance* :",background="white",\
                         foreground="black",font="none 15")
    Healthlabel.place(y=400)
    Healthentry=tk.Entry(root,background="white",border=2)
    Healthentry.place(y=400,x=200,width=200)
    Transportlabel=tk.Label(root,text="Transport Allowance*:",background="white",\
                         foreground="black",font="none 15")
    Transportlabel.place(y=500)
    Transportentry=tk.Entry(root,background="white",border=2)
    Transportentry.place(y=500,x=200,width=200)
    Otherlabel=tk.Label(root,text="Other Allowance* :",background="white",\
                         foreground="black",font="none 15")
    Otherlabel.place(y=600)
    Otherentry=tk.Entry(root,background="white",border=2)
    Otherentry.place(y=600,x=200,width=200)
    def savedata():
        selectedvalue=originalvalue.get()
        
        
        def savebutfunc():
            completeName = os.path.join("D:/PyOS/New Compile Fix/taxcalfile",\
                                entry.get()+".txt") 
            
            if str(entry.get()+".txt") in existing_files:
                    h=tk.messagebox.askyesnocancel(title="Warning", message="File With Same Name Exists.\nDo You Wish To Overwrite?")
                    if h==True:
                        f=open(completeName,"w")
                        f.write(selectedvalue)
                        f.write("\n"+"Income:"+str(Incomeentry.get()))
                        f.write("\n"+"Health:"+str(Healthentry.get()))
                        f.write("\n"+"Transport:"+str(Transportentry.get()))
                        f.write("\n"+"Other:"+str(Otherentry.get()))
                        
                        f.write("\n"+taxamountlabel["text"])
                        f.close()
                        save.destroy()
                    
                    elif h==False:
                        save.destroy()
            else:
                
                f=open(completeName,"w")
                f.write(selectedvalue)
                f.write("\n"+"Income:"+str(Incomeentry.get()))
                f.write("\n"+"Health:"+str(Healthentry.get()))
                f.write("\n"+"Transport:"+str(Transportentry.get()))
                f.write("\n"+"Other:"+str(Otherentry.get()))
                        
                f.write("\n"+taxamountlabel["text"])
                f.close()
                save.destroy()
                
        save=tk.Tk()
        existing_files=os.listdir("D:/PyOS/New Compile Fix/taxcalfile")
        save.configure(bg="white")
        
        File_name=tk.Label(save,text="File name",bg="white")
        File_name.pack()
        entry=tk.Entry(save,background="grey",border=2)
        savebut=tk.Button(save,text="Save",command=savebutfunc)
        savebut.pack()
        
        entry.pack()
        
                    
    def calculatefunc():
        netamount=float(Incomeentry.get())+float(Healthentry.get())+float(Transportentry.get())+\
        float(Otherentry.get())
        selectedvalue=originalvalue.get()
        if selectedvalue=="under 60 male" or selectedvalue=="under 60 female":
            if netamount<=250000:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str("Nil")
            elif 250000<netamount<=500000:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(netamount*0.05)
            elif 500000<netamount<1000001:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(12500+0.2*(netamount-500000))
            else:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(112500+0.3*(netamount-1000000))
        elif selectedvalue=="60 or more male" or selectedvalue=="60 or more female" :
            if netamount<=300000:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str("Nil")
            elif 300000<netamount<=500000:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(netamount*0.05)
            elif 500000<netamount<1000001:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(10000+0.2*(netamount-500000))
            else:
                taxamountlabel["text"]="Tax Amount : "+"Rs "+str(110000+0.3*(netamount-1000000))
        else:
            pass
    
    calculatebut=tk.Button(root,text="Calculate",background="blue",foreground="black",\
                           command=calculatefunc,font="none 16")
    calculatebut.place(y=350,x=750,width=110)
    taxamountlabel=tk.Label(root,text="Tax Amount : ",background="white",\
                         foreground="black",font="none 15")
    taxamountlabel.place(y=450,x=750)
    
    savebut=tk.Button(root,text="Save",background="blue",foreground="black",\
                           command=savedata,font="none 16")
    savebut.place(y=550,x=750,width=110)
        
    root.mainloop()
    
    menu()
