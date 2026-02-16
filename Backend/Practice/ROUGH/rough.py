# s="python"
# i=0
# while(i<=len(s)-1):
#     print(s[i])
#     i=i+1

# n=int(input("Enter a number :"))
# s=0
# while(n>0):
#     res=n%10
#     # if res%2==0:
#     s=s+res
#     # print(res)
#     # n=n//10    
# print(n)    
# print(s)


# n=input("Emter a number :")
# d=n.split()
# s=0
# print(d)
# for val in d[0]:
#     s=s+int(val)
# print(s)

# n=input("Enter number ")
# for val in n:
#     if int(val)%2==0:
#         print(val)

# n=input("Enter number :")
# i=0
# while(i<len(n)):
#     if int(n[i])%2!=0:
#         print(n[i])
#     i=i+1

# num=input("Enter number :")


# s="python"
# for val in s:
#     if val=="o":
#         break
#     print(val)

# s="python"
# i=0
# while(i<=len(s)):
#     if s[i]=='o':
#         break
#     print(s[i])
#     i=i+1

# s="MISSISSIPPI"
# count=0
# for val in s:
#     if val=="S":
#         count=count+1

#     if count==3:
#         break
#     print(val)


# s="MISSISSIPPI"
# count=0
# i=0
# while(i<len(s)):
#     # print(s[i])
#     if(s[i]=="S"):
#         count=count+1
#     print(s[i])

#     if count==2:
#         break    
#     i=i+1

# s="python"
# for val in s:
#     if val=="t":
#         continue
#     print(val)

# s="python"
# i=0
# while(i<len(s)):
#     if s[i]=="o":
#         break    
#     print(s[i])
#     i=i+1

# s="python"
# i=0
# while(i<len(s)):
#     if s[i]=="t":
#         i=i+1
#         continue
#     print(s[i])
#     i=i+1

# n=int(input("Enter a number :"))
# if n<=0:
#     print("Invalid input to Enter ")
# else :
#     res="prime"    
#     for val in range(2,n):
#         if n%val==0:
#             res="Not prime"
#             break    
# if res:
#     print(res)        
# else:    
#     print(res)        

# n=int(input("Enter a number :"))
# i=2
# res="prime"
# while(i<n):
#     if n%i==0:
#         res="Not prime"
#         break
#     i=i+1
# if res:
#     print(res)    
# else:
#     print(res)    

# word=input("Emter a word :").lower()
# for val in word:
#     if val in "aeiou":
#         print(val)

# word=input('Enter a word:')
# for val in word:
#     if val not in "aeiou":
#     # if "aeiou":
#         print(val)
#         continue
#     # print(val)
#^--------------------------------------------------------------------------------------------------
# lst=[1,2,33,33,33,33,33,33,5,6,7,1,4,6]

# for val in lst:
#     if val==33:
#         continue
#     lst.append(val)
# print(lst)
# i=0
# while(i<=len(lst)-1):
#     # print(lst[i])
#     if lst[i]<33:
#         lst.append(lst[i])
#     i=i+1




#^--------------------------------------------------------------------------------------------------
# l1=[1,2,10,10,10,10,5,10,10,10,10,3,4,4]
# # d1={ val:l1.count(val) for val in l1  }
# # print(d1)
# d1={}
# for val in l1:
#     d1[val]=l1.count(val)
# print(d1)    


#^------------------------------------------------------------------------------------------------------
# for i in range(1,4):
#     print("----------")
#     print(i)
#     print("----------")
#     for j in range(1,4):
#         print(j)


# for i in range(1,3):
#     print("--------")
#     print(i)
#     print("--------")
#     j=1
#     while(j<=2):
#         print(j)
#         j=j+1

# i=1
# while(i<=3):
#     print("----------")
#     print(i)
#     print("----------")
#     for j in range(1,3):
#         print(j)

#     i=i+1

# i=1
# while(i<=3):
#     print("----------------")
#     print(i)
#     print("---------------")
#     j=1
#     while(j<=3):
#         print(j)
#         j=j+1
#     i=i+1    

# for i in range(1,4):
#     print("------------")
#     print(i)
#     print("------------")
#     j=3
#     while(j>=1):
#         print(j)
#         j=j-1

