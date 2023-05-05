#pickle module to read, write in binary files
import pickle
import os
import pathlib
from tkinter import*
import tkinter.messagebox 
import time
import datetime
class Account :
   empNo = 0
   name = ''
   salary=0
   dept = ''
   phone_no=0
   address=''    
   def createemployee(self):      
       self.empNo= int(input("Enter the EMPLOYEE ID : "))       
       print('\n')       
       self.name = input("Enter the EMPLOYEE NAME : ")       
       print('\n')       
       self.dept = input("Ente the dept: ")       
       print('\n')
       self.salary = int(input("Enter the salary: "))       
       print('\n')       
       self.address=input("Enter address:  ")
       print('\n')
       self.phone_no=int(input("Enter phone number:   "))
   def showAccount(self):
       print("EMPLOYEE ID : ",self.empNo)       
       print('\n')       
       print("EMPLOYEE NAME : ",self.name)       
       print('\n')       
       print("DEPT",self.dept)       
       print('\n')       
       print("SALARY : ",self.salary)       
       print('\n')       
       print("CONTACT DETAILS :  ",self.address,self.phone_no,end='\t')       
       print("\n")       
   def depositAmount(self,amount):      
       self.salary += amount       
   def withdrawAmount(self,amount):      
       self.salary -= amount       
   def report(self):      
       print(self.empNo,self.name ,self.dept, self.salary,self.address,self.phone_no,end="")  
   def getemployeeNo(self):      
       return self.empNo
   def getEmployeeName(self):      
       return self.name
   def getemployeedept(self):      
       return self.dept
   def getsalary(self):      
       return self.salary   
   def getaddress(self):      
       return self.address      
   def getphonenumber(self):      
       return self.phone_no
#function outside the class
def writeemployee():   
   account = Account() #accout has been assigned the value inside the classAccounts   
   account.createemployee() #since account is being assigned the class Account(), the function createemployee() is being called through account
   writeemployeesFile(account)
#function definiton to dispaly all the records
def displayAll():
   file = pathlib.Path("employee.data")
   if file.exists ():
       infile = open('employee.data','rb')
       mylist = pickle.load(infile)
       if (len(mylist)!=0):
          for item in mylist :
                print(item.empNo,"          ",item.name,"          ",item.dept,"          ",item.salary,"          ",item.phone_no,"          ",item.address,end='\n')
          infile.close()
       elif (len(mylist)==0):
          print("NO DATA TO DISPLAY....PLEASE ADD RECORDS")
   else :
       print("file does not exist")        
