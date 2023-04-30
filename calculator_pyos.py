import tkinter as tk
from math import *
def calculator(menu):
    global hlist
    calculatorlist=["10**","**-1","**2","**3","**","factorial(","**0.5",\
                                                       "**(1/","log("]
    hlist=[]
    def invertrigo(inversefunc):
        inpt["text"]+=inversefunc
    def reversefunction():
        sinbut["text"]="sin("
        sinbut["command"]= lambda : textadd(sinbut)
        cosbut["text"]="cos("
        cosbut["command"]= lambda :textadd(cosbut)
        tanbut["text"]="tan("
        tanbut["command"]= lambda :textadd(tanbut)
        sinhbut["text"]="sinh("
        sinhbut["command"]= lambda :textadd(sinhbut)
        coshbut["text"]="cosh("
        coshbut["command"]=lambda : textadd(coshbut)
        tanhbut["text"]="tanh("
        tanhbut["command"]= lambda :textadd(tanhbut)
        octalbut["text"]="octal"
        octalbut["command"]=octalfunc
        binarybut["text"]="binary"
        binarybut["command"]=binaryfunc
        hexadecimalbut["text"]="hexadecimal"
        hexadecimalbut["command"]=hexadecimalfunc
        inversebut["command"]=inversefunction
    def inversefunction():
        sinbut["text"]="sin^-1"
        sinbut["command"]= lambda :invertrigo("asin(")
        cosbut["text"]="cos^-1"
        cosbut["command"]= lambda :invertrigo("acos(")
        tanbut["text"]="tan^-1"
        tanbut["command"]= lambda :invertrigo("atan(")
        sinhbut["text"]="sinh^-1"
        sinhbut["command"]= lambda :invertrigo("asinh(")
        coshbut["text"]="cosh^-1"
        coshbut["command"]= lambda :invertrigo("acosh(")
        tanhbut["text"]="tanh^-1"
        tanhbut["command"]= lambda :invertrigo("atanh(")
        octalbut["text"]="oct to dec"
        octalbut["command"]=lambda : inversenum("o")
        binarybut["text"]="bin to dec"
        binarybut["command"]=lambda : inversenum("b")
        hexadecimalbut["text"]="hex to dec"
        hexadecimalbut["command"]=lambda : inversenum("h")
        inversebut["command"]=reversefunction
    def textadd(button):
        text=button["text"]
        inpt["text"]+=text
    def listadd(no):
        text=calculatorlist[no]
        inpt["text"]+=text
    def allclear():
        inpt["text"]=""
    def delete():
        temp=inpt["text"]
        inpt["text"]=temp[:-1]
    def calculatetotal():
        inptvalue=inpt["text"]
        ans=eval(inptvalue)
        inpt["text"]=str(ans)
        global hlist
        hlist.append(inptvalue+"=")
        hlist.append(str(ans))
        if len(hlist)>6:
            temp=len(hlist)-6
            del hlist[:temp]
    def historyfunc():
        inpt["text"]=""
        global hlist
        for i in hlist:
            inpt["text"]+="\n"+i
    def binaryfunc():
        num=eval(inpt["text"])
        global hlist
        hlist+=["binary("+inpt["text"]+")"+"="]
        def bint(x):
            s=""
            while x!=0:
                a=x%2
                s+=str(a)
                x//=2
            return s[::-1]
        def bindec(q):
            l=[]
            k=""
            while q!=0 and q not in l:
                l+=[q]
                q=2*q
                r=int(q)
                k+=str(r)
                q-=r
            return(k)
        if int(num)==num:
            binarynum=bint(num)
            inpt["text"]=binarynum
        else:
            binaryint=bint(int(num))
            decimalnum=num-int(num)
            binarydec=bindec(decimalnum)
            binarynum=binaryint+"."+binarydec
            inpt["text"]=binarynum
        hlist+=[binarynum]
    def hexadecimalfunc():
        num=eval(inpt["text"])
        global hlist
        hlist+=["hexadecimal("+inpt["text"]+")"+"="]
        def hexint(x):
            s=""
            while x!=0:
                a=x%16
                if a>=10:
                    a=chr(65+(a-10))
                s+=str(a)
                x//=16
            return s[::-1]
        def hexdec(q):
            l=[]
            k=""
            while q!=0 and q not in l:
                l+=[q]
                q=16*q
                r=int(q)
                if r>=10:
                    r=chr(65+(r-10))
                k+=str(r)
                q-=r
            return(k)
        if int(num)==num:
            binarynum=hexint(num)
            inpt["text"]=binarynum
        else:
            binaryint=hexint(int(num))
            decimalnum=num-int(num)
            binarydec=hexdec(decimalnum)
            binarynum=binaryint+"."+binarydec
            inpt["text"]=binarynum
        hlist+=[binarynum]
    def octalfunc():
        num=eval(inpt["text"])
        global hlist
        hlist+=["octal("+inpt["text"]+")"+"="]
        def bint(x):
            s=""
            while x!=0:
                a=x%8
                s+=str(a)
                x//=8
            return s[::-1]
        def bindec(q):
            l=[]
            k=""
            while q!=0 and q not in l:
                l+=[q]
                q=8*q
                r=int(q)
                k+=str(r)
                q-=r
            return(k)
        if int(num)==num:
            binarynum=bint(num)
            inpt["text"]=binarynum
        else:
            binaryint=bint(int(num))
            decimalnum=num-int(num)
            binarydec=bindec(decimalnum)
            binarynum=binaryint+"."+binarydec
            inpt["text"]=binarynum
        hlist+=[binarynum]
    def inversenum(x):
        num=inpt["text"]
        s=""
        m=0
        if x=="b":
            le=len(num)
            for i in range(le):
                n=int(num[i])
                q=n*2**(le-1-i)
                m+=q
        elif x=="o":
            num=inpt["text"]
            s=""
            le=len(num)
            for i in range(le):
                n=int(num[i])
                q=n*8**(le-1-i)
                m+=q
        elif x=="h":
            num=inpt["text"]
            s=""
            le=len(num)
            for i in range(le):
                if num[i].isdigit()==False:
                    i=ord(i)-55
                n=int(num[i])
                q=n*16**(le-1-i)
                m+=q
        s+=str(m)
        inpt["text"]=s
        global hlist
        hlist+=["decimal("+num+")"+"="]
        hlist+=[s]
    root=tk.Tk()
    root.attributes("-fullscreen",True)
    root.title("Calculator")
    root.configure(background="white")
    exit_but=tk.Button(root,text="EXIT",bg="black",fg="white",font=80,command=root.destroy)
    
    exit_but.pack()
    
    inpt=tk.Label(root,borderwidth=1,relief="solid",text="",height=6,font="None 16",anchor="se",)
    inpt.pack(fill=tk.X)
    pane=tk.Frame(root,bg="black").pack(fill=tk.X)
    inversebut=tk.Button(pane,text="inverse",background="white",foreground="brown",\
                         command=inversefunction,borderwidth=0,font="None 16")
    inversebut.place(width=110,x=0,y=316+42)
    leftbracketbut=tk.Button(pane,text="(",background="white",foreground="brown",\
                         command= lambda :textadd(leftbracketbut),borderwidth=0,\
                         font="None 16")
    leftbracketbut.place(width=110,x=110,y=316+42)
    rightbracketbut=tk.Button(pane,text=")",background="white",foreground="brown",\
                         command= lambda :textadd(rightbracketbut),borderwidth=0,\
                         font="None 16")
    rightbracketbut.place(width=110,x=220,y=316+42)
    tentothepowerbut=tk.Button(pane,text="10^",background="white",foreground="brown",\
                         command= lambda :listadd(0),borderwidth=0,\
                         font="None 16")
    tentothepowerbut.place(width=110,x=330,y=316+42)
    factorialbut=tk.Button(pane,text="factorial !",background="white",foreground="brown",\
                         command= lambda :listadd(5),borderwidth=0,\
                         font="None 16")
    factorialbut.place(width=110,x=0,y=190)
    squarepanebut=tk.Button(pane,text="^0.5",background="white",foreground="brown",\
                         command= lambda :listadd(6),borderwidth=0,\
                         font="None 16")
    squarepanebut.place(width=110,x=110,y=190)
    panebut=tk.Button(pane,text="^(1/x)",background="white",foreground="brown",\
                         command= lambda :listadd(7),borderwidth=0,\
                         font="None 16")
    panebut.place(width=110,x=220,y=190)
    lnbut=tk.Button(pane,text="ln",background="white",foreground="brown",\
                         command= lambda :listadd(8),borderwidth=0,\
                         font="None 16")
    lnbut.place(width=110,x=330,y=190)
    allclearbut=tk.Button(pane,text="Clear",background="white",foreground="blue",\
                         command=allclear ,borderwidth=0,\
                         font="None 16")
    allclearbut.place(width=110,x=440+110,y=190)
    calculatebut=tk.Button(pane,text="=",background="blue",foreground="white",\
                         command=calculatetotal ,borderwidth=0,\
                         font="None 16")
    calculatebut.place(width=110,x=440+110+55,y=190+42)
    
    arrow=tk.PhotoImage(file=r"D:\PyOS\New Compile Fix\Blue_arrow.png")
    deletebut=tk.Button(pane,text="<--",background="white",foreground="blue",\
                         command= delete,borderwidth=0,image=arrow)
    deletebut.place(width=110,x=660,y=190)
    dividebut=tk.Button(pane,text="/",background="white",foreground="blue",\
                         command= lambda :textadd(dividebut),borderwidth=0,\
                         font="None 16")
    dividebut.place(width=110,x=880,y=190)
    multiplybut=tk.Button(pane,text="*",background="white",foreground="blue",\
                         command= lambda :textadd(multiplybut),borderwidth=0,\
                         font="None 16")
    multiplybut.place(width=110,x=990,y=190)
    addbut=tk.Button(pane,text="+",background="white",foreground="blue",\
                         command= lambda :textadd(addbut),borderwidth=0,\
                         font="None 16")
    addbut.place(width=110,x=1100,y=190)
    subtractbut=tk.Button(pane,text="-",background="white",foreground="blue",\
                         command= lambda :textadd(subtractbut),borderwidth=0,\
                         font="None 16")
    subtractbut.place(width=110,x=1210,y=190)
    historybut=tk.Button(pane,text="History",background="white",foreground="orange",\
                         command= historyfunc,borderwidth=0,\
                         font="None 16")
    historybut.place(width=110,x=1310,y=190)
    inversenumberbut=tk.Button(pane,text="^-1",background="white",foreground="brown",\
                         command= lambda :listadd(1),borderwidth=0,\
                         font="None 16")
    inversenumberbut.place(width=110,x=0,y=232)
    squarebut=tk.Button(pane,text="^2",background="white",foreground="brown",\
                         command= lambda :listadd(2),borderwidth=0,\
                         font="None 16")
    squarebut.place(width=110,x=110,y=232)
    cubebut=tk.Button(pane,text="^3",background="white",foreground="brown",\
                         command= lambda :listadd(3),borderwidth=0,\
                         font="None 16")
    cubebut.place(width=110,x=220,y=232)
    powerbut=tk.Button(pane,text="^",background="white",foreground="brown",\
                         command= lambda :listadd(4),borderwidth=0,\
                         font="None 16")
    powerbut.place(width=110,x=330,y=232)
    sinbut=tk.Button(pane,text="sin",background="white",foreground="brown",\
                         command= lambda :textadd(sinbut),borderwidth=0,\
                         font="None 16")
    sinbut.place(width=110,x=0,y=274)
    cosbut=tk.Button(pane,text="cos",background="white",foreground="brown",\
                         command= lambda :textadd(cosbut),borderwidth=0,\
                         font="None 16")
    cosbut.place(width=110,x=110,y=274)
    tanbut=tk.Button(pane,text="tan",background="white",foreground="brown",\
                         command= lambda :textadd(tanbut),borderwidth=0,\
                         font="None 16")
    tanbut.place(width=110,x=220,y=274)
    pibut=tk.Button(pane,text="pi",background="white",foreground="brown",\
                         command= lambda :textadd(pibut),borderwidth=0,\
                         font="None 16")
    pibut.place(width=110,x=330,y=274)
    sinhbut=tk.Button(pane,text="sinh",background="white",foreground="brown",\
                         command= lambda :textadd(sinhbut),borderwidth=0,\
                         font="None 16")
    sinhbut.place(width=110,x=0,y=316)
    coshbut=tk.Button(pane,text="cosh",background="white",foreground="brown",\
                         command= lambda :textadd(coshbut),borderwidth=0,\
                         font="None 16")
    coshbut.place(width=110,x=110,y=316)
    tanhbut=tk.Button(pane,text="tanh",background="white",foreground="brown",\
                         command= lambda :textadd(tanhbut),borderwidth=0,\
                         font="None 16")
    tanhbut.place(width=110,x=220,y=316)
    ebut=tk.Button(pane,text="e",background="white",foreground="brown",\
                         command= lambda :textadd(ebut),borderwidth=0,\
                         font="None 16")
    ebut.place(width=110,x=330,y=316)
    num1but=tk.Button(pane,text="1",background="white",foreground="black",\
                         command= lambda :textadd(num1but),borderwidth=0,\
                         font="None 16")
    num1but.place(width=110,x=330+550,y=232)
    num2but=tk.Button(pane,text="2",background="white",foreground="black",\
                         command= lambda :textadd(num2but),borderwidth=0,\
                         font="None 16")
    num2but.place(width=110,x=990,y=232)
    num3but=tk.Button(pane,text="3",background="white",foreground="black",\
                         command= lambda :textadd(num3but),borderwidth=0,\
                         font="None 16")
    num3but.place(width=110,x=1100,y=232)
    num4but=tk.Button(pane,text="4",background="white",foreground="black",\
                         command= lambda :textadd(num4but),borderwidth=0,\
                         font="None 16")
    num4but.place(width=110,x=1210,y=232)
    num5but=tk.Button(pane,text="5",background="white",foreground="black",\
                         command= lambda :textadd(num5but),borderwidth=0,\
                         font="None 16")
    num5but.place(width=110,x=880,y=274)
    num6but=tk.Button(pane,text="6",background="white",foreground="black",\
                         command= lambda :textadd(num6but),borderwidth=0,\
                         font="None 16")
    num6but.place(width=110,x=990,y=274)
    num7but=tk.Button(pane,text="7",background="white",foreground="black",\
                         command= lambda :textadd(num7but),borderwidth=0,\
                         font="None 16")
    num7but.place(width=110,x=1100,y=274)
    num8but=tk.Button(pane,text="8",background="white",foreground="black",\
                         command= lambda :textadd(num8but),borderwidth=0,\
                         font="None 16")
    num8but.place(width=110,x=1210,y=274)
    num9but=tk.Button(pane,text="9",background="white",foreground="black",\
                         command= lambda :textadd(num9but),borderwidth=0,\
                         font="None 16")
    num9but.place(width=110,x=880+55,y=316)
    num0but=tk.Button(pane,text="0",background="white",foreground="black",\
                         command= lambda :textadd(num0but),borderwidth=0,\
                         font="None 16")
    num0but.place(width=110,x=990+55,y=316)
    pointbut=tk.Button(pane,text=".",background="white",foreground="black",\
                         command= lambda :textadd(pointbut),borderwidth=0,\
                         font="None 16")
    pointbut.place(width=110,x=1100+55,y=316)
    binarybut=tk.Button(pane,text="Binary",background="white",foreground="black",\
                         command=binaryfunc,borderwidth=0,\
                         font="None 16")
    binarybut.place(width=110,y=316+42+42,x=0+935)
    hexadecimalbut=tk.Button(pane,text="Hexadecimal",background="white",foreground="black",\
                         borderwidth=0,\
                         command=hexadecimalfunc,font="None 16")
    hexadecimalbut.place(width=120,y=358+42,x=220+10+935)
    octalbut=tk.Button(pane,text="Octal",background="white",foreground="black",\
                         command=octalfunc,borderwidth=0,\
                         font="None 16")
    
    
    octalbut.place(width=110,y=316+42+42,x=110+935)
    
    root.mainloop()
    menu()




