import tkinter as tk
from tkinter import ttk
import random as rd
import os


    
def notepad_launch(window,trt="",bol=True):
    global directory_files
    notepad=tk.Tk()
    button_pane=tk.Frame(notepad)
    button_pane.pack(pady=20)
    directory_files=os.listdir("D:/PyOS/New Compile Fix/Notes")
    def save():
        global cv
        text=TextArea.get("1.0",tk.END)
        save_window=tk.Tk()
        lab=tk.Label(save_window,text="Enter file name:").grid(row=0,column=0)
        fil_name=tk.Entry(save_window)
        fil_name.grid(row=0,column=1)
        cv=tk.StringVar(save_window)
        format=ttk.Combobox(save_window,textvariable=cv,width=10,values=(".py",".txt"))
        format.current(1)
        format.grid(row=0,column=2)
        def sav_fil():
            global cv
            name=os.path.join("D:/PyOS/New Compile Fix/Notes/",str(fil_name.get())+cv.get())
            f=open(name,"w")
            if (str(fil_name.get())+cv.get()) in directory_files:
                h=tk.messagebox.askyesnocancel(title="Warning", message="File With Same Name Exists In Directory.\nDo You Wish To Overwrite?")
                if h==True:
                    f.write(text)
                    f.close()
                    save_window.destroy()
                    notepad.destroy()
                elif h==False:
                    save_window.destroy()
                    save()
                else:
                    save_window.destroy()
            else:
                f.write(text)
                f.close()
                save_window.destroy()
                notepad.destroy()
        fil_sav=tk.Button(save_window,text="Save File",command=sav_fil).grid(row=1,column=1)
        
        save_window.mainloop()
    def open_note():
        global directory_files,n
        if len(directory_files)==0:
            h=tk.messagebox.showinfo(title="Warning", message="No File In Directory")
        else:
            open_window=tk.Tk()
            n=tk.StringVar(open_window)
            list_files=ttk.Combobox(open_window,textvariable=n,values=tuple(directory_files)).pack()
            def get_file():
                global z,n
                z=n.get()
                file_dir=os.path.join("D:/Computer Science Project Class XII-A/New Compile Fix/Notes/",str(z))
                file_text=open(file_dir).read()
                notepad.destroy()
                open_window.destroy()
                notepad_launch(window,file_text,bol=False)
            lab=tk.Label(open_window,text="Choose File")
            but=tk.Button(open_window,text="Open",command=get_file).pack()
            open_window.mainloop()
    sav=tk.Button(button_pane,text='Save As',font=40,width=10,command=save).grid(row=0,column=1,padx=10)
    ope=tk.Button(button_pane,text='Open',font=40,width=10,command=open_note).grid(row=0,column=2,padx=10)
    ex=tk.Button(button_pane,text='Exit',font=40,width=10,command=notepad.destroy).grid(row=0,column=3,padx=10)
    button_pane.config(bg="grey")
    write_pane=tk.Frame(notepad)
    write_pane.pack(pady=20)
    TextArea = tk.Text(write_pane,height=40,width=130,wrap=tk.NONE,bg="black",fg="white",insertbackground="white",font=40)
    TextArea.insert(tk.END,trt)
    ScrollBary= tk.Scrollbar(write_pane)
    ScrollBary.config(command=TextArea.yview)
    ScrollBarx= tk.Scrollbar(write_pane,orient="horizontal")
    ScrollBarx.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=ScrollBarx.set,yscrollcommand=ScrollBary.set)
    ScrollBary.pack(side=tk.RIGHT, fill=tk.Y)
    ScrollBarx.pack(side=tk.BOTTOM, fill=tk.X)
    TextArea.pack(expand=tk.YES, fill=tk.BOTH)
    notepad.config(bg="grey")
    notepad.attributes('-fullscreen',True)
    notepad.mainloop()
    if bol==True:
        window()
