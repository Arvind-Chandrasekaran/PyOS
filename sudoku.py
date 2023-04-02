import random as rd
import tkinter as tk
import time

l1=[[4,3,5,2,6,9,7,8,1],[6,8,2,5,7,1,4,9,3],[1,9,7,8,3,4,5,6,2],[8,2,6,1,9,5,3,4,7],[3,7,4,6,8,2,9,1,5],[9,5,1,7,4,3,6,2,8],[5,1,9,3,2,6,8,7,4],[2,4,8,9,5,7,1,3,6],[7,6,3,4,1,8,2,5,9]]
l2=[[6,2,5,8,4,3,7,9,1],[7,9,1,2,6,5,4,8,3],[4,8,3,9,7,1,6,2,5],[8,1,4,5,9,7,2,3,6],[2,3,6,1,8,4,9,5,7],[9,5,7,3,2,6,8,1,4],[5,6,9,4,3,2,1,7,8],[3,4,2,7,1,8,5,6,9],[1,7,8,6,5,9,3,4,2]]
l3=[[4,1,8,3,5,2,7,6,9],[6,2,9,8,4,7,5,3,1],[7,3,5,1,6,9,4,8,2],[3,7,4,5,9,8,1,2,6],[2,9,6,4,1,3,8,7,5],[8,5,1,7,2,6,9,4,3],[5,6,2,9,8,4,3,1,7],[1,8,3,2,7,5,6,9,4],[9,4,7,6,3,1,2,5,8]]
l4=[[1,3,6,8,9,4,5,7,2],[5,9,2,7,6,1,3,4,8],[7,4,8,3,5,2,1,6,9],[2,8,7,6,4,3,9,5,1],[3,6,5,9,1,8,4,2,7],[9,1,4,5,2,7,8,3,6],[6,7,9,4,8,5,2,1,3],[4,2,3,1,7,9,6,8,5],[8,5,1,2,3,6,7,9,4]]
l5=[[1,3,6,8,9,4,5,7,2],[5,9,2,7,6,1,3,4,8],[7,4,8,3,5,2,1,6,9],[2,8,7,6,4,3,9,5,1],[3,6,5,9,1,8,4,2,7],[9,1,4,5,2,7,8,3,6],[6,7,9,4,8,5,2,1,3],[4,2,3,1,7,9,6,8,5],[8,5,1,2,3,6,7,9,4]]
l6=[[6,9,5,2,1,7,4,3,8],[7,1,2,4,8,3,6,5,9],[3,4,8,6,9,5,1,7,2],[5,7,1,8,2,9,3,6,4],[8,6,9,1,3,4,7,2,5],[4,2,3,7,5,6,9,8,1],[9,3,6,5,4,2,8,1,7],[2,8,7,9,6,1,5,4,3],[1,5,4,3,7,8,2,9,6]]

l=[l1,l2,l3,l4,l5,l6]
rules="""The rules of the game are simple:

1.Each of the nine blocks has to contain all the numbers 1-9 within its squares.\n Each number can only appear once in a row, column or box.

2.The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across,\n within the larger square, must also contain the numbers 1-9, without repetition or omission.

3.Every puzzle has just one correct solution."""

k=list()

