
#* program for need of iterator 
#* program for Demonistrating the need of iterator
#^========================================================================================================
#! iterator
#^========================================================================================================
#*listiterEx.py
# x = [10,"RS",23.45,3+4j,True,False]
# print("Type of x = ",type(x)) #
#* To Convert Iterable object into Iterator Object, we use iter()
# itrobj = iter(lst)
# itr = iter(x)
# print("type of iter = ",type(itr))

# print("Content of the itrobj : ",itrobj)   #* <list_iterator object at 0x0000019D15D5AE00>
# print("Type Of the itrobj : ",type(itrobj))  #* <class 'list_iterator'>
# print('---------------------------------------------')
# while(True):
#     try:
#         print(next(itr))
#     except StopIteration:
        #   print("-----------------------------------")
#         break    

#^========================================================================================================

#!TupleiterEx.py
#^========================================================================================================

# tup = (10,"RS",23.45,3+4j,True,False)
# print("content of the tuple = ",tup)

# print("Type of a = ",type(tup))

# #* TO convert iterable object into Iterable   object we use iter()
# itrobj = iter(tup)
# print("Content of iterobj =",itrobj)
# print("Type of iterobj  =",type(itrobj))

# #* to Convert Iterable object into Iterable object we use iter()
# iterobj = iter(tup)
# print("Content of iterobj =",iterobj)  #*<tuple_iterator object at 0x00000203F875AE00>
# print("Type of iterobj",type(iterobj)) #*<class 'tuple_iterator'>
# print("Content of the iterobj using while loop")
# while True:
#     try:
#         print(next(iterobj))
#     except StopIteration:
#         break    

#^========================================================================================================

#! program for Demonstrating the need of Iterable
#! IterEx3.py

# s1 = {10,20,30,40,50,60,"Rossum","python"}
# print("Content of s1 = ",s1)
# print( "Type of s1 = ",type(s1))

# #* Convert the iterable  object into the iterable object
# iterobj = iter(s1)
# print("Copntent of itrobj = ",iterobj) #*<set_iterator object at 0x000002078FA891C0> 
# print("Type of iterobj = ",type(iterobj)) #*Type of iterobj =  <class 'set_iterator'>

# print("Content of Iterobj using for loop")
# for val in iterobj:
#     print(val)

#^========================================================================================================
#! program for Demonstrating the need of Iterators
#! IterEx4.py
# fs1 = frozenset({10,20,30,40,50,60,"Rossum","python"})
# print("Content of fs1 = ",fs1)
# print("Type of fs1 =",type(fs1))

#todo -Creating the object of iterable object  

# iterobj = iter(fs1)
# print("Content of iterobj =",iterobj) #*<set_iterator object at 0x000002D5383B9980>
# print("Type of Iterobj = ",type(iterobj)) #* <class 'set_iterator'>

# print("Content of the frozenset by using for loop ")
# #* for loop with next() function a hote te
# for val in iterobj: 
#     print(val)
#^========================================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx5.py
d1={1:"Python",2:"C",3:"C++",4:"Java",5:"DSA"}
print("Content of d1 = ",d1)
print("Type of d1 = ",type(d1))

#todo -convert the iterable object into iterablr object
iterobj = iter(d1)
print("content of iterobj = ",iterobj) #* <dict_keyiterator object at 0x0000011DC4080AE0>
print("Type of iterobj =",type(iterobj)) #* <class 'dict_keyiterator'>

# print(next(iterobj))
# print(next(iterobj))
# print(next(iterobj))


# k = next(iterobj)
# print(k,d1.get(k))
# k = next(iterobj)
# print(k,d1.get(k))  
# #* or
# print(k,d1[k])

# for val in iterobj:
#     print(f"{val} --->{d1.get(val)}")

# # print("By using for loop")
# while(True):
#     try:
#         k = next(iterobj)
#         print(k,d1.get(k))
#         print(k,d1[k])
#     except StopIteration:
#         break
#^========================================================================================================

#! Program for Demonstrating the need of Iterators
#! IterEx6.py
# s="PYTHON"
# print("Content of s : ",s)
# print("Type of s : ",type(s))
# #* convert the iterable  object into iterable iter object

# itr = iter( s)
# print("type of str = ",type(itr))
# print("----------------------------------")
# print("Content of str itreater")
# print("------------------------------")

# for val in itr:
#     print(val)
# print("-----------------------")    

#^========================================================================================================
#! Program for Demonstrating the need of Iterators
#! IterEx7.py
r = range(10,21,2)
print("Content of r= ",r)
print("type of r = ",type(r))

#* convert the iterable object into the iterabe object
iterobj = iter(r)
# print("Content of itrobj : ",itrobj)   #* <range_iterator object at 0x000001B2588AAEF0>
# print("Type of itrobj : ",type(itrobj))    #*<class 'range_iterator'>

print("Content of iterable object using for loop ")
for val in iterobj:
    print(val) #for loop can direct print value with out the next() function 

#^========================================================================================================
#!Program for Demonstrating ---It is not possible to apply on Non-Iterable Objects like int,float, bool,complex and NoneType
#! IterEx8.py

a = 0
print("Content of a =",a)       # * Here a object is called Non-Iterable Object
print("Tyep of a = ",type(a))


iterobj = iter(a) #* TypeError: 'int' object is not iterable
print(iterobj)

#^========================================================================================================




  








 
    


