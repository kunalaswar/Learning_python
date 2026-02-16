# i=1
# while(i<=5):
#     print(i)
#     i=i+1

# i=1
# while(i<=5):
#     print("=========")
#     print(f"\t{i}")
#     print("=========")
#     j=1
#     while(j<=3):
#         print(j)
#         j=j+1
#     i=i+1
# else:
#     print("it is outer while loop else part ")    

# i=1
# while(i<=5):
#     print("======")
#     print(f"\t{i}")
#     print("======")
#     j=1
#     while(j<=3):
#         print(j)
#         j=j+1
#     i=i+1

# i=1
# while(i<=5):
#     print("======")
#     print(i)
#     print("======")
#     for j in range(1,4):
#         print(j)
#     else:
#         i=i+1    

# for i in range(1,6):
#     print("======")
#     print(i)
#     print("======")
#     j=1
#     while(j<=3):
#         print(j)
#         j=j+1
# else:
#     print(" it is else part")  


#! print  table in Nested for loop
# for i in range(1,6):
#     print("======")
#     print(i)
#     print("======")
#     for j in range(1,11):
#         # print("*************")
#         print( f"\t{i} X {j} = {i*j}")
#         # print("*************")

# for i in range(20,9,-2):
#     print(i)

# for i in range(10,21,2):
#     print(i)


#! print  table in Nested for loop to N number 
# n=int(input("How many muntiplication table you want :"))
# for i in range(1,n+1):
#         print("******************")
#         print("\t",i)
#         print("******************")
#         for j in range(1,11):
#               print( f"\t{i} X {j} = {i*j}")

#! write a program to which will display Random multiplication table you want
#^ Innerrandom table  you want
# n=int(input("How many muntiplication table you want :"))

# for i in range(1,n+1):
#     value =int(input("Enter a number which table you want:"))
#     print(value)
#     for j in range(1,11):
        
#         print( f"\t{value} X {j} = {value*j}")

#*  Take a number from input and add into list
# n=int(input("Enter a number:"))
# if(n<=0):
#     print("Invalid Input ")
# else:
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input(f"Enter a { i} number:"))
#         lst.append(value)
# print(lst)        



# n=int(input("Enter a number:"))
# if(n<=0):
#     print("Invalid Input ")
# else:
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input(f"Enter a {i} number:"))
#         lst.append(value)
#     else:
#         print(lst)
#         for number in lst:
#             if(number<=0):
#                 print("Invalid Input")
#             else:
#                 for i in range(1,11):
#                     print(f"{number} X {i}={number*i}")    
#             print(number)    


# n=int(input("Enter a number :"))
# if(n<=0):
#     print("Invalid Input")
# else:
#     lst=[]    
#     for i in range(1,n+1):
#          value=int(input(f"Enter a {i} number:"))
#          lst.append(value)
#     print(lst)        
#     for num in lst:
#         print("=========")
#         for k in range(1,11):
#             print(f"{num} X {k} ={num*k} ")


# n=int(input("How many number to table  you  want to generate :"))
# if(n<=0):
#     print("Invalid input ")
# else:
#     lst=[]    
#     for i in range(1,n+1):
#         value=int(input(f"Enter a {i} number : "))
#         lst.append(value)
#     print(lst)    
#     for num in lst:
#         print("-------------------")
#         print(f" munltiplication table for {num}")
#         if(num<=0):
#             print("Invalid input ")
#         else:
#             for j in range(1,11):
#                 print(f"\t{ num} X {j} = {num*j}")    

#! write a program which will display list of prime with in given range
# n=int(input("Enter a range of prime number : "))
# if(n<=0):
#     print("Invalid number :")
# else:
#     lst=[]
#     for num in range(2,n):
#         res="prime"
#         for i in range(2,num):
#             if(num%i==0):
#                 res="Not prime"
#                 break
#         if(res=="prime"):
#             lst.append(num)
# print(lst)            

#^ write a program which will display list of prime with in given range

# n=int(input("Enter a number :"))
# if(n<=0):
#     print("invalid input")
# else:
#     lst=[]
#     for num in range(2,n):
#         res="prime"        
#         for i in (2,num):
#             if(num%i==0):
#                 res="Not prime"
#                 break
#         if(res=="prime"):
#             lst.append(num)
#     print(lst)



#* prime number in given number

# n=int(input("Enter a number :"))    
# if(n<=0):
#     print("Invalid Input :")
# else:
#     res="prime"
#     i=2
#     while(i<n):
#         if(n%i==0):
#             res="Not prime"
#             break
#         i=i+1        

# print(f"{n} is {res}")

# n=int(input("Enter a number :"))    
# if(n<=0):
#     print("Invalid Input :")
# else:
#     res="prime"
#     for i in range(2,n):
#         if(n%i==0):
#             res="Not prime"
#             break
# print(f"{n} is {res}")        

# num=int(input("Enter a number :"))
# res=True
# i=2
# while(i<num):
#     if num%i==0:
#         res=False
#         break
#     i=i+1
# res="Prime" if res else "Not prime"
# print(f"{num} is {res}")

# num=int(input("Enter a number :"))
# res="prime"
# for i in range(2,num):
#     if(num%i==0):
#         res="Not prime"
#         break
# print(f"{res}")    

# num=int(input("Enter a number :"))
# res="prime"
# i=2
# while(i<num):
#     if(num%i==0):
#         res="Not prime"

#     i=i+1
# print(f"{res}")    

#! prime number
#^ prime number
#* prime number
# num=int(input("Enter a number :"))
# if(num<=0):
#     print("Invalid input :")
# else:
#     res="prime"    
#     i=2
#     while(i<num):
#         if(num%i==0):
#             res="Not prime"
#             break
#         i=i+1
# print(res)












































