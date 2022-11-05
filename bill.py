

from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Bill managing by @invincible")
        
        self.cus_name = StringVar()
        self.c_phone = StringVar()

        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()

        self.c_bill_no.set(str(x))

        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()
        self.bath_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maza = IntVar()

        bg_color = "#5B2C6F"
        fg_color = "white"
        lbl_color = 'white'
        title = Label(self.root,text = "Bill management by @invincible",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)

        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        F2 = LabelFrame(self.root,text = 'Cosmetics',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bath Soap")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bath_soap)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Cream")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_cream)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Wash")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_wash)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hair Spray")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hair_spray)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Body Lotion")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.body_lotion)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)


        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Daal")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.daal)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)


        F2 = LabelFrame(self.root,text = 'cold drink',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.maza)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.frooti)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nimkos")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.nimko)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)


        
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)

        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_cosmetics)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "cold drink Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "cold drink Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

    def total(self):

        self.total_cosmetics_prices = (
            (self.bath_soap.get() * 40)+
            (self.face_cream.get() * 140)+
            (self.face_wash.get() * 240)+
            (self.hair_spray.get() * 340)+
            (self.body_lotion.get() * 260)
        )
        self.total_cosmetics.set("Rs. "+str(self.total_cosmetics_prices))
        self.tax_cos.set("Rs. "+str(round(self.total_cosmetics_prices*0.05)))

        self.total_grocery_prices = (
            (self.wheat.get()*100)+
            (self.food_oil.get() * 180)+
            (self.daal.get() * 80)+
            (self.rice.get() *80)+
            (self.sugar.get() * 170)

        )
        self.total_grocery.set("Rs. "+str(self.total_grocery_prices))
        self.tax_groc.set("Rs. "+str(round(self.total_grocery_prices*0.05)))

        self.total_other_prices = (
            (self.maza.get() * 20)+
            (self.frooti.get() * 50)+
            (self.coke.get() * 60)+
            (self.nimko.get() * 20)+
            (self.biscuits.get() * 20)
        )
        self.total_other.set("Rs. "+str(self.total_other_prices))
        self.tax_other.set("Rs. "+str(round(self.total_other_prices*0.05)))

    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Hanan's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")

    def clear(self):
        self.txt.delete('1.0',END)

    def bill_area(self):
        self.welcome_soft()
        if self.bath_soap.get() != 0:
            self.txt.insert(END,f"\nBath Soap         {self.bath_soap.get()}           {self.bath_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END,f"\nFace Cream        {self.face_cream.get()}           {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END,f"\nFace Wash         {self.face_wash.get()}           {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END,f"\nHair Spray        {self.hair_spray.get()}           {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0 :
            self.txt.insert(END,f"\nBody Lotion       {self.body_lotion.get()}           {self.body_lotion.get() * 260}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat             {self.wheat.get()}           {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil          {self.food_oil.get()}           {self.food_oil.get() * 180}")
        if self.daal.get() != 0:
            self.txt.insert(END,f"\nDaal              {self.daal.get()}           {self.daal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice              {self.rice.get()}           {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar             {self.sugar.get()}           {self.sugar.get() * 170}")
        if self.maza.get() != 0:
            self.txt.insert(END,f"\nMaza              {self.maza.get()}           {self.maza.get() * 20}")
        if self.frooti.get() != 0:
            self.txt.insert(END,f"\nFrooti            {self.frooti.get()}           {self.frooti.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke              {self.coke.get()}           {self.coke.get() * 60}")
        if self.nimko.get() != 0:
            self.txt.insert(END,f"\nNimko             {self.nimko.get()}           {self.nimko.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits          {self.biscuits.get()}           {self.biscuits.get() * 20}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_cosmetics_prices+self.total_grocery_prices+self.total_other_prices+self.total_cosmetics_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")



    def exit(self):
        self.root.destroy()

root = Tk()
object = Bill_App(root)
root.mainloop()












# import mysql.connector
# import webbrowser

# conn = mysql.connector.connect(user='root', password='',
#                               host='localhost',database='company')

# if conn:
#     print ("Connected Successfully")
# else:
#     print ("Connection Not Established")

# select_employee = """SELECT * FROM employee"""
# cursor = conn.cursor()
# cursor.execute(select_employee)
# result = cursor.fetchall()

# p = []

# tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
# p.append(tbl)

# for row in result:
#     a = "<tr><td>%s</td>"%row[0]
#     p.append(a)
#     b = "<td>%s</td>"%row[1]
#     p.append(b)
#     c = "<td>%s</td>"%row[2]
#     p.append(c)
#     d = "<td>%s</td></tr>"%row[3]
#     p.append(d)


# contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
# <html>
# 	<head>
# 		<title> Personal Form </title>
# 	</head>
# <body bgcolor="#BC354C">
# <table border = 1>
# <form>
# <h1>Feedback Form</h1>
# <tr><td>Name:</td><td><input type=text size=50 value=></td></tr>
# <tr><td>Address:</td><td><input type=text size 50></td></tr>
# <tr><td>Mobile Number:</td><td><input type=number value=></td></tr>
# <tr><td>Email address:</td><td><input type=mailid value=></td></tr>
# <tr><td>Password:</td><td><input type=password max length=20></td></tr>
# <tr><td>Phone Number(optional):</td><td><input type=number value=></td></tr>
# <tr><td>Photo:</td><td><input type=file></td></tr>
# <tr><td>Your ID Proof:</td><td><input type=file></td></tr>
# <tr><td>Father Name:</td><td><input type=text size=50></td></tr>
# <tr><td>Father's Mobile Number:</td><td><input type=number value=></td></tr>
# <tr><td>Father's Email address:</td><td><input type=mailid value=></td></tr>
# <tr><td>Father's Phone Number:</td><td><input type=number value=></td></tr>
# <tr><td>Address:</td><td><input type=text size=50></td></tr>
# <tr><td>Mother's Name:</td><td><input type=text size =50></td></tr>
# <tr><td>Mother's Mobile Number:</td><td><input type=number value=></td></tr>
# <tr><td>Mother's Email address:</td><td><input type=mailid value=></td></tr>
# <tr><td>Mother's Phone Number:</td><td><input type=number value=></td></tr>
# <tr><td>Address:</td><td><input type=text size=50></td></tr>
# <tr><td>Gender</td>
# <td><input type=radio name="gen">Male
# <input type=radio name="gen">Female</td></tr>
# <tr><td>Hobby:</td>
# <td><input type=checkbox> Cricket<br>
# <input type=checkbox> Football<br>
# <input type=checkbox> Hockey<br>
# <input type=checkbox> Badminton<br>
# <input type=checkbox> Swimming<br>
# <input type=checkbox> Reading<br>
# <input type=checkbox> Singing<br>
# <input type=checkbox> Rugby<br>
# <input type=checkbox> Table Tennis<br>
# cold drink<input type=text size=50><br></td></tr>
# <tr><td>City:</td>
# <td><select size=5>
# <option>ahmedabad
# <option>rajkot
# <option>surat
# <option>baroda
# <option>bhavnagar
# <option>himatnagar
# <option>lucknow
# <option>gaziabad
# <option>mumbai
# <option>delhi
# <option>amritsar
# <option>kutch
# <option>bhuj
# <option>chennai
# <option>banglore
# <option>hydrabad
# <option>jaipur
# <option>indore
# <option>bhopal
# <option>patna
# <option>nashik
# <option>coimbatore
# <option>ranchi
# <option>meerut
# <option>varanasi
# <option>alwar
# <option>anantapuram
# <option>thrissur
# <option>bally
# <option>imphal
# <option>bharatpur
# <option>kolkata
# <option>pune
# <option>nagpur
# <option>thane
# <option>faridabad
# <option>jabalpur
# <option>jalandar
# <option>madurai
# <option>srinagar
# <option>visakapatnam
# <option>howrah
# <option>vellore
# <option>bhiwani
# <option>mango
# <option>junagadh
# <option>kattankulathur
# <option>agra
# <option>noida
# <option>jamshedpur
# <option>jhansi
# <option>amravati
# <option>cuttack
# <option>bikaner
# <option>nellore
# <option>Asansol
# <option>durgapur
# <option>Rourkela
# <option>nanded
# <option>akola
# <option>gulbarga
# <option>Loni
# <option>ulhasnagar
# <option>Erode
# <option>Manglore
# <option>Kurnool
# <option>Ambattur
# <option>Tirunelveli
# <option>Malegaon
# <option>kakinada
# <option>bellary
# <option>Gopalpur
# <option>Bhagalpur
# <option>Muzaffarnagar
# <option>Bhatpara
# <option>Latur
# <option>Dhule
# <option>Rohtak
# <option>Sagar
# <option>Korba
# <option>Bhilwara
# <option>Kollam
# <option>Mathura
# <option>Ahmednagar
# <option>Avadi
# <option>Kadapa
# <option>Anantapuram
# <option>Satara
# <option>Rampur
# <option>Shimoga
# <option>Chandrapur
# </select></td></tr>
# <tr><td><INPUT TYPE=SUBMIT VALUE="REGISTER"></td>
# <td><INPUT TYPE=RESET VALUE="Clear"></td></tr>
# </form>
# </table>
# </body>
# </html>
# '''%(p)

# filename = 'webbrowser.html'

# def main(contents, filename):
#     output = open(filename,"w")
#     output.write(contents)
#     output.close()

# main(contents, filename)    
# webbrowser.open(filename)

# if(conn.is_connected()):
#     cursor.close()
#     conn.close()
#     print("MySQL connection is closed.")    

















# import mysql.connector
# import webbrowser

# conn = mysql.connector.connect(user='root', password='',
#                               host='localhost',database='company')

# if conn:
#     print ("Connected Successfully")
# else:
#     print ("Connection Not Established")

# select_employee = """SELECT * FROM employee"""
# cursor = conn.cursor()
# cursor.execute(select_employee)
# result = cursor.fetchall()

# p = []

# tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
# p.append(tbl)

# for row in result:
#     a = "<tr><td>%s</td>"%row[0]
#     p.append(a)
#     b = "<td>%s</td>"%row[1]
#     p.append(b)
#     c = "<td>%s</td>"%row[2]
#     p.append(c)
#     d = "<td>%s</td></tr>"%row[3]
#     p.append(d)


# contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
# <html>
# <head>
# <meta content="text/html; charset=ISO-8859-1"
# http-equiv="content-type">
# <title>Python Webbrowser</title>
# </head>
# <body>
# <table>
# %s
# </table>
# </body>
# </html>
# '''%(p)

# filename = 'webbrowser.html'

# def main(contents, filename):
#     output = open(filename,"w")
#     output.write(contents)
#     output.close()

# main(contents, filename)    
# webbrowser.open(filename)

# if(conn.is_connected()):
#     cursor.close()
#     conn.close()
#     print("MySQL connection is closed.")