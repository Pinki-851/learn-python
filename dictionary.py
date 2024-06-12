dic={"name":"alice","age":20,"marks":[99,68,78]}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("name"))
print(dic.update({"name":"bob"}))
print(dic)

# to add on empty dictionary
marks={}
x=int(input("enter your marks"))
marks.update({"phy":x})
print(marks)

