
    #?================================================================
    #!   All students are requested to slove the following Questions
	#?================================================================

#?--------------------------------------------------------------------------------------
#! 1. Write a Python program to sum all the items in a list. 
#?--------------------------------------------------------------------------------------

# lst=[1,233,45,56,67,89,-40,-10]
#*logic-1
# s=0
# for i in lst:
#     s=s+int(i)
# print(s)    
#*logic-2
# print(sum(lst))
#*logic-3
# lst=[1,233,45,56,67,89,-40,-10]
# i=0
# s=0
# while(i<len(lst)):
#     s=s+lst[i]
#     i=i+1
# print(s)

#*logic-4
# n=int(input("Enter a number to give a sum of generated list :"))
# lst=[]
# for i in range(1,n+1):
#     value =int(input(f"Enter a {i} number :"))
#     lst.append(value)
# print(lst)
# s=0
# for i in lst:
#    s=s+int(i) 
# print(f"Sum of generated list : {s}")   

#*logic-5
# lst=[1,233,45,56,67,89,-40,-10]
# s=[]
# print(sum(s+lst))

#?--------------------------------------------------------------------------
#!2. Write a Python program to multiply all the items in a list. 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[1,2,3,4,5,6,7,8,9,10,-40,-10]
# mul=1
# for i in lst:
#     mul=mul*int(i)
# print(mul)   

#*logic-2
# num=int(input("Enter a number to generate a list : "))
# lst=[]
# for i in range(1,num+1):
#     value =int(input(f"Enter a {i} number :"))
#     lst.append(value)
# print(lst)    
# mul=1
# for i in lst:
#     mul=mul*int(i)
# print(mul)    
#*logic-3
# lst=[1,2,3,4,5,6,7,8,9,10,-40,-10]
# mul=1
# i=0
# while(i<len(lst)):
#     mul=mul*lst[i]
#     i=i+1
# print(mul)    
#*logic-4
# lst=[1,2,3,4,5,6,7,8,9,10,-40,-10]


#?--------------------------------------------------------------------------
# !3. Write a Python program to get the largest number from a list.
#?--------------------------------------------------------------------------
# *logic-1
# lst=[10,30,45,5,25,80]
# val=max(lst)
# print(val)

# #*logic-2
# lst=[10,30,45,5,25,80]
# temp=lst[0]
# # print(temp)
# for i in lst:  
#     if(i>=temp): #80
#         temp=i
# print(temp)            

# #*logic-3
# n=int(input("Enter a how many number you wnat to generate  :"))
# lst=[]
# for i in range(1,n+1):
#     value=int(input("enter a number to add in list :"))
#     lst.append(value)
# print(lst)    
# temp=lst[0]
# for i in lst:
#     if(i<=temp):
#         temp=i
# print(temp)        
    # print(i)

#?--------------------------------------------------------------------------
#! 4. Write a Python program to get the smallest number from a list.
#?--------------------------------------------------------------------------
# #*logic-1
# lst=[10,30,45,5,25,80]
# val=min(lst)
# print(val)

# #*logic-2
# lst=[10,30,45,5,25,80]
# temp=lst[0]
# for i in lst:
#     if(temp>=i):
#         temp=i
# print(temp)        

 #*logic-3
# n=int(input("Enter a how many number you want to genetare :"))
# lst=[]
# for i in range(1,n+1):
#     value=int(input("Enter a list of value :"))
#     lst.append(value)
# print(lst)    
# temp=lst[0]
# for i in lst:
#     if(i<=temp):
#         temp=i
# print(temp)    

#?--------------------------------------------------------------------------
#! 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2
#?--------------------------------------------------------------------------
# #*logic-1
# lst=['abc', 'xyz', 'aba', '1221']
# # count=0    
# count=0
# for i in lst:
#     if len(i)>=2 and i[0]==i[-1]:
#         print(i)
#         count=count+1
# print(count)    

# #*logic-2

# lst=['abc', 'xyz', 'aba', '1221']  
# count=0
# for i in lst:
#     for j in i:
#         if(j[0]==j[-1]):
#             # print(j)
#             count=count+1
# print("-------")            
# print(count)            

#?--------------------------------------------------------------------------
#! 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#?--------------------------------------------------------------------------
# lst= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# lst2=[]
# for i in lst:
#     print(i)

















#?--------------------------------------------------------------------------
#! 7. Write a Python program to remove duplicates from a list. 
#?--------------------------------------------------------------------------
#*logic-1
# lst1=[1,2,3,4,1,2,]
# lst2=[]
# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)
#     # print(i)

#*logic-2

# lst1=[1,2,3,4,1,2,]
# lst2=[]
# i=0
# while(i<len(lst1)):
#     if(lst1[i] not in lst2):
#         lst2.append(lst1[i])
#     i=i+1
# print(lst2)

#*logic-3



#?--------------------------------------------------------------------------
#! 8. Write a Python program to check a list is empty or not. 
#?--------------------------------------------------------------------------
# lst=[]
# if(len(lst)==0):
#     print("it is empty list")    
# else:
#     print("It is non empty list ")


#?--------------------------------------------------------------------------
#! 9. Write a Python program to clone or copy a list.
#?--------------------------------------------------------------------------

#*logic-1  shallow copy()
# lst=[12,34,54,80,6,19]
# lst2=lst.copy()
# print(lst2)

#*logic-2  deep copy()
# lst=[12,34,54,80,6,19]
# lst2=lst
# print(lst2)

#*logic-3
# lst=[12,34,54,80,6,19]
# lst2=[]
# for i in lst:
#     lst2.append(i)
# print(lst2)    
#*logic-4
# lst=[12,34,54,80,6,19]
# lst2=[]
# i=0
# while(i<len(lst)):
#     lst2.append(lst[i])
#     i=i+1
# print(lst2)    

