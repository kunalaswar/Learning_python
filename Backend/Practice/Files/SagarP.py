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


# l1= [int(i) for i in input("Enter values for first list : ").split()]
# l2 = [int(j) for j in input("Enter values for Second list : ").split()]

# if len(l1)<len(l2):
#      for i in range(len(l2)-len(l1)):
#           l1.append(0)
# if len(l1)>len(l2):
#      for i in range(len(l1)-len(l2)):
#           l2.append(0)

# else:
#   sumlist = list(map(lambda a,b : a+b,l1,l2))

#   print(sumlist)


# def getval():
#      return 10

# def square(getval):
#      def calculation():
#       n = getval()
#       return n,n**2
#      return calculation
# res = square(getval)
# n,square = res()
# print(n,square)


# def box(function):
#  def new_display():
#   print("*")
#   function()
#   print("")
#  return new_display

# @box
# def display():
#  print("Hello python")

# display()


# def getval():
#      return int(input("Enter value : "))

# def square(getval):
#    def sqrcalc():
#       n=  getval()
#       sqres = n**2
#       return n, sqres
#    return sqrcalc

# def cube(getval):
#     def cbcal():
#       c = getval()
#       cubres  = c**3
#       return c,cubres
#     return cbcal

# n,sqres= square(getval)()
# print(n,sqres)
# c,sqres= cube(getval)()
# print(c,sqres)


# def getval():
#      return int(input("Enter first value : ")),int(input("Enter second value : "))

# def addop(getval):
#      def addcal():
#           n1, n2 = getval()
#           res =n1+n2
#           return n1,n2,res
#      return addcal

# n1,n2,res  = addop(getval)()
# print(f"sum of ({n1},{n2})={res}")

# def getval():
#      return int(input("Enter first value :  ")),int(input())

# def getval():
#      return int(input("Enter First value : ")),int(input("Enter second value : "))

# def multable(getval):
#   def multablecal():
#       n1,n2= getval()
#       res = n1*n2
#       return n1,n2, res
#   return multablecal


# n1,n2, res= multable(getval)()
# print(f"Multiplication of : ({n1},{n2}) = {n1*n2}")


# def square(getval):
#      def sqop():
#           n = getval()
#           res = n**2
#           return n ,res
#      return sqop

# @square
# def getval():

#      return int(input("Enter a number :"))

# n,res = getval()
# print(n,res)


# try:
#      a = int(input("Enter first value : "))
#      b = int(input("Enter Second value :"))
#      c = a/b
#      print(c)
#      s = "python"
#      print(s[0])
#      print("My name is anthony gunjaliwsh ")
# except ValueError:
#      print("Dont Enter alnums ,alphabets,symbols...")
# except ZeroDivisionError:
#      print("Dont Enter Zero As Denominator")
# except IndexError:
#      print("Index is out of range()")
# except:  # noqa: E722
#      print("Ooops something went wrong - check for exception ")


# class NumberDivisonError(Exception):pass
# class NotNumberError(BaseException):pass
# try:
#  a= input("Enter first Value : ")
#  b= input("Enter Second Value : ")
#  if not a.isdigit() or not b.isdigit():
#       raise NotNumberError
#  x = int(a)
#  y = int(b)
#  if y==0:
#       raise NumberDivisonError
#  else:

#   print(x/y)
# except NumberDivisonError:
#    print("Dont Enter Zero as Denominator")
# except NotNumberError:
#    print("Dont enter alnums,alphabets , symbols")


# class InvalidNameError(Exception):pass
# class ZeroLenghtError(Exception):pass
# class SpaceError(Exception):pass
# n = input("Enter Name : ")
# try:
#   if len(n)==0:
#        raise ZeroLenghtError
#   elif n.isspace():
#        raise SpaceError
#   else:
#    lst = n.split()
#    for word in lst:
#         if not word.isalpha():
#             raise InvalidNameError
#    print(n)
# except InvalidNameError:
#     print("Please Enter Valid Name  ")
# except ZeroLenghtError:
#     print("Please Enter Name - Dont Leave Empty")
# except SpaceError:
#     print("Dont Enter SPaces ")


# class NegNumberError(Exception):pass


# def mulop():
#      try:
#       a = int(input("Enter first Number  : "))
#       b = int(input("Enter Second Number :"))

#       if a<0 or b<0:
#            raise NegNumberError
#       else:
#            c= a*b
#            print(f"Multiplication : {c}")
#      except NegNumberError:
#           print("Dont Enter Negative Number ")
#      except ValueError:
#           print("Dont Enter alums,alphabets , symbols")
# mulop()


