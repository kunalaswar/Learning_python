# i=1
# while(i<=5):
#     print(i)    
#     i=i+1


# i=1
# while(i<=10):
#     print(i)
#     i=i+1


# n=int(input("Entera  number :"))
# i=4
# while(i<=100):
#     print( "Even munber ",i )
#     i=i+2

# num=int(input("Enter a number :"))
# if(num<0):
#     print("Negative input :")
# if(num>0):
#     print("positive input")
# if (num==0):
#     print("Zero input")


# #Program for Generating 1 to N Numebrs where N is +VE
# #WhileLoopEx1.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("--------------------------------")
#     print("Numbers within :{}".format(n))
#     print("--------------------------------")
#     i=1 # InitLization Part
#     while(i<=n): # Conditional Part
#         print("\t\t{}".format(i))
#         i=i+1 # OR i+=1  Updation part
#     else:
#         print()
#         print("--------------------------------")


# n=int(input("Enter a a number :"))
# if(n<=0):
#     print("Invalid input = {}".format (n))
# else:
#     i=1
#     while(i<=n):
#         print(i)    
#         i=i+1
#     else:
#         # print()
#         print("------------WHILE LOOP ELSE ")




# print(5<=5)


#Program for Generating 1 to N Numebrs where N is +VE
#WhileLoopEx1.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("--------------------------------")
#     print("Numbers within :{}".format(n))
#     print("--------------------------------")
#     i=1 # InitLization Part
#     while(i<=n): # Conditional Part
#         print("\t\t{}".format(i))
#         i=i+1 # OR i+=1  Updation part
#     else:
#         print()
#         print("--------------------------------")


# num=int(input("Enter a number :"))
# if(num<=0):
#     print(" Invalid input ={}".format(num))
# else:
#     i=num 
#     while(i>=1):
#         print(i)
#         i=i-1


# num=int(input("Enter a number :"))
# i=1
# while(i<=num):
#     print(f"kunal {i}")
#     i=i+1
# print("------------------while loop------------- ")


#print in reverse direction in from user input
# num=int(input("Enter a number :"))
# i=num
# while(i>=1):
#     print(i)
#     i=i-1



# #print in  Even number by taking  user input
# num=int(input("Enter a number :"))
# i=2 #Even number start from 2 so we give i=2
# while(i<=num):
#     print(i)
#     i=i+2

# #print in  odd number by taking  user input
# num=int(input("Enter a number :"))
# i=1 # odd number start from 1 so we give i=1
# while(i<=num):
#     print(i)
#     i=i+2



#print in  Even -Reverse number by taking  user input
# # num=int(input("Enter a number :"))
# i=11 #Even number start from 2 so we give i=2
# while(i>=1):
#     print(i)
#     i=i-2

# print in  Even -Reverse number by taking  user input
# num=int(input("Enter a number :"))
# i=num #Even number start from 2 so we give i=2
# while(1>=num):
#     print(i)
#     i=i-1
# else:
#     print("-----------while else--------------")    


# n=int(input("Enter a number :"))
# if(n<=0):
#     print(f"invalid input{n}")
# else:
#     i=1
#     while(i<=n):
#         print(i)
#         i=i+1    

# n=int(input("Enter a number :"))
# i=1
# while(i<=10):
#     print(i)
    
        
#Program for accepting a Word and Display char by char
#WhileLoopEx4.py
# word=input("Enter  a word:")
# i=0
# while(i<=len(word)-1): # i < len(word)
#     print(word[i] ,i)
#     i=i+1



# n=int(input("Enter a number :"))
# i=1
# while(i<=10):
#     print( f"{n} X {i} = {n*i}")
#     i=i+1


# n=int(input("Enter a number"))
# if not(n%2==0):
#     pass
# else:
#     print("odd number")



#Program Even program
#WhileLoopEx5.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# i=2
# while(i<=n):
#     print(i)
#     i=i+2
# else:
#     print("-------while else block---------------")




#Program odd program
#WhileLoopEx5.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+2
# else:
#     print("-------while else block---------------")

#Program Even program
# #WhileLoopEx6.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# i=1
# while(i>=n):
#     print(i)
#     i=i+2
# else:
#     print("-------while else block------------")


# num=int(input("Enter a number :"))
# i=0 #Even number start from 2 so we give i=2
# while(i<=num):
#     if i%2==0:
#         print(i)
#     i=i+1
# else:
#     print("-----------while else--------------")   

num = int(input("Enter a number :"))
i=num
while(i>=0):
    if i%2==0:
        print(i)
    i-=1