#*logic-5 with the use of copy function
# lst=[12,34,54,80,6,19]
# ad=0
# for i in lst:
#     print(i,type(i))

#     res=i%10
#     ad=ad+res
# print(ad)


#?--------------------------------------------------------------------------
#! 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
#?--------------------------------------------------------------------------
# lst=["kunal","harshal","aniket","sagar","prathmesh"]
# lst2=[]
# n=int(input("Entre a number :"))
# i=0
# while(i<len(lst)):
#     if(n<len(lst[i])):
#         print(lst[i])
#     i=i+1

# lst=["kunal","harshal","aniket","sagar","prathmesh"]
# n=int(input("Enter a number :"))
# lst2=[]
# for i in lst:
#     if(str(n)<len(lst[i])):
#         print(i)






#?--------------------------------------------------------------------------
#! 11. Write a Python function that takes two lists and returns True if they have at least one common member.
#?--------------------------------------------------------------------------

# def ch(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 return True
#     return False
    

# lst1=[11,12,13,14]
# lst2=[15,16,17]
# print(f"Is common : {ch(lst1,lst2)}")

# def commom(lst1,lst2):
#     res="no common"
#     for i in lst1:
#         for j in lst2:
#             if(i==j):
#                 res="common"
#                 break


#     if(res=="common"):
#         print("common")
#     else:
#         print("Not common")    

#!main program   
# lst1=[11,12,13,14]
# lst2=[15,16,17,11]
# commom(lst1,lst2)
#?--------------------------------------------------------------------------
#! 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 		Expected Output : ['Green', 'White', 'Black']
#?--------------------------------------------------------------------------
# lst= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# lst1=[]
# lst.remove("Red")
# lst.remove("Pink")
# lst.remove("Yellow")
# print(lst)


#?--------------------------------------------------------------------------
#! 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 
#?--------------------------------------------------------------------------







#?--------------------------------------------------------------------------
#! 14.Write a Python program to print the numbers of a specified list after removing even numbers from it. 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if i%2!=0:
#         print(i)

#*logic-2
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if(i%2==0):
#         continue
#     else:
#         print(i)

#*logic-3
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if(i  not in [2,4,6,8]):
#         print(i)

#*logic-4
# lst=[1,2,3,4,5,6,7,8,9]
# for i in range()






#?--------------------------------------------------------------------------
#! 15. Write a Python program to shuffle and print a specified list.
#?--------------------------------------------------------------------------
#*logic-1
# lst=[23,34,45,56,67,9,31]
# lst[0],lst[1]=lst[1],lst[0]
# lst[2],lst[3]=lst[3],lst[2]
# lst[4],lst[5]=lst[5],lst[4]

# print(lst)

#*logic-2
# lst=[23,34,45,56,67,9,31]
# lst.sort()
# print(lst)

#*logic-3
# lst=[23,34,45,56,67,9,31]
# lst.sort(reverse=True)
# print(lst)

#*logic-4
# import random 
# my_list = [1, 2, 3, 4,5,6,7,8,9]
# random.shuffle(my_list)  #^ Now my_list is shuffle by using the random module [3, 1, 4, 2]
# print(my_list)



#?--------------------------------------------------------------------------
#! 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# lst2=[]
# for i in lst:
#     print("sum=",i*i)
#     lst2.append(i*i)
# print(lst2)    
# print(lst2[0:5])
# print(lst2[-5:])

#*logic-2
# lst=[]
# lst1=[]
# lst2=[]
# for i  in range(1,31):
#     # print(i*i)
#     lst.append(i*i)
# print(lst) 
# for j in lst[0:5]:
#         print(j)
#         lst1.append(j)
# print("-------")    
# print("lst1 =",lst1)   
# for k in lst[-5:]:
#     print(k)
#     lst2.append(k)
# print( "lst2 =",lst2)    


#*logic-3

#!17
#*logic-1
# lst=[]
# for i in range(1,31):
#     # print(i,end=" ")
#     if(i>5):
#         print(f"{i}---> {i*i}")
#         lst.append(i*i)
# print(lst)        





#?--------------------------------------------------------------------------
#! 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[]
# new_list=[]
# for i in range(1,31):
#     # print(i*i)
#     lst.append(i*i)
# print(lst)  

# for j in range(5,len(lst)):
#     # print(j*j)
#     new_list.append(j*j)
# print(new_list)

#*logic-2
# lst=[]
# i=1
# while(i<=30):
#     print(i)
#     lst.append(i*i)
#     i=i+1
# print(lst)
# lst2=[]
# j=6
# while(j<len(lst)):
#     print(j)
#     lst2.append(j*j)
#     j=j+1
# print(lst2)
# 

#*logic-3
# lst=[]
# lst2=[]
# for i in range(1,31):
#     # print(i)
#     lst.append(i*i)  
# print(lst) 
# for j in lst[5:]:
#         lst2.append(j)
#         # print(j)
# print(lst2)

#*logic-4
#! 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 
# lst=[]
# # lst1=[]
# for i in range(1,31):
#     # print(i*i)
#     lst.append(i*i)
# print(lst)
# print(lst[6:])










#?--------------------------------------------------------------------------
#! 18. Write a Python program to generate all permutations of a list in Python.
#?--------------------------------------------------------------------------

#?--------------------------------------------------------------------------
#! 19. Write a Python program to get the difference between the two lists. 
#?--------------------------------------------------------------------------
#*logic-1
# lst1=[10,20,30,40,50]
# lst2=[10,20,60,70,80]
# lst3=[]
# for i in lst1:
#     # print("------")
#     # print(i)
#     # print("------")
#     for j in lst2:
#         if(i==j):
#             # print(j)
#             lst1.remove(i)
# # print(lst3)            
# print(lst1)            


#*logic-2






#*logic-3