# class NonPrimeError(Exception):pass
# n = int(input("Enter A Number : "))
# try:
#  if n<=1:
#       raise NonPrimeError
#  else:
#       res = True
#       for i in range(2,n):
#            if n%2==0:
#                res = False
#                break
#  if res :
#   print(f"{n} is Prime Number ")
#  else:
#   print(f"{n} is Not a Prime Number")

# except NonPrimeError:
#      print(f"Dont Enter 1 and Negative Number ")
# except ValueError:
#      print("Dont Enter alnums,alphabets , symbols")


# class NonPrimeError(Exception):pass
# try:
#  n = int(input("Enter A Number : "))
#  if n<=1:
#       raise NonPrimeError
#  else:
#       res = True
#       for i in range(2,n):
#            if n%2==0:
#                res = False
#                break
#  if res :
#   print(f"{n} is Prime Number ")
#  else:
#   print(f"{n} is Not a Prime Number")

# except (NonPrimeError,ValueError):
#      print(f"Dont Enter 1 and Negative Number ")
#      print("Dont Enter alnums,alphabets , symbols")


# class ZeroError(Exception):pass
# class NegNumError(BaseException):pass

# try:
#  n = int(input("Enter a number :"))

#  if n==0:
#       raise ZeroError
#  elif n<0:
#       raise NegNumError
#  else:
#     for i in range(1,11):
#        print(f"{n} X {i} = {n*i}")

# except ZeroError:
#  print("Dont Enter Zero ")
# except NegNumError:
#    print("Dont Enter Negative Number")
# except ValueError:
#    print("Dont Enter ALnums , Alphabets , Symbols")
# except :
#    print("Oooppps Something went Wrong- check for Exception")


# class ZeroError(Exception):pass
# class NegNumError(BaseException):pass
# try:
#  n = int(input("Enter a number :"))
#  if n==0:
#       raise ZeroError
#  elif n<0:
#       raise NegNumError
#  else:
#     for i in range(1,11):
#        print(f"{n} X {i} = {n*i}")
# except (ZeroError,NegNumError,ValueError):
#  print("Dont Enter Zeros As input ")
#  print("Dont Enter Negative Number ")
#  print("Dont enter alnums, alphabets, symbols ")


# def kvrrange(x):
#      s = 0
#      while s<x:
#          yield s
#          s =  s+1

# # n = int(input("Enter A Value : "))
# res = kvrrange(6)
# while True:
#      try:
#       print(next(res))
#      except StopIteration:
#            break


# def kvrrange(n):
#      s = 0
#      while s<n:
#           yield s
#           s= s+1
# r = kvrrange(6)
# print("------")
# print(next(r))
# print("--------")
# for i in r:
#      print(i)


# def getcrs():
#      yield "python","kvr"
#      yield "java"
#      yield 1234 ,"Numbers"
#      yield "data Science"
# r = getcrs()
# for val in r:
#      print(val)


# def kvrange(start,stop=0,step=1):
#      if start>stop:
#         stop= start
#         start = 0
#      else:
#       while start<=stop:
#        yield start
#        start = start+step

# print("---------first--------------------")
# r = kvrange(1,10,3)
# for val in r:
#   print(val)

# print("-------------second----------------")
# r= kvrange(1,9)
# for val in r:
#    print(val)
# print("--------------third---------------")

# r = range(9)
# for val in r:
#    print(val)


# class student:
#     pass


# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))


# print(f"Student Number : {s1.sno}")
# print(f"Student Name  : {s1.sname}")
# print(f"Student Marks : {s1.marks} ")


# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))


# print(f"Student Number : {s2.sno}")
# print(f"Student Name  : {s2.sname}")
# print(f"Student Marks : {s2.marks} ")


# class student:pass

# s1 = student()
# s2 = student()


# print("---------------------")
# print(f"Content of s1 :{s1._dict_}")
# print(f"Lenght :{len(s1._dict_)}")
# print(f"Content of s1 :{s2._dict_}")
# print(f"Lenght :{len(s2._dict_)}")
# print("---------------------")

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))


# print(f"Content of s1 :{s1._dict_}")
# print(f"Lenght :{len(s1._dict_)}")

# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# print(f"Content of s1 :{s2._dict_}")
# print(f"Lenght :{len(s2._dict_)}")


# print("-----------------")
# for k,v in s1._dict_.items():
#      print(f"{k}-->{v}")

# print("-----------------")


# for k in s1._dict_:
#      print(k,"--->",s1._dict_[k])


# for k in s1._dict_.keys():
#      print(k,"--->",s1._dict_[k])

# print("-----------------")


# class student:
#     pass
# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter Student Number : "))
# s1.sname = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))

# for dmn, dmv in s1._dict_.items():
#     print(f"{dmn}--> {dmv}")

