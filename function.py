def cal_sum(a,b):
    sum=a+b
    return sum

res=cal_sum(2,3)   
# print(res)

# there to type of function built in , user defined
# builtin- print(),len(),
# 

# make user defind len function
def getLen(list):
    len=0
    for i in list:
        len+=1
    return len   
# 

# print in same line
def print_same_line(a):
    for i in a:
        print(i,end=" ")

# print_same_line(["a","b","c","d"])        

# /wap to get factorial

def getFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

# print(getFactorial(5))

# wap to conert usd to inr
def conveter(usd):
    usd_val=83
    inr=usd_val*usd
    print(usd,"usd=",inr,"INR")

# conveter(79)    

# find odd even

def findOddEven(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

findOddEven(7)            