# lst1=[10,20,30,40,50]
# lst2=[10,20,60,70,80]
# set1=set(lst1)
# set2=set(lst2)
# print(set1)
# print(set2)
# getss=set1.difference(set2)
# print(set1)
# print(set2)
# print(getss)








#?--------------------------------------------------------------------------
#! 20. Write a Python program access the index of a list. 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[10,20,30,40,50,60,70,80]
# for i in lst:
#     print(lst.index(i))

#*logic-2
# lst=[10,20,30,40,50,60,70,80]
# i=0
# while(i<=len(lst)):
#     print(i)
#     i=i+1
#*logic-3
# lst=[10,20,30,40,50,60,70,80]
# for index,value in enumerate(lst):
#     print(f"Index {index}--->value {value}")

#*logic-4


















#?--------------------------------------------------------------------------
#! 21. Write a Python program to convert a list of characters into a string. 
#?--------------------------------------------------------------------------

#*logic-1
# lst=["kunal","harshal","sagar","aniket","prathmesh"]
# for i in lst:
#     print(i)
# s="".join(lst)
# print(s)    
#^
# lst=["kunal","harshal","sagar","aniket","prathmesh"]
# s1=""
# for i in lst:
#     s1=s1+' '+i
# print(s1)    
#^
# lst=["kunal","harshal","sagar","aniket","prathmesh"]
# s=" ".join(lst)
# print(s)
#^
# lst=["kunal","harshal","sagar","aniket","prathmesh"]

#^
# lst=["kunal","harshal","sagar","aniket","prathmesh"]
# lst=["k","u","n","a","l"]
# l=list(lst)
# print(l)
# for i in lst:
#     print(i,end="")

#! 
# lst=["k","u","n","a","l"]
# print(lst)
# i=0
# while(i<=len(lst)-1):
#     print(lst[i],end="")
#     i=i+1
#^
# lst=["k","u","n","a","l"]
# for index,value in enumerate(lst):
#     print(value,end="")


#?--------------------------------------------------------------------------
#! 22. Write a Python program to find the index of an item in a specified list. 
#?--------------------------------------------------------------------------
# lst=[10,20,30,40,50,60,70,80]
# for i in lst:
#     print(lst.index(i))

# print(i)
# #!
# lst=[10,20,30,40,50,60,70,80,90,100]
# n=int(input("Enter  a number to give a index in betw 10 to 100:"))
# for i in lst:
#     print(lst.index(n))
#     break
# else:
#     print("item not present in list")    
#!

#?--------------------------------------------------------------------------
#! 23. Write a Python program to flatten a shallow list. 
#?--------------------------------------------------------------------------
# INPUT = [[7,8,9],[4,5,6],[1,2,3]] 
# OUTPUT = [7,8,9,4,5,6,1,2,3] 
# logic-1
# lst=[[7,8,9],[4,5,6],[1,2,3]] 
# lst1=[]
# lst2=[]
# lst3=[]
# for i in lst[0] :
#     # print(i)
#     lst1.append(i)
# print(lst1)  
# for j in lst[1]  :
#     # print(j)
#     lst2.append(j)
# print(lst2)    
# for k in lst[2]:
#     # print(k)
#     lst3.append(k)
# print(lst3)
# print(lst1+lst2+lst3)



# INPUT = [[7,8,9],[4,5,6],[1,2,3]] 
# OUTPUT = [7,8,9,4,5,6,1,2,3] 
# lst=[[7,8,9],[4,5,6],[1,2,3]] 
# lst2=[]
# for i in lst:
#     # print(i)
#     for j in i:
#         # print(j)
#         lst2.append(j)
# print(lst2)        

#?--------------------------------------------------------------------------
# !24. Write a Python program to append a list to the second list. 
#?--------------------------------------------------------------------------
#* logic-1
# lst=[10,20,30,40,50,]
# # print(lst)
# print(lst.append([21,22,34,45]))
# print(lst)

#* logic-2
# lst=[10,20,30,40,50]
# lst1=[]
# for i in lst:
#     lst1.append(i)
# print(lst1)    

#* logic-3

#?--------------------------------------------------------------------------
#! 25. Write a Python program to select an item randomly from a list. 
#?--------------------------------------------------------------------------
# INPUT = [1,2,3,3,7,75,75,5,764]
# RANDOM_ELEMENT = 7
# import random
# lst=[1,2,3,3,7,75,75,5,764]
# for i in lst:
#     k=random.randint(1,10)
# print(k) 

#!string random import 
# import random
# s="kunalaniketharshal"
# print(random.choice(s))

# import random
# lst=[1,2,3,3,7,75,75,5,764]





#?--------------------------------------------------------------------------
#! 26. Write a python program to check whether two lists are circularly identical.
#?--------------------------------------------------------------------------










#?--------------------------------------------------------------------------
#! 27. Write a Python program to find the second smallest number in a list. 
#?--------------------------------------------------------------------------
#*when we add the two number same at that time this is not solved 
#! This is not a logic
# lst=[10,4,67,80,44,23,54,72,4]
# lst.sort(reverse=True)
# # print(x)
# print(lst)
# print(lst[-2])

#*logic-1
# lst=[10,4,67,80,44,23,54,72,4]
# temp=lst[0]
# for i in lst:
#     if(temp>len(lst)):
#         print(temp)



#?--------------------------------------------------------------------------
#! 28. Write a Python program to find the second largest number in a list. 
#?--------------------------------------------------------------------------

#?--------------------------------------------------------------------------
#! 29. Write a Python program to get unique values from a list. 
#?--------------------------------------------------------------------------
#*logic-1
# lst=[23,1,23,45,67,89,67]
# lst2=[]
# lst3=[]
# i=0
# while(i<len(lst)):
#     if(lst[i] not in lst2):
#         lst2.append(lst[i])
#         # print(lst[i])
#     else:
#         lst3.append(lst[i])    
#         # print(lst[i])
#     i=i+1
# print("unique values from a list",lst2)
# print(lst3)