#function definition to search for a particular record and dispaly it
def displaySp(num):
   file = pathlib.Path("employee.data")
   if file.exists ():
       infile = open('employee.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       found = False
       for item in mylist :
          root=Tk()                                
          f=Frame(root)
          frame1=Frame(root)
          frame2=Frame(root)
          frame3=Frame(root)
          root.title("MENU")
          root.geometry("830x395")
          root.configure(background="green")
          label1=Label(root,text="THE RECORD OF SEARCHED EMPLOYEE")
          label1.config(font=('TIMES NEW ROMAN',20,), justify=CENTER, background="green",fg="RED", anchor="center")
          label1.pack(fill=X)
          button1=Button(f,text="continue",font=('times new roman',10),width=15, background="Brown", fg="White", command=root.destroy)
          button1.pack(side=RIGHT,padx=20,pady=10)
          f.configure(background="green")
          f.pack()
          root.mainloop()
          if item.empNo == num : 
            print("the details of the employee with the id numbe",item.empNo, 'are',item.name,item.dept,item.salary)
            found = True
   else :
       print("No records to Search")
   if not found :
       print("No existing record with this number")        
#function definition to add or detuct salary
def pfandincrement(num1,num2):
   file = pathlib.Path("employee.data")
   if file.exists ():
       infile = open('employee.data','rb')
       mylist = pickle.load(infile)
       infile.close()
       os.remove('employee.data')
       for item in mylist :
        if item.empNo == num1 :
            if num2 == 1 :
                amount = int(input("Enter the increment : "))
                print('\n')
                item.salary += amount
                print("The salary of the employee after increment is  : ", item.salary)
                root=Tk()                                
                f=Frame(root)
                frame1=Frame(root)
                frame2=Frame(root)
                frame3=Frame(root)
                root.title("MENU")
                root.geometry("830x395")
                root.configure(background="green")
                label1=Label(root,text="INCREMENT ADDED SUCCESSFULLY")
                label1.config(font=('TIMES NEW ROMAN',20,), justify=CENTER, background="green",fg="RED", anchor="center")
                label1.pack(fill=X)
                button1=Button(f,text="continue",font=('times new roman',10),width=15, background="Brown", fg="White", command=root.destroy)
                button1.pack(side=RIGHT,padx=20,pady=10)
                f.configure(background="green")
                f.pack()
                root.mainloop()
                print('\n')
                print("The salary of the employee has been updated")
            elif num2 == 2 :
                amount = int(input("Enter the amount to detuct: "))
                print('\n')
                if amount <= item.salary :
                    item.salary -=amount
                    print("The salary of the employee after the detuction of pf is : ", item.salary)                    
                    root=Tk()                                
                    f=Frame(root)
                    frame1=Frame(root)
                    frame2=Frame(root)
                    frame3=Frame(root)
                    root.title("MENU")
                    root.geometry("830x395")
                    root.configure(background="green")
                    label1=Label(root,text="PF DETUCTED SUCCESSFULLY")
                    label1.config(font=('TIMES NEW ROMAN',20,), justify=CENTER, background="green",fg="RED", anchor="center")
                    label1.pack(fill=X)
                    button1=Button(f,text="continue",font=('times new roman',10),width=15, background="Brown", fg="White", command=root.destroy)
                    button1.pack(side=RIGHT,padx=20,pady=10)
                    f.configure(background="green")
                    f.pack()
                    root.mainloop()
                else :
                    print("You cannot detuct amount more than the salary") 
        else:
            print("Please check the employee id!")
            break
   outfile = open('newemployees.data','wb')
   pickle.dump(mylist, outfile)
   outfile.close()
   os.rename('newemployees.data', 'employee.data')      
#function to delete the particular record
def deleterecord(num):
   file = pathlib.Path("employee.data")
   if file.exists ():
       infile = open('employee.data','rb')
       oldlist = pickle.load(infile)
       infile.close()
       newlist = []
       for item in oldlist :
           if item.empNo != num :
               print("No record to delete")
               newlist.append(item)
       os.remove('employee.data')
       outfile = open("newemployees.data",'wb')
       pickle.dump(newlist, outfile)
       outfile.close()
       os.rename('newemployees.data', 'employee.data')
#function to modiy a particular record
def modifyrecord(num):
   file = pathlib.Path("employee.data")
   if file.exists ():
       infile = open('employee.data','rb')
       oldlist = pickle.load(infile)
       infile.close()
       os.remove('employee.data')
       for item in oldlist :
           if item.empNo == num :
               print('\n')               
               print("Details before modification are  ")
               print('\n')               
               print("name","dept","salary","address","phone_no",end='\t')               
               print('\n')               
               print(item.name,item.dept,item.salary,item.address,item.phone_no,end="\t")               
               print('\n')               
               print("Account Number : ",item.empNo)               
               print('\n')               
               item.name = input("Modify Employee Name :")
               print('\n')
               item.dept = input("Modify dept  :")
               print('\n')
               item.salary = int(input("Modify salary :"))               
               print('\n')               
               item.address=input("Modify address  :")               
               print('\n')
               item.phone_no=int(input("modify phone_no  :"))
               print('\n')               
               print("Details after modification are  ")               
               print('\n')
               print("name","dept","salary","address","phone_no",end='\t')               
               print('\n')               
               print(item.name,item.dept,item.salary,item.address,item.phone_no,end='\t')               
               print('\n')                                         
       outfile = open('newemployee.data','wb')       
       pickle.dump(oldlist, outfile)       
       outfile.close()
       os.rename('newemployee.data', 'employee.data')
def salary_calculation():
   root=Tk()
   root.title("Employee payroll system")
   root.geometry('1350x650+0+0')
   root.configure(background="black")

   Tops=Frame(root,width=1350,height=50,bd=8,bg="red")
   Tops.pack(side=TOP)

   f1=Frame(root,width=600,height=600,bd=8,bg="green")
   f1.pack(side=LEFT)
   f2=Frame(root,width=300,height=700,bd=8,bg="yellow")
   f2.pack(side=RIGHT)

   fla=Frame(f1,width=600,height=200,bd=8,bg="powder blue")
   fla.pack(side=TOP)
   flb=Frame(f1,width=300,height=600,bd=8,bg="powder blue")
   flb.pack(side=TOP)

   lblinfo=Label(Tops,font=('times new roman',45,'bold'),text="Employee Payment Management system ",bd=10,fg="green")
   lblinfo.grid(row=0,column=0)

   def exit():
     exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
     if exit>0:
       root.destroy()
       return
   def enterinfo():
     txtpayslip.delete("1.0",END)
     txtpayslip.insert(END,"\t\tPay Slip\n\n")
     txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
     txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
     txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
     txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
     txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n")
   def monthlysalary():
     txtpayslip.delete("1.0",END)
     hoursworkedperweek=int(HoursWorked.get())
     wagesperhours=int(wageshour.get())
     
     paydue=wagesperhours*hoursworkedperweek
     paymentdue="INR",str('%.2f'%(paydue))
     Payable.set(paymentdue)
     
     tax=(paydue*0.001)
     taxable="INR",str('%.2f'%(tax))
     Taxable.set(taxable)
     
     netpay=paydue-tax
     netpays="INR",str('%.2f'%(netpay))
     NetPayable.set(netpays)
     
     if hoursworkedperweek > 40:
       overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
       overtime="INR",str('%.2f'%(overtimehours))
       OverTimeBonus.set(overtime)
     elif hoursworkedperweek<=40:
       overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
       overtimehrs="INR",str('%.2f'%(overtimepay))
       OverTimeBonus.set(overtimehrs)
     btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=8,font=('times new roman',16,'bold'),width=14,command=enterinfo,fg="red",bg="powder blue").grid(row=0,column=2)
     return  
       
   #=============================== Variables ========================================================
   HoursWorked=StringVar()
   wageshour=StringVar()
   Payable=StringVar()
   Taxable=StringVar()
   NetPayable=StringVar()
   GrossPayable=StringVar()
   OverTimeBonus=StringVar()
   DateOfOrder=StringVar()

   DateOfOrder.set(time.strftime("%d/%m/%Y"))

   #================================ Label Widget =================================================

   
   lblHoursWorked=Label(fla,text="Hours Worked in a week",font=('times new roman',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=0)
   lblHourlyRate=Label(fla,text="Hourly Rate",font=('times new roman',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=2)
  
   #=============================== Entry Widget =================================================

   etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('times new roman',16,'bold'),bd=16,width=22,justify='left')
   etxhoursworked.grid(row=1,column=1)
   
   etxwagesperhours=Entry(fla,textvariable=wageshour,font=('times new roman',16,'bold'),bd=16,width=22,justify='left')
   etxwagesperhours.grid(row=1,column=3)


   #=============================== Text Widget ============================================================

   payslip=Label(f2,textvariable=DateOfOrder,font=('times new roman',21,'bold'),fg="red",bg="powder blue").grid(row=0,column=0)
   txtpayslip=Text(f2,height=22,width=34,bd=16,font=('times new roman',13,'bold'),fg="green",bg="powder blue")
   txtpayslip.grid(row=1,column=0)

   #=============================== buttons ===============================================================

   btnsalary=Button(flb,text='montly Salary',padx=16,pady=16,bd=8,font=('times new roman',16,'bold'),width=14,fg="red",bg="powder blue",command=monthlysalary).grid(row=0,column=0)


   btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('times new roman',16,'bold'),width=14,command=exit,fg="red",bg="powder blue").grid(row=0,column=3)

   root.mainloop()