# num=int(input("Enter a number :"))
# res='prime'
# for i in range(2,num+1):
#     # print(i)
#     for j in range(2,i):
#         if j%i==0:
#             res="not prime"
# if res:
#     print(res)            
# else:
#     print(res)    


# num=int(input("Enter number :"))
# i=2
# while(i<=num):
#     j=2
#     res="prime"
#     while(j<i):
#         if i%j==0:
#             res="not prime"
#             break
#         j=j+1   
#     if res:
#         print(f"{i}---> {res}")     
#     else:
#         print(f"{i}---> {res}")     
            
#     i=i+1    

# while(True):
#     sno=input("Enter a number :")
#     if (sno.isdigit()) and (int(sno)in range(100,201)):
#         print(sno)
#         break
    
#^------------------------------------------------------------------------------------------------------
# dict1={}
# def find_max_length_word(list1):
#     dict1 = {i:len(i) for i in list1}
#     max = 0
#     # print(dict1)
#     for i in dict1:
#         # print(dict1[i])
#         if dict1[i]>max:
#             max=dict1[i]
#             idx=i
            
#     return idx,max

# list1 = [input("Enter names :") for i in range(1,5)]
# word,l=find_max_length_word(list1)
# print(word,l)
#^------------------------------------------------------------------------------------------------------

# def addlst(lst):
#     return lst
#     # print(lst)

# def len_word(lst):
#     dict={}
#     for i in lst:
#         dict[i]=len(i)
#         return dict
#         # print(dict)
# def min_lenword(dict):
#     mv=min(dict.values())    
#     for key,value in dict.items():
#         if val==mv:
#             print(key,value)

# lst=[]
# n=int(input("Enter a number :"))    
# for val in range(1,n+1):
#     value=input("Enter a number to add number :")
#     lst.append(value)
# lstres=addlst(lst)
# dictval=len_word(lstres)
# min_lenword(dictval)    



# tup1 = (10,2,4,2,8,3,2)
# temp=tup1[1]
# for val in tup1:
#     if val>temp:
#         temp=val

# print(temp)


# lst=[v for v in input("Enter a text :").split()]
# print(lst)

# lst=["kunal"]
# dict={val:len(val) for val in lst}
# print(dict)


# lst=[i for i in input("Enter :").split()]
# # print(lst)
# dict={}
# for val in lst:
#     dict[val]=len(val)
#     print(dict[val])
# print(dict)    

# temp=0
# for k in dict:
#     if dict[k]>temp:
#         temp=dict[k]
# print(temp)



# dict={"kunal":5,"sagar":5,"paa":3}
# for val in dict:
#     # print(val)
#     print(dict[val])



# def reversed_fun(n):
#     lst=[]
#     x=n.split() 
#     # print(x)
#     for val in x:
#         lst.append(val[::-1])
#     print(lst)
#         # return lst
    

# n=input("Enter a line of Text :")
# reversed_fun(n)
# # print(l)

# program for Magic number 
# def magic_num(n):
#     square=n*n
#     sn=str(n)
#     ssquare=str(square)
#     if ssquare.endswith(sn):
#         print("Magic number")
#     else:
#         print("NOt a Magic number ")    




# n=int(input("Enter a number :"))
# magic_num(n)



# def sum(a,b):
#     c=a+b
#     print(c)


# a=int(input("Enter aa number: "))
# b=int(input("Enter a number: "))
# sum(a,b)



# def disp(sno ,name,marks):
#     print(f"{sno} {name} {marks}")


# disp(100,"RS",90)
# disp(200,'TS',80)
# disp(sno=200,marks=70,name="KH")

# def disp(sno,name,marks):
#     print(f"{sno} {name} {marks}")


# disp(100,"kk",99)    
# disp(name="TT",200,marks=60)

# def disp(sno,name,marks):
#     print(f"{sno} {name} {marks}")


# sno=int(input("enter a number :"))
# name=input("Enter a Name :")
# marks=int(input("Enter a marks :"))
# # disp(100,"ks",90)
# disp(sno,name,marks)

# def disp(sno,name,marks,city="HYD"):
#     print(f"{sno} {name} {marks} {city}")
    

# disp(100,"jd",90)  
# disp(200,"ll",50,city="Ben")  

