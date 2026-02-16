#  varname=map(FunctionName,Iterable_object)
# def fun(a,b):
#     return a+b


# lst=[int(i) for i in input("Enter a number :").split()]
# lst1=[int(i) for i in input("Enter a number :").split()]
# # mapobj=list(filter(lambda a+b : ))    
# mapobj=list(map(fun, lst,lst1))
# print(mapobj)



#!Program for accepting the Salaries of emp and give 50% Hike to every EMP
#MapEx1.py
# def hike(sal):
#     return(sal+sal*50/100)

# #Main Program
# print("Enter Emp Salaries separated By Space ")
# oldsal=[float(sal) for sal in input().split() if float(sal)>0]
# mapobj=map(hike,oldsal)
# print("type of mapobj=",type(mapobj)) # <class 'map'>
# newsal=list(mapobj)
# print("Old Salary\t\tNew Salary")
# for osl,nsl in zip(oldsal,newsal):
#     print("\t{}\t\t{}".format(osl,nsl))



# def hike(sal):
#     return(sal+sal*50/100)

# print("Enter Emp Salaries seperated by space")    
# oldsal=[int(i) for i in input().split()]
# objmap=map(hike,oldsal)
# print(list(objmap))
# for osl,nsl in zip(oldsal,objmap):
#     print(osl,nsl)

# print("entre a  emp salaries seperated by sapce ")
# oldsal=[int(i) for i in input().split()]
# # objmap=map(lambda a,b:a+b )
# objmap=map(lambda a:int(a+a*50/100),oldsal)
# print(objmap)
# print(list(objmap))


#!Program for accepting the Salaries of emp and give 50% Hike to every EMP
#MapEx2.py
# hike=lambda sal:sal+sal*50/100
# #Main Program
# print("Enter Emp Salaries separated By Space ")
# oldsal=[float(sal) for sal in input().split() if float(sal)>0]
# newsal=list(map(hike,oldsal))
# print("*"*50)
# print("Old Salary\t\tNew Salary")
# print("*"*50)
# for osl,nsl in zip(oldsal,newsal):
#     print("\t{}\t\t{}".format(osl,nsl))
# print("*"*50)


# hike=lambda sal:sal+sal*50/100
# oldlst=[int(i) for i in input().split()]
# newlst=list(map(hike,oldlst))
# print(oldlst,newlst)
# for osl,nsl in zip(oldlst,newlst):
#     print(osl,nsl)


# hike=lambda sal:sal+sal*50/100

# lst=[int(i) for i in input("Entre please").split() if int(i)>0]
# newlst=list(map(hike,lst))
# # print(lst)
# print(newlst)
# for osl,nsl in zip(lst,newlst):
#     print(osl,nsl)
#^-------------------------------------------------------------------------------------------

#!PROGRAM WHICH WILL ACCEPT THREE LIST TYPE OF ELEMENT AND MULTIPLY THEM
# def fun(a,b):
#     return a*b
# lst1=[int(val) for val in input().split()]
# lst2=[int(val) for val in input().split()]
# # if(len(lst1)>len(lst2)):
# # lst3=list(map(lambda k,v:k*v lst1,lst2))
# lst3=map(fun,lst1,lst2)
# print(list(lst3))




#^-------------------------------------------------------------------------------------------
#!PROGRAM FOR ADDING TWO LIST OF ELEMENT if not equal to list then equal it
# print("Enter a list of item to add into list1")
# lst1=[int(val) for val in input().split()]
# print("Enter a list of item to add into list2")
# lst2=[int(val) for val in input().split()]
# if len(lst2)>len(lst1):
#     for i in range(len(lst2)-len(lst1)):
#         lst1.append(0)
# elif len(lst1)>len(lst2):
#     for i in range(len(lst1)-len(lst2)):
#         lst2.append(0)

# lst3=list(map(lambda k,v: k+v, lst1,lst2 ))
# print(lst3)
# for l1,l2,l3 in zip(lst1,lst2,lst3):
#     print(l1 , l2 , l3)

#^-------------------------------------------------------------------------------------------
#!PROGRAM FOR FINDINNG SQUAREROOT
# print("Enter a number to find squareroot of that number in list")
# lst=[int(i) for i in input().split()]
# squt=map(lambda val : val**0.5 ,lst)
# print(list(squt))
#*for v,s in zip(lst,squt):
        # print(v,s)

#^-------------------------------------------------------------------------------------------
#!PROGRAM WHICH WILL ACCEPT THREE LIST TYPE OF ELEMENT AND MULTIPLY THEM

# lst1=[int(val) for val in input().split()]
# lst2=[int(val) for val in input().split()]
# lst3=[int(val) for val in input().split()]
# if(len(lst1)>len(lst2)):
#     for i in range(len(lst1)-len(lst2)):
#         lst2.append(0)
# elif(len(lst2)>len(lst3)):
#     for i in range(len(lst2)-len(lst3)):
#         lst3.append(0)
# elif(len(lst3)>len(lst1)):
#     for i in range(len(lst3)-len(lst1)):
#         lst1.append(0)

# lst4=lambda a,b,c:a*b*c
# mapobj=list(map(lst4,lst1,lst2,lst3))
# # lst4=list(map(lambda a,b:a*b lst1,lst2,lst3))
# print(mapobj)

#?======================================================================================================
#! Giving 10% hike to the Dict vluese:
#write a python program to Take the dict vlaue fron the input












#!     28-10-2024