#function for writing in the binary file
def writeemployeesFile(account) :  
   file = pathlib.Path("employee.data")
   
   if file.exists ():       
       infile = open('employee.data','rb')       
       oldlist = pickle.load(infile)       
       oldlist.append(account)       
       infile.close()       
       os.remove('employee.data')       
   else :       
       oldlist = [account]       
   outfile = open('newemployee.data','wb')   
   pickle.dump(oldlist, outfile)   
   outfile.close()   
   os.rename('newemployee.data', 'employee.data')
#function for the welcome screen
def welcome():
   root=Tk()                               #Main window 1
   f=Frame(root)
   frame1=Frame(root)
   frame2=Frame(root)
   frame3=Frame(root)
   root.title("EMPLOYEE MANAGEMENT SYSTEM")
   root.geometry("830x395")
   root.configure(background="green")
   #label 1 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 2 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 3 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 4 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 5 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 6 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 7 welcome screen
   label1=Label(root,text="EMPLOYEE PAYROLL")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="white",fg="BLUE", anchor="center")
   label1.pack(fill=X)
   #label 8 welcome screen
   label1=Label(root,text="EMPLOYEE MANAGEMENT SYSTEM")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="WHITE",fg="blue", anchor="center")
   label1.pack(fill=X)
   #label 9 welcome screen
   label1=Label(root,text="WELCOMES YOU")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="WHITE",fg="BLUE", anchor="center")
   label1.pack(fill=X)
   #label 10 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 11 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 12 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 13 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 14 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 15 empty line
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   #label 16 name
   label1=Label(root,text="DONE BY : TRISHALA")
   label1.config(font=('times new roman',15,'bold'), justify=CENTER, background="green",fg="black", anchor="nw")
   label1.pack(fill=X)
   #label 17 school name
   label1=Label(root,text="COLLEGE : MISRIMAL NAVAJEE MUNOTH JAIN ENGINEERING COLLEGE ")
   label1.config(font=('times new roman',15,'bold'), justify=CENTER, background="green",fg="black", anchor="nw")
   label1.pack(fill=X)
   button6=Button(f,text="CONTINUE", background="BROWN", fg="White", width=10, command=root.destroy)
   button6.pack(side=LEFT,ipadx=20,pady=10)
   f.configure(background="green")
   f.pack()

   root.mainloop()
