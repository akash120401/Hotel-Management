print("*************************************")
print("                                     ")
print("  WELCOME TO RESTAURENT APPLICATION  ")
print("                                     ")
print("*************************************")
class Admin:
  def __init__(self):
    self.username=0
    self.password=0
    self.conform_password=0
    self.registration()
    self.login()

  def registration(self):
     print("================================")
     print("registration:")
     import csv 
     with open("Credential.csv",'w',newline="") as f:
            w =  csv.writer(f)
            self.username = input("Enter and set username      :")
            self.password = input("Enter and set your password :")
            self.conform_password=input(("enter conform password:"))
            #saving a data into database
            w.writerow([self.username,self.conform_password])

     if self.password==self.conform_password:
         print("register successfully")
         
     else:
         print("enter wright password")

     print("=================================")

  def login(self):
      print(" ")
      print("login:")
      import csv
      passuser=[] #list for storing data and retrieving from adminCredential.csv file
      with open("Credential.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
           # print(data)
            for i in data:#i=0
                for j in i:#j=0
                    passuser.append(j)
   
      print("================================")
      self.username=input(("enter username:"))
      self.password=input (("enter password:"))
      
      
      if self.username == str(passuser[0]) and self.password == str(passuser[1]):
        print("login successfully")
        
        self.getdata_details()
          
      else:
          print("please enter correct username")
       
      print("================================")
  def getdata_details(self):
      print("1. add food details")
      print('2. Add Tables')
      print("3. Add Waiters")
      choice = int(input("Enter your choice")) # subject selection logic part
      if choice==1:
        self.Add_food_details() # calling function
      elif choice==2:
        self.Add_Table()
      elif choice==3:
        self.waiters()
      else:
       print("choose correct choice")

  def Add_food_details(self):
      
      import csv 
      food_details=[ 
         {"foodname":"khichadi","foodprize":"100","foodid":"01"},
         {"foodname":"BhajiBhakar","foodprize":"120","foodid":"02"},
         {"foodname":"pohe","foodprize":"40","foodid":"03"},
 ]
            
      with open("food_details.csv",'w',newline="") as csvfile:
       fieldname=food_details[0].keys()
       writer=csv.DictWriter(csvfile,fieldnames=fieldname)
       for row in food_details:
        writer.writerow(row)
       print("saved")


  def Add_Table(self):

     import csv 
     table_details=[ 
         {"tableid":"111","nameof_table":"Right_corner"},
         {"tableid":"112","nameof_table":"Left_corner"},
         {"tableid":"113","nameof_table":"Middle"},
 ]
            
     with open("table_details.csv",'w',newline="") as csvfile:
       fieldname=table_details[0].keys()
       writer=csv.DictWriter(csvfile,fieldnames=fieldname)
       for row in table_details:
        writer.writerow(row)
       print("saved")
        

  def waiters(self):
     import csv 
     waiters_details=[ 
         {"waiter_name":"Akash","waiterid":"97"},
         {"waiter_name":"prashant","waiterid":"98"},
         {"waiter_name":"rushi","waiterid":"99"},
 ]
            
     with open("waiters.csv",'w',newline="") as csvfile:
       fieldname=waiters_details[0].keys()
       writer=csv.DictWriter(csvfile,fieldnames=fieldname)
       for row in waiters_details:
        writer.writerow(row)
       print("saved")
  
      

  
obj=Admin()
obj.registration()
obj.login()
