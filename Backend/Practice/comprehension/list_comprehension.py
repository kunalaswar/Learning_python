# #  listobj=[ expression   for  varname  in  Iterable_object   if test Cond ] obj
# # lst=[1,2,3,-5,-6,-7]
# # obj= [val for val in lst if val>0]
# # print(obj)

# print("Enter List of values separated by space:")  # [10 2  22  50  10 4 55  -3  0  22]
# lst=  [float(val)  for val  in input().split() ]
# print("content of lst",lst)

# # print("Enter a list of  value seperated by space :")
# # lst=[float(val) for val in input().split()]
# # print(lst)

# # print("Enter a value for list ")
# # lst=[float(val) for val in input().split() ]
# # print(lst)

# # lst=[3,5,6,-1,-7,-9]
# # newlst=[int(val) for val in lst if val>0]
# # print(newlst)

# # lst=[1,2,3,-5,-6,-7]
# # newlst=[int(val) for val in lst if(val>0)]
# # print(newlst)

# # lst=[1,3,4,6,-4,-6,-7]
# # lst2=[val*2 for val in lst if(val>0)]
# # print(lst2,type(lst2))




# #!Program for Obtaining List of -Ve Values from List of Combination +ve and -ve vals
# #*ListComprehensionEx2.py

# # neglst=[ float(val)  for val in input("Enter list of Vals separated by space:").split() if float(val)<0 ]
# # print("List of -Ve Values")
# # print(neglst)

# # neglst=[val for val in input("Enter a list vals seperated by space").split() if int(val)<0]
# # print("List of (-ve) value",neglst)


# # n=(input("Enter list of value seperated by space"))
# # lst2=[]
# # lst=n.split()
# # # print(lst)
# # for val in lst:
# #     if(float(val)<0):
# #         lst2.append(val)

# # print(lst2)


# # n=input("Entre a list of value : ")
# # lst=n.split()
# # print(lst)


# # n=int(input("Entre  a number :"))
# # lst2=[]
# # for val in range(n):
# #     value=int(input("Entre  a number to add into list :"))
# #     lst2.append(value)

# # print(lst2)




# #!Program for Reading the Values from KBD by using Comprehension Tech
# #*ListComprehenReadValuesEx.py

# # lst=[int(val)  for val in input("Enter List of Values Separated by space:").split()]
# # print(lst,type(lst))

# # lst=[int(val) for val in input("Entre a List of value Seperated by space").split()]
# # print(lst,type(lst))

# # s=input("Entre  a text :")
# # x=s.split()
# # print(x)

# # s=int(input("Entre a number :"))
# # lst=[]
# # for val in range(s):
# #     value=input("Entre  a text :")
# #     lst.append(value)
# # print(lst)    






# #!Program for Obtaining List of -Ve Values from List of Combination +ve and -ve vals
# #*ListComprehensionEx2.py

# # neglst=[ float(val)   for val in input("Enter list of Vals separated by space:").split() if float(val)<0 ]
# # print("List of -Ve Values")
# # print(neglst)

# # neglst=[val for val in input("Entre a value :").split() if float(val)<0 ]
# # print(neglst)


# #!Program Obtaining List of +Ve Values from List of Numerical Values
# #*SetComprehensionEx1.py

# # lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]

# # pslist= { val  for val in lst   if val>0 }

# # nglist= {val for val in lst if val<0}
# # print("List of +Ve Vals=",pslist,type(pslist))
# # print("List of -Ve Vals=",nglist,type(nglist))


# # lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]
# # pslist={val for val in lst if(val>0)}
# # nslist={val for val in lst if(val<0)}
# # print("Item of list are in set (+ve)value",pslist)
# # print("Item of list are in set (-ve)value",nslist)

# #!-5,-5 Set is not take a dublicate value so we use list comprehension 
# # lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]
# # pslist={val for val in lst if(val>0)}
# # nslist=[val for val in lst if(val<0)]
# # print("Item of list are in set (+ve)value",pslist,type(pslist))
# # print("Item of list are in set (-ve)value",nslist,type(nslist))

# # lst=input("Enter a number of text : ")
# # x=lst.split()
# # print(x)


# # lst=input("Enter a number of text : ")
# # x=lst.split()
# # print(x)
# # for val in x:
# #     if int(val)<0:
# #         print(val)


#! Program for Deciding whether the given number is Prime or Not from List of Numbers
#* ListComprehensionEx4.py

# def decideprime(val):
#     res=1
#     for i in range(2,val):
#         if(val%i==0):
#             res=0
#             break
#     return res

# #Main Program
# print("Enter List of Values Seperated by space:")
# vals=[int(val) for val in input().split() if int(val)>1]
# primes=[ val   for val in vals  if decideprime(val) ]
# print("List of Given Values:{}".format(vals))
# print("List of Primes:{}".format(primes))


# # def decideprime(val):
# #     res=1
# #     for i in range(2,val):
# #         if(val%i==0):
# #             res=0
# #             break
# #     return res    