#function for the menu screen
def menu():
    root=Tk()                               #Menu 
    f=Frame(root)
    frame1=Frame(root)
    frame2=Frame(root)
    frame3=Frame(root)
    root.title("MENU")
    root.geometry("836x700")
    root.configure(background="green")
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 1 menu
    label1=Label(root,text="MENU")
    label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="white",fg="green", anchor="center")
    label1.pack(fill=X)
    #label 2 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 3 all employee lsit
    label1=Label(root,text="1.ALL EMPLOYEE LSIT")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 4 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 5 search employee
    label1=Label(root,text="2.SEARCH EMPLOYEE")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 6 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 7 creating a new record
    label1=Label(root,text="3.NEW RECORD")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 2 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 9 modifying the existing record
    label1=Label(root,text="4.MODIFY RECORD")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 10 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 11 detucting pf from the salary
    label1=Label(root,text="5.DETUCT PF ")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 12 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 13 adding increment to the salary
    label1=Label(root,text="6.INCREMENT")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 14 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 15 deleteing the record
    label1=Label(root,text="7.DELETE RECORD")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 16 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 17 exit
    label1=Label(root,text="8.Salary Calculation")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 18 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 19 exit
    label1=Label(root,text="9.EXIT")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 20 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="WHITE", anchor="nw")
    label1.pack(fill=X)
    #label 21 from the above listed option select one
    label1=Label(root,text="SELECT YOUR CHOICE")
    label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="green",fg="green", anchor="sw")
    label1.pack(fill=X)
    #label 22 empty line
    label1=Label(root,text="")
    label1.config(font=('times new roman',12,'bold'), justify=CENTER, background="green",fg="green", anchor="nw")
    label1.pack(fill=X)
    #button 1
    button6=Button(f,text="Continue", background="Brown", fg="White", width=8, command=root.destroy)
    button6.pack(side=LEFT,ipadx=20,pady=10)
    f.configure(background="green")
    f.pack()
    root.mainloop()
