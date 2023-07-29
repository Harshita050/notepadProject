from tkinter import *
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename,askopenfilename
root=Tk()
def newfile():
    global file 
    root.title("Untitled 1")
    file=NONE
    Textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes = [("All Files","*.*"),  ("Text Documents", "*.txt")])
    if file == "":
       file=NONE
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()

def quit():
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad as a python project")
root.geometry("400x500")
root.title("Untitled.txt")
Textarea=Text(root,font="lucida 13")
file=None
Textarea.pack(expand=True,fill=BOTH)
Menubar=Menu(root)
FileMenu=Menu(Menubar,tearoff=0)
FileMenu.add_command(label="New",command=newfile)
FileMenu.add_command(label="Open",command=openfile)
FileMenu.add_command(label="Save",command=savefile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=quit)
Menubar.add_cascade(label="File",menu=FileMenu)
root.config(menu=Menubar)

EditMenu=Menu(Menubar,tearoff=0)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)
Menubar.add_cascade(label="Edit",menu=EditMenu)

viewMenu=Menu(Menubar,tearoff=0)
viewMenu.add_command(label="About",command=about)
Menubar.add_cascade(label="View",menu=viewMenu)

root.config(menu=Menubar)
scrollbar=Scrollbar(Textarea)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scrollbar.set)
root.mainloop()