# def disp(*kvr):
    # print("NUmber of Length =",len(kvr))
    # print(kvr)
    # for val in kvr:
        # print(val,end=" ")
    # for v in kvr:
    #     print(v,end=" ")    

# disp(10,20,30)    
# disp(10,20,30,40,50)

# disp([],{},())
# disp(set())
# disp(str("hi"),tuple([57]),set(),list(),dict(),dict({2:4}))


# def calculation(sno,name,*val,city="HYD"):
#     print(f"{sno} {name} {city}")
#     print(f"{val}")
#     for v in val:
#         print(v,end=" ")

# calculation(10,"IF",10,20,30,40,city="MUmbai")



# def findtot(sno,name,*vals,city="MH",**submarks):
#     for val in vals:
#         print(val,end=" ")
#     print("Student",sno)    
#     print("Name",name)
#     print("CITY",city)
#     s=0
#     for k,v in submarks.items():
#         print(f"{k}--->{v}")
#         s=s+v
#     print("total is =",s)        

# findtot(100,"kdd",10,20,30,city="TS",pmark= 90,cmarks= 80)    


# # lang="python" #Global Keyword
# def learnAI():
#     sub1="AI"
#     print("TO develop ",sub1,"we use ",lang)

# def learnML():
#     sub2="ML"    
#     print("TO develop ",sub2,"we use ",lang)

# lang="python" #Global Keyword
# #! It must Define another of the Function Call

# learnAI()    
# learnML()


# var1=10
# var2=20
# var3=30

# def fun1():
#     global var1
#     print(var1+30)

# def fun2():
#     print(var2)    

# fun1()
# fun2()



# a=10
# b=20

# def increment():
#     global a,b    #*unboundlocalerror
#     a=a+1
#     b=b+1

# def updation():
#     global a,b
#     a=a+5
#     b=b+5

# def accessvalue():
#     c=a+2
#     d=b+2
#     print(f"{c} ,{d}")



# increment()
# print(f"{a} , {b} ,")
# updation()
# print(f"{a},{b}")
# accessvalue()

# lst=(input("Enter a number :"))
# lst1=[]
# x=lst.split()
# print(x)
# for val in x:
#     if int(val)>0:
#         lst1.append(int(val))
# print(lst1)        

# lst=[int(val) for val in input().split() if int(val)>0]
# print(lst)
# lst1=[int(val)for val in input().split() if int(val)<0 ]
# print(lst1)

# print("Enter a Comma seperated value :")
# lst=[val for val in input().split() if int(val)>0]
# print(lst)
# sqrt=[float(val)**0.5 for val in lst]
# print(sqrt)
# for val1,val2 in zip(lst,sqrt):
#     print(f"{val1}--->{val2}")

# lst=[val for val in input().split() ]
# # print(lst)
# for val in lst:
#     print(val)

# lst=[val for val in input().split() ]
# pset={pval for pval in lst if int(pval)>0}
# nset={nval for nval in lst if int(nval)<0}
# print(pset)
# print(nset)

#*Wring this is
#* lst=[val for val in input().split() if int(val)>0]

# n=int(input('Enter a number :'))
# lst=[]
# for i in range(1,n+1):
#     val=int(input("Enter a value to add an the list:"))
#     lst.append(val)
# dict={int(val):int(val)*int(val) for val in lst}
# print(dict)

# dict={int(val):int(val)*0.5 for val in input().split() if int(val)>0}
# print(dict)
# for k,v in dict.items():
#     print(f"{k}--->{v}")


# def decideprime(val):
#     res=True
#     for i in range(2,val):
#         if val%i==0:
#             res=False
#             break    
#         return res
        
# print("Enter a value here:")
# lst=[int(val) for val in input().split() if int(val)>1]
# print(lst)
# lst1=[val for val in lst if decideprime(val)]
# print("list of Prime number ",lst1)

#* Wrong Program is this To Find the product
# def product(val):
#     for i in range(2,val):
#         return val*i


# lst=[int(val) for val in input().split() if int(val)>0]        
# # print(lst)
# prod=[v for v in lst if product(v) ]
# print(prod)


# def fprime(value):
#     if value==1:
#         return 0
#     res=1
#     for i in range(2,value):
#         if value%i==0:
#             res=0
#         return res    
    
