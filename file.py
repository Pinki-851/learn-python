# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f=open("demo.txt","a")
# data=f.write("I'm learning python")
# print(data)
# print(type(data))
# f.close()

# f=open("sample.txt","a")
# data=f.write("I'm learning python")
# print(data)
# print(type(data))

# with open("demo.txt","r") as f:
#     data=f.read()
#     if(data.find("learning")!=-1):
#         print("found")
#     else:
#         print("not found")    

def chek_file():
    with open("demo.txt","r") as f:
        data=True
        word="python"
        line=1
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line+=1
    return -1
chek_file()