#*logic-2
# lst=[23,34,45,56,67,23,45,67]
# lst2=[]
# lst3=[]
# for i in lst:
#     if(i not in lst2):
#         lst2.append(i)
#     else:
#         lst3.append(i)
# print(lst2) 
# print(lst3)       


#?--------------------------------------------------------------------------
#! 30. Write a Python program to get the frequency of the elements in a list. 
#?--------------------------------------------------------------------------
#!wrong output is this
# lst=[10,20,10,20,40,50,60]
# for i in lst:
#     print(lst.count(i))
#*logic-1
# lst=[4,1,2,2,3,4,5,61,7,9,7,8]
# print(lst.count(4))

#*logic-2

# lst=[1,1,2,3,4,5,6,7,]
# count=0
# for index ,value in enumerate(lst):
#     if(value==2):
#         print(f"{index}--->{value}")
#         count=count+1

# print(count)

#?--------------------------------------------------------------------------
#! 31. Write a Python program to count the number of elements in a list within a specified range. 
#?--------------------------------------------------------------------------
#*logic-1
# sn=int(input("Enter a a start number :"))
# en=int(input("Enter a a end number :"))
# lst=[]
# count=0
# for i in range(sn,en+1):
#     value=int(input("Entre  a list of item to add into list : "))
#     lst.append(value)
#     count=count+1
# print(lst)    
# print(f"count of the list : {count}")


#*logic-1
# lst=[1,2,3,4,5,6,7,8,9]
# count=0
# for i in lst:
#     count=count+1

#*logic-2
# print(count)
# lst=[12,23,34,45,6,78,89,80,2,31]
# count=0
# i=0
# while(i<len(lst)):
#     print(lst[i])
#     count=count+1
#     i=i+1
# print(f" count the number of elements in a list within a specified range {count}")

#*logic-3
















#?--------------------------------------------------------------------------
#! 32. Write a Python program to check whether a list contains a sublist.
#?--------------------------------------------------------------------------
# lst=[23,12,34,45,56,[90,80,70,60,50]]
# for i in lst:




#?--------------------------------------------------------------------------
#! 33. Write a Python program to generate all sublists of a list. 
#?--------------------------------------------------------------------------
# lst=[12,23,13,34,24,45,36,66]
# for i in lst:

    # print(i)


# lst=[12,23,13,34,24,45,36,66]
# lst.append([1,2,3])
# print(lst)

#?--------------------------------------------------------------------------
#! 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# 	Sample list : ['p', 'q']
# 	n =5
# 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
#?==============================================================================
# lst =  ['p', 'q']
# lst2=[]
# n=5
# for i in range(n):
#     # print(lst[0]+str(i))
#     lst2.append(lst[0]+(str(i+1)))
#     lst2.append(lst[1]+str(i+1))

# print(lst2)

#?--------------------------------------------------------------------------

#?--------------------------------------------------------------------------
#! 36. Write a Python program to get variable unique identification number or string. 
#?--------------------------------------------------------------------------
# s="kuna422"
# if type(s)==str:
#     print("it is string")
# elif type(s)==int:
#     print("it is digit")
# else:
#     print("it is alphabatic or number")    


#?--------------------------------------------------------------------------
#! 37. Write a Python program to find common items from two lists.
#?--------------------------------------------------------------------------
#*logic- wrong program common item from one list
# lst=[12,90,23,34,45,67,34,12,90]
# lst2=[]
# lst3=[]
# for i in lst:
#     if(i not in lst2):
#         lst2.append(i)
#     else:
#         lst3.append(i)    


# print(lst3)     
# print(lst2)     
# # print(lst2)        

# 37. Write a Python program to find common items from two lists.

# lst1=[10,20,30,40]
# lst2=[10,20,50,60]
# lst=[]
# for i in lst1:
#     if(i in lst2):
#         lst.append(i)
# print(lst) 



# lst1=[10,20,30,40]
# lst2=[10,20,50,60]
# lst=[]
# for i in lst1:
#     for j in lst2:
#         if(i==j):
#             lst.append(i)
# print("for with in for",lst)            

#* wrong program
# lst1=[10,20,30,40]
# lst2=[10,20,50,60]
# s1=set(lst1)
# s2=set(lst2)
# # print(s1)
# # print(s2)
# # for val in s1:
# #     if(s1.isdisjoint(s1)):
# #         print(val)

# print(s1.isdisjoint(s2))




#?--------------------------------------------------------------------------
#! 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# 	Sample list: [0,1,2,3,4,5]
# 	Expected Output: [1, 0, 3, 2, 5, 4]
#?--------------------------------------------------------------------------
# lst = [0,1,2,3,4,5]
# for i in range(0,len(lst)-1,2):
#     lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst)



#?--------------------------------------------------------------------------
#! 39. Write a Python program to convert a list of multiple integers into a single integer. 
# 		Sample list: [11, 33, 50]
# 		Expected Output: 113350
#?--------------------------------------------------------------------------
#* Answer is right but not it in integer its str and converted into int  Through Harshal
# lst=[11, 33, 50]
# s = ''
# for i in lst:
#     s = s+str(i)

# n = int(s)
# print(n,type(n))


#  39. Write a Python program to convert a list of multiple integers into a single integer. 

# lst=[11, 33, 50]
# for i in range(len(lst)):
#     print(lst[i])
# s=""    
# s.join(lst[i])
# print(s)




#*
# lst=[11, 33, 50]











#?--------------------------------------------------------------------------
#! 40. Write a Python program to split a list based on first character of word.      
#?--------------------------------------------------------------------------
# logic-1
# s="aniket","ankush","ankit","sagar","kunal"
# lst=[]
# lst2=[]
# for i in s:
#     if(i[0].startswith("a")):
#         lst.append(i)
#     else:
#         lst2.append(i)
# print("the first letter are startwith a ",lst)        
# print("the first letter are NOT startwith a ",lst2)        

