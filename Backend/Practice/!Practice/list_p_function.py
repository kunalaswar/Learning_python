# # #Append function
# l1=[1,2,"Rossum",True]
# print(l1,type(l1),len(l1))
# l1.append("kunal")
# l1.append(2+3j)
# l1.append(False)
# print(l1,type(l1),"length = ",len(l1))
# #       l1.append(10,20,30)   TypeError: list.append() takes exactly one argument (3 given) IMP
# l1.append([10,20,30])
# print(l1,type(l1),len(l1))
# print(l1[8,0])

# insert function
# lst=[1,2,3,4,5,6]
# print(lst,type(lst))
# lst.insert(0,100)
# lst.insert(-1,100)
# # lst.insert(4,100)
# print(lst,type(lst))

# lst=[10,"Rossum",34.56]
# print(lst,type(lst))
# # print(lst.insert(2,200))
# lst.insert(2,200)
# print(lst)
# lst.insert(0,100)
# print(lst)
# lst[-1]=44.45 # to replace the value
# print(lst)
# lst.insert(2,"python")
# print(lst,type(lst))
# lst[3]="kunal"
# print(lst,type(lst))
# # adding the value its not an index error 
# lst.insert(10,"harshal")# index 10 is not present in index this list
# print(lst,type(lst))
# lst.insert(-10,"HYD")# to insert in the first of the list
# print(lst,type(lst))
# lst.insert(3,["ani",60,2+3j])
# print(lst,type(lst))


# clear function

# clear function two method is there
# lst=[1,2,3]
# # print(lst.clear())
# lst.clear()
# print(lst,type(lst))

#remove function

# lst=[10,20,"Rossum",2+3j,True]
# print(lst,type(lst))
# lst.remove(10)
# print(lst,type(lst))
# lst.remove(2+3j)
# print(lst,type(lst))
# lst.remove(20)
# print(lst,type(lst))
# lst.remove(100)
# print(lst,type(lst))# ValueError: list.remove(x): x not in list

# l1=[10,20,"Rossum",20,30,2+3j,True]
# print(l1,len(l1))
# l1.remove(10)
# print(l1,len(l1))
# l1.remove(30)
# print(l1,len(l1))
# l1.remove(20)
# print(l1,len(l1))
# l1.remove("Rossum")
# print(l1,len(l1))
# l1.remove(100)
# print(l1,len(l1))#ValueError: list.remove(x): x not in list
# l1.remove([2+3j,True])
# print(l1,len(l1))


#pop function 

# lst=[10,20,30,"Rossum",True,2+3j]
# print(lst)
# lst.pop(0)
# print(lst,len(lst))
# lst.pop(-1)
# print(lst,len(lst))
# lst.pop(-1)
# print(lst,type(lst))
# list().pop(100)
# print(list)


# del operator

# lst=[10,20,30,40,50,60]
# print(lst,len(lst))
# del lst[3]
# print(lst,len(lst))
# del lst[0:2]
# print(lst,len(lst))
# del lst[0]
# print(lst,len(lst))
# del lst[::-1]
# print(lst,len(lst))
# del lst #lst delete  NameError: name 'lst' is not defined. Did you mean: 'list'?
# print(lst,len(lst))

# Index() function

# lst=[10,20,30,40,50,60]
# print(lst,len(lst))
# print(lst.index(10))
# print(lst.index(30))
# print(lst.index(40))
# print(lst.index(60))

# Enumarete function 
# lst=[10,20,30,20,30,10,40]
# print(lst,len(lst))
# lst.index(10)
# print(lst)
# for val in lst:
#     print(val ,end=" ")
# for index,value in enumerate(lst):
#     print(index,"==>",value)

# for index,value in enumerate(lst):
#     if(value==60):
#         print(index,"==>",value)
#     else:
#         print("This value is not present in the given list") 
#         break   

# copy function 

# lst1=[10,20,"Rossum"]
# print(lst1,len(lst1))
# lst2=lst1.copy()
# print("lst2 => ",lst2)
# lst1.append("python")
# lst2.append("HYD")
# print(lst1,id(lst1)) #2690268838336
# print(lst2,id(lst2)) #2690268834688

# shallow copy
# lst1=[10,"Kunal",23.34,2+3j,True]
# print(lst1,id(lst1))
# lst2=lst1.copy()
# print(lst2,id(lst2))

# Deep copy 
# Same id or Memory Address
# list1=[10,20,30,"Rossum",2+3j,False]
# list2=list1
# print(list1 ,id(list1))
# print(list2,id(list2))
# list1.remove("Rossum")
# # print(list2,id(list2))
# print(list1,id(list1))


# count() function

# lst=[10,20,30,40,20,30,10,50,10,30]
# print(lst,len(lst))
# lst1=lst.count(10)
# print(lst1)
# lst2=lst.count(50)
# print(lst2)
# lst3=lst.count("python")
# print(lst3)
# kunal=list().count(10)
# print(kunal)
# kunal1=[].count(10)
# print(kunal1)

# s="MISSISSIPPI"
# print(s,type(s))
# list("1231231234561").count("1")
# print(list)
# # list(1231231234561).count(1)
# print(list)
# list([1231231234561]).count(1)
# print(list)
# list("1231231234561").count("1")

# list(["MISSISSIPPI"]).count("M")
# list(["MISSISSIPPI"]).count("I")
# list(["MISSISSIPPI"]).count("P")
# list(["MISSISSIPPI"]).count("MISS")
# list("MISSISSIPPI").count("I")
# list("MISSISSIPPI").count("M")
# list("MISSISSIPPI").count("MISS")


# Reverse() function

# lst1=[10,20,"RS",2+3j,30,"Python"]
# lst2=lst1.reverse()
# print(lst2,id(lst2))# list2 is he NONE cha rahate
# print(lst1,id(lst1))
# lst2=lst1[::-1]
# print(lst2,id(lst2))# list2 is he pan reverse karate list le 
# print(lst1,id(lst1))

#Extend Function
# lst1=[10,"kunal"]
# lst2=[20,"aniket"]
# print(lst1,id(lst1))
# print(lst2,id(lst2))
# lst1.extend(lst2)
# print(lst1)

# lst1=[10,20,30,"kunal"]
# lst2=[31,32,33,"aniket"]
# lst3=[34,21,22,"harshal"]
# print(lst1,id(lst1))
# print(lst2,id(lst2))
# print(lst3,id(lst3))
# lst1=lst1+lst2+lst3 # fro multiple value only  
# print(lst1,id(lst1))
# OR
# lst1.extend(lst2)
# lst1.extend(lst3)
# print(lst1,id(lst1))


# sort Function

# lst=[10,2,3,9,15,19,-4,1,23,]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# lst.sort(reverse=False)
# print(lst)



