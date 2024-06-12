class Student:
    def __init__(self,name):
        self.name=name
       
s1=Student("pinki")   
print(s1.name)    


class StudentMarks:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def getMarksAvg(self):
            sum=0
            print("length",len(self.marks))
            for mark in self.marks:
                sum+=mark
            avg= sum/len(self.marks)  
            return [sum,avg]    

s2=StudentMarks("Alice",[99,55,78])

# res=s2.getMarksAvg()
# print(res,"res",s2.name)

class Account:
     def __init__(self,account,balance):
          self.account=account
          self.balance=balance

     def credit(self,amount):
          bal=self.balance
          self.balance=bal+amount
          print("Rs.",amount,"credited amount") 
          print("total amount",self.printamount()) 


     def debit(self,amount):
        
          self.balance-=amount
          print("Rs.",amount,"debited amount") 
          print("total amount",self.printamount()) 

     def printamount(self):
          print(self.balance)
          return self.balance         

# acc=Account(123,10000)
# print(acc.account)          
# print(acc.balance) 
# acc.credit(200)   
# acc.printamount()   

# private in class

class Account2:
     def __init__(self,acc_no,acc_pass):
          self.acc_no=acc_no
          self.__acc_pass=acc_pass #to make private add __
     def get_pass(self):
          return self.__acc_pass

acc=Account2(12,"abcd") 
print(acc.get_pass())         
# print(acc.acc_pass)         
            