#* logic-1






#?--------------------------------------------------------------------------
#! 41. Write a Python program to create multiple lists.      
#?--------------------------------------------------------------------------
#*logic-1
# while(True):
#     lst=[1,2,3,4,5,6]
#     print(lst)
#         break

#*logic-2
# while(True):
#     n=int(input("Entre a number you want to add into the list "))
#     lst=[]
#     for val in range(1,n+1):
#         value=int(input("Entre a value to add into list :"))
#         lst.append(value)
#     print(lst)    

#*logic-3
# n=int(input("Entre a number"))
# for val in range(1,n+1):
#     lst=[1,2,3,4,5,6]
#     print(lst)

#*logic-4

# n=int(input("Entre a number"))
# i=0
# while(i<n):
#     lst=[1,2,3,4,5,6]
#     print(lst)
#     i=i+1




#?--------------------------------------------------------------------------
#! 42. Write a Python program to find missing and additional values in two lists.      
# 	Sample data : Missing values in second list: b,a,c
# 	Additional values in second list: g,h
#?--------------------------------------------------------------------------
# list1= ['a', 'b', 'c', 'd', 'e']
# list2= ['d', 'e', 'f', 'g', 'h']
# for val in list1:
#     if val not in list2:
#         print(val)
#     else:
#         print("Additonal value",val)    
# # print("ADDitional value=",val)   

        


#?--------------------------------------------------------------------------
#! 43. Write a Python program to split a list into different variables. 
#?--------------------------------------------------------------------------

# lst=[1,2,3]
# a,b,c=lst
# print(a,b,c)

# a=lst[0]
# b=lst[1]
# c=lst[2]
# print(a,b,c)    



#?--------------------------------------------------------------------------
#! 44. Write a Python program to generate groups of five consecutive numbers in a list. 
#?--------------------------------------------------------------------------
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for val in lst[0:5]:
#     print(val)

# lst=[]
# for val in range(1,21):
#     lst.append(val)
# print(lst)  
 
# lst=[i for i in range(1,6)]
# lst1=[]
# count=0
# for val in lst:
#     for i in range(0,len(lst)+1,5):
#         print(i)
        
# num = 0
# l1=[]
# l2=[]
# for i in range(5):
#     for j in range(5):
#         num=num+1
#         l2.append(num)
#     l1.append(l2)
# print(l1)    

# num = 0
# l1=[]
# for i in range(5):
#     l2=[]
#     for j in range(5):
#         num=num+1
#         l2.append(num)
#     l1.append(l2)
# print(l1)    

#OUTPUT:
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    
        

#?--------------------------------------------------------------------------
#! 45. Write a Python program to convert a pair of values into a sorted unique array. 
#?--------------------------------------------------------------------------





#?--------------------------------------------------------------------------
#! 46. Write a Python program to select the odd items of a list. 
#?--------------------------------------------------------------------------
# lst=[1,2,3,4,5,6,7,8,9]
# for val in lst:
#     if val%2!=0:
#         print(val)

#?--------------------------------------------------------------------------
#! 47. Write a Python program to insert an element before each element of a list.
#?--------------------------------------------------------------------------
# Input list: [1, 2, 3]
# Inserted element: "X"

# Output: ['X', 1, 'X', 2, 'X', 3]

# lst=[1,2,3]
# lst2=[]
# for val in lst:
#     lst2.append('x')
#     lst2.append(val)

# print(lst2)



#?--------------------------------------------------------------------------
#! 48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 
#?--------------------------------------------------------------------------
# lst1=[[4,2],[7,9],[0,8]]
# # lst2=[]
# for val in lst1:
#     print(val)
#     # for j in range(1,5):
        # lst1.append(j)
    # print()    
# print(lst1)
# print(lst2)


#?--------------------------------------------------------------------------
#! 49. Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
#?--------------------------------------------------------------------------

# color_name=["Black", "Red", "Maroon", "Yellow"]
# color_code=["#000000", "#FF0000", "#800000", "#FFFF00"]
# dict={}





# for val in color_name:
#     dict=val
#     print(dict)
# for name,color in zip(color_name,color_code):
#     dict[name]=color
# print(dict)

    

#?--------------------------------------------------------------------------
#! 50. Write a Python program to sort a list of nested dictionaries. 
# 		my_collection = {
# 						'KEY1':{'name':'foo','data':1351,'completed':100},
# 						'KEY2':{'name':'bar','data':1541,'completed':12},
# 						 'KEY3':{'name':'baz','data':58413,'completed':18}
# 					    }
# sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['completed']))
# print(sorted_keys)






#?--------------------------------------------------------------------------
# 51. Write a Python program to split a list every Nth element. 
# 	Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# 	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']



#?--------------------------------------------------------------------------

#! 52. Write a Python program to compute the difference between two lists.      
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']

# l1 = ["red", "orange", "green", "blue", "white"]
# l2 = ["black", "yellow", "green", "blue"]

# # l3 = [color for color in l1 if color not in l2]
# # l4 = [color for color in l2 if color not in l1]
# l3=[]
# l4=[]
# for val in l1:
#     if val not in l2:
#         l3.append(val)
#     else:
#         l4.append(val)

# print(l3)
# print(l4)
#?--------------------------------------------------------------------------
#! 53. Write a Python program to create a list with infinite elements. 
#?--------------------------------------------------------------------------
# lst=[]
# # for val in 
# while(True):
#     val=int(input("Enter a value :"))
#     lst.append(val)
#     print(lst)    


#?--------------------------------------------------------------------------
#! 54. Write a Python program to concatenate elements of a list. 
# lst=[]
# lst=['Hello', 'World', '!']
# s=""
# for val in lst:
#     s=s +val
# print(s)    

