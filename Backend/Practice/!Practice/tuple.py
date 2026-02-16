# t1=(10,20,30,40,50,60)
# print(t1,type(t1))
# a=tuple()
# t1=tuple(a)
# print(t1,type(t1))
# t1=tuple([a])
# print(t1,type(t1))
# t1=(10,20,"RS",2+3j,True,10)
# print(t1,type(t1))
# t1.append(40) #AttributeError: 'tuple' object has no attribute 'append'
# print(t1,type(t1))

# t1.insert(1,"Python") #AttributeError: 'tuple' object has no attribute 'insert'
# print(t1,type(t1))

# t1.clear() #AttributeError: 'tuple' object has no attribute 'clear'
# print(t1,type(t1))

# t1.pop()#AttributeError: 'tuple' object has no attribute 'pop'
# print(t1,type(t1))

# t1.pop("RS") #AttributeError: 'tuple' object has no attribute 'pop'
# print(t1,type(t1))

# print(t1.count(10),type(t1)) # 2 <class 'tuple'>

# print(t1.index(10),type(t1)) # 0 <class 'tuple'>

# lst1=[10,20,30,30,20,10,10,20,30,10]
# print(lst1)
# for val in lst1:
#     print(val,lst1.count(val))

# t2=t1.copy()
# print(t1,type(t1)) #AttributeError: 'tuple' object has no attribute 'copy'
# print(t2,type(t2))

# t1=(10,20,"RS",2+3j,True,10)
# t1=(40,11,54,21,77,56,10,20)
# print(t1,type(t1))#^ ya cha var sort function chalat nahi manum he list madhe convert kela aani mag te parat tuple madhe convert kela
# t1.sort()# AttributeError: 'tuple' object has no attribute 'sort'
# print(t1,type(t1))
# lst=list(t1)
# print(lst)
# lst.sort()
# print(lst)
# t1=tuple(t1)
# print(t1)

# t1=(10,-23,12,45,67,12,45)
# print(t1,type(t1)) #(10, -23, 12, 45, 67, 12, 45) <class 'tuple'>
# x=sorted(t1) 
# print(x,type(x)) #[-23, 10, 12, 12, 45, 45, 67] <class 'list'>
# t1=tuple(x)
# print(t1,type(t1)) #(-23, 10, 12, 12, 45, 45, 67) <class 'tuple'>
# t2=t1[::-1] # Reversed of the tuple (67, 45, 45, 12, 12, 10, -23) <class 'tuple'>
# print(t2,type(t2))


# tup=(1,2,3,4,5,6)
# print(tup)
# tuple=1,2,3,4,5,6,7,8
# print(tuple)
# tup=1,2,3,4,5,6,7,8
# print(tup)

# a=1,2,3,4,5,6,7,8
# print(a)

# tup=(10,)
# print(tup)

# tup=list([1,])
# tup=tuple([1,])
# print(tup,type(tup))

# tup=tuple((1))   #!Error 
# print(tup)
# tup=tuple((1,))
# print(tup)

# s=str(123456)     #!TypeError: 'int' object is not iterable
# # s="RADAR"
# # print(s,type(s))
# tup=tuple(s)
# print(tup,type(tup))
# k=list(tup)
# print(k,type(k))

# t=(10)
# print(t,type(t))

# t=(10,)
# print(t,type(t))

# x="python"
# print(x,type(x))

# x=("python")
# print(x,type(x))

# t1=(10,20,30,40,50,60)
# t2=t1    #!Deep copy is possible not shallow copy 
# print(t2)

# t1=(10,"RS",45.67,77)
# # print(t1)
# t1.index(10)
# print(t1.index(10))
# print(t1.index("RS"))
# #print(t1.index(45.67))
# #print(t1.index(77))

# t1=(10,"RS",45.67,77,10,20,20)
# print(t1.count(10))
# print(t1.count(20))
# print(t1.count("RS"))

# t1=(10,-4,100,90,44,50,2,-7)
# print(tuple(sorted(t1)))

# t1=(10,20,30,40,50,60)
# print(t1)
# t2=t1[::-1]
# print(t2)

# t1=(10,-4,100,90,44,50,2,-7)
# # print(tuple(sorted(t1)))
# # print(tuple(sorted(t1)[::-1]))
# x=sorted(t1)
# print(x,type(x))
# print(x[::-1],type(x))



# t1=(10,-4,100,90,44,50,2,-7)
# lst=list(t1)
# lst.sort()
# print(lst)
# tup=tuple(lst)
# print(tup)

 #! Inner tuple OR nested tuple
# tup=(10,20,30,(90,80,70))
# print(tup)
# print(tup[3][0])
# # print(tup[3][1])
# # print(tup[3][2])


# t1=(10,"RS",(16,19,17),(67,80,78),"CET")
# print(t1[3])
# print(t1[2])
# for i in t1:
#     print(i,type(t1))
# print(t1[2][0])
# print(t1[2][2])

# t1=(10,"RS",[16,19,17],[67,80,78],"CET")
# print(t1,type(t1))
# for i in t1:
    # print(i,type(i))

# t1[2].append(99)
# print(t1[2])
# t1[2].insert(1,100)
# print(t1[2])
# t1[2].sort()
# print(t1[2])
# t1[2].sort(reverse= False)
# print(t1[2])
# t1[2].sort(reverse= True)
# print(t1[2])

# t1=(10,"RS",[16,19,17],[67,80,78],"CET")


#& To Add NEW key :value in the Dict

dict={"kunal":1}
dict["sagar"]=2
print(dict)