# # vals=[int(val) for val in input().split() if(int(val)>1)]
# # primes=[int(val) for val in vals if(decideprime(val))]
# # print( vals)
# # print( primes)
# #

# # def decideprime(val):
# #     res=1
# #     for j in range(2,val):
# #         if(val%j)==0:
# #             res=0
# #     return res        




# # kunal=[int(val) for val in input().split() if(int(val)>1)]
# # # print(kunal)
# # primes=[i for i in kunal if(decideprime(i))]
# # print(kunal)
# # print(primes)

# #?======================================================================================================
# #*
# def decideprime(val):
#     res=1
#     for i in range(2,val):
#         if(val%i==0):
#             res=0
#     return res        


# kunal=[int(i) for i in input().split() if int(i)>1]
# primes=[val for val in kunal if(decideprime(val))]
# print(kunal)
# print(primes)
# #?======================================================================================================


# # def decideprime(val):
# #     res=1
# #     for i in range(2,val):
# #         if(val%i==0):
# #             res=0
# #     return res        



# # kunal=[int(val)for val in input().split() if int(val)>1]
# # primes=[val for val in kunal if(decideprime(val))]
# # print(kunal)
# # print(primes)
# #?====================================================================================================
# # lst = [45,34,54,33,0,-1,-3,17,29,-36]
# # pv = [ val  for val in lst if val>0]
# # nv = [val for val in lst if val<0]
# # print("positive values  : ",pv)
# # print("negative values : ",nv)
# #?====================================================================================================


# #?====================================================================================================
# #!PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING DICT COMPARASION using function 
# lst=[10,13,12,9,6]
# #?====================================================================================================
# def decideprime(val):
#     if val == 1 :
#         return False
#     res=True
#     for i in range(2,val):
#         if val%i==0:
#             res=False
#     return res  

    
# lst_value=[int(val) for val in input("enter values").split()]
# prime={val :"prime" if decideprime(val) else " not prime"   for val  in lst_value}
# for k,v in prime.items():
#     print(k ,v)


# def fprime():
#     res=True
#     for k in range(2,val):


# lst=input("Entre a values:").split()
# lst_value={int(i)for i in lst}
# lst_prime={val:"prime" if fprime(val) else "Not prime" for val in lst_value }
# for k,v in lst_prime.items():
#     print(k,v)



# def fprime(val):
#     res=True
#     for i in range(2,val):
#         if val%i==0:
#             res=False
#         return res




# lst=input("Entre  a value :").split()
# lst_value=[int(val) for val in lst]
# lst_prime={val:"prime"if fprime(val) else  "Not prime" for val in lst_value }
# for k,v in lst_prime.items():
#     print(k,v)

#^ --------------------------------------------------------------------------------------------
# lst = [45,34,54,33,0,-1,-3,17,29,-36]
# pv = [ val  for val in lst if val>0]
# nv = [val for val in lst if val<0]
# print("positive values  : ",pv)
# print("negative values : ",nv)`
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING DICT COMPREHENSIOIN 
# def prime(i):
#     if i ==1 :
#      return False
#     res =True
#     for k in range(2,i//2+1):
#         if i%k==0:
#             res = False
#     return res 

# lst = input("ENTER VALUES : ").split() 
# lst_values = {int(i) for i in lst }
# lst_primes = {val:"PRIME" if prime(val) else "NOT PRIME" for val in lst_values }
# for k,v in lst_primes.items():
#     print(k,"-->",v)
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING LIST COMPREHENSIOIN 
# def decideprime(i):
#      res = True
#      for j in range(2,i//2+1):
#           if i%j == 0 :
#            res = False
#      return res 

# lst = input("ENTER COMMA SEPRATED VALUES : ").split()
# values = [int(val) for val in lst if int(val)>1 ]
# primes = [ i for i in values if decideprime(i)]
# non_primes = [i  for i in values if i<1 or  not decideprime(i)]
# print(primes)
# print(non_primes)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to create a list of squares of numbers from 1 to 10.
# lst = [ i**2  for i in range(1,11)]
# print(lst)





#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to generate a list of even numbers between 1 and 20.
# lst = [i for i in range(1,21) if i%2 == 0]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension that creates a list of numbers from 1 to 10, but only include numbers greater than 5.
# lst = [i for i in range(1,11) if i>5]
# print(lst)

#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to convert all characters in the string "hello world" to uppercase.
# lst = [i.upper()  for i in "hello world" ]
# print("".join(lst))
#^ --------------------------------------------------------------------------------------------
#! Generate a list of tuples (x, x^2) for x in the range 1 to 10 using a list comprehension.
# lst = [(x,x**2) for x in range(1,11)]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
# d = {i:i**3 for i in range(1,6)}
# print(d)
#^ --------------------------------------------------------------------------------------------
#! Use a set comprehension to create a set of unique vowels present in the string "comprehension is fun".
# set = { i for i in "comprehension is fun" if i in "aeiouAEIOU" }
# print(set)
#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to flatten the following list of lists: [[1, 2, 3], [4, 5], [6, 7, 8]].
# lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
# fst =  [j for i in lst for j in i]
# print(fst)


















