#?--------------------------------------------------------------------------
# 55. Write a Python program to remove key values pairs from a list of dictionaries. 
#?--------------------------------------------------------------------------
lst=[
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles", "gender": "Male"},
    {"name": "Charlie", "age": 35, "city": "Chicago", }
]
# print(lst[0].popitem())

# 56. Write a Python program to convert a string to a list. 
#?--------------------------------------------------------------------------

#! 57. Write a Python program to check if all items of a given list of strings is equal to a given string. 
#?--------------------------------------------------------------------------
# lst=["k","kunal","kunal"]
# s=input("Enter a string :")
# for val in lst:
#     if s != val:
#         print("NIh aahe equal")
#         break
# else:
#     print("Equal")

#?--------------------------------------------------------------------------
#! 58. Write a Python program to replace the last element in a list with another list. 
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# lst=[1, 3, 5, 7, 9, 10]
# lst2=[2,3,4,6]
# for val in lst2:
#     lst[-1]=val
# print(lst)
# print(lst[:len(lst)-1]+lst2[:])

# lst=[1, 3, 5, 7, 9, 10]
# lst2=[2,3,4,6]
# lst3=[]
# for val in range(len(lst)-1):
#     lst3.append(lst[val])
# lst3+=lst2   
# print(lst3)

# lst=[1, 3, 5, 7, 9, 10]
# lst2=[2,3,4,6]
# lst3=[]
# for val in range(len(lst)-1):
#     lst3.append(lst[val])
# lst3.extend(lst2)  
# print(lst3)





#?--------------------------------------------------------------------------
#! 59. Write a Python program to check whether the n-th element exists in a given list. 
#?--------------------------------------------------------------------------
# lst=[1,2,3,4,5,6,7,8]
# n=int(input("Enter a number :"))
# for val in lst:
#     if n == val:
#         print("present")
#         break
# else:
#     print(" not Present")  
    
#?--------------------------------------------------------------------------
# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
#?--------------------------------------------------------------------------
#! 61. Write a Python program to create a list of empty dictionaries. 
#?--------------------------------------------------------------------------
# lst=[]
# # lst1=[{} for i in range(5)]
# # val = {}
# for i in range(1,6):
#     lst.append(dict())
# print(lst)        

#! 62. Write a Python program to print a list of space-separated elements.
#?--------------------------------------------------------------------------
# lst=['apple', 'banana', 'cherry']
# s=" ".join(lst)
# print(s)

# for val in lst:
    # s.join(val)
# print(s)    

#! 63. Write a Python program to insert a given string at the beginning of all items in a list.
# 	Sample list : [1,2,3,4], string : emp
# 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
#?--------------------------------------------------------------------------
# lst = [1,2,3,4]
# st = "emp"
# lst2=[]
# for val in lst:
#     s="emp"+str(val)    
#     lst2.append("emp"+str(val))   
        
# print(lst2)

#! 64. Write a Python program to iterate over two lists simultaneously.
#?--------------------------------------------------------------------------
# List1= ['a', 'b', 'c']
# List2= [1, 2, 3]
# for l1,l2 in zip(List1,List2):
#     print(l1,l2)

#?--------------------------------------------------------------------------
#! 65. Write a Python program to move all zero digits to end of a given list of numbers. 
# 	Expected output:
# 	Original list:
# 	[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# 	Move all zero digits to end of the said list of numbers:
# 	[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#*This is no a logic
# lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# lst1=[]
# lst2=[]
# for val in lst:
#     if val<=0:
#         lst1.append(val)
#     else:
#         lst2.append(val)   
# print(lst2) 
# print(lst1) 
# print(lst2+lst1)      

#*
# lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# for i in lst:
#     for j in lst:
#         lst[0],lst[1]=lst[0],lst[1]
#     print(j)    


#?--------------------------------------------------------------------------
#! 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]
#?--------------------------------------------------------------------------
        #^ Harshal  Code Aasa lehayach 
# lst=[[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# idx=0
# s=0
# for val in range(len(lst)):
#     if sum(lst[val])>s:
#         s+=sum(lst[val])
#         idx=val
# print(lst[idx])

      
        

# print(s)
# a=sum(l1)
# b=sum(l2)
# c=sum(l3)
# d=sum(l4)
# print(a,b,c,d)
# print(l3)


#?--------------------------------------------------------------------------
# 67. Write a Python program to find all the values in a list are greater than a specified number. 
#?--------------------------------------------------------------------------
# List=[12, 45, 7, 89, 21, 34, 56]
# list2=[]
# Specifiedn= 30
# for val in List:
#     if val>Specifiedn:
#         list2.append(val)

# print(list2)


#?--------------------------------------------------------------------------
#! 68. Write a Python program to extend a list without append.      
# 	Sample data: [10, 20, 30]
# 	[40, 50, 60]
# 	Expected output : [40, 50, 60, 10, 20, 30]
#?--------------------------------------------------------------------------
# lst1=[10, 20, 30]
# lst2=[40, 50, 60]
# # for val in lst1:
# lst2.extend(lst1)
# print(lst2)   
# print(lst2+lst1) 



#?--------------------------------------------------------------------------
#! 69. Write a Python program to remove duplicates from a list of lists.      
# 		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# 		New List : [[10, 20], [30, 56, 25], [33], [40]]
#?--------------------------------------------------------------------------
# list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# list2=[]
# for val in list:
#     if val not in list2:
#         list2.append(val)
# print(list2)        


#?--------------------------------------------------------------------------
#! 70. Write a Python program to find the items starts with specific character from a given list. 
# 		Expected Output:
# 		Original list:
# 		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# 		Items start with a from the said list:
# 		['abcd', 'abc', 'acjd']
# 		Items start with d from the said list:
# 		['dagfa']
# 		Items start with w from the said list:
# 		[]

