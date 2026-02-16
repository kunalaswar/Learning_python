# n = int(input("Enter a number : "))
# i = 0
# while i<=n:
#    print(i)
#    i = i+1
# n=int(input("Enter a number :"))
# i=0
# while(i<=n):
#     print(i)
#     i=i+1



# n = int(input("Enter a number : "))
# i = n
# while i >=0:
#    print(i)
#    i = i-1
# n=int(input("Enter a number :"))
# i=n
# while(i>=0):
#     print(i)
#     i=i-1


# n = int(input("Enter a number upto you want : "))
# i = 1
# while i<=n:
#      if i %2==0:
#           print(i)
#      i= i+1

# n = int(input("Enter a number upto you want : "))
# i = 1
# while i<=n:
#      if i %2!=0:
#           print(i)
#      i= i+1

# n = int(input("Enter a number from where you want : "))
# i = n
# while i>=0:
#      if i%2==0:
#           print(i)
#      i = i-1

# n = int(input("Enter a number from where you want : "))
# i = n
# while i>=0:
#      if i%2!=0:
#           print(i)
#      i = i-1

# n = int(input("Enter a number from where you want : "))
# i = 0
# s = 0
# while i<=n:
#      print(i)
#      s = s+i
#      i = i+1
# print("sum =",s)

# n = int(input("Enter a number from where you want : "))
# i = 1
# s = 1
# while i<=n:
#      print(i)
#      s = s*i
#      i = i+1
# print("multiplication =",s)


# n = int(input("Enter a number upto where you want to genrate : "))
# for i in range(2,n+1):
#      for j in range(1,11):
#           print(f" {i} X {j} = {i*j}")
#      print()


# n = int(input("Enter a number upto where you want to genrate :"))
# if n < 2:
#      print(f"{n} is not a prime number ")
# for i in range(2,n+1):
#      res = True
#      for j in range(2,i//2+1):
#           if i%j == 0:
#                res = False
#                break
#      if res:
#          print(f"{i} is Prime Number  ")
#      else:
#           print(f"{i} is not a prime Number ")


# n = int(input("Enter a number : "))
# res = True
# for i in range(2,n):
#      if n%i == 0:
#           res = False
#           break
# if res:
#          print(f"{i} is Prime Number  ")
# else:
#           print(f"{i} is not a prime Number ")

# n = int(input("Enter a number upto you want to genrate prime numbers : "))
# if n < 2:
#     print(f"{n} is not a Prime Number ")
# else:
#     i = 2
#     while i <= n:
#         j = 2
#         res = True
#         while j <= i // 2:
#             if i % j == 0:
#                 res = False
#                 break
#             j = j + 1

#         if res:
#             print(f"{i} is Prime Number ")
#         else:
#             print(f"{i} is not Prime Number ")
#         i = i + 1


# n = int(input("Enter number upto where you want to genrate : "))
# if n <2:
#      print(f"{n} is Prime Number : ")
# else:
#      i = 2
#      while i<=n:
#           j = 2
#           res = True
#           while j<=i//2:
#            if i%j== 0:
#                res = False
#                break
#            j = j+1
#           if res :
#              print(f"{i} is Prime Number ")
#           else:
#              print(f"{i} is Not Prime Number ")
#           i = i+1




# n=int(input("Enter number where you wnat to generated a :"))
# if  n < 2:
#     print(f"{n} is prime number ")
# else:
#     i=2
#     while(i<=n):
#         # print(i)
#         j=2
#         res=True
#         while(j<i):
#             if i%j==0:
#                 res=False
#                 break
#             j=j+1
#     if(res)            :
#         print(res)
#     else:
#         print(res)

#         i=i+1


# n = input("Enter a lIne of text :")
# x = n.split()
# for i in x:
#    print(i)
#    for j in i:
#       print(j)

# n=input("Enter a line of the text")
# x=n.split()
# print(x)
# for val in x:
#     # print(val)
#     for j in val:
#         print(j)

# while True:
#  n = input("Enter a number : ")
#  if int(n) in range(100,201) and n.isdigit():
#        break
#  else:
#   print("Please enter valid input")
# print(n)

# while True:
#  n = input("Enter a student name : ")
#  x = n.split()
#  res = True
#  for i in x:
#       if not i.isalpha():
#        res = False
#  if res :
#       break
#  else:
#      print("Please enter valid input")
# print(n)


# dict = {}
# for val in list:
#      dict[val]=len(val)
# print(dict)


# def readvalues():
#      n = int(input("Enter how many numbers do you want to enter : "))
#      if n<=0:
#           return ("It is invalid input ")
#      else:
#           lst = []
#           for i in  range(1,n+1):
#             val = input(f"Enter {i} value : ")
#             lst.append(val)
#      return lst
# def wordlen(lst):
#  dict = {}
#  for val in lst:
#      dict[val]=len(val)
#      return dict

# def highestlen(dict):
#  mv = max(dict.values())
#  for k,v in dict.items():
#      if v == mv:
#           print(k,"->",v)


# lst= readvalues()
# if type(lst)==str:
#      print(lst)
# else:
#  wl = wordlen(lst)
#  highestlen(wl)


# def readvalues():
#     n = int(input("Enter how many numbers do you want to enter : "))
#     if n <= 0:
#         print("It is invalid input ")
#     else:
#         lst = []
#         for i in range(1, n + 1):
#             val = input(f"Enter {i} value : ")
#             lst.append(val)
#         print("you have entere : ", lst)


# def wordlen(readvalues):
#     dict = {}
#     for val in readvalues():
#         dict[val] = len(val)
#         return dict


# def highestlen(wordlen):
#     mv = max(wordlen.values())
#     for k, v in wordlen.items():
#         if v == mv:
#             print(k, "->", v)
# readvalues()
# wordlen()
# highestlen()



# n = input("Enter a line of text ")
# x = n.split()
# lst = []
# for i in x:
#      lst.append(i[::-1])
# print(" ".join(lst))


# n=input("Enter a number : ")
# x=n.split()
# print(x)
# lst=[]
# for i in x:
#     lst.append(i[::-1])
# print(lst)  
# print(" ".join(lst))  