# lst=input("Enter a value :").split()
# lst_value={int(val) for val in lst }
# lst_Prime={value:"prime" if fprime(value) else "Not prime" for value in lst_value }
# print(lst_Prime)
# for k,v in lst_Prime.items():
#     print(f"{k}--->{v}")

#!Fibonacci series
#^---------------------------------------------------------------------------------------------------
# n=int(input('Enter a number for upto you want:'))
# a=0
# b=1
# for val in range(1,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#^---------------------------------------------------------------------------------------------------

# addop=lambda a,b:a+b
# print(addop,type(addop))
# res=addop(100,200)
# print(res)


# def arithmenu():
#     print("""
#             1.ADDITION
#             2.SUBSTRACTION
#             3.MULTILICATION
#             4.NORMAL  DIVISION
#             5.MUDULO DIVISION
#             6.EXPONENTATION
# """)
# sumop =lambda a,b:a+b
# subop=lambda a,b:a-b
# mulop=lambda a,b:a*b
# divop=lambda a,b :a/b
# floordiv=lambda a,b:a//b
# mudulodiv=lambda a,b:a%b
# exop=lambda a,b:a**b
# arithmenu()
# while(True):
#     ch=int(input("Enter U choice here to Give an result"))
#     match(ch):
#         case 1:
#             a,b= int(input("Enter :")),int(input("Enter :"))
#             res=sumop(a,b)
#             print(res)
#         case 2:
#             a,b =int(input("Enter :")),int(input("Enter :"))    
#             res=subop(a,b)
#             print(res)
#         case 3:
#             a,b =int(input("Enter :")),int(input("Enter :"))    
#             res=mulop()
#             print(res)
#         case 4:
#             a,b=int(input("Enter :")),int(input("Enter :"))    
#             res=divop(a,b)
#             print(res)
#         case 5:
#             a,b =int(input("Enter :")) ,int(input("Enter :"))
#             res=floordiv(a,b)
#             print(res)
#         case 6:
#             a,b=int(input("Enter :")),int(input("Enter :"))    
#             res=mudulodiv(a,b)
#             print(res)
            
#         case _:
#           print("No one case in is this type")    


# a=int(input("Enter a value for A :"))
# b=int(input("Enter a value for B :"))
# c=int(input("Enter a value for C :"))
# small=lambda a,b,c : a if b>=a<c else b if a>b<=c else c if a>=c<b else "ALLVALUE EQUAL"
# print("Smallest value is =",small(a,b,c))


# def kmax(lst):
#     mv=lst[0]  #1 2 3 4 
#     for i in lst:
#         if i>mv:
#             mv=i
#     return mv


# def kmin(lst1):
#     minv=lst1[0]
#     for i in lst1:
#         if i<minv:
#             minv=i
#     return minv    

# k=lambda lst:kmin(lst)
# l=[int(val) for val in input("Enter :").split()]
# lst1=[int(val) for val in input("Enter :").split()]

# o=k(lst1)
# print(o)



# def kmax(lst):
#     mv=lst[0]  #[2,3,4,5]
#     for i in lst:
#         if i>mv:
#             mv=i
#     return mv        
            
# def kmin(lst):
#     mn=lst[0]
#     for i in lst:
#         if i<mn:
#             mn=i
#     return mn


# lst_max=lambda lst :kmax(lst)
# lst_min=lambda lst :kmin(lst)


# lst=[int(val) for val in input().split()]
# print(lst)

# res1=lst_max(lst)
# res2=lst_min(lst)
# print(res1)
# print(res2)

#! Reduce Function
# def pos(val):
#     if val>0:
#         return True
#     else:
#         return  False   

# print("Enter a list of  Value seperated by comman")
# lst=[int(val) for val in input().split()]
# obj1=filter(pos,lst)
# print(list(obj1))


# def pos(val):
#     lst1=[]
#     lst2=[]
#     if val>0:
#         lst1.append(val)
#     else:
#         lst2.append(val)

# print("Enter a list  of value seperated by comman")    
# lst=[int(val) for val in input().split()]
# obj=list((filter(pos,lst)))
# # print(list1)


# def pos(val):
#     if val>0:
#         return True
#     else:
#         return False    


# print("Enter a number list of  value seperated by comman")
# lst=[int(val) for val in input().split()]
# obj=list(filter(pos,lst))
# print(obj)