# lst=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# lst1=[]
# lst2=[]
# lst3=[]
# for val in lst:
#     if val.startswith("a"):
#         lst1.append(val)
#     elif val.startswith("d"):
#         lst2.append(val)
#     elif val.startswith("w"):
#         lst3.append(val)    
# print(lst1)        
# print(lst2)        
# print(lst3)        



#?--------------------------------------------------------------------------
#! 71. Write a Python program to check whether all dictionaries in a list are empty or not. 
# 	Sample list : [{},{},{}]
# 	Return value : True
# # 	Sample list : [{1,2},{},{}]
# # 	Return value : False
#?--------------------------------------------------------------------------

# l1 = [{},{1},{}]
# def check(l1):
#     for dict in l1:
#         if len(dict)>0:
#             return False
#     return True

# print(check(l1))
#?--------------------------------------------------------------------------
#! 72. Write a Python program to flatten a given nested list structure.
# 		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 		Flatten list:
# 		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# list2=[]
# for val in list:
#     list2.append(val)
# print(list2+val)


#?--------------------------------------------------------------------------
#! 73. Write a Python program to remove consecutive duplicates of a given list. 
# 		Original list:
# 		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 		After removing consecutive duplicates:
# 		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# lst2=[]
# for i in lst:
#     if i not in  lst2 :
#         lst2.append(i)
# # print(lst2)        
# lst2.append(lst[-1])
# print(lst2)

# lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# lst2=[]
# for i in lst:
#     if not lst2 or i!=lst2[-1]:
#             lst2.append(i)
# print(lst2)            

   

#?--------------------------------------------------------------------------
# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# 	Original list:
# 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 	After packing consecutive duplicates of the said list elements into sublists:
# 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

# lst=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# lst2=[]




#?--------------------------------------------------------------------------
# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4.3, 5, 1]
# 	List reflecting the run-length encoding from the said list:
# 	[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# 	Original String:
# 	automatically
# 	List reflecting the run-length encoding from the said string:
# 	[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

#?--------------------------------------------------------------------------
# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

#?--------------------------------------------------------------------------
# 77. Write a Python program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

#?--------------------------------------------------------------------------
# 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Length of the first part of the list: 3
# 	Splited the said list into two parts:
# 	([1, 1, 2], [3, 4, 4, 5, 1])

# lst=[1, 1, 2, 3, 4, 4, 5, 1]
# lst1=[]
# lst2=[]
# count=0
# for val in lst[0:3]:
#     lst1.append(lst[val])

# for val in lst[3:]:
#     lst2.append(lst[val])
# print(lst1)    
# print(lst2)   
# print([lst1]+[lst2]) 


# print(lst[3:])



#?--------------------------------------------------------------------------
#! 79. Write a Python program to remove the K'th element from a given list, print the new list. Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After removing an element at the kth position of the said list:
# 	[1, 1, 3, 4, 4, 5, 1]

# lst=[1, 1, 2, 3, 4, 4, 5, 1]


# k=2
# lst.pop(k)
# print(lst)    

#?--------------------------------------------------------------------------
#! 80. Write a Python program to insert an element at a specified position into a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After inserting an element at kth position in the said list:
# 	[1, 1, 12, 2, 3, 4, 4, 5, 1]

# lst=[1, 1, 2, 3, 4, 4, 5, 1]
# # for val in lst:
# lst.insert(2,12)    
# print(lst)

# lst=[1, 1, 2, 3, 4, 4, 5, 1]



#?--------------------------------------------------------------------------
#! 81. Write a Python program to extract a given number of randomly selected elements from a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Selected 3 random numbers of the above list:
# 	[4, 4, 1]

# import random


# lst=[1, 1, 2, 3, 4, 4, 5, 1]
# # for val in range(len(lst)):
# print(random.choices(lst),end=" ")
# print(random.choices(lst),end=" ")
# print(random.choices(lst),end=" ")





#?--------------------------------------------------------------------------
# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 
# HINT
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
# lst2=[]
# lst1=[]
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     lst1.append(lst[0])
#     lst1.append(lst[-1])

#     # lst2.append()


# print(lst1) 
# print(lst2) 

#?--------------------------------------------------------------------------
#! 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. 
# 	Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# 	Result:
# 	243
# lst=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# s=0
# # l=len(lst)
# for val in lst:
#     s=round(val,1)

# print(s*len(lst))   









#*kunal
# lst=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# y=len(lst)
# print(y)
# s=0
# for val in range(len(lst)):
#     # round(lst[val])
#     s=s+ round(lst[val])
# print(s) 
# print(s*y)

#*sagar
# s = 0
# for i in lst:
#     s= s+round(i,1)
# print(s*len(lst))



#?--------------------------------------------------------------------------
# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 
# 	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# 	Minimum value: 4
# 	Maximum value: 22
# 	Result:
# 	20 25 45 55 60 70 80 90 110

# lst=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# lst1=[round(val) for val in lst ]
# # print(lst1)
# lst1.sort()
# print("maxinum number is =",lst1[-1])
# print("min number is =",lst1[0])
# # lst2=[i*5 for i in lst1]
# for i in lst1:
#     print(i*5,end=" ")



# lst=[9,2,5,1,6,3,8,7]
# a=lst[0]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
#             print(lst)
# print(lst)            
# print(val)




#?--------------------------------------------------------------------------
# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. 
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]
# lst=[0,0]

# lst=[i for i in range(11) if i%2==0]
# print(lst)

# l1 = []
# for i in range(3):
#     l2 = []
#     for j in range(2):
#         num = 0
#         l2.append(num)
#     l1.append(l2)
# print(l1)