# s2.sno = int(input("Enter Student Number : "))
# s2.sname = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# for dmn in s2._dict_.keys():
#     print(f"{dmn}--> {s2._dict_[dmn]}")


# class student :
#      crs = input("Enter Course Name : ")
#      city = input("Enter City : ")

# s1 = student()
# s2= student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)

# class student :pass

# student.crs = input("Enter Course Name  : ")
# student.city = input("Enter City Name : ")

# s1 = student()
# s2 = student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)


# class student : 
#      def readstudentdata(self,objinfo):
#           print("-"*50)
#           print(f"Enter {objinfo} student Data")
#           print("-"*50)
#           self.sno = int(input("Enter Student Number : "))
#           self.sname= input("Enter Student Name : ")
#           self.marks = float(input("Enter Stuent Marks : "))
#      # def displaystudentdata(self,objinfo):
#      #      print("-"*50)
#      #      print(f"Display {objinfo} student Data")
#      #      print("-"*50)
#      #      print(self.sno)
#      #      print(self.sname)
#      #      print(self.marks)




# s1 = student()
# s1.readstudentdata("first")
# # s1.displaystudentdata("first")
# for k, v in s1._dict_.items():
#      print(k,"-->",v)
# s2 = student()
# s2.readstudentdata("second")
# # s2.displaystudentdata("second")
# for k, v in s2._dict_.items():
#      print(k,"-->",v)

# try:
#  fp = open("open.txt","r")
#  print("File opened successfully ")

# except FileNotFoundError:
#  print("File does not exist ")
# else:
#   print(f"File Mode is : {fp.mode}")
#   print(f"Type of fp : {type(fp)}")
#   print(f"Does the file is readable : {fp.readable()}")  # funtion
#   print(f"Does the file is Writale : {fp.writable()}")
#   print(f"Does the file is closed : {fp.closed}")
#   print(f"File Mode is : {fp.mode}")
# finally:
#  try :
#   print("I am from finaly block ")
#   fp.close()
#   print("after manual closing")
#   print(f"Does the file is closed : {fp.closed}")
#  except NameError:
#   print("Unable to open there is no need to close")


# with open("open.txt","+a") as fp:
#      print(f"file opened successfully in {fp.mode}")
#      print(f"Does the file is readable : {fp.readable()}")
#      print(f"Does the file is Writeble : {fp.writable()}")
#      print("before the indentation ")
#      print(f"Does The file is cloesd : {fp.closed}")
# print("After the indentation ")
# print(f"Does The file is cloesd : {fp.closed}")




# class student : 
#   def readstudentdata(self,objinfo):
#     print("-"*30)
#     print(f"Enter {objinfo} Student Data")
#     print("-"*30)
#     self.sno = int(input("Enter Student Number : "))
#     self.sname = input("Enter Student Name : ")
#     self.marks = float(input("Enter Student Marks : "))
#   def displaydata(self,objinfo):
#       print("-"*30)
#       print(f"Display {objinfo} Student Data")
#       print("-"*30)
#       for k,v in self._dict_.items():
#          print(k,"-->",v)
         

# s1 = student()
# s1.readstudentdata("First")
# s1.displaydata("First")
# s2 = student()
# s2.readstudentdata("Second")
# s2.displaydata("Second")


# class student : 
#      def readstudentdat(self):
#           print(id(self))


# s1 = student()
# print(id(s1))
# s1.readstudentdat()
# s2 = student()
# print(id(s2))
# print(id(s2))



# with open("open.txt","a") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter Student Name : ")
#      marks = float(input("Enter Student Marks : "))
#      fp.write(f"{sno} \t {sname}  \t {marks} \n")
#      print("Data Written Into File Successfully - verify")


# with open("open.txt","r") as fp:
#      filedata = fp.read()
#      print(filedata)

# with open("x+5.txt","x+") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter Student Name : ")
#      marks = float(input("Enter Student Marks : "))
#      fp.write(f"{sno} \t {sname}  \t {marks} \n")
#      fp.seek(0)
#      filedata = fp.readlines()
#      for val in filedata:
#           print(val)
#           print('------fpreadlines---')
#      fp.seek(0)
#      filedata = fp.read()
#      print(filedata)
#      print('------fpreadlines---')




# print("Enter Data - Press @ to stop : ") 
# with open("rr.txt" ,"a") as fp:
#  while True:
#     filedata = input()
#     if  filedata!= "@":
#       fp.write(filedata + "\n")
#     else:
#       print("filedata Written Successfully - verify")
#       break
        
     
   
# class student : pass


# s1 = student()
# s2 = student()