#funciton for the thank you screen
def thankyou():
   root=Tk()                               #THANK you
   f=Frame(root)
   frame1=Frame(root)
   frame2=Frame(root)
   frame3=Frame(root)
   root.title("THANK YOU")
   root.geometry("830x395")
   root.configure(background="green")
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="WHITE",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="WHITE",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="THANK YOU")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="white",fg="BLUE", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="WHITE",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text=" FOR USING EMPLOYEE MANAGEMENT SYSTEM")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="WHITE",fg="blue", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',16,'bold'), justify=CENTER, background="WHITE",fg="BLUE", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   label1=Label(root,text="")
   label1.config(font=('times new roman',5,'bold'), justify=CENTER, background="green",fg="Yellow", anchor="center")
   label1.pack(fill=X)
   button6=Button(f,text="EXIT", background="BROWN", fg="White", width=10, command=root.destroy)
   button6.pack(side=LEFT,ipadx=20,pady=10)
   f.configure(background="green")
   f.pack()

   root.mainloop()    
welcome()   
#Main program starts from here
print("                                                                    WELCOME                                                                       ")

print('\n')

print("                                                        EMPLOYEE REOCRD MANAGEMENT SYSTEM                                                               ")

print('\n')

print("                                                               EMPLOYEE DATA                                                                 ")

print('\n')


num=0
root=Tk()                                
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("MENU")
root.geometry("830x395")
root.configure(background="green")
def show_entry_fields():
    #print("ENTERED USER NAME:%s\nENTERED PASSWORD:%s"%(e1.get(),e2.get()))
    if(e1.get()=="ADMIN" and e2.get()=="admin"):
        print("Login successful")
        cont()
        menu()
        return True
    else:
        if (len(e1.get())==0 and len(e2.get())==0):
           a=tkinter.messagebox.askyesno("Employee system","Do you want to exit")
           if a<0:
              show_entry_fields
           print("Login failed")
        leave()
        thankyou()
        return False
def cont():
   button1=Button(f,text="continue", background="Brown", fg="White", command=root.destroy, width=8)
   button1.pack(side=LEFT,ipadx=25,pady=15)
   f.configure(background="green")
   f.pack()

   root.mainloop()
def leave():
   label1=Label(root,text="PLEASE CHECK FOR YOUR USERNAME AND PASSWORD")
   label1.config(font=('TIMES NEW ROMAN',20,), justify=CENTER, background="green",fg="RED", anchor="center")
   label1.pack(fill=X)
   button1=Button(f,text="quit",font=('times new roman',10),width=15, background="Brown", fg="White", command=root.destroy)
   button1.pack(side=RIGHT,padx=20,pady=10)
   f.configure(background="green")
   f.pack()
   root.mainloop()
