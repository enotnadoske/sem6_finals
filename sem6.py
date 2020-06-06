from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import subprocess

def insertText():
    try:
        global file_name 
        file_name = fd.askopenfilename()
        l1.configure(text = str(file_name))
        text.delete(1.0, END)
        result = subprocess.run(["xxd", "-g1", file_name], stdout=subprocess.PIPE)
        text.insert(1.0, result.stdout)
    except:
        mb.showerror("Error", "Something went wrong with file opening")  
 
def extractText():
    try:
        file_name = fd.asksaveasfilename()
        s = text.get(1.0, END)
        result = subprocess.run(["xxd", "-r","-", file_name], input = s.encode())  
    except:
        mb.showerror("Error", "Something went wrong with saving")              

def onlyExtractText():
    try:
        global file_name
        s = text.get(1.0, END)
        l1.configure(text = "File:")
        result = subprocess.run(["xxd", "-r","-", file_name], input = s.encode())  
        text.delete(1.0, END)
    except:
        mb.showerror("Error", "Something went wrong with saving")  
    

file_name = "" 
root = Tk()
text = st.ScrolledText(width = 100, height = 50)
text.grid(columnspan = 3, row = 0)
b1 = Button(text = "open", command = insertText)
b1.grid(row = 1, sticky = E)
b2 = Button(text = "save as", command = extractText)
b2.grid(row = 1, column=2, sticky = W)
b3 = Button(text = "save", command = onlyExtractText)
b3.grid(row = 1, column = 1, sticky = S)
l1 = Label(text = "File: ") 
l1.grid(row = 2, sticky = W+N+S)
root.mainloop()
