
#! print tables from 1 to 5 using while loop
# i=1
# while i<=5:
#     j=1
#     while j<=10:
#         p=i*j
#         print(p)
#         j=j+1
#     i=i+1    

#?=====================================================================================================
# num=1
# while num<=5:
#     i=1
#     while i<=10:
#         print(f"{num}x{i}={num*i}")
#         i=i+1
#     num=num+1    


#! Write a program to armstrong numbers from 100 to 999
#?======================================================================================================
#! harshal code 
# print("Amstrong number ")
# for i in range(100,1000):
#     total = 0
#     n = i
#     while n>0:
#         r = n%10
#         total += r**3
#         n = n//10
#     if i == total:
#         print(f"{i} is an amstrong number")


#! 
# num=100
# while num<=999:
#     num1=num
#     s=0
#     while num>0:
#         r=num%10
#         s=s+(r**3)
#         num=num//10
#     if s==num1:
#         print(num1)
#     num=num1+1        



#! Write a program to find input number is prime or not using break keyword
#?=====================================================================================================
# num=int(input("Enter a any number :"))
# count=0
# for j in range(1,num+1):
#     if num%j==0:
#         count=count+1
#     if count>2:
#         break
# if count==2:
#     print(f"{num} is prime")
# else:    
#     print(f"{num} is not prime")
#!
# num=int(input("Enter any number "))
# c=0
# for i in range(1,num+1):
#     if num%i==0:
#         c+=1
#     if c>2:
#         break
# if c==2:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")


#! finding factorial of a number
#?=====================================================================================================
# num=int(input("Enter a number :"))
# fact=1
# i=num
# while(num>0):
#     print(num)
#     fact=fact*num
#     num=num-1
# print(fact)    

#!for loop
# num=int(input("Enter a number :"))
# fact=1
# for i in range(1,num+1):
#     print(num)
#     fact=fact*i
  
# print(fact)    

#! Write a program to add or print sum of elements or items
# list1=[10,20,30,40,50,60,70,80,90,100]
#?=====================================================================================================
# list1=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# for val in list1:
#     sum=sum+val
#     print(val)
# print(sum)

#!
# list1=[10,20,30,40,50,60,70,80,90,100]
# s=0
# for i in range(len(list1)):
#     s=s+list1[i]
# print(f"List is {list1}")
# print(f"Sum of elements are {s}")
#!
# list1=[10,20,30,40,50,60,70,80,90,100]
# s=0
# for i in range(len(list1)):
#     s+=list1[i]
# print(s)    

#! Write a program to find maximum element of list
# list1=[10,50,20,70,30,60,40]
#?=====================================================================================================
# list1=[10,50,20,70,30,60,40]
# max_val=0
# for val in range(len(list1)):
#     if list1[val]>max_val:
#         max_val=list1[val]
# print(max_val)        

      



#! Write a program to find minimum element of list
# list1=[10,50,20,70,30,5,60,40]
#?=====================================================================================================
# list1=[10,50,20,70,30,5,60,40]
# max_val=list1[0]
# for val in range(len(list1)):
#     if list1[val]<max_val:
#         max_val=list1[val]
# print(max_val)  

#?=====================================================================================================
#! Write a program to find avg of list
# list1=[10,50,20,70,30,5,60,40]
# avg=0
# sum=0
# for val in range(len(list1)):
#     sum=sum+list1[val]
# print(f"sum of list is {sum}")    
# avg=sum/len(list1)
# print(f"average of list {avg}")



# Example: 
#! Write a program to find median
# list1=[10,50,20,70,30,5,60,40]
# l=len(list1)
# if l%2==0:
#     i=l//2
#     median=(list1[i]+list1[i-1])/2
# else:
#     i=l//2
#     median=list1[i]
# print(f"Median is {median}")







#?=====================================================================================================
#! iter function 
# list1=[10,20,30,40,50]
# a=iter(list1)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
## print(next(a))    #!StopIteration


#?=====================================================================================================
#! Missing in Array
# n=5
# arr=[1,2,3,5]
# for x in range(1,n+1):
#     if x not in arr:
#         print(x)

# Output
# 4


#! Removing duplicate values from list
# list1=[1,2,3,1,2,3,1,2,3]
# list2=[]
# for value in list1:
#     if value not in list2:
#         list2.append(value)
# print(list1)
# print(list2)
# Output
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [1, 2, 3]



#*Without using extend method append more than value?
#*Without extend method, we can append more than value using slicing.
#?==================================================================================================
# Syntax:
# list-name[len(list):len(list)]=iterable

## Example:
# list1=[10,20]
# print(list1)
# # [10, 20]
# list1[len(list1):len(list1)]=[30,40,50,60]
# print(list1)



#!Python program to interchange first and last elements in a list
#?==================================================================================================
# list1=list(range(10,110,10))
# print(f"Before interchanging {list1}")

# list1[0],list1[-1]=list1[-1],list1[0]
# print(f"After Interchanging {list1}")
#!
# list1=list(range(10,110,10))
# print(f"list before interchanging {list1}")
# list1[0],list1[-1]=list1[-1],list1[0]
# print(f"list after interchanging {list1}")


#?==================================================================================================
# Example: #!    IMP LOGIC

#! Write a program to sort elements of list in ascending order
# n=int(input("Enter How Many Elements"))
# list1=[]

# for i in range(n):
#     ele=int(input("Enter Element"))
# list1.append(ele)
# print(list1)
# for i in range(n):
#     for j in range(n-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]

# print(list1)

# Output
# Enter How Many Elements?6
# Enter Element3
# Enter Element1
# Enter Element5
# Enter Element2
# Enter Element4
# Enter Element0
# [3, 1, 5, 2, 4, 0]
# [0, 1, 2, 3, 4, 5]


#?==================================================================================================
# Example:  #!IMP LOGIC
#! Write a program to remove all occurences of given value from list
# list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
# value=10
# print(list1)
# while True:
#     if value in list1:
#         list1.remove(value)
#     else:
#         break

# print(list1)

# Output
# [10, 20, 30, 10, 10, 20, 40, 50, 60, 10, 10, 90, 80]
# [20, 30, 20, 40, 50, 60, 90, 80]
