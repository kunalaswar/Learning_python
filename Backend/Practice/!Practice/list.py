# l1=[10,20,23,45,56,67]
# print(l1,type(l1),id(l1))
# l2=[ 12,20,"Rossum",True,(2+3j)]
# print(l2,type(l2))
# print(l2[0])
# print(l2[-1])
# print(l2[-2])
# print(l2[2])
# l2[0]=555 #Item assignment is possible
# print(l2)
# l2[1]="kunal" #Item assignment is possible
# print(l2)
# print(l2[::2],id(l2))
# print(l2[::-1],id(l2))
# l1=[12,23,45,56,67,78,89]
# print(l1,type(l1),len(l1))

# l2=[]
# print("l2 = ",l2,len(l2))
# l3=list()
# print("l3 = ",l3,len(l3))
#IMPORTANT

# l1=[10,20,30,40,50]
# print(l1,type(l1))
# b=bytes(l1)
# print(b,type(b))
# l2=list(b)
# print(l2,type(l2))
# print(l2[3:])
# print(l2[3:][::-1])

# a=[10]
# print(a,type(a))
# x=100
# b=list([x])
# print(b,type(b))

# lst=[]
# print(lst)
# lst=list()
# print(lst)
# lst1=[1,2,3,4,5,6]
# print(lst1)
# lst2=[12,23,"Rossum",2+3j,True]
# print(lst2)
# print(lst2[2])
# print(lst2[7:0:-1])
# print(lst2[:-1])
# print(lst1[1])



# To create an Empty list there are two steps
# lst1=list()
# lst2=[]

# indexing and sclice based modification

# lst=[10,20,30,40,50,10,20]
# print(lst,type(lst),id(lst))
# lst[0]=100 #index based modification
# print(lst,type(lst),id(lst))
# lst[1:5]=[200,300,400,500] #slicing based modification
# print(lst,type(lst),id(lst))

#Non Empty list
# lst=[1,2,3,"Rossum",34.56]
# print(lst,type(lst),len(lst))
# print(lst[2])
# print(lst[3])
# print(lst[4])

# lst1=[]#Empty list
# print(lst1,type(lst1),len(lst1))
# lst2=list()#Empty list
# print(lst2,type(lst2),len(lst2))


# lst=[1,2,3,4,5,6]
# print(lst,type(lst),len(lst))   
# b=bytes(lst)
# print(b,type(b))
# lst2=list(b)#to convert the bytes data into to the list
# print("list2 = ",lst2,type(lst2)) 


#lst=[1,2,3,4,5,6]


# s="123456"
# print(s,type(s),id(s))
# l1=list(s)
# print(l1,type(l1),id(l1))

# k="PYTHON"
# print(k,type(k) ,id(k))
# # l2=list(k)
# l2=list([k])
# print(l2),type(l2),id(l2)

# list=[1,2,3,4,5,6]
# print(list)
# # for  i in list:
# #     print(i)

# a=10
# lst=list[a]
# print(lst)

# a=10
# lst=list([a])
# print(lst)

# lst=[10,20,30]
# lst.append(True)
# print(lst)

# lst=[]
# lst.append(9)
# lst.append(True)
# lst.append(2+3j)
# lst.append(100)
# print(lst)

# lst=[10,20,30]
# lst.insert(10,"java")
# print(lst)
# lst.insert(-10,"python")
# print(lst)

# lst=[10,"RS",33.45]
# lst.insert(-1,2+3j)
# print(lst)

# lst= [1, 2, 2+3j, True, "RS"]
# print(lst)
# lst.remove(2+3j)
# lst.remove("RS")
# lst.remove(True)
# print(lst)

# lst= [1, 2, 2+3j, True, "RS"]
# print(lst)
# lst.pop(0) #!index error
# lst.pop(1)
# lst.pop(2)
# print(lst)

# lst=[10,20,30,40,50,10] #! last index pop 
# # print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)
# lst.pop()
# print(lst)#! indexerror
# lst.pop()

# lst=[10,20,30,40,50]
# del lst[-2]
# del lst[0]
# del lst[1]
# print(lst)

