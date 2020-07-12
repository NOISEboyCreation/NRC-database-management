from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import newtwo


class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("NATIONAL REGISTATION OF CITIZENS")
        self.root.geometry("1350x800+0+0")

        
        CusID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address=StringVar()
        PostCode =StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB =StringVar()
        Gender =StringVar()
        global hd
        title=Label(self.root,text="WELCOME TO BE A PART OF INDIAN CITIZEN",bd=10,relief=GROOVE, font=("time new roman",40,"bold"),bg="yellow",fg="blue")
        title.pack(side=TOP,fill=X)
        
        LeftFrame=Frame(self.root,bd=5,relief=RIDGE,bg="crimson")#,bg="crimson"
        LeftFrame.place(x=20,y=100,width=470,height=550)
        RightFrame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        RightFrame.place(x=520,y=100,width=820,height=550)
        RightFrame2=Frame(RightFrame,bd=4,relief=RIDGE)
        RightFrame2.place(x=25,y=70,width=760,height=450)
        BottomFrame = Frame(self.root, bd=10, width=1350,height=150, padx=2, relief=RIDGE,bg="crimson")
        BottomFrame.pack(side=BOTTOM,fill=X)




        def iExit():
                iExit = tkinter.messagebox.askyesno("Addhar Management Systems", "Do you want to exit")
                if iExit > 0:
                    root.destroy()
                    return
        def Reset():
            Nationality.set("")
            Gender.set("")
            self.txtCusID.delete(0,END)
            self.txtDOB.delete(0,END)
            self.txtEmail.delete(0,END)  
            self.txtFirstname.delete(0,END)
            self.txtSurname.delete(0,END)      
            self.txtAddress.delete(0,END) 
            self.txtPostCode.delete(0,END)    
            self.txtMobile.delete(0,END) 
        def addData():
            if(len(CusID.get())!=0):
                newtwo.addHotelRec(CusID.get(), Firstname.get(),  Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                     Nationality.get(),Email.get())
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(), Firstname.get(),  Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                     Nationality.get(),Email.get()))

        def DisplayData():
            lstHotel.delete(0,END)
            for row in newtwo.viewData():
                lstHotel.insert(END,row,str(" "))




        def HotelRec(event):
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb )

            self.txtCusID.delete(0,END)
            self.txtCusID.insert(END,hd[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,hd[2])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,hd[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,hd[4])
            self.cboGender.delete(0,END)
            self.cboGender.insert(END,hd[5])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,hd[6])            
            self.cboNationality.delete(0,END)
            self.cboNationality.insert(END,hd[7])
            self.txtEmail.delete(0,END)
            self.txtEmail.insert(END,hd[8]) 
            

        def DeleteData():
            if(len(CusID.get())!=0):
                newtwo.deleteRec(hd[0] )
                Reset()
                DisplayData()

        def searchDatabase():
            lstHotel.delete(0,END)
            for row in newtwo.searchData(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),Email.get()):
                lstHotel.insert(END,row,str(" "))


        def update():
            if(len(CusID.get())!=0):
                newtwo.deleteRec(hd[0])
            if(len(CusID.get())!=0):                
                newtwo.addHotelRec(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),Email.get())           
                lstHotel.delete(0,END)            
                lstHotel.insert(END,(CusID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),
                                      Nationality.get(),Email.get()))










                
        
