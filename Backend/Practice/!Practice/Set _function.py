#SET IS MUTABLE AND IMMUTABLE BOTH 
# Clear function in Set

# s1={10,20,30,40,50,10}
# print(s1,type(s1),id(s1))#{50, 20, 40, 10, 30} <class 'set'> 2296601582880
# s1.clear() 
# print(s1,type(s1),id(s1)) #set() <class 'set'> 2296601582880
# s1.clear()
# print(s1 ,type(s1),id(s1))


# s1={10,20,30,40,50,10}
# #add() function in set
# s1.add("kunal")
# print(s1,type(s1),id(s1))
# s1.add("python")
# print(s1,type(s1),id(s1))

#remove function in set
# s1={10,20,30,40,50,10}
# print(s1.remove(10))
# print(s1,type(s1))
# s1.remove(10)
# print(s1,type(s1),id(s1))
# s1.remove(100) #keyError :100
# print(s1,type(s1))

# Discard function in set 

# s1={10,20,30,40,50,10}
# # print(s1.discard(10))
# s1.discard(10)
# print(s1)
# s1.discard(20)
# print(s1)

#pop function in set
# s1={10,20,"Python",30,"RS",40,50,10}
# s1.pop()
# # print(s1,type(s1),id(s1))
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())

#serial Delete karate he
# >> s1={10,20,30,40,50,10}
# >>> print(s1,type(s1))
# {50, 20, 40, 10, 30} <class 'set'>
# >>> s1.pop()
# 50
# >>> s1.pop()
# 20
# >>> s1.pop()
# 40
# >>> s1.pop()
# 10
# >>> s1.pop()
# 30

# s2={10,60,50,70,80,20,30,90}
# print(s2,type(s2)) #{70, 10, 80, 50, 20, 90, 60, 30} <class 'set'>
# # s2.pop()
# print(s2.pop())#70 90, 60, 30
# print(s2.pop()) # 10
# print(s2.pop()) # 80
# print(s2.pop()) # 50
# print(s2.pop()) # 20
# print(s2.pop()) # 90
# print(s2.pop()) # 60
# print(s2.pop()) # 30
# print(s2.pop()) # KeyError: 'pop from an empty set'

#disjoint() function in set
# s1={10,20,30,40}
# s2={15,25,35}
# s3={10,100,200,300}

# print(s1.isdisjoint(s2))# True
# print(s1.isdisjoint(s3))# False
# print(s2.isdisjoint(s3))# True


#issubset() function in set
# s1={0,1,2,3,4,5,6,7,8,9}
# s2={2,3,4}
# s3={10,20,30}
# s4={1,2,3,10}
# print(s2.issubset(s1)) #True
# print(s3.issubset(s1)) #false
# print(s1.issubset(s3)) #false
# print(s2.issubset(s4)) #false 4 aahe mahun
# print(s1.issubset(s3))
# print(s1.issubset(s2))


#issuperset() function in set
# s1={0,1,2,3,4,5,6,7,8,9}
# s2={2,3,4}
# s3={10,20,30}
# s4={1,2,3,10}
# print(s1.issuperset(s2)) #True
# print(s1.issuperset(s3)) #False
# print(s1.issuperset(s4)) #False

# union () function in set
# cp={"sachin","Rohit","kohli"}
# tp={"kohli","Rossum","travis"}
# print(cp,type(cp),id(cp))
# print(tp,type(tp),id(tp))

# allcptp=cp.union(tp)
# allcptp=tp.union(cp)
# print(allcptp)



#intersection() function in set
# bothcptp=cp.intersection(tp)
# print(f"intersection ==> {bothcptp}")
# k={10,20,30}.intersection({'a','e','i'}) # set()
# print(k)
# print({10,20,30}.intersection({'a','e','i',10}))

# difference() funtion in set
# cp={"sachin","Rohit","kohli"}
# tp={"kohli","Rossum","travis"}
# print(cp,type(cp),id(cp))
# print(tp,type(tp),id(tp))

# onlycp=cp.difference(tp)
# onlytp=tp.difference(cp)
# print(onlycp)
# print(onlytp)

# exclcptp=cp.symmetric_difference(tp)
# print(exclcptp)


# print(set().issubset(set()))
# print(set().issubset({"HYD"}))
# print({10,20,30,}.issubset(set()))
# s1={"a","e","i","o","u"}
# s2={10,20,30,"a","u","i"}
# # s3=s1.symmetric_difference_update(s2)
# s3=s2.symmetric_difference_update(s1)
# print(s3)#----------------------None
# # print(s1)#----------------------{20, 30, 'o', 10, 'e'}
# print("s2==>",s2)#----------------------{20, 30, 'o', 10, 'e'

# cp={"Rohit","Kohli","Rossum"}
# tp={"Rossum","Travis","Hunter"}
# print(cp,type(cp))#-------------------------------{'Rossum', 'Kohli', 'Rohit'} <class 'set'>
# print(tp,type(tp))#--------------------------------{'Rossum', 'Hunter', 'Travis'} <class 'set'>
# exclcptp=cp.symmetric_difference(tp)
# print(exclcptp,type(exclcptp))#------------------{'Rohit', 'Hunter', 'Travis', 'Kohli'} <class 'set'>

# s1={10,20,{'a','b','c'},{33,44,55},"ok"}
# s2={10,20,['a','b','c'],[33,44,55],"ok"}
# s3={10,20,('a','b','c'),(33,44,55),"ok"}
# # print(s1)
# # print(s2)
# print(s3)


#symmetric difference function in set

# s1={10,20,30}
# s2={10,20,60}
# print(s1,type(s1))
# print(s2,type(s2))
# # s3=s1.symmetric_difference(s2)
# # print(s3)
# s4={10,20,30}.symmetric_difference({1,2,3})
# print(s4)
# s5={10,20,30}.symmetric_difference({10,2,3})
# print(s5)

#update()  function in set

# s1={10,20,30}
# s2={1,2,9}
# s3=s1.update(s2)
# print(s3)
# print(s1)


# st1={10,20,30}
# st2={10,20,40}
# st3=st1.update(st2)
# print(st3)
# print(st2)
# print(st1)

