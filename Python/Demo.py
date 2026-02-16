# list1 = ["Apple","Orange","Spinach","Cooliflower","Gauvav","Carrot"]
# print(list1)
# fruits = []
# veg = []
# for i in range(len(list1)):
#     if(list1[i]=="Apple" or list1[i]=="Orange" or list1[i]=="Gauvav"):
#         fruits.append(list1[i])
#     else:
#         veg.append(list1[i])
# print(fruits)
# print(veg)



# list1 = ["harshal_01","rushi_02","aniket_03"]
# l1 = []
# l2 = []
# y=0
# for i in range(len(list1)):
#     if(i==0):
#         y=7
#     elif(i==1):
#         y=5
#     elif(i==2):
#         y=6
#     l1.append(list1[i][:y])
#     l2.append(int(list1[i][-2:]))

# print(l1)
# print(l2)       

# name = "Harshal_01"
# count = 0
# for i in name :
#     if i == "_":
#         y=count
#         break
#     count += 1
# print("'_' at index number ",y)

# print(f"Finding index of '' using find method : {name.find('')}")

# def findUnderscore(name):
#     index = name.find("_")
#     return index

# list1=["harshal_01","pratik_02","aniket_03","rushi_04"]
# l1=[]
# l2=[]
# for i in range(len(list1)):
#     l1.append(list1[i][:findUnderscore(list1[i])])
#     l2.append(int(list1[i][findUnderscore(list1[i])+1:]))
# print(l1)
# print(l2)

def add(a,b):
    print(f"sum = {a+b}")

def sub(a,b):
    print(f"sub = {a-b}")

def mul(a,b):
    print(f"mul = {a*b}")

def div(a,b):
    try:
        print(f"div = {a/b}")
    except:
        print("it is not divisible by 0 ")

def userInput(operator):
    if operator=="+":
        add(a,b)
    elif operator=="-":
        sub(a,b)
    elif operator=="*":
        mul(a,b)
    elif operator=="/":
        div(a,b)
try:
    a = int(input("Enter a val : "))
    b = int(input("Enter a val : "))
except:
    print("plz enter integers")
op = input(
    'operator : '
)
userInput(op)

# list1 = ["harshal","7028653774","abhi","9766094065","ram"]
# l1=[]
# for i in range(len(list1)):
#     length=len(list1[i])
#     if length==10 :
#         try:
#             l1.append(int(list1[i]))
#         except:
#             print("Something Wrong!")

# print(l1)

# list1 = [- 120.5, "HELLO", 60, -50,[5], {'name': 'Pratik'}]
# l1=[]
# for elements in list1:
#     l1.append(type(elements))
# print(l1)

# list2 = [2,3,5,9,15,98,131,122]
# even = []
# odd = []
# for ele in list2:
#     if ele%2==0:
#         even.append(ele)
#     else:
#         odd.append(ele)

# print(even)
# print(odd)

# str1 = input("Enter value : ")
# print(str1)
# str2 = ""
# for i in range(len(str1)-1,-1,-1):
#     s = str1[i]
#     str2 = str2 + s

# print(str2)
# if(str1==str2):
#     print("It is palandriom!")
# else:
#     print("Is not palandriom!")