#===================================widget============
        self.m_title=Label(LeftFrame,text="_NRC Database System_",bg="orange",fg="white",font=("times new roman",30,"bold"),bd=5,relief=GROOVE)
        self.m_title.grid(row=0,columnspan=2,pady=20,padx=11,sticky="w")
        
        self.lblCusID =Label(LeftFrame, font=('arial',20,'bold'),text="Addhar No:",fg="white",bg="crimson",padx=1)
        self.lblCusID.grid(row=1,column=0, sticky =W)
        self.txtCusID =Entry(LeftFrame, font=('arial',15,'bold'),textvariable =CusID,width =18)
        self.txtCusID.grid(row=1,column=1,pady=3, padx=20)

        self.lblFirstname =Label(LeftFrame, font=('arial',20,'bold'),text="Firstname:",fg="white",bg="crimson",padx=1)
        self.lblFirstname.grid(row=2,column=0, sticky =W)
        self.txtFirstname =Entry(LeftFrame, font=('arial',15,'bold'),textvariable =Firstname,width =18)
        self.txtFirstname.grid(row=2,column=1,pady=3, padx=20)

        self.lblSurname =Label(LeftFrame, font=('arial',20,'bold'),text="Surname:",fg="white",bg="crimson",padx=1)
        self.lblSurname.grid(row=3,column=0, sticky =W)
        self.txtSurname =Entry(LeftFrame, font=('arial',15,'bold'),textvariable =Surname,width =18)
        self.txtSurname.grid(row=3,column=1,pady=3, padx=20)

        self.lblAddress =Label(LeftFrame, font=('arial', 20,'bold'), text="Indian Address:",fg="white",bg="crimson",padx=1,pady=2 )
        self.lblAddress.grid(row=4, column=0,sticky=W)
        self.txtAddress=Entry(LeftFrame, font=('arial', 15,'bold'),textvariable = Address, width =18)
        self.txtAddress.grid(row=4, column=1, pady=3, padx=20)
        
        self.lblDOB =Label(LeftFrame, font=('arial', 20,'bold'), text="Date of Birth:",fg="white",bg="crimson",padx=2,pady=2)
        self.lblDOB.grid(row=5, column=0,sticky=W)
        self.txtDOB=Entry(LeftFrame, font=('arial', 15,'bold'),textvariable = DOB, width =18)
        self.txtDOB.grid(row=5, column=1, pady=3, padx=20)

        self.lblPostCode =Label(LeftFrame, font=('arial', 20,'bold'), text="Comming Date:",fg="white",bg="crimson",padx=2,pady=2 )
        self.lblPostCode.grid(row=6, column=0,sticky=W)
        self.txtPostCode=Entry(LeftFrame, font=('arial', 15,'bold'),textvariable = PostCode, width =18)
        self.txtPostCode.grid(row=6, column=1, pady=3, padx=20)

        self.lblMobile =Label(LeftFrame, font=('arial', 20,'bold'), text="Mobile No:",fg="white",bg="crimson",padx=2,pady=2)
        self.lblMobile.grid(row=7, column=0,sticky=W)
        self.txtMobile=Entry(LeftFrame,font=('arial', 15,'bold'),textvariable = Mobile,width =18)
        self.txtMobile.grid(row=7, column=1, pady=3, padx=20)

        self.lblEmail =Label(LeftFrame, font=('arial', 20,'bold'), text="Email:",fg="white",bg="crimson",padx=2,pady=2)
        self.lblEmail.grid(row=8, column=0,sticky=W)
        self.txtEmail=Entry(LeftFrame, font=('arial', 15,'bold'),textvariable = Email, width =18)
        self.txtEmail.grid(row=8, column=1, pady=3, padx=20)

        self.lblNationality =Label(LeftFrame,font=('arial',20,'bold'),text="Nationality:",fg="white",bg="crimson",padx=2,pady=2)
        self.lblNationality .grid(row=9, column=0,sticky=W)
        self.cboNationality =ttk.Combobox(LeftFrame, state='readonly', font=('arial', 15,'bold'),textvariable = Nationality,width=16)                                        
        self.cboNationality['value']=('','Pakistan','Bangladesh','Nepal','Sri Lanka','Afganistan','Mayamar','Bangladesh', 'China')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=9,column=1,pady=3,padx=2)



        self.lblGender =Label(LeftFrame, font=('arial', 20,'bold'), text="Gender:",fg="white",bg="crimson",padx=2,pady=2)
        self.lblGender.grid(row=10, column=0,sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame, state='readonly',font=('arial', 15,'bold'),textvariable = Gender, width=16)
        self.cboGender['value']=(' ','Male','Female','Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=10, column=1, pady=3, padx=2)
#=====================================================================================================
#===========================================widget==================================

        self.lblLabel=Label(RightFrame,text="_ADDHAR NO\tFirstname Surname\tAddress\tDate of Dirth\tGender\tMobile\tNationality\tEmail_",bg="orange",fg="white",font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        self.lblLabel.grid(row=0, column=0,columnspan=10,pady=20,padx=25,sticky="w")

        

#=========================================Listbox and Scrollbar=======Receipt========================================

        

        
        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=1, sticky ='ns')

        lstHotel = Listbox(RightFrame2, width = 81, height=22, font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)
        lstHotel.bind('<<ListboxSelect>>',HotelRec)
        lstHotel.grid(row=0, column=0)
        scrollbar.config(command = lstHotel.yview)
#==========================================================button============================================

        self.btnTotalandAddData=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
            width=13,height=2,text="AddNew",command=addData).grid(row=0, column=0,padx=4)

        self.btnDisplay=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Display",command=DisplayData).grid(row=0, column=1,padx=4)

        self.btnUpdate=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Update",command=update).grid(row=0, column=2,padx=4)

        self.btnDelete=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Delete",command=DeleteData).grid(row=0, column=3,padx=4)


        self.btnSearch=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Search",command=searchDatabase).grid(row=0, column=4,padx=3)

        self.btnReset=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                            width=13,height=2,text="Reset",command=Reset).grid(row=0, column=5,padx=4)

        self.btnExit=Button(BottomFrame,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),
                    width=13,height=2, text="Exit",command=iExit).grid(row=0, column=6,padx=4)

        
        









if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()