# s1.sno =  int(input("Enter Student Number : "))
# s1.name = input("Enter Student Name : ")
# s1.marks = float(input("Enter Student Marks : "))

# for k,v in s1._dict_.items():
#   print(k,v)
# print(s1.sno)
# print(s1.name)
# print(s1.marks)


# s2.sno =  int(input("Enter Student Number : "))
# s2.name = input("Enter Student Name : ")
# s2.marks = float(input("Enter Student Marks : "))

# for k,v in s2._dict_.items():
#   print(k,v)
# print(s2.sno)
# print(s2.name)
# print(s2.marks)






  
# class student : 
#   def readvalues(self,objinfo):
#    print(f"Enter {objinfo} Student Data")
#    self.sno =  int(input("Enter Student Number : "))
#    self.name = input("Enter Student Name : ")
#    self.marks = float(input("Enter Student Marks : "))
  
#   def displayvalues(self,objinfo):
#     print(f"Display {objinfo} Student Data")
#     print(self.sno)
#     print(self.name)
#     print(self.marks)


# s1 = student()
# s2 = student()

# s1.readvalues("First")
# s1.displayvalues("First")


# s2.readvalues("Second")
# s2.displayvalues('Second')

# class student:
#    def readvalues(self,objinfo):
#     print(f"Enter {objinfo} Student Data")
#     self.sno =  int(input("Enter Student Number : "))
#     self.name = input("Enter Student Name : ")
#     self.marks = float(input("Enter Student Marks : "))

#    def displayvalues(self,objinfo):
#      print(f"Display {objinfo} Student Data")
#      for k,v in self._dict_.items():
#       print(k,v)



# s1 = student()
# s2 = student()

# s1.readvalues("First")
# s1.displayvalues("First")


# s2.readvalues("Second")
# s2.displayvalues('Second')



# class student :
#   crs = "python"
#   city = "Hyd"


# s1 = student()

# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)



# class student : pass


# student.crs = "python"
# student.city = "hydrabad"

# s1= student()
# s2 = student()
# print("------s1-----")
# print(s1.crs)
# print(s1.city)

# print(student.crs)
# print(student.city)
# print("------s1-----")
# print("------s2-----")
# print(s2.crs)
# print(s2.city)

# print(student.crs)
# print(student.city)
# print("------s2-----")

#todo FILE CONCEPT

# try:
#  with open("sagar.txt","x+") as fp:
#      print(f"File opened in mode : {fp.mode}")
#      print(f"Does the file is readable : {fp.readable()}")
#      print(f"Does the file is Writable : {fp.writable()}")
# except FileExistsError:
#    print("File already exist ")


# with open("open.txt","w") as fp:
#      # fp.write("sagar \t")
#      # fp.write(str(100)+"\t")
#      # fp.write(str(200000)+"\n")
#      fp.write(f" Sagar \t {10000} \t {False} \n")
#      fp.write(f" Sagar \t {10000} \t {False} \n")
#      print("data Written successfully - verify ")

# x = (10,20,30,40)
# with open("open.txt","a") as fp:
#      fp.writelines(f"{x} \n")
#      print("Data written successfully - verify")

# with open("open.txt","a") as fp:
#      sno = int(input("Enter Student Number : "))
#      sname = input("Enter student Name : ")
#      smarks = float(input("Enter Student Marks : "))

#      # fp.write(str(sno)+"\t")
#      # fp.write(sname+"\t")
#      # fp.write(str(smarks)+"\n")

#      fp.write(f"{sno} \t {sname} \t {smarks} \n")
#      print('data written successfully - verify')


# lst = [10,20,30]
# with open("open.txt","a") as fp:
#      fp.writelines(f"{lst} \n")
#      print("Data Written to file successfully -  verify ")



# with open("open.txt",'r') as fp:
#      # filedata = fp.read()
#      # print(filedata)

#      filedata = fp.readlines()
#      # print(filedata)
#      for val in filedata:
#           print(val)


# srcfile = input("Enter Source file name  : ")
# with open(srcfile, "r") as fp:
#      filedata = fp.read()
#      dstfile = input("Enter Destination File Name : ")
#      with open(dstfile,"a") as fp:
#           fp.write(str(filedata))
#           print("File Copied Successfully - verify")

# with open("open.txt","r") as fp:
#      filedata = fp.readlines()

#      nl = 0
#      nw = 0
#      nc = 0 
#      for line in filedata:
#         nl = nl+1
#         nw = nw+len(line.split())
#         nc = nc+len(line)
#      print("Number of line : ",nl)
#      print("Number of words : ",nw)
#      print("Number of Chatacters : ",nc)

# with open("open.txt","r")as fp:
#     filedata = fp.readlines()


# with open()