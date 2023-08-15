from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import student
import os
from train import Train




class Face_Recpgnization_System:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Face Recognization System")
        
        # First Image
        img=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/image1.jpeg")
        img=img.resize((500,200))
        self.photoimag=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimag)
        f_lbl.place(x=0,y=0,width=500,height=200)


        # Second Image
        img2=Image.open(r"//Users/safirahmad/Desktop/Advance face recognization system /images/image 6.jpeg")
        img2=img2.resize((500,200))
        self.photoimag2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimag2)
        f_lbl.place(x=501,y=0,width=500,height=200)


        # Thirst Image
        img3=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/image4.webp")
        img3=img3.resize((500,200))
        self.photoimag3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimag3)
        f_lbl.place(x=1001,y=0,width=500,height=200)


        # Background Image
        img4=Image.open(r"//Users/safirahmad/Desktop/Advance face recognization system /images/iamge 3.png")
        img4=img4.resize((1530,820))
        self.photoimag4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimag4)
        bg_img.place(x=0,y=200,width=1530,height=820)


        title_lbl=Label(bg_img,text="ADVANCED FACE RECOGNIZATION ATTENDANCE SYSTEM SOFTWARE",font=("Exo",30,"bold"), fg="white")
        title_lbl.place(x=0,y=-1,width=1520,height=50)


        # Student Button 
        img5=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy.webp")
        img5=img5.resize((500,200))
        self.photoimag5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimag5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Student details",command=self.student_details, cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)




        # Face Detection Button 
        img6=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/image4.webp")
        img6=img6.resize((500,200))
        self.photoimag6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimag6,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detection", cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Attandance  Button 
        img7=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/00980284_medium.jpeg")
        img7=img7.resize((500,200))
        self.photoimag7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimag7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Attandance", cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)


         # Help Desk  Button 
        img8=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy 2.webp")
        img8=img8.resize((500,200))
        self.photoimag8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimag8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)


         # Train  Button 
        img9=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/image7.webp")
        img9=img9.resize((500,200))
        self.photoimag9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimag9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data ,cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=200,y=600,width=220,height=40)


         # Photo  Button 
        img10=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy 3.webp")
        img10=img10.resize((500,200))
        self.photoimag10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimag10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Photo Data", cursor="hand2",command=self.open_img,font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=500,y=600,width=220,height=40)

         # Developer  Button 
        img11=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (2).webp")
        img11=img11.resize((500,200))
        self.photoimag11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimag11,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Developer", cursor="hand2",font=("Exo",15,"bold"), fg="black")
        b1_1.place(x=800,y=600,width=220,height=40)


         # Exit  Button 
        img12=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (4).webp")
        img12=img12.resize((500,200))
        self.photoimag12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimag12,cursor="hand2",command=self.open_img)
        b1.place(x=1100,y=400,width=220,height=200)

        b1_1=Button(bg_img,text="Exit", cursor="hand2",font=("Exo",15,"bold"),command=self.open_img, fg="black")
        b1_1.place(x=1100,y=600,width=220,height=40)
    

        

  
    
    def open_img(self):
        
        folder_path = "/Users/safirahmad/Desktop/Advance face recognization system /data"
        os.path(folder_path)



        

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    
    
    
        
     
#==================Generate data set or Take Photo Sample===========

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recpgnization_System(root)
    root.mainloop()




