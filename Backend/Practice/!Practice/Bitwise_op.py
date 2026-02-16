#Bitwise leftshift operator 
# a=10
# b=a<<3
# print(b)

# print(100<<0)
# print(4<<3)
# print(10<<0)
# print(10.0<<2) # TypeError: unsupported operand type(s) for <<: 'float' and 'int'
# print(4<<-1) #ValueError: negative shift count
# print(12<<2)


#Bitwise Rightshift operator 
# print(16>>3)
# print(32>>3)
# print(805>>4)
# print(22>>4)
# print(22<<4)
# print(40<<-3) # ValueError: negative shift count
# print(10>>3)    # 1



#Bitwise OR operator 

# print(1|0)
# print(0|1)
# print(0|0)
# print(1|1)

#using set Predefined function 
# s1={10,20,30}
# s2={15,10,25}
# s3=s1.union (s2)
# print(s3)

# #by using Bitwise OR operator 
# s1={10,20,30}
# s2={15,10,25}
# s3=s1|s2
# print(s3)

# s3={1.2,2.3,4.5}
# s4={1.2,2.3,4.6}
# s5=s3|s4
# print(s5)

# s1={"python","Danjo"}
# s2={"c","html","c++"}
# s3=s1|s2
# print(s3)

# print(1.2|2.3) # TypeError: unsupported operand type(s) for |: 'float' and 'float'

# "python"|"django" # TypeError: unsupported operand type(s) for |: 'str' and 'str'

# print({1,2,3}|{3,4,5})
#  list
# lst1=[1,2,3]
# lst2=[1,4,5]
# print(set(lst1))
# print(set(lst2))
# print(set(lst1)|set(lst2))
    # tuple
# tpl1=(10,20,30)
# tpl2=(10,40,50)
# # print(set(tpl1)|set(tpl2))
# print(tpl1|tpl2) #TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
    # string
# str1="MISSISSIPPI"
# str2="MISSISSIPPI"
# # print(str1|str2)
# print(set(str1)|set(str2))  # {'S', 'I', 'P', 'M'}

# print(set([1,2,3])|set([1,4,5,]))


# Bitwise AND operator (&)
# print(1 & 0)
# print(0 & 1)
# print(0 & 0)
# print(1 & 1)

# print(10&4)

# a=10
# b=4
# c=a & b
# print(c)

# print(5&7)

# print(bin(18))

#   prime number 
# num=int(input("Enter a number :"))

# Bitwise XOR operator 
# print(~11)
# print(~(-11))
# print(~100)

# print(1^0)
# print(0^1)
# print(0^0)
# print(1^1)

# print(2^3)
# print(10^15)

# s1={10,20,30}
# s2={15,20,25}
# s3=s1.symmetric_difference(s2)
# print(s3)