#!filter with the use of Normal function

# def pos(val):
#     if val>0:
#         return 1
#     else:
#         return 0

# lst=[int(val) for val in input().split()]        
# obj=list(filter(pos,lst))
# print(obj)

#! with the use of lambda function

# pos=lambda val:val>0
# neg=lambda val:val<0

# lst=[int(i) for i in input().split()]
# obj=(filter(pos, lst))
# print("List of positive =",list(obj))
# obj1=filter(neg ,lst)
# print("List of Negative =",list(obj1))
# # print(l1)


# pos=lambda val:val%2==0
# neg=lambda val:val%2!=0


# lst=[int(val) for val in input().split()]
# obj=(list(filter(pos,lst)))
# print(obj)
# obj1=(list(filter(neg,lst)))
# print(obj1)

# pos=lambda val :val>0
# lst=[int(val) for val in input().split()]
# obj=(list(filter(pos,lst)))
# print(obj)



# lst=[int(val) for val in input().split()]
# pslst=list(filter(lambda val:val>0,lst))
# nglst=list(filter(lambda val:val<0,lst))
# print(pslst)
# print(nglst)

# s=input("Enter a line of text :")
# s1=s.split()
# print(s1)
# lst2=[]
# for val in s1:
#     if val==val[::-1]:
#         lst2.append(val)
# print(lst2)        

# lst=[int(val) for val in input().split()]
# print(lst)

# lst=[val for val in input().split()]
# obj=list(filter(lambda val:val==val[::-1],lst))
# print(obj)

# word=input("Enter a value :").lower()
# lst=[]
# for val in word:
#     # print(val)
#     if val in "aeiou":
#         lst.append(val)
# print(lst)

# word=input("Enter a line of text: ")
# lst=[val.lower() for val in word ]
# # print(lst)
# vwords=list(filter(lambda word: "a" in word or "e" in word or "i" in word or "o" in word or "u" in word ,lst))
# print(vwords)

# word=input("Enter a line of text :")
# lst=[val.lower() for val in word]
# # print(lst)
# words=list(filter(lambda val: 4>=len(val)<3,lst))
# print(words)


# lst=[val for val in input("Enter :").split() ]
# print(lst)
# obj=list(filter(lambda val: val[0]==val[-1] and val!=val[::-1],lst))
# print(obj)

# lst=[int(val) for val in input().split()]
# # print(lst)
# enlist=list(filter(lambda val: val%2==0 and val>0,lst))
# oddlist=list(filter(lambda val :val %2!=0 and val<0,lst))

# print(enlist)
# print(oddlist)


# def decideprime(val):
#     res=True
#     for i in range(2,val):
#         if val%i==0:
#             res=False
#             break
#         return res    
        

# lst=[int(val) for val in input().split() if int(val)>1] 
# obj=[v for v in lst if decideprime(v)]
# print(obj)


# def findpos(i):
#     if int(i)>0:
#         return i
#     else:
#         return i
    


# # lst=[val for val in input().split()]
# n=int(input('How many value you want to Enter :'))
# lst=[]
# for val in range(1,n+1):
#     value =input("Enter a number :")
#     lst.append(value)


# obj=[int(i) for i in lst if findpos(i)]
# print(obj)


# def even(val):
#     if val%2==0:
#         return True
#     else:
#         return False
        
# odd=lambda val:val%2!=0

# lst=[int(v) for v in input().split()]
# obj=list(filter(even,lst))
# print(obj)
# obj2=list(filter(odd,lst))
# print(obj2)

# def hike(lst):
#     return (lst+lst*50/100)


# n=input("Enter a Salaries seperated by space :")
# oldsal=[float(sal) for sal in n.split()]

# newsal=list(map(hike,oldsal))
# print(newsal)

#!
# def hike(val):
#     return val*val

# lst=[float(val) for val in input().split()]    
# print(lst)
# mapobj=list(map(hike,lst))
# print(mapobj)

# hike= lambda sal :sal+sal*50/100


# lst=[int(val) for val in input().split()]
# print(lst)
# obj = list(map(hike,lst))
# print(obj)

#!
# def listadd(k,v):
#     return k+v

