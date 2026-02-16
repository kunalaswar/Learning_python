# print(11<10)
# print(11>10)
# print (11<10)
# print (not 11<10)

# n=int(input("Enter a number :"))
# s=0
# i=0
# while(i<=n):
#     print(i)
#     s=s+i
#     i=i+1
# print("sum ===>",s)    
# # print(s)    


# n= int(input("Entera  number :"))
# s=0
# i=0
# while(i<=n):
#     print(i)
#     s=s+i
#     i=i+1
# else:
#     print("sum ===>",s)    



# n=int(input("Enter a number :"))
# s=0
# i=0
# while(i<=6):
#     print(i)
#     s=s+i
#     i=i-1

# n=int(input("Enter a value"))
# for i in range(1,10+1):
#     print( f"{n} X  {i} = {n*i}" )


# n=(input("enter a  word :"))
# for i in n:
#     # print(i,end="")
#     print(i)
# n=(input("enter a  word :"))
# for i in str(n):
#     print(i)


# n=(input("enter a  word :"))
# for i in list([n]): #for i in [n]
#     print("list",i)


# # n=(input("enter a  word :"))
# for i in [1,2,3]:
#     print(i)

# # n=(input("enter a  word :"))
# for i in {1,2,3,4,5,6} :
#     print(i)



#Program for Generating N to 1 where N is +VE
#ForLoopEx2.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("----------------------------------------")
#     print("Numbers from {} to 1".format(n))
#     print("----------------------------------------")
#     for i in range(n,0,-1):
#         print("\t\t{}".format(i))
#     else:
#         print("----------------------------------------")



#Program for Generating 1 to N Numbers where N is +VE
#ForLoopEx1.py
# n=int(input("Enter How Many Numbers u want to Generate:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     print("Numbers within :{}".format(n))
#     for i in range(1,n+1):
#         print("\t{}".format(i))
  

# for val in {10:"kunal",20:"sagar"}:
#         print(val )


# i=1
# while(i<=10):
#     print(i)
#     i=i+1
# else:
#     print("else block")



#even number
# n=int(input("Enter a  number :"))
# i=2
# while(i<=n):
#     print(i)
#     i=i+2

# n= int(input("Enter a  number :"))
# i=n
# while(i>=0):
#     if(i%2!=0):
#         print(i)
#     i=i-1

# n=int(input("Entera value : "))
# for i in range(n,0,-2):
#     if(i%2==0):
#         print(i)


# n=int(input("Entera  number :"))
# for i in range(0,n+1,1):
#     print(i)

# for val in range(-10,0,1):
#     print(val)

# for i in range(11,1,-1)[::-1]:
#     print(i)

# for i in range(100,9,-10):
#     print(i)
# print("---------------")    
# for i in range(10,101,10):
#     print(i)



# n= int(input("enter  a number :"))
# if(n<=0):
#     print("invalid value ")
# else:
#     i=1
#     while(i<=n):
#         print(i)
#         i=i+1    

# n= int(input("enter  a number :"))
# for i  in range(1,n+1,1):
#     print(i)

# n=int(input("Enter a number :"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1

# n= int(input("Entera  number :"))
# i=n
# while(i>=0):
#     print(i)
#     i=i-2

# n= int(input("Entera  number :"))
# for i in range(1,n,1):
#     print(i)

# n= int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(i)

# word=input("Enter a word:")
# for  i in word:
#     print(i)

# word=input("Enter a word:")
# for i in range(len(word)):
#     print(word[i])

# a="python"
# print(len(a))
# print(a[0])
# print(a[5])
# print()
# for i in range(1,6):
    # print(i)


# word=input("Enter a word:")
# for i in str(word)[::-1]:
#     print(i)


# # program for finding sum of N natural number     
# USING FOR LOOP
# n=int(input("Enter a number :"))
# s=0
# for i in range(1,n+1,1):
#     print(i)
#     s=s+i
# print("sum = ",s)     


# # program for finding sum of N natural number
# USING  WHILE LOOP
# n=int(input("Enter a number :"))
# s=0
# ss=0
# i=1
# while(i<=n):
#     # print(f"{i}   {i*i}")
#     print("{}  {}".format(i,i*i))
#     i=i+1
#     s=s+i
#     ss=ss+i*i
# print("sum = ", s )
# print("squaresum = ", ss )

 # program for finding sum  and Square of N natural number     
# USING FOR LOOP
# n=int(input("Enter a number :"))
# s=0
# squaresum=0
# for i in range(1,n+1,1):
#     print(i,i*i)
#     s=s+i
#     squaresum=squaresum+i*i
# print("sum = ",s)  
# print("squaresum = ",squaresum)   


# product for finding product of n natural  number
n= int(input("Entera  number "))
s=1
p=1
cubeproduct=1
for i in range(1,n+1):
    print(f"{i}, {n*i}, {n*i*i}")
    s=s+i
    p=p*i
    cubeproduct=cubeproduct*i
print("sum=",s)
print("product=",p)
print("cubeproduct=",cubeproduct)




# # program for finding sum of N natural number
# n=int(input("Enter a number :"))
# s=0
# squares=0
# for i in range(1,n+1,1):
#     print(i)
#     s=s+i
#     squares=squares+i*i
# print("sum = ",s)  
# print("suareroot = ",squares)   


# x=10
# y=10
# print(id(x))
# print(id(y))