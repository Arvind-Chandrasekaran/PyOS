import calculator_pyos
import tax_pyos
import tkinter as tk
import sudoku
import notepad_pyos
from datetime import datetime
def menu_launch():
    global time_refresh
    menu=tk.Tk()
    def exit_menu():
        menu.destroy()
    cross=tk.PhotoImage(file=r"D:\Computer Science Project Class XII-A\New Compile Fix\cross.png")
    exit_button=tk.Button(menu,text="Exit",command=exit_menu,font="None 20",image=cross,bg="black").place(x=0,y=0)
    logo=tk.Canvas(menu,bg="black",width=231,height=231,highlightthickness=0)
    logo.pack(pady=50)
    img = tk.PhotoImage(file="Logo1.png",master=menu)
    logo.create_image(0,0,anchor=tk.NW,image=img)

    def calc_launch():
        menu.destroy()
        calculator_pyos.calculator(menu_launch)        
    def tax_launch():
        menu.destroy()
        tax_pyos.tax(menu_launch)
    def notepad_start():
        menu.destroy()
        notepad_pyos.notepad_launch(menu_launch)
    def sud_game():
        menu.destroy()
        sudoku.sudoku_game()
        menu_launch()
    
    
    clock_frame=tk.Frame(menu,bg="black")
    clock_frame.pack()
    time_panel=tk.Label(clock_frame,borderwidth=1,text='',bg="black",fg="red",anchor='nw',relief="solid",font=('None 40 bold'))
    time_panel.pack()
    def time_refresh():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")
        time_panel.config(text=current_time)
        time_panel.after(1000,time_refresh)
    try:
        time_refresh()
    except:
        pass
    
    button_box=tk.Frame(menu,bg="black")
    button_box.pack()
    calculator_button=tk.Button(button_box,text="Calculator",width=30,command=calc_launch,font="None 20").pack(side=tk.TOP,pady=5)
    tax_button=tk.Button(button_box,text="Tax Calculator",width=30,command=tax_launch,font="None 20").pack(side=tk.TOP,pady=5)  
    sud_button=tk.Button(button_box,text="Sudoku",width=30,command=sud_game,font="None 20").pack(side=tk.TOP,pady=5)
    notepad_button=tk.Button(button_box,text="Notepad",width=30,command=notepad_start,font="None 20").pack(side=tk.TOP,pady=5)
    

    
    menu.config(bg="black")
    menu.title("PyOS")
    menu.attributes('-fullscreen',True)
    menu.mainloop()
    
    