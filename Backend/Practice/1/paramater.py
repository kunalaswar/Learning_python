#
#^
# def fun1(a,b):
#     print(a,b)

# fun1(10,20)    
# fun1(a=10,b=20)

#^
# def positional(a,b,/):
#     print(a,b)

# positional(10,20)
## positional(a=10,b=20)
#^
# def keyword(*,a,b):
#     print(a,b)

# keyword(b=20,a=10) 
## keyword(20,10) 

#^
# def default(a,b=20):
#     print(a,b)

# default(10,30)
# default(10)
# default(a=10)
# default(1)

#^
# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input('Enter a number :'))        
# b=int(input("Enter a number :"))
# res=maximum(a,b)    
# print("maximun number is ",res)

#^

# def isprime(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         return "prime"
#     else:
#         return "Not prime"


# num=int(input("Enter a number: "))
# res=isprime(num)
# print(res)
#^

# def ispal(val):
#     if val==val[::-1]:
#         return True
#     else:
#         return False   

# num=input("Enter a number :")    
# res=ispal(num)    
# print(res)


# num=int(input("Enter a number :"))#123
# rev=0
# while(num>0):
#     res=num%10
#     rev=(rev*10)+res
#     num=num//10

# print(rev)


# s="madam"
# k=""
# for i in range(len(s)-1,-1,-1):
#     k=k+s[i]
# # print(k)  
# if s==k:
#     print("palin")  
# else:
#     print("not")    


# a=[7,5,6,1,4,2,3]
# for i in range(0,len(a)):
#     # print(i)
#     for j in range(len(a)-1):
#         a[j],a[j+1]=a[j+1],a[j]
#     print(a[j])


#     print("----")
    




































