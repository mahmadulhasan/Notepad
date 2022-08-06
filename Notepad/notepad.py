from tkinter import*
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


#functions start

def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)
    
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "."),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0, END)
        f=open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    
    
def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "."),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            #save as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " -Notepad")
            print("file saved")

    else:
        #save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by MAHMADUL HASAN")



#function end


#------------------------------------------------------------------------------



if __name__ == '__main__':
    #basic thinter setup

    root = Tk()
    root.title("Untitled - Nodepad")
    root.wm_iconbitmap("1.jpg")
    root.geometry("600x750")

    #add text area
    TextArea = Text(root, font="lucida 13")
    #will point the file about to open
    file = None
    TextArea.pack(expand= True, fill=BOTH)

    #creat a menubar
    Menubar = Menu(root)
#file menu start
    FileMenu = Menu(Menubar, tearoff=0)

    #to open new file
    FileMenu.add_command(label="New", command=newFile)

    #to open existing file
    FileMenu.add_command(label="Open", command = openFile)

    #to save the current file
    FileMenu.add_command(label="Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command = quitApp)
    Menubar.add_cascade(label = "file", menu= FileMenu)
#file menu ends

#Edit menu start

    EditMenu= Menu(Menubar, tearoff=0)
    #cut, copy, paste feature
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit", menu=EditMenu)

#Edit menu end

#Help menu start
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)


#help menu end
    root.config(menu=Menubar)

    #adding Scrollbar
    Scroll= Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()