def sudoku_game():
    global k,sol,user_in,t1,t2,sud,early
    global user_in,A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9
    
    def valid(bo, num, pos):
            # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False
        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False
            # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False
        return True
        
    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col
        return None
    def solve(bo):
        find = find_empty(bo)
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i
                if solve(bo):
                    return True
                bo[row][col] = 0
        return False
    
    def generate():
        global k,sol,early,dif
        k=[]
        i=rd.randint(0,len(l)-1)
        k=l[i][:]
        x=dif
        for h in k:
            if x%2==0 and x<5:
                b=rd.randint(x-1,x)
            elif x>=5:
                b=rd.randint(x-2,x)
            else:
                b=x
            while True:
                f=rd.randint(0,8)
                h[f]=0
                if h.count(0)>=b:
                    break
        sol=[]
        for i in k:
            v=[]
            for j in i:
                v.append(j)
            sol.append(v)
        check=solve(sol)
        if check==False:
            generate()
        else:
            pass
    def easy():
        global early,dif
        early=False
        dif=3
        generate()
        sud.destroy()
    def norm():
        global early,dif
        early=False
        dif=4
        generate()
        sud.destroy()
    def hard():
        global early,dif
        early=False
        dif=5
        generate()
        sud.destroy()
    def quit_game_early():
        global early,sud
        early=True
        sud.destroy()
        
    def get():
        global t2,early,user_in,A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9
        for s in [A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9]:
            z=s.get()
            try:
                user_in.append(int(z))
            except:
                user_in.append(0)
        t2=time.time()-t1
        sudmain.destroy()
    sud=tk.Tk()
    sud.title("Sudoku")
    sud.attributes('-fullscreen',True)
    logo=tk.Canvas(sud,bg="black",width=500,height=200,highlightthickness=0)
    logo.pack(pady=20)
    img = tk.PhotoImage(file="sudoku.png",master=sud)
    logo.create_image(0,0,anchor=tk.NW,image=img)
    head=tk.Label(sud,text="Choose difficulty",font='None 20',bg="black",fg="white").pack(pady=10)
    dif1=tk.Button(sud,text="Easy",width=30,command=easy,font='None 20').pack(pady=10)
    dif2=tk.Button(sud,text="Medium",width=30,command=norm,font='None 20').pack(pady=10)
    dif3=tk.Button(sud,text="Hard",width=30,command=hard,font='None 20').pack(pady=10)
    quit_game=tk.Button(sud,text="Quit",width=30,command=quit_game_early,font='None 20').pack(pady=10)
    sud.config(bg="black")
    sud.mainloop()
    if early==True:
        pass
    else:
        sudmain=tk.Tk()
        sudmain.title("Sudoku")
        ent=[]
        A1,A2,A3,A4,A5,A6,A7,A8,A9,B1,B2,B3,B4,B5,B6,B7,B8,B9,C1,C2,C3,C4,C5,C6,C7,C8,C9,D1,D2,D3,D4,D5,D6,D7,D8,D9,E1,E2,E3,E4,E5,E6,E7,E8,E9,F1,F2,F3,F4,F5,F6,F7,F8,F9,G1,G2,G3,G4,G5,G6,G7,G8,G9,H1,H2,H3,H4,H5,H6,H7,H8,H9,I1,I2,I3,I4,I5,I6,I7,I8,I9=tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
        exec("A1.set(0) \nA2.set(0) \nA3.set(0) \nA4.set(0) \nA5.set(0) \nA6.set(0) \nA7.set(0) \nA8.set(0) \nA9.set(0)")
        exec("B1.set(0) \nB2.set(0) \nB3.set(0) \nB4.set(0) \nB5.set(0) \nB6.set(0) \nB7.set(0) \nB8.set(0) \nB9.set(0)")
        exec("C1.set(0) \nC2.set(0) \nC3.set(0) \nC4.set(0) \nC5.set(0) \nC6.set(0) \nC7.set(0) \nC8.set(0) \nC9.set(0)")
        exec("D1.set(0) \nD2.set(0) \nD3.set(0) \nD4.set(0) \nD5.set(0) \nD6.set(0) \nD7.set(0) \nD8.set(0) \nD9.set(0)")
        exec("E1.set(0) \nE2.set(0) \nE3.set(0) \nE4.set(0) \nE5.set(0) \nE6.set(0) \nE7.set(0) \nE8.set(0) \nE9.set(0)")
        exec("F1.set(0) \nF2.set(0) \nF3.set(0) \nF4.set(0) \nF5.set(0) \nF6.set(0) \nF7.set(0) \nF8.set(0) \nF9.set(0)")
        exec("G1.set(0) \nG2.set(0) \nG3.set(0) \nG4.set(0) \nG5.set(0) \nG6.set(0) \nG7.set(0) \nG8.set(0) \nG9.set(0)")
        exec("H1.set(0) \nH2.set(0) \nH3.set(0) \nH4.set(0) \nH5.set(0) \nH6.set(0) \nH7.set(0) \nH8.set(0) \nH9.set(0)")
        exec("H1.set(0) \nH2.set(0) \nH3.set(0) \nH4.set(0) \nH5.set(0) \nH6.set(0) \nH7.set(0) \nH8.set(0) \nH9.set(0)")
        user=[[A1,A2,A3,A4,A5,A6,A7,A8,A9],[B1,B2,B3,B4,B5,B6,B7,B8,B9],[C1,C2,C3,C4,C5,C6,C7,C8,C9],[D1,D2,D3,D4,D5,D6,D7,D8,D9],[E1,E2,E3,E4,E5,E6,E7,E8,E9],[F1,F2,F3,F4,F5,F6,F7,F8,F9],[G1,G2,G3,G4,G5,G6,G7,G8,G9],[H1,H2,H3,H4,H5,H6,H7,H8,H9],[I1,I2,I3,I4,I5,I6,I7,I8,I9]]
        col=dict()
        stat=dict()
        for i in range(9):
            for j in range(9):
                if k[i][j]!=0:
                    user[i][j].set(k[i][j])
                    col.update({(str(['A','B','C','D','E','F','G','H','I'][i])+str(j+1)):"black"})
                    stat.update({(str(['A','B','C','D','E','F','G','H','I'][i])+str(j+1)):"disabled"})
                else:
                    user[i][j].set("")
                    col.update({(str(['A','B','C','D','E','F','G','H','I'][i])+str(j+1)):"red"})
                    stat.update({(str(['A','B','C','D','E','F','G','H','I'][i])+str(j+1)):"normal"})
        play=tk.Label(sudmain,text="PLAY!",fg='white',bg='black',font=300).pack(pady=20)
        pane=tk.Frame(sudmain)
        pane.pack(pady=50)
        blue="lightblue"
        a1,a2,a3,a4,a5,a6,a7,a8,a9=tk.Entry(pane,width=3,font='None 19',fg=col['A1'],state=stat['A1'],textvariable=A1).grid(row=0,column=0),tk.Entry(pane,width=3,fg=col['A2'],state=stat['A2'],textvariable=A2,font='None 19').grid(row=0,column=1),tk.Entry(pane,width=3,fg=col['A3'],state=stat['A3'],textvariable=A3,font='None 19').grid(row=0,column=2),tk.Entry(pane,width=3,fg=col['A4'],state=stat['A4'],textvariable=A4,bg=blue,disabledbackground=blue,font='None 19').grid(row=0,column=3),tk.Entry(pane,width=3,fg=col['A5'],state=stat['A5'],textvariable=A5,bg=blue,disabledbackground=blue,font='None 19').grid(row=0,column=4),tk.Entry(pane,width=3,fg=col['A6'],state=stat['A6'],textvariable=A6,bg=blue,disabledbackground=blue,font='None 19').grid(row=0,column=5),tk.Entry(pane,width=3,fg=col['A7'],state=stat['A7'],textvariable=A7,font='None 19').grid(row=0,column=6),tk.Entry(pane,width=3,fg=col['A8'],state=stat['A8'],textvariable=A8,font='None 19').grid(row=0,column=7),tk.Entry(pane,width=3,fg=col['A9'],state=stat['A9'],textvariable=A9,font='None 19').grid(row=0,column=8)    
        b1,b2,b3,b4,b5,b6,b7,b8,b9=tk.Entry(pane,width=3,font='None 19',fg=col['B1'],state=stat['B1'],textvariable=B1).grid(row=1,column=0),tk.Entry(pane,width=3,fg=col['B2'],state=stat['B2'],textvariable=B2,font='None 19').grid(row=1,column=1),tk.Entry(pane,width=3,fg=col['B3'],state=stat['B3'],textvariable=B3,font='None 19').grid(row=1,column=2),tk.Entry(pane,width=3,fg=col['B4'],state=stat['B4'],textvariable=B4,bg=blue,disabledbackground=blue,font='None 19').grid(row=1,column=3),tk.Entry(pane,width=3,fg=col['B5'],state=stat['B5'],textvariable=B5,bg=blue,disabledbackground=blue,font='None 19').grid(row=1,column=4),tk.Entry(pane,width=3,fg=col['B6'],state=stat['B6'],textvariable=B6,bg=blue,disabledbackground=blue,font='None 19').grid(row=1,column=5),tk.Entry(pane,width=3,fg=col['B7'],state=stat['B7'],textvariable=B7,font='None 19').grid(row=1,column=6),tk.Entry(pane,width=3,fg=col['B8'],state=stat['B8'],textvariable=B8,font='None 19').grid(row=1,column=7),tk.Entry(pane,width=3,fg=col['B9'],state=stat['B9'],textvariable=B9,font='None 19').grid(row=1,column=8)
        c1,c2,c3,c4,c5,c6,c7,c8,c9=tk.Entry(pane,width=3,font='None 19',fg=col['C1'],state=stat['C1'],textvariable=C1).grid(row=2,column=0),tk.Entry(pane,width=3,fg=col['C2'],state=stat['C2'],textvariable=C2,font='None 19').grid(row=2,column=1),tk.Entry(pane,width=3,fg=col['C3'],state=stat['C3'],textvariable=C3,font='None 19').grid(row=2,column=2),tk.Entry(pane,width=3,fg=col['C4'],state=stat['C4'],textvariable=C4,bg=blue,disabledbackground=blue,font='None 19').grid(row=2,column=3),tk.Entry(pane,width=3,fg=col['C5'],state=stat['C5'],textvariable=C5,bg=blue,disabledbackground=blue,font='None 19').grid(row=2,column=4),tk.Entry(pane,width=3,fg=col['C6'],state=stat['C6'],textvariable=C6,bg=blue,disabledbackground=blue,font='None 19').grid(row=2,column=5),tk.Entry(pane,width=3,fg=col['C7'],state=stat['C7'],textvariable=C7,font='None 19').grid(row=2,column=6),tk.Entry(pane,width=3,fg=col['C8'],state=stat['C8'],textvariable=C8,font='None 19').grid(row=2,column=7),tk.Entry(pane,width=3,fg=col['C9'],state=stat['C9'],textvariable=C9,font='None 19').grid(row=2,column=8)
        d1,d2,d3,d4,d5,d6,d7,d8,d9=tk.Entry(pane,width=3,font='None 19',fg=col['D1'],state=stat['D1'],textvariable=D1,bg=blue,disabledbackground=blue).grid(row=3,column=0),tk.Entry(pane,width=3,font='None 19',fg=col['D2'],state=stat['D2'],textvariable=D2,bg=blue,disabledbackground=blue).grid(row=3,column=1),tk.Entry(pane,width=3,fg=col['D3'],state=stat['D3'],textvariable=D3,font='None 19',bg=blue,disabledbackground=blue).grid(row=3,column=2),tk.Entry(pane,width=3,fg=col['D4'],state=stat['D4'],textvariable=D4,font='None 19').grid(row=3,column=3),tk.Entry(pane,width=3,fg=col['D5'],state=stat['D5'],textvariable=D5,font='None 19').grid(row=3,column=4),tk.Entry(pane,width=3,fg=col['D6'],state=stat['D6'],textvariable=D6,font='None 19').grid(row=3,column=5),tk.Entry(pane,width=3,fg=col['D7'],state=stat['D7'],textvariable=D7,bg=blue,disabledbackground=blue,font='None 19').grid(row=3,column=6),tk.Entry(pane,width=3,fg=col['D8'],state=stat['D8'],textvariable=D8,bg=blue,disabledbackground=blue,font='None 19').grid(row=3,column=7),tk.Entry(pane,width=3,fg=col['D9'],state=stat['D9'],textvariable=D9,bg=blue,disabledbackground=blue,font='None 19').grid(row=3,column=8)
        e1,e2,e3,e4,e5,e6,e7,e8,e9=tk.Entry(pane,width=3,font='None 19',fg=col['E1'],state=stat['E1'],textvariable=E1,bg=blue,disabledbackground=blue).grid(row=4,column=0),tk.Entry(pane,width=3,font='None 19',fg=col['E2'],state=stat['E2'],textvariable=E2,bg=blue,disabledbackground=blue).grid(row=4,column=1),tk.Entry(pane,width=3,fg=col['E3'],state=stat['E3'],textvariable=E3,font='None 19',bg=blue,disabledbackground=blue).grid(row=4,column=2),tk.Entry(pane,width=3,fg=col['E4'],state=stat['E4'],textvariable=E4,font='None 19').grid(row=4,column=3),tk.Entry(pane,width=3,fg=col['E5'],state=stat['E5'],textvariable=E5,font='None 19').grid(row=4,column=4),tk.Entry(pane,width=3,fg=col['E6'],state=stat['E6'],textvariable=E6,font='None 19').grid(row=4,column=5),tk.Entry(pane,width=3,fg=col['E7'],state=stat['E7'],textvariable=E7,bg=blue,disabledbackground=blue,font='None 19').grid(row=4,column=6),tk.Entry(pane,width=3,fg=col['E8'],state=stat['E8'],textvariable=E8,bg=blue,disabledbackground=blue,font='None 19').grid(row=4,column=7),tk.Entry(pane,width=3,fg=col['E9'],state=stat['E9'],textvariable=E9,bg=blue,disabledbackground=blue,font='None 19').grid(row=4,column=8)
        f1,f2,f3,f4,f5,f6,f7,f8,f9=tk.Entry(pane,width=3,font='None 19',fg=col['F1'],state=stat['F1'],textvariable=F1,bg=blue,disabledbackground=blue).grid(row=5,column=0),tk.Entry(pane,width=3,font='None 19',fg=col['F2'],state=stat['F2'],textvariable=F2,bg=blue,disabledbackground=blue).grid(row=5,column=1),tk.Entry(pane,width=3,fg=col['F3'],state=stat['F3'],textvariable=F3,font='None 19',bg=blue,disabledbackground=blue).grid(row=5,column=2),tk.Entry(pane,width=3,fg=col['F4'],state=stat['F4'],textvariable=F4,font='None 19').grid(row=5,column=3),tk.Entry(pane,width=3,fg=col['F5'],state=stat['F5'],textvariable=F5,font='None 19').grid(row=5,column=4),tk.Entry(pane,width=3,fg=col['F6'],state=stat['F6'],textvariable=F6,font='None 19').grid(row=5,column=5),tk.Entry(pane,width=3,fg=col['F7'],state=stat['F7'],textvariable=F7,bg=blue,disabledbackground=blue,font='None 19').grid(row=5,column=6),tk.Entry(pane,width=3,fg=col['F8'],state=stat['F8'],textvariable=F8,bg=blue,disabledbackground=blue,font='None 19').grid(row=5,column=7),tk.Entry(pane,width=3,fg=col['F9'],state=stat['F9'],textvariable=F9,bg=blue,disabledbackground=blue,font='None 19').grid(row=5,column=8)
        g1,g2,g3,g4,g5,g6,g7,g8,g9=tk.Entry(pane,width=3,font='None 19',fg=col['G1'],state=stat['G1'],textvariable=G1).grid(row=6,column=0),tk.Entry(pane,width=3,fg=col['G2'],state=stat['G2'],textvariable=G2,font='None 19').grid(row=6,column=1),tk.Entry(pane,width=3,fg=col['G3'],state=stat['G3'],textvariable=G3,font='None 19').grid(row=6,column=2),tk.Entry(pane,width=3,fg=col['G4'],state=stat['G4'],textvariable=G4,bg=blue,disabledbackground=blue,font='None 19').grid(row=6,column=3),tk.Entry(pane,width=3,fg=col['G5'],state=stat['G5'],textvariable=G5,bg=blue,disabledbackground=blue,font='None 19').grid(row=6,column=4),tk.Entry(pane,width=3,fg=col['G6'],state=stat['G6'],textvariable=G6,disabledbackground=blue,bg=blue,font='None 19').grid(row=6,column=5),tk.Entry(pane,width=3,fg=col['G7'],state=stat['G7'],textvariable=G7,font='None 19').grid(row=6,column=6),tk.Entry(pane,width=3,fg=col['G8'],state=stat['G8'],textvariable=G8,font='None 19').grid(row=6,column=7),tk.Entry(pane,width=3,fg=col['G9'],state=stat['G9'],textvariable=G9,font='None 19').grid(row=6,column=8)
        h1,h2,h3,h4,h5,h6,h7,h8,h9=tk.Entry(pane,width=3,font='None 19',fg=col['H1'],state=stat['H1'],textvariable=H1).grid(row=7,column=0),tk.Entry(pane,width=3,fg=col['H2'],state=stat['H2'],textvariable=H2,font='None 19').grid(row=7,column=1),tk.Entry(pane,width=3,fg=col['H3'],state=stat['H3'],textvariable=H3,font='None 19').grid(row=7,column=2),tk.Entry(pane,width=3,fg=col['H4'],state=stat['H4'],textvariable=H4,bg=blue,disabledbackground=blue,font='None 19').grid(row=7,column=3),tk.Entry(pane,width=3,fg=col['H5'],state=stat['H5'],textvariable=H5,bg=blue,disabledbackground=blue,font='None 19').grid(row=7,column=4),tk.Entry(pane,width=3,fg=col['H6'],state=stat['H6'],textvariable=H6,disabledbackground=blue,bg=blue,font='None 19').grid(row=7,column=5),tk.Entry(pane,width=3,fg=col['H7'],state=stat['H7'],textvariable=H7,font='None 19').grid(row=7,column=6),tk.Entry(pane,width=3,fg=col['H8'],state=stat['H8'],textvariable=H8,font='None 19').grid(row=7,column=7),tk.Entry(pane,width=3,fg=col['H9'],state=stat['H9'],textvariable=H9,font='None 19').grid(row=7,column=8)
        i1,i2,i3,i4,i5,i6,i7,i8,i9=tk.Entry(pane,width=3,font='None 19',fg=col['I1'],state=stat['I1'],textvariable=I1).grid(row=8,column=0),tk.Entry(pane,width=3,fg=col['I2'],state=stat['I2'],textvariable=I2,font='None 19').grid(row=8,column=1),tk.Entry(pane,width=3,fg=col['I3'],state=stat['I3'],textvariable=I3,font='None 19').grid(row=8,column=2),tk.Entry(pane,width=3,fg=col['I4'],state=stat['I4'],textvariable=I4,bg=blue,disabledbackground=blue,font='None 19').grid(row=8,column=3),tk.Entry(pane,width=3,fg=col['I5'],state=stat['I5'],textvariable=I5,bg=blue,disabledbackground=blue,font='None 19').grid(row=8,column=4),tk.Entry(pane,width=3,fg=col['I6'],state=stat['I6'],textvariable=I6,disabledbackground=blue,bg=blue,font='None 19').grid(row=8,column=5),tk.Entry(pane,width=3,fg=col['I7'],state=stat['I7'],textvariable=I7,font='None 19').grid(row=8,column=6),tk.Entry(pane,width=3,fg=col['I8'],state=stat['I8'],textvariable=I8,font='None 19').grid(row=8,column=7),tk.Entry(pane,width=3,fg=col['I9'],state=stat['I9'],textvariable=I9,font='None 19').grid(row=8,column=8)
        t1=time.time()
        t2=None
        sudmain.config(bg="black")
        user_in=[]
        sub=tk.Button(sudmain,text="Submit",command=get,font=80).pack()
        rule=tk.Label(sudmain,text=rules,bg="black",fg="RED",font="None 20").pack()
        sudmain.attributes('-fullscreen',True)
        sudmain.mainloop()
        correct=[]
        

        
        for h in sol:
            for g in h:
                correct.append(g)
        res=(correct==user_in)
        if res==True:
            res="Yes!"
            sn="green"
        else:
            res="No..."
            sn="red"
    
        def end_game():
            global early
            early=False
            result.destroy()
        
        result=tk.Tk()
        result.title("Sudoku Result")
        sp=tk.Label(result,text="\n \n",font=100,bg="black",fg=sn)
        sp.pack()
        mes=tk.Label(result,text="Did you get it right?",font=100,bg="black",fg="white")
        mes.pack()
        mes1=tk.Label(result,text=res,font=100,bg="black",fg=sn)
        mes1.pack()
        if res=="Yes!":
            mes2=tk.Label(text="Time Taken To Complete",fg="white",bg="black",font=100).pack()
            mes3=tk.Label(text=str(int(t2)+1)+" Seconds",fg="Blue",bg="black",font=100).pack()
        sp1=tk.Label(result,text="\n",font=100,bg="black",fg="white")
        sp1.pack()
        ex=tk.Button(result,text="Exit",font=100,fg="black",command=end_game)
        ex.pack()
        result.attributes('-fullscreen',True)
        result.config(bg="black")
        result.mainloop()