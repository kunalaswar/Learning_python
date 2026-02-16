# #! login App
# user = ""
# pwd = ""
# while user!="nit" and pwd!="n123":
#     user=input("Enter a username :")
#     pwd=input("Enter a password :")

# print("Welcome !")    

# for val in "123456":
#     print("python")

# for ch in "python":
#     print(ch)

#?=======================================================================================================
#!write a program  to print  following  character series
#! A B C D E .....Z
#! a b c d e .....z
# for val in range(65,91):
#     print(chr(val),end=" ")

# print()
# for  val in range(97,123):
#     print(chr(val),end=" ")


#?=======================================================================================================
#! Not generated any value not  an Error 
#* Not generated any error
# for val in range(10,1):
#     print(val)

# for val in range(1,10,-1):
#     print(val)

# for val in range(-1,-10):
#     print(val)

# for val in range(-10,-1,-1):
#     print(val)

# for val in range(ord("A"),ord("Z")):
#     print(chr(val),end=" ")

#?=======================================================================================================
#! write a program to input n number and print sum ,avg
# n=int(input("Enter a  number :"))
# sum=0
# for val in range(1,n+1):
#     num=int(input(f"Enter {val} number :"))
#     sum=sum+num
# print("sum ",sum)
# print("Average ",sum/n)

#!Write a program to find the sum of square 
# n=int(input("Enter a number :"))
# sqr_sum=0
# for val in range(1,n+1):
#     print(val*val)
#     sqr_sum=sqr_sum+val*val

# print("----------------")
# print("sum of square : ",sqr_sum)

#?=======================================================================================================
#^ IMP QUESTION 
#!fibonacci series 
#! 0 1 1 2 3 5 8 13 21







#?=======================================================================================================
#!write a program to find factorial of input number 
# num=int(input('Enter s number :'))
# fact=1
# for val in range(1,num+1):
#     fact=fact*val
# print(fact)

# num=int(input("Entera number :"))
# fact=1
# i=1
# while(i<num):
#         fact=fact*i
#         i=i+1
#         print(i)
# print(fact)        


# num=int(input("Enter a number :"))
# i=1
# while(i<=num):
#     print(i)
#     i=i+1

#?=======================================================================================================
# #^  for with in for Nested for loop
# #! nested for loop
# #! Q prime number with in 1 to 100
# for val in range(2,101):
#     for i in range(val):
        
#?=======================================================================================================
#! write a table from 1 to 10
# for num in range(1,11):
#     print("---------------")                
#     for i in range(1,11):
#         print(f"{num} X {i} = {num*i}")

#?=======================================================================================================
#! write a program to find the prime number from 2 to 30
# for num in range(2,31):
#     for i in range(1,num+1):
#         res=num%i
#     print(res)

# for num in range(2,31):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     # if count==3: #* that why 4 is not comming in that prime number 
#     if count==2:
#         print(num,end=" ")        
        

#?=======================================================================================================
#! write a program to find factorial of all the number from 1 to 5
for num in range(1,6):
    # print()
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact,end=" ")        


#?=======================================================================================================






#?=======================================================================================================























#?=======================================================================================================
