# lst1=[int(i) for i in input("Enter first list :").split()]
# lst2=[int(j) for j in input("Enter Second list :").split()]
# var = list(map(listadd,lst1,lst2))
# print(var)
# for l1,l2,l3 in zip(var,lst1,lst2):
#     print(l1,l2,l3)

#!program for finding the square of value


# n=input("Enter a number :").split()
# lst=[int(val) for val in n]
# print(lst)
# mapobj=list(map(lambda val:val*val,lst))
# print(mapobj)

# def squareop(val):
#     return val*val

# n=input("Enter a number: ").split()
# lst=[int(val) for val in n]
# print(lst)
# mapobj=list(map(squareop,lst))
# print(mapobj)

# n=input("Enter a number :").split()
# lst=[int(val) for val in n]
# print(lst)
# lst1=list(map(lambda val:val*0.5,lst))
# print(lst1)

# dictemp={10:1500,20:2000,30:3000,40:5000}
# for k,v in dictemp.items():
#     print(k,v)

# modsal=list(map(lambda x:dictemp[x]+dictemp[x]*50/100,dictemp))
# print(modsal)
# for val,val2 in zip(dictemp,modsal):
#     print(val,val2)

# import sys
# while(True):
        
#     dictemp={}

#     empno=int(input("Enter a Employee number :"))
#     esal=int(input("Enter a  Employee salary :"))
#     dictemp[empno]=esal
#     ch=input("Enter U chioce (YES/NO):")
#     if ch.lower()=="no":
#         break
#     if ch.lower() not in ["yes","no"]:
#         sys.exit()

#     for k,v in dictemp.items():
#         print(k,v)

# print(dictemp)        


# modsal=list(map(lambda x:dict[x]*50/100,dictemp))
# print(modsal)

# for k,v in modsal.items():
#     print(k,v)

#! even number 
# def sumop(val):
#     return val*val   
    


# lst=[int(val) for val in input().split() if int(val)>0]
# obj=list(filter(sumop,lst))
# print(obj)
# print(lst)

#! map function()

# import functools
# def reduce_mt(a,b):
#     return a+b

# lst=[int(val) for val in input("Enter a number here with the space").split()]
# res=functools.reduce(reduce_mt,lst)
# print(lst)
# print(res)

#!
# import functools 
# reduce_mt=lambda a,b:a+b

# lst=[int(val) for val in input().split()]
# print(lst)
# objredeuce=functools.reduce(reduce_mt,lst)
# print("sum = ",objredeuce)

#!
# import functools

# lst=[int(i) for i in input().split() if int(i)>0]
# # print(lst)
# objreduce=functools.reduce(lambda a,b : a+b ,lst)
# print("sum = ",objreduce)

#!
# lst=[[i,j] for j in range(2)  for i in range(3)]
# print(lst)

# for i in range(3):
#     for j in range(2):
#         print(i,j)


# import functools
# def minumum (k,v):
#     if k<v:
#         return k
#     else:
#         return v
    
# lst=[int(val) for val in input().split()]    
# print(lst)
# reduceobj=functools.reduce(minumum,lst)
# # maximun=functools.reduce(lambda k,v:k>v ,lst)
# print(reduceobj)
# # print(maximun)


# import functools

# lst=[int(val)for val in input().split()]
# print(lst)
# minvalue=functools.reduce(lambda k,v:k if k>v  else v,lst)
# print(minvalue)

#!program for join the word
# import functools

# word=input("Enter a line of Text :")
# lst=[val for val in word.split() ]
# print(lst)
# # joinGen=functools.reduce(lambda k,v:k+""+v ,lst)
# joinGen=functools.reduce(lambda k,v:k+" "+v ,lst)
# print(joinGen)



# import functools
# n=int(input("enter How Many Number you want to Enter into list"))
# lst=[]
# for i in range(n+1):
#     val=input("Enter a word into the string:")
#     lst.append(val)
# print(lst)   
# joinwords=functools.reduce(lambda k,v:k+""+ v,lst)
# print(joinwords)
 

#!Find the Maximun into the list
# lst=[2,5,1,89,45,23,43]
# temp=lst[0]
# # print(temp)
# for val in range(len(lst)):
#     if temp<lst[val]:
#         temp=lst[val]
# print("MAX value = ",temp)        