def login():
    global a
    a=show_entry_fields()
    while (a):
       print('\n')       
       ch = input("Enter your choice: ")
       print('\n')
       if ch == '1':
           root=Tk()                                
           f=Frame(root)
           frame1=Frame(root)
           frame2=Frame(root)
           frame3=Frame(root)
           root.title("")
           root.geometry("830x395")
           root.configure(background="green")
           label1=Label(root,text="THE LIST OF ALL THE EMPLOYEES WORKING IN THE COMPANY")
           label1.config(font=('TIMES NEW ROMAN',20,), justify=CENTER, background="green",fg="RED", anchor="center")
           label1.pack(fill=X)
           button1=Button(f,text="continue",font=('times new roman',10),width=15, background="Brown", fg="White", command=root.destroy)
           button1.pack(side=RIGHT,padx=20,pady=10)
           f.configure(background="green")
           f.pack()
           root.mainloop()
           displayAll()
           print('\n')
           ch1=input("Do you want to continue?")
           print('\n')
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
             menu()
             continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break

           else:
                print("wrong choice")          
       elif ch == '2':          
           num = int(input("\tEnter The account No. : "))
           displaySp(num)
           ch1=input("Do you want to continue?")
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
             menu()
             continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
           else:
                print("wrong choice")
       elif ch == '3':
          writeemployee()
          ch2=input("Do you want to view all employee?(y/n)").lower()
          if ch2=="y":
             displayAll()
          ch1=input("Do you want to continue?")
          if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
             menu()
             continue
          elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
          else:
                print("wrong choice")
       
       elif ch == '4':
           num = int(input("\tEnter The account No. : "))
           print('\n')
           a=modifyrecord(num)
           ch1=input("Do you want to continue?")
           print('\n')
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
              menu()
              continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
           else:
                print("wrong choice")
       elif ch == '5':
          num = int(input("\tEnter The account No. : "))
          pfandincrement(num, 2)           
          ch1=input("Do you want to continue?")
          if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
             menu()
             continue
          elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
          else:
                print("wrong choice")
       elif ch =='6':
           num = int(input("\tEnter The account No. : "))
           pfandincrement(num, 1)
           ch1=input("Do you want to continue?")
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
              menu()
              continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
           else:
                print("wrong choice")
                
       elif ch == '7':
           print('\n')
           num =int(input("\tEnter The account No. : "))
           print('\n')
           deleterecord(num)       
           displayAll()
           print('\n')
           ch1=input("Do you want to continue?")
           print('\n')
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
                menu()
                continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
           else:
                print("wrong choice")
       elif ch == '8':
           salary_calculation()
           ch1=input("Do you want to continue?")
           print('\n')
           if (ch1=="YES") or (ch1=="Yes") or (ch1=="yes") or (ch1=="y") or (ch1=="Y"):
                menu()
                continue
           elif (ch1=="NO") or (ch1=="no") or (ch1=="No") or (ch1=="n") or (ch1=="N"):
             thankyou()
             break
           else:
                print("wrong choice")
       elif ch == '9':
           print('\n')
           thankyou()
           break
       else :
           print("Invalid choice")
    else:
       print("Check for your username and password")
frame2.pack_forget()
frame3.pack_forget()
label1=Label(root,text="SIMPLE EMPLOYEE RECORD SYSTEM")
label1.config(font=('TIMES NEW ROMAN',20,'bold','underline'), justify=CENTER, background="green",fg="RED", anchor="center")
label1.pack(fill=X)
user=Label(frame1,text="Enter the username: ",font=('times new roman',20,'bold','underline'),bg="black",fg="white")
user.grid(row=1,column=1,padx=10)
e1=Entry(frame1,textvariable=user,font=('TIMES NEW ROMAN',20),bd=16,width=22,justify='left')
e1.grid(row=1,column=2,padx=10)
password=Label(frame1,text="Enter the password: ",font=('TIMES NEW ROMAN',20,'bold','underline'),bg="black",fg="white")
password.grid(row=2,column=1,padx=10)
e2=Entry(frame1,textvariable=password,font=('TIMES NEW ROMAN',20),bd=16,width=22,show='*',justify='left')
e2.grid(row=2,column=2,padx=10)
e2.focus()
frame1.configure(background="white")
frame1.pack(pady=10)
button1=Button(f,text="login",font=('TIMES NEW ROMAN',10),width=15, background="Brown", fg="White", command=login )
button1.pack(side=LEFT,ipadx=20,pady=10)
f.configure(background="green")
f.pack()
root.mainloop()
