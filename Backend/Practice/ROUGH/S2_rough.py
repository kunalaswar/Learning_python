# n = int(input("Enter a number : "))
# i = 0
# while i<=n:
#    print(i)
#    i = i+1


# n = int(input("Enter a number : "))
# i = n
# while i >=0:
#    print(i)
#    i = i-1

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


# n = input("Enter a lIne of text :")
# x = n.split()
# for i in x:
#    print(i)
#    for j in i:
#       print(j)




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



# def decideprime(val):
#      if val <=1:
#           res = False
#      else : 
#           res = True
#           for i in range(2,val):
#                if val%i==0:
#                     res = False
#                     break
#      return res
# lst = [int(i) for i in input("Enter values seprated by space : ").split()]
# dict = {val:"Prime" if decideprime(val) else "Not Prime" for val in lst}
# for k,v in dict.items():
#      print(f"{k}-->{v}")

# addop = lambda a,b :a+b
# res =addop(10,20)
# print(res)
# print(type(addop))


# print("""

#         1.Addition
#         2.Substraction
#         3.multiplication
#         4.division
#         5.floordivion
#         6.ModuloDivision
#         7.Exponention

#         8.Exit
# """)
# sumop = lambda a,b : a+b
# subop= lambda a,b : a-b
# mulop = lambda a,b:a*b
# division = lambda a,b:a/b
# floordv = lambda a,b:a//b
# modulodv = lambda a,b:a%b
# expon = lambda a,b : a**b

# while True:
#  ch = int(input("Enter your choice : "))
#  match(ch):
#       case 1 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = sumop(a,b)
#            print(f"sum : {res}")
#       case 2 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = subop(a,b)
#            print(f"sub : {res}")
#       case 3 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = mulop(a,b)
#            print(f"multiplication : {res}")
#       case 4 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = division(a,b)
#            print(f"division : {res}")
#       case 5 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = floordv(a,b)
#            print(f"floordiv : {res}")
#       case 6 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = modulodv(a,b)
#            print(f"modulo division : {res}")
#       case 7 :
#            a = int(input("Enter Fist value : "))
#            b = int(input("Enter Second value : "))
#            res = expon(a,b)
#            print(f"Exponention : {res}")
#       case 8 :
#               print("Thanks for using this progrm ")
#               break
#       case _ :
#              print("Invalid input please enter valid input ")



# biggest = lambda a,b,c : a if b<=a>c else b if a<b>=c else c if a<=c>b else "All values are same"
# a = int(input("Enter first value : "))
# b = int(input("Enter second value : "))
# c = int(input("Enter third value : "))
# res = biggest(a,b,c)
# print(res)

# biggest=lambda a,b,c :a if b<=a>c else b if a<b>=c else c if b<c>=a else "All value are equal"
# a=int(input("Enter :"))
# b=int(input("Enter :"))
# c=int(input("Enter :"))
# res=biggest(a,b,c)
# print(res)



# bigv =lambda a,b : a if a>b else b if b>a else " Both Values are same "
# smlv = lambda a,b : a if a<b else b if b<a else "Both values are same "

# a =int(input("Enter first value : "))
# b = int(input("Enter Second Value : "))
# res_bigv = bigv(a,b)
# res_smlv = smlv(a,b)
# print(f"biggest value : {res_bigv}")
# print(f"smallest value  : {res_smlv}")


# def sgrmax(lst):
#      mv = lst[0]
#      for i in lst:
#           if i>mv:
#                mv = i
#      return mv
# def sgrmin(lst):
#      mnv = lst[0]
#      for j in lst:
#           if j<mnv:
#                mnv = j
#      return mnv

# findmax = lambda lst : sgrmax(lst)
# findmin = lambda lst: sgrmin(lst)

# lst = [int(i) for i in input("Enter values seprated by commas : ").split()]
# res_findmax = findmax(lst)
# res_findmin = findmin(lst)
# print(f"Maximum value is : {res_findmax}")
# print(f"SMallest value is : {res_findmin}")


# def findpos(val):
#           if val>0:
#             return False
#           if val<0:
#                return True



# lst= [int(i) for i in input("Enter space seprated values : ").split()]
# pos  = filter(findpos,lst)
# # print(type(pos))
# obj = list(pos)
# print(obj,type(obj))


# def findpos(val):
#           if val>0:
#             return False
#           if val<0:
#                return True


# n = int(input("Enter how many do you want : "))
# lst = []
# for i in range(1,n+1):
#       val = int(input(f"Enter {i} value : "))
#       lst.append(val)

# pos  = filter(findpos,lst)
# # print(type(pos))
# obj = list(pos)
# print(obj,type(obj))

