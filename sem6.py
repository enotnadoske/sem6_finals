from tkinter import *
from tkinter import filedialog as fd
import subprocess
 
def insertText():
    file_name = fd.askopenfilename()
    result = subprocess.run(["xxd", "-g1", file_name], stdout=subprocess.PIPE)
    text.insert(1.0    , result.stdout)
 
def extractText():
    pass
def onlyExtractText():
    pass   
 
root = Tk()
text = Text(width = 100, height = 50)
text.grid(columnspan = 3)
b1 = Button(text = "open", command = insertText)
b1.grid(row = 1, sticky = E)
b2 = Button(text = "save as", command = extractText)
b2.grid(row = 1, column=2, sticky = W)
b3 = Button(text = "save", command = onlyExtractText)
b3.grid(row = 1, column = 1, sticky = S)
 
root.mainloop()
