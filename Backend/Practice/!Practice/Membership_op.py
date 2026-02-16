
#Assignment operator 

# a=10
# b=20
# print(a+b)

# multiline Assignment
# a,b = 10,20
# print(a,b)

#logic 1 for swapping 

# a=int(input("Enter a number a: "))
# b=int(input("Enter a number b: "))
# print(f"origanl value of a,b= {a},{b}")
# a,b=b,a
# print(f"swapiing value of a and b is {a},{b}")

#logic 2 for swapping 

# a=10
# b=20
# print(f"original value of a and b is {a},{b}")
# temp=a
# a=b
# b=a
# print(f"Swapping value of aand b is {a},{b}")

# logic 3 for swapping 
# a=int(input("Enter a number a: "))
# b=int(input("Enter a number b: "))
# # a=10
# # b=20
# print(f"origanl value of a , b = {a}, {b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"swapping value of a and b is = {a}, {b}")

#logic 4 for swapping 

# a=int(input("Enter a number a: "))
# b=int(input("Enter a number b: "))
# print(f"origanl value of a,b= {a},{b}")

# print(10<2)
# print(10<20)
# print(10<50)
# print(50<5)
# print(50<50)
# print(10>=20)
# print(10>=2)
# print(10>10)
# print(10>=10)
# print(10<=10)
# print(10<=90)
# print(10<=5)
# print(10<=50)
# print(10==5)
# print(10!=5)
# print(10!=5)
# for i in range(97,123):
#     print("{}--->{}".format(i,chr(i)))


# print(ord("rader")) #TypeError: ord() expected a character, but string of length 5 found

# Membership operator

# s="python"
# print("p" in s)
# print("p" not in s)
# print("k" in s)
# print("k"  not in s)

# s = "python"
# print("pyth" in s)
# print("kvr" in s)
# print("kvr"  not in s)
# print("thon"  in s)
# print("pto" in s )
# print("pto" not in s)
# print("noh"[::-1] in s)
# print("noh"[::-1] not in s)
# print("pto" in s[::2])

# list data type
# lst=[10,"Rossum",34.56,2+3j]
# print(10 in lst)
# print(100 in lst)
# print(100 not in lst)
# print("Ros" in lst)
# print("Rossum" in lst)
# print("Ross" in lst)
# print("Ros" in lst[1])
# print("Rossum" in lst[1][::-1])
# print("mussoR" in lst[1][::-1])
# print(2+3j in lst)
# print(2+3j in lst[1])
# print(2.0 not in lst[-1].real)


# dict data type
# d1={10:1.2,20:2.3,30:3.4,40:4.5}
# print(1.2 in d1)
# print(10 in d1)
# print(20 in d1)
# print(30 in d1)
# print(10,1.2 in d1)

# print(1.2 in d1.values())
# print(4.5 in d1.values())
# print( 10 in d1.values())
# print( 70 not in d1.values())
# print( 20 in d1.keys())
# print( 10 in d1.keys())
# print( 100 in d1.keys())
# d1={10:1.2,20:2.3,30:3.4,40:4.5}
# print((10,1.2) in d1.items())
# print(1.2 in d1[10])
# print( 1.2 in d1.get(10))

# s1="1234"
# print("12" in s1)
# print(123 in s1)
# lst=[10,20,30]
# print(lst[0] in lst[::-1])
# print(lst[0] in lst)



# lst1=[10,20,30]
# lst2=[50,60,70]
# print(lst1+lst2)

s="python"
# print("p" in s)
# print("k" not in s)
# print("p" not in s)
# print("k" not in s)
# print("noh" not in s)
# s1="PYTHON"
# print("NOH" not in s1)
# s="1234"
# s="python"
# print("12" in s)
# print("12" not in s)
# print(123 not in s)
# print( s in s)
# lst=[10,20,30]
# print(lst in lst)


#   What will the following code output?
# x = 20
# if x < 10:
#     print("Less")
# elif x < 30:
#     print("Between 10 and 30")
# else:
#     print("Greater")

# s1="python"
# s2="python"
# print(s1,id(s1))
# print(s2,id(s2))

# lst=[10,20,30]
# lst=[40,50,60]
# print(lst in lst)
# print(lst ,id(lst))
# print(lst ,id(lst))


# Identity operator 

lst1=[10,20,30]
# lst2=lst1 #Deep copy
# print(lst1,id(lst1))
# print(lst2,id(lst2))
# print(lst1 is lst1)
# print(lst1 is not lst2)

# lst3=lst1.copy() #Shallow copy
# print(lst1,id(lst1))
# print(lst3,id(lst3))
# print(lst1  is lst3)
# print(lst1  is not lst3)
 
 # keyword

# a=None
# print(a,id(a))
# b=None
# print(b,id(b))
# print(a is b)
# print(a is not b)

# # dict 
# d1={10:"apple",20:"banana",30:"kiwi"}
# d2={10:"apple",20:"banana",30:"kiwi"}
# print(d1,id(d1))
# print(d2,id(d2))
# print(d1 is d2)
# print(d1 is not d2)
# print(10 in d1.keys())
# print("apple" in d1.values())
# print("apple" in d1[10])
# print( d2 is not  d1)
# print( d1 is d1)
# print( d1 is not d1)
# print( d1 is not d2)

 # set
# s1={10,20,30,40}
# s2={50,60,70,80}
# print(s1 is s2)
# print(s1 is not s2)
# print(10 in s1)
# print(20 in s1)
# print(100 in s1)
# print(50 in s2)
# print(80 in s2)

 # frozenset()
# fs1=frozenset({10,20,30,40})
# fs2=frozenset({50,60,70,80})
# print(fs1,id(fs1))
# print(fs2,id(fs2))
# print(fs1 is fs2)
# print(fs2 is fs1)
# print(fs1 is not fs2)
# print(fs2 is not fs1)
# print(fs1 is  fs1)
# print(fs1 is not fs1)
# print(10 is fs1)
# print(10 is not fs1)

# list()
# lst1=[10,20,70,80]
# lst2=[10,20,70,80]
# print(lst1,id(lst1))
# print(lst1,id(lst2))
# print(lst1 is lst2)
# print(lst1 is not lst2)

#tuple()
# t1=(10,20,80,90)
# t2=(10,20,80,90)
# print(t1,id(t1))
# print(t2,id(t2))
# print(t1 is t2)


# range()
# r1=range(10,21,2)
# for i  in r1:
#     print(i)
# r1=range(10,20,2)
# r2=range(10,20,2)
# print(r1,id(r1))
# print(r2,id(r2))
# print(r1 in  r2)
# print(r1 not in r2)

#bytearray()
# print(0b01)
# print(bin(1))
# ba1=bytearray([10,20,30,])
# ba2=bytearray([10,20,30,])
# print(ba1,id(ba1))
# print(ba2,id(ba2))
# print(ba1 is ba2)
# print(ba1 is not ba2)

# Bytes()
# b1=bytes([10,20,30])
# b2=bytes([10,20,30])
# print(b1,id(b1))
# print(b2,id(b2))
# print(b1 is b2)
# print(b1 is not b2)


# Most IMP

# s1="python"
# s2="python"
# print(s1,id(s1))
# print(s2,id(s2))
# print(s1 is s2)
# print(s1 is not s2)

# s1="python"
# s2="pythoN"
# print(s1,id(s1))
# print(s2,id(s2))
# print(s1 is s2)
# print(s1 is not s2)


#