# findpos = lambda val :  val>0

# lst= [int(i) for i in input("Enter Space Seprated values : ").split()]
# pos = tuple(filter(findpos,lst))
# print(pos,type(pos))


# lst = [int(i) for i in input("Enter Space Seprated values : ").split()]
# pos = tuple(filter(lambda val : val<0,lst))
# print(pos,type(pos))


# lst = [i for i in input("Enter a word : ")]
# vowels = list(filter(lambda word:  "a" in word or "e" in word or "i" in word or "o" in word or "u" in word ,lst))
# print(vowels)


# lst = [int(i) for i in input("Enter space seprated values : ").split()]
# pos = list(filter(lambda val : val>0,lst))
# nl = list(filter(lambda val: val<0 ,lst))
# print(pos)
# print(nl)

# lst = [i for i in input("Enter a word : ").split()]
# plst = list(filter(lambda word : word== word[::-1],lst))
# print(plst)




# lst = [i for i in input("Enter a line of text : ").split()]
# nl = list(filter(lambda word:4>=len(word)>=3,lst ))
# print(nl)

# lst = [i for i in input("Enter a line of text : ").split()]
# nl = list(filter(lambda word:word[0]==word[-1] and word!=word[::-1],lst ))
# print(nl)

# def evenval(val):
#      if val %2==0:
#           return True
#      else:
#           return False

# lst = [int(i) for i in input("Enter values  : ").split()]
# el  =  list(filter(evenval,lst ))
# ol = list(filter(lambda val : val%2!=0,lst ))
# print(f"Even list : {el}")
# print(f"odd list : {ol} ")

# def hike(sal):
#      return sal +sal*50/100


# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(hike , lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)



# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(lambda sal :sal+sal*50/100, lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)


# lst = [int(i) for i in input("Enter salary fo employee : ").split()]
# newsal = list(map(lambda sal :sal<0, lst))
# # print(newsal,type(newsal))
# print("OLD SALARY \t NEW SAL")
# for os ,ns in zip(lst,newsal):
#      print(os,"\t\t",ns)

# def sumop(val1,val2):
#   return val1+val2

# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for second list : ").split() ]
# sv = list(map(sumop, l1,l2))
# print("VAL1 VAL2 \t  SUM")
# for v1,v2 ,s in zip(l1,l2,sv):
#   print(v1,"\t",v2,"\t",s)


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for second list : ").split() ]
# sv = list(map(lambda v1,v2 :v1+v2, l1,l2))
# print("VAL1 VAL2 \t SUM")
# for v1,v2 ,s in zip(l1,l2,sv):
#   print(v1,"\t",v2,"\t",s)



# l1= [int(i) for i in input("Enter values for first list : ").split()]
# sv = list(map(lambda v1:v1**0.5, l1))
# print("VALUE \t SQRT")
# for v1 ,s in zip(l1,sv):
#   print(v1,"\t",s)



# l1= [int(i) for i in input("Enter values for first list : ").split()]
# sv = list(map(lambda v1:v1**2, l1))
# print("VALUE \t SQUARE")
# for v1 ,s in zip(l1,sv):
#   print(v1,"\t",s)

# empdt = {"karan":1000,"jay":2000,"sahil":3000,"paa":4000}

# upsal = list(map(lambda x :empdt[x]+empdt[x]*50/100 ,empdt)) 

# print("OlD SALRY NEW SALRY")
# for os,ns in zip(empdt,upsal):
#      print(os,ns)


# n = int(input("Enter values : "))
# dict = {input(f"Enter {i} value : "): input(f"Enter {i} value : ") for i in range(1,n+1)}
# print(dict)



# n =  int(input("Enter how many do you want to enter : "))
# dict= {}
# for i in range(1,n+1):
#      key = float(input("Enter key value : "))
#      value = float(input("Enter value of key : "))
#      dict[key] = value

# import sys
# dict = {}
# while True:
#         eno = float(input("Enter Employee number : "))
#         salary = float(input("Enter Employee Salary : "))
#         dict[eno] = salary
#         ch = input("do you want to enter anothe emp data - (yes/ no): ").lower()
#         if ch == "no":
#           break
#         if ch not in ["yes","no"]:
#           sys.exit()

# print("ENO \t OLD SALARY")
# for eno,nwsal in dict.items():
#   print(eno,"\t",nwsal)

        

# modsal = list(map(lambda x :x+x*50/100  ,dict.values()))   
# #[1500.0, 3000.0, 4500.0]
# for k,v in zip(dict,modsal):
#   dict[k]=v
# print(dict)

# print("ENO \t NEW SALARY")
# for eno,nwsal in dict.items():
#   print(eno,"\t",nwsal)
