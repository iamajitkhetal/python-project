import datetime
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
#========================Variable==============
        self.member_var=StringVar()
        self.pnr_var=StringVar()
        self.id_var=StringVar()
        self.firstnamer_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()










        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
#================= DataFrame lef ==========
        DataFrameleft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="Black",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameleft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameleft,bg="powder blue",text="Member Type",textvariable=self.member_var,font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameleft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameleft,font=("arial",12,"bold"),text="PRN No",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.pnr_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameleft,font=("arial",12,"bold"),text="ID No",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        lblTitle=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.id_var,width=29)
        lblTitle.grid(row=2,column=1)
     
        lblFirstName=Label(DataFrameleft,font=("arial",12,"bold"),text="First Name",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.firstnamer_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameleft,font=("arial",12,"bold"),text="Last Name",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameleft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameleft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostalCode=Label(DataFrameleft,font=("arial",12,"bold"),text="Postal Code",padx=2,pady=6,bg="powder blue")
        lblPostalCode.grid(row=7,column=0,sticky=W)
        txtPostalCode=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=29)
        txtPostalCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameleft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameleft,font=("arial",12,"bold"),text="Book Id",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameleft,font=("arial",12,"bold"),text="Book Title",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtMobile.grid(row=1,column=3)

        lblAuther=Label(DataFrameleft,font=("arial",12,"bold"),text="Auther Name",padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameleft,font=("arial",12,"bold"),text="Date of Borrowed",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameleft,font=("arial",12,"bold"),text="Date Due",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)


        lblDaysOnBook=Label(DataFrameleft,font=("arial",12,"bold"),text="Days on Book",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameleft,font=("arial",12,"bold"),text="Late Return Fine",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameleft,font=("arial",12,"bold"),text="Date Over Due",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameleft,font=("arial",12,"bold"),text="Actual Price",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=7,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameleft,font=("arial",12,"bold"),width=29)
        txtActualPrice.grid(row=7,column=3)
        


#=============DataFrame Right =======
        
        DataFrameright=LabelFrame(frame,text="Book Details",bg="powder blue",fg="Black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameright.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameright,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listscrollbar=Scrollbar(DataFrameright)
        listscrollbar.grid(row=0,column=1,sticky='ns')


        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','secret Rashy','Python CookBook','Machine Techno',                                             
                    "Machine Tool","Elite in Python",'My Python','Inton Python','Advance Python','Redchilli Python','Joss Ellife Guru']
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Jame Kenny")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")

            elif (x=="Python Programming"):
                self.bookid_var.set("BKID003")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")
            
            elif (x=='secret Rashy'):
                self.bookid_var.set("BKID004")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Kine Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")


            elif (x=='Python CookBook'):
                self.bookid_var.set("BKID005")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")

            elif (x=='secret Rashy'):
                self.bookid_var.set("BKID006")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")

            
            elif (x== 'Machine Techno'):
                self.bookid_var.set("BKID007")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("jilly Mike")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(day=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs 788")       
 
            
            



        listBox=Listbox(DataFrameright,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
    





# ================ Button Frame ===============
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(Framebutton,text='Add Data',command=self.add_data,font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text='Show Data',font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text='Update',font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text='Delet',command=self.delet,font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text='Reset',font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text='Exit',command=self.iExit,font=("arial",12,"bold"),width=23,bg='blue',fg='White')
        btnAddData.grid(row=0,column=5)






# ================ Info Frame ===============
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg='powder blue')
        Table_frame.place(x=0,y=2,width=1460,height=190)
         
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)




        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile",
                                                            "bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=xscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

 

    def add_data(self):
        conn=mysql.connector.Connect(host='localhost',username='root',password='root',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("inser into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                               self.member_var.get(),
                                                                                                               self.pnr_var.get(),
                                                                                                               self.id_var.get(),
                                                                                                               self.firstnamer_var.get(),
                                                                                                               self.lastname_var.get(),
                                                                                                               self.address1_var.get(),
                                                                                                               self.address2_var.get(),
                                                                                                               self.postcode_var.get(),
                                                                                                               self.mobile_var.get(),
                                                                                                               self.bookid_var.get(),
                                                                                                               self.booktitle_var.get(),
                                                                                                               self.auther_var.get(),
                                                                                                               self.dateborrowed_var.get(),
                                                                                                               self.daysonbook_var.get(),
                                                                                                               self.latereturnfine_var.get(),
                                                                                                               self.finalprice_var.get(),))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted succesfully")
    def update(self):
        conn=mysql.connector.Connect(host='localhost',username='root',password='root',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,Booktitle=%s,Auther=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                
                                                                                                               self.member_var.get(),
                                                                                                               self.firstnamer_var.get(),
                                                                                                               self.lastname_var.get(),
                                                                                                               self.address1_var.get(),
                                                                                                               self.address2_var.get(),
                                                                                                               self.postcode_var.get(),
                                                                                                               self.mobile_var.get(),
                                                                                                               self.bookid_var.get(),
                                                                                                               self.booktitle_var.get(),
                                                                                                               self.auther_var.get(),
                                                                                                               self.dateborrowed_var.get(),
                                                                                                               self.daysonbook_var.get(),
                                                                                                               self.latereturnfine_var.get(),
                                                                                                               self.finalprice_var.get(),
                                                                                                               self.pnr_var.set()))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        

        if len(rows)!=0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                        self.library_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.pnr_var.set(row[1]),
        self.firstnamer_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])




    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.pnr_var.get()+"\n")
        self.txtBox.insert(END,"ID No\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstnamer_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.set()+"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther\t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice_var.get()+"\n")



    def reset(self):
        self.member_var.set(""),
        self.pnr_var.set(""),
        self.id_var.set(""),
        self.firstnamer_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END),


    def iExit(self):
        iExit=tkinter.Messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delet(self):
        if self.pnr_var.get()=="" or self.id_var.get()== "":
                messagebox.showerror("Error","FIrst select the Member")
        else:
                conn=mysql.connector.Connect(host='localhost',username='root',password='root',database='mydata')
                my_cursor=conn.cursor()
                query="delet from library where PRN_no=%s"
                value=(self.pnr_var.get())
                my_cursor.execute(query,value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been deleted")




    



      



        
    
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    
     
    

    