#!Second Maximum into the list
# lst=[45,4,21,3,89,45,23,43]
# temp=lst[0]
# # print(temp)
# for i in range(len(lst)):
#     if temp<lst[i]:
#         temp=lst[i]
# print(temp)        

#?==================================================================================================
# def outer():
#     x=100
#     y=200
#     def inner():

#         print(x+10)
#         print(y+10)
#     inner()    
# outer()    

# def outer():
#     x=100
#     y=200
#     def inner1():
#         print(f"{x}")
#         print(f"{y}")
#     def inner2():    
#         x=400
#         y=500
#         print(x)
#         print(y)
#    inner1()     
#    inner2()

# outer()
 
# #!Wrong program
# def outer():
#     def inner():
#         x=100
#         y=200
#         print(x)
#         print(y)
#     inner()
#     # print(x)
#     # print(y)
# outer()    


# def outer():
#     x=100
#     y=200
#     print(x)
#     print(y)
#     def inner():
#         nonlocal x,y
#         x=300
#         y=400
#     inner()    
#     print(x)
#     print(y)
# outer()

#!Decorator
# def getvals():
#     return float(input("Enter a number :"))

# def getvals():
#     return int(input("Enter a number :"))     

# def square():
#     n=getvals()
#     return n*n

# res=square()        
# print(res)


# def getvals():
#     return int(input("Enter a number :"))

# def outer(kvr):
#     def inner():
#         n=kvr
#         res=n**2
#         return n,res

#     return inner()
        
# n,res=outer(getvals())        
# print(n,res)

#!
# def getvals():
#     return int(input("Enter a  Value :"))

# def outer(kvr):
#     def inner():
#         n=kvr
#         res=n*n
#         return n,res
#     return inner()    

# n,res=outer(getvals())
# print(n,res)

# res=outer(getvals())
# print(res[0],res[1])

#!
# def getvals():
#     return int(input("enter a number :"))

# def outer(kvr):
#     def inner():
#         n=kvr
#         res=n**2
#         return res
#     return inner()   


# res=outer(getvals())        
# print(res)

#& Filter can take only True Value from the list

#!program to find the +VE and -VE in this the list of value

# lst=[int(val) for val in input().split()]
# print(lst)
# poslist=list(filter(lambda val: val>0 ,lst))
# nglist=list(filter(lambda val : val<0 ,lst))
# print("List of Positve element : ",poslist)
# print("List of Negative Element :",nglist)


#!program to find only Palindrome String

# line=[val for val in input().split()]
# print(line)
# pal=list(filter(lambda val : val!=val[::-1] and val[0]==val[-1],line))
# # pal=list(filter(lambda val : val[0]==val[-1],line))
# print(pal)

# #!Program for Adding the Two list of element into the list

# lst1=[int(i) for i in input("Enter 1 list:").split()]
# lst2=[int(j) for j in input("Enter 2 list:").split()]
# if len(lst2)>len(lst1):
#     for val in range(len(lst2)-len(lst1)):
#         lst1.append(0)
# elif len(lst1)>len(lst2):
#     for val in range(len(lst1)-len(lst2)):
#         lst2.append(0)
# print(lst1)        
# print(lst2)        

# mapobj=list(map(lambda val1,val2: val1+val2,lst1,lst2))
# print("Adding the two list value : ",mapobj)

# #!program for find the squarroot
# lst=[int(val) for val in input().split()]
# # print(lst)
# mapobj=list(map(lambda val:val*0.5,lst))
# print(mapobj)

#!program for implementing  the Following 
#* Given line of Text :S8ti4n%GV@Val2u
#*Alphabets :
#*Digits :
#*Special Symbols :
# lst=[val for val in input("Enter line :")]
# # print(lst)
# alphalist=list(filter(lambda val:val.isalpha(),lst))
# dglist=list(filter(lambda val:val.isdigit(),lst))
# dglist=list(filter(lambda val:val.isalnum() and not val.isspace(),lst))

# print(alphalist)
# print(dglist)
# print(dglist)

#& decorator

# def outer(kvr):
#     def inner():
#         n=kvr()
#         res=n*n
#         return res
#     return inner    

# def getvals():
#     return int(input("Enter a number :"))        

# res=outer(getvals)
# p=res()
# print(p)

#^--------------------------------------------------------------------------------------------------
#!

