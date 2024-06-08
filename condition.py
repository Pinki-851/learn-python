# if-else

# age=14
# if(age>18):
#     print("Can vote")
# else:
#     print("cannot vote")

# if-elif

light="black"
 
if(light == "red"):
     print("stop")
elif(light == "yellow"):
    print("look") 
elif(light == "green"):
    print("Go") 
else:
    print("not aval")        

# grade
marks=int(input("enter marks"))
if(marks>=90):
    print("a")
elif(90>marks and marks>=80):
    print("b")
elif(80>marks and marks>=70):
    print("c")
elif(70>marks):
    print("d")
else:
    print("enter correct marks")

# wap to find odd and even

num=int(input("enter number"))
if(num%2==0):
    print("even number")
else:
    print("odd number")    

#wap to find grates in 4 number
a=int(input("enter number 1"))
b=int(input("enter number 3"))
c=int(input("enter number 2"))
d=int(input("enter number 4"))

if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
else:
    print(d)            