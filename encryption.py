import tkinter.filedialog as files
from tkinter import *
from tkinter import messagebox
import os 
from PIL import ImageTk,Image
root=Tk()
root.geometry('600x600')
root.configure(bg='#a88532')
root.iconbitmap('assets\pirate_treasure.ico')
inp_var=StringVar()
root.title("Treasure")
def data_encode(data):
   binary_codes=[]
   for i in data:
      binary_codes.append(format(ord(i),'08b'))
   return binary_codes 
def change_pix(img,data):
       modified_data=data_encode(data)
       data_length=modified_data.__len__()
       imgdata=iter(img)
       for i in range(data_length):
        pix=[value for value in imgdata.__next__()[:3]+imgdata.__next__()[:3]+imgdata.__next__()[:3]]
        for j in range(0,8):
             if (modified_data[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
             elif (modified_data[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if (i == data_length - 1):
         if (pix[-1] % 2 == 0):
               if(pix[-1] != 0):
                  pix[-1] -= 1
               else:
                 pix[-1] += 1
 
        else:
         if (pix[-1] % 2 != 0):
            pix[-1] -= 1        
        pix = tuple(pix)
        yield pix[0:3] 
        yield pix[3:6]
        yield pix[6:9]
        
       
       
def encryption(img,data):
     wd=img.size[0]
     (x,y)=(0,0)
     for pixel in change_pix(img.getdata(),data):
          img.putpixel((x, y), pixel)
          if (x == wd - 1):
            x = 0
            y += 1
          else:
            x += 1
        
     
def Data_collection():
    
    filebox=files.askopenfile(filetypes=[('images','*.png *.jpeg *jpg')])
    imagepath=os.path.realpath(filebox.name)
    if filebox:
       img=Image.open(imagepath,mode='r')
       err_img=Image.open('assets/tryagain.jpg')
       messagebox.showinfo("File",f"you selected {imagepath}")
       input_data=input_entry.get()
       if (len(input_data)==0):
         messagebox.showerror("Input","give input")
         return imageHolder(False,err_img)
       
      
    else:
          messagebox.showerror("Error","You havenot selected any file")
    encryption(img,input_data)
    imageHolder(True, img)   
    img.save("encryptedimage.png")
def imageHolder(a,img):
         enctxt=Label(root,text="Encrypted Text",bg='#a88532',font=('bold',10))
         enctxt.grid(row=4,column=1)
         can=Canvas(root,height=300,width=300)
         can.grid(column=1,row=5)
         
         if(a==False):
          resize_image=img.resize((300,300),Image.ANTIALIAS)
         else:
            resize_image=img.resize((300,300),Image.ANTIALIAS)  
         can.image=ImageTk.PhotoImage(resize_image)
         can.create_image(0,0,image=can.image,anchor='nw')
def decryption():
    image = Image.open('encryptedimage.png',mode='r') 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data     
def decryptedtext():
    data=decryption()
    messagebox.showinfo("Decrypted text",data)                
label1 = Label(root, text = 'Encrypt With Image', font=('calibre',30, 'bold',),bg='#a88532')    
input_label = Label(root, text = 'Plain text', font=('calibre',10, 'bold'),bg='#a88532')
input_entry = Entry(root,textvariable = inp_var, font=('calibre',10,'normal'),width=50)
btn= Button(text="Encrypt",command=lambda:Data_collection(),bg='red',width=15,font=('bold'))
btn2= Button(text="Decrypt",command=lambda:decryptedtext(),bg='red',width=15,font=('bold'))
label1.grid(row=0,column=1,pady=20) 
input_label.grid(row=1,column=0,pady=20,padx=10)
input_entry.grid(row=1,column=1,pady=20)
btn.grid(row=2,column=1,pady=5)
btn2.grid(row=3,column=1)
root.maxsize(600,600)
root.mainloop()