#?--------------------------------------------------------------------------
# 86. Write a Python program to create a 3X3 grid with numbers.
# 	3X3 grid with numbers:
# 	[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# l=[val for val in range(1,4)  for j in range())]
# print(l)


# lst=[]
# for val in range(1,4):
#     for j in range(1,4):
#         lst.append(j)
# print(lst)    



#?--------------------------------------------------------------------------
# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
# 	Input rows: 2
# 	Input columns: 2
# 	Input number of elements in a row (1, 2, 3):
# 	1 2
# 	3 4
# 	sum for each column:
# 	4 6

# for val in range(1,3):
#     for j in range(1,val):

        



#?--------------------------------------------------------------------------
# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
# 	Input the size of the matrix: 3
# 	2 3 4
# 	4 5 6
# 	3 4 7
# 	Sum of matrix primary diagonal:
# 	14

#?--------------------------------------------------------------------------
# 89. Write a Python program to Zip two given lists of lists. 
# 	Original lists:
# 	[[1, 3], [5, 7], [9, 11]]
# 	[[2, 4], [6, 8], [10, 12, 14]]
# 	Zipped list:
# 	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


# lst1=[[1, 3], [5, 7], [9, 11]]
# lst2=[[2, 4], [6, 8], [10, 12, 14]]
# lst3=[]
# for val in zip(lst1,lst2):
#     lst3.append(val) 
# print(lst3)    

# lst1=[[1, 3], [5, 7], [9, 11]]
# lst2=[[2, 4], [6, 8], [10, 12, 14]]
# lst3=[]
# for k,v in enumerate(2,4):





#?--------------------------------------------------------------------------
# 90. Write a Python program to count number of lists in a given list of lists. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		Number of lists in said list of lists:
# 		4
# 		Original list:
# 		[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# 		Number of lists in said list of lists:
# 		3

# count=0
# lst=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# for val in lst:
#     count=count+1
# print(count)   


# lst1=[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# count=0
# for val in lst:
#     count=count+1
# print(count)    

#?--------------------------------------------------------------------------
# 91. Write a Python program to find the list with maximum and minimum length. 
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 	List with maximum length of lists:
# 	(3, [13, 15, 17])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(3, [3, 5, 7])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(4, [1, 34, 5, 7])
# 	List with minimum length of lists:
# 	(1, [12])

lst=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# print(max(lst))
# print((len(max(lst)),max(lst)))
# print((len(min(lst)),min(lst)))
    



#?--------------------------------------------------------------------------
# 92. Write a Python program to check if a nested list is a subset of another nested list. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		[[1, 3], [13, 15, 17]]
# 		If the one of the said list is a subset of another.:
# 		True   
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		True
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		False

# # def check():
# lst1=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lst2=[[1, 3], [13, 15, 17]]
# res=False
# for val in lst2:
#     if val in lst1:  
#         res=True

# if res:
#     print(res)       
#         # else:
#         #     print(False)    

# # check()

# lst1=[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# lst2=[[[3, 4], [5, 6]]]
# res=False
# for val in lst1:
#     if val in lst2:
#         res=True
# 
#print(res)        

# lst1=[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# lst2=[[[3, 4], [5, 6]]]
# res=False
# for val in lst2:
#     if val in lst1:
#         res=True

# print(res)        




#?--------------------------------------------------------------------------
# 93. Write a Python program to count the number of sublists contain a particular element. 
# 		Original list:
# 		[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# 		Count 1 in the said list:
# 		3
# 		Count 7 in the said list:
# 		2
# 		Original list:
# 		[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# 		Count 'A' in the said list:
# 		3
# 		Count 'E' in the said list:
# 		1

# count=0
# count1=0
# lst=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# for i in lst:
#     for j in i:
#         if j==1:   
#             count=count+1
#     for k in i:
#         if k ==7:
#             count1=count1+1     
# print(count)            
# print(count1)

# count=0
# count1=0
# lst=[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# for i in lst:
#     # print(val)
#     for j in i:
#         if 'A' in j:
#             count=count+1
#     for k in i:
#         if 'E' in k:
#             count1=count1+1        
# print(count)            
# print(count1)            







#?--------------------------------------------------------------------------
# 94. Write a Python program to count number of unique sublists within a given list. 
# 	Original list:
# 	[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# 	Number of unique lists of the said list:
# 	{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# 	Original list:
# 	[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# 	Number of unique lists of the said list:
# 	{('green', 'orange'): 2, ('black',): 1, ('white',): 1}

# lst = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# lst5=[]
# for i in lst:
#     # print(i)
#     for j in i:
#         if j not in lst5:
#             lst5.append(j)
# print(lst5)            

#?--------------------------------------------------------------------------
# 95. Write a Python program to sort each sublist of strings in a given list of lists. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# lst=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# for i in lst:
    







#?--------------------------------------------------------------------------
# 96. Write a Python program to sort a given list of lists by length and value. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]









#?--------------------------------------------------------------------------

# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. 
# 	Original list:
# 	[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# 	After removing sublists from a given list of lists, which contains an element outside the given range:
# 	[[13, 14, 15, 17]]




#?--------------------------------------------------------------------------
# 98. Write a Python program to scramble the letters of string in a given list. 
# 	Original list:
# 	['Python', 'list', 'exercises', 'practice', 'solution']
# 	After scrambling the letters of the strings of the said list:
# 	['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

#?--------------------------------------------------------------------------
# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list. 
# 	Original list:
# 	['Python', 3, 2, 4, 5, 'version']
# 	Maximum and Minimum values in the said list:
# 	(5, 2)

#?--------------------------------------------------------------------------
# 100. Write a Python program to extract common index elements from more than one given list. 
# 	Original lists:
# 	[1, 1, 3, 4, 5, 6, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	Common index elements of the said lists:
# 	[1, 7]
#?--------------------------------------------------------------------------


























#*logic-2
#*logic-3
#*logic-4