# def outer(kvr):
#     def inner():
#         n=kvr()
#         res=n**2
#         return res
#     return inner()    

# @outer
# def getvals():
#     return int(input("Enter a number:"))

# res=getvals()   
# print(res)

#^--------------------------------------------------------------------------------------------------
#! write  python program which will accept line of text and display completely in lowercase ans uppercase sepereted by using decorator 
# def outer(kvr):
#     def inner():
#         n=kvr()
#         res=n.upper()
#         res1=n.lower()
#         return res,res1
#     return inner    


# @outer
# def getvals():
#     return input("Enter a line of Text here :") 

# res,res1=getvals()
# print("UPPERCASE LETTER= ",res)    
# print("LOWERCASE LETTER= ",res1)
#^--------------------------------------------------------------------------------------------------
#&  RESURSION
#!program for print 0 to 5 with out use of loop
# def print_num(num):
#     if num>0:
#         print_num(num-1)
#     print(num)    


# print_num(5)

#!write a program to find factorial of input number with use of function
# def fun1(num):
#     if num==0:
#         return 1
#     else:
#         return num *fun1(num-1)    
# num=int(input("Enter a number :"))
# res=fun1(num)
# print("factorial  of the given number :",res)

#! write  a program to count digit 
# count=0
# def digit(num):
#     global count
#     if num>0:
#         count=count+1
#         digit(num//10)    


# # num=int(input("Enter a number here :"))

# digit(123)
# print(count)

#!# Write a program to sort elements of list in ascending order

#! Python Program to Find Sum of Array
# # Input : arr[] = {1, 2, 3}
# # Output : 6
# # Explanation: 1 + 2 + 3 = 6
# arr= {1, 2, 3}
# lst=[]
# s=0
# for val in arr:
#     lst.append(val)
# print(lst)    
# # print(s)
# for val in lst:
#     s=s+val
# print(s)    

#! generator function 
# def functions(x):
#     s=0
#     while(s<x):
        # yield s
#         s+=1

# r=functions(5)        
# # print(r)
# for val in r:
#     print(val)

#!

# def func(x):
#     s=0
#     while(s<x): 
#         yield s
#         s=s+1   
# r=func(5)        
# # print(r)
# # for val in  r:
# #     print(val)
# while(True):
#     try:
#         print(next(r))
#     except StopIteration:
#         break    

# #!
# def generator():
#     yield "python"
#     yield "java"
#     yield "Danjo"
#     yield "javascript"
#     yield "c"
#     yield "c++"

# res=generator()    
# print(res)
# while(True):
#     try:

#         print(next(res))
#     except StopIteration:
#         print("-------------------")    
#         break
#*OR 
# for val in res:
#     print(val)
# else:
#     print("-----------------")    


#!Range function with the yeild

# def krange(start,stop=0,step=1):
#     if start>stop:
#         stop=start
#         start=0
#     while start<=stop:
#         yield start 
#         start =start +step    
# r1=krange(100,10,10)
# for val in r1:
#     print(val)        

#!
# text=input("Enter a Line of text :").lower()
# for val in text:
#     if val not in "aeiou":
#         continue
#     else:
#         print(val,end=" ")
    
#!
# try:
#     a=int(input("Enter a first a number :"))
#     b=int(input("Enter a second number :"))
#     c=a/b
# except ZeroDivisionError:
#     print("Dont's enter a zero for Den")
# except ValueError:
#     print("Dont's Enter alnum Sppecial symbols ")    
# else:
#     print(c)
# finally:

#     print("I am finally block")    

#!
# try:
#     a=int(input("Enter  a number "))
#     b=int(input("Enter s number "))
#     c=a/b

# except ValueError:
#     print("Dont Enter a str symbols and any type of data")

# except ZeroDivisionError:
#     print("Dont Enter a zero for  Den")


# else:
#     # print(c)
#     print("Result ",c)

# finally:
#     print("Finally block is optional ")

#!
# try:
#     a=int(input("Enter a number :"))
#     b=int(input("Enter a number "))
#     c=a/b
# except ValueError  as v :
#     print("Dnt enter  a str symbols ",v)

# except ZeroDivisionError as z:
#     print("Dont Enter a zero for Den ",z)


# else:
#     print("Division of a/b =",c)

# finally:
#     print("I am From finally block ")