# lst=[10,20,30,40,50]
# del lst[0:3:1]
# print(lst)


# lst=[10,20,30,40,50]
# print(lst)
# print(lst.index(10))
# print(lst.index(20))
# print(lst.index(30))
# print(lst.index(40))
# print(lst.index(50))
# print(lst)

# lst=[10,20,30,40,50]
# # for index,value in enumerate(lst):
#     # print(index,value)
# for index,value in enumerate(lst):
#         print(index,value)
#         # if(value==10):
#             # print(index,value)
        
# s="MISSISSIPI"
# for index,value in enumerate(s):
#     print(index,value)

# s="MISSISSIPI"
# count=0
# for index,value in enumerate(s):
#     if(value=="I"):
#         print(index,"--->",value)
#         count=count+1
# print(f"the value of I is repeated {count}")        

# l=123456789123456789232323
# l2 = []
# # print(l,type(l))
# while l>0:
#     n = l%10
#     l2.append(n)
#     l //= 10
# print(l2)


# l=123456789123456789232323
# l2 = []
# # print(l,type(l))
# while l>0:
#     n = l%10
#     l2.append(n)
#     l //= 10
# print(l2)
# count=0
# for index,value in enumerate(l2):
#     if(value==2):
#         print(index,value)
#         count=count+1
# print(f"the repeated value of the 2 is  {count} Time")        



# l=123456789123456789232323
# l1=[]
# # print(l1,type(l1))
# while(l>0):
#     n=l%10
#     l1.append(n)
#     l=l//10
# print(l1)    

# s="123456789123456789232323"
# # print(s,type(s))
# lst=s.split()
# print(lst)
# for i in lst[0]:
#     print(list[i])

# lst1=[10,20,30,40]
# lst2=lst1.copy()
# # print(lst2)
# lst1.append("python")
# lst1.append(True)
# print(lst1)

# lst1=[10,20,30,40]
# lst2=lst1
# print(lst2)
# lst1.append(10)
# lst1.append("python")
# lst1.append(True)
# lst1.append("RS")
# lst1.append(2+3j)
# print(lst1)

# lst=[10,20,30,40,50,10,30,50,60,70,80,10,20,30]
# # print(len(lst))
# print(lst.count(10))
# print(lst.count(20))
# print(lst.count(30))
# print(lst.count(100))


# s="MISSISSIPI"
# print(s.count("I"))
# print(s.count("P"))
# print(list(s).count("P"))


# lst1=[10,20,30,40]
# lst2=lst1.reverse()
# print(lst2)
# print(lst1)


# lst1=[10,20,30,40]
# lst1.reverse()
# print(lst1)


# lst1=[10,20,30,40]
# print(lst1[::-1])

# lst=[1,10,-3,4,5,6,7,39,-90,60,70,80]
# lst.sort(reverse=True)
# lst.sort(reverse=False)
# print(lst)

# # lst.sort(reverse=False)
# lst.sort(reverse=True)
# print(lst)

# lst1=[10,20,30]
# lst2=[40,50,60]
# lst1.extend(lst2)
# print(lst1)
# print(lst2)
#!list within list
# lst=[1,2,3,[4,5,6,]]
# print(lst[0])
# print(lst[3][0])

# lst=[1,2,3,[4,5,6,]]
# lst1=[1,2,3,[4,5,6,]]
# print(lst.extend(lst1))
# print(lst)
# print(lst1)

# #lst=[10,"kalesh",[20,16,18],[70,76,65],"JNTU"]
# for val in lst:
#     print(val,type(val))
# lst[-2].append(15)
# print(lst)
# lst.append(20)
# print(lst)
# lst[2].insert(1,77)
# lst[2].insert(0,90)
# print(lst)

lst=[10,"kalesh",[20,16,18],[79,76,65],"JNTU"]
# lst[2].sort()
# print(lst[2])
# lst[3].sort()
# print(lst[3])

# del lst[2][::2]
# print(lst)

# lst[2].clear()
# print(lst[2])
# print(lst)
