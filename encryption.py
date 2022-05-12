import tkinter.filedialog as files
from tkinter import *
import os 
from PIL import ImageTk,Image
root=Tk()
root.geometry('500x500')

root.title("Treasure")
def selectFile():
    filebox=files.askopenfile(filetypes=[('images','*.png *.jpeg')])

    if filebox:
       imagepath=os.path.realpath(filebox.name)
       can=Canvas(root,bg='black',height=250,width=300)
       can.pack(expand=YES,fill=BOTH)
       img=Image.open(imagepath)
       can.image=ImageTk.PhotoImage(img)
       can.create_image(0,0,image=can.image,anchor=NW)
    

btn= Button(text="select file",command=selectFile)
btn.pack(side=TOP,pady=80)    
root.mainloop()


