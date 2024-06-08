str1="Hello "
str2="world"

print(str1 + str2)

# legth of a string

string="hey! how are you doing?"
print("length",len(string))

newlinestr="hey I'm learing python. \nlet's see how soon I can finish this"
print(newlinestr)


# slicing
strSlice="learn fast"
print(strSlice[0:5])
print(strSlice[1:6])
print(strSlice[6:])
print(strSlice[6:len(strSlice)])

# some basic str methods
strSlice="find end character" #we can define same var in python it will override always old one
print(strSlice.endswith("er"))

print(strSlice.capitalize())# always make first letter caps
print(strSlice.count("end"))
print(strSlice.replace("end","start"))
print(strSlice.find("end"))


# practice

# WAP to input user name and print it's value
name=input("enter your name:")
print(len(name))

# find $ count in string
str="I'm $learning python $"
print(str.count("$"))