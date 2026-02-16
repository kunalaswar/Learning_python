# for val in range(1,6):
#     print("*" ,end=" ")
#?========================================================

# for  val in range(1,6):
#     for i in range(1,6):
#         print("*",end=" ")
#     print()
#?========================================================

# for val in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()    
#?========================================================

# for val in range(1,6):
#     for j in range(1,6):
#         print(val,end=" ")
#     print()    
#?========================================================

# for i in range(6,0,-1):
#     for j in range(6,1,-1):
#         print(i,end=" ")
#     print()    
#?========================================================
#!wrong program 
# for i in range(1,-1,-1) :
#     # print(i)
#     for j in range(1,6):
#         print(i,end=" ")
#     print()    

# for i in range(1,-1,-1):
    # print(i)

# for i in range(1,6):
#     for j in range(1,6):
#         print("1",end=" ")
#         print("0",end=" ")
#     print()    
#?========================================================
#* IMP QUESTION 
# for i in range(1,6):
#     for j in range(1,6):
#         if(i%2==0):
#             print("0",end=" ")
#         else:
#             print("1",end=" ")    
#     print()        

#?========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()    

#?========================================================
# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()    

#?========================================================
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()    

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    

#?========================================================
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()  

#?========================================================
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()   

#?========================================================
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()    
#?========================================================

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    
#?========================================================
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    

#?========================================================
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    

#?========================================================
# try:
#     x = int("123abc")
# except (ValueError, TypeError):
#     print("Caught an exception")
#?========================================================
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i>=j:
#             print(j,end=" ")
#         else:    
#             print("-" ,end=" ") #* to understand this  we print ( - ) not a space
#     print()        



#?========================================================
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print("-",end=" ")    
#     print()
# print("---------------------------------------")
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")    
#     print()
#?========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if(i<=j):
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")    
#     print()    
#!nahi samajala
# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print(" ",end= " ")
#         else:
#             print(j,end=" ")    
#     print()

#?========================================================
# for i in range(1,6):
#     for j in range(5,0,-1):
#         if j>=i:
#             print(j,end=" ")
#         else:
#             print("-",end=" ")    
    # print()        
#?========================================================
# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         if j>=i:
#             print(j,end=" ")
#         else:
#             print("-",end=" ")    
#     print()        
#?========================================================
#! yekach program lehayache many logic asatat fakt logic lavata yayala pahije
#^ logic-1
# for i in range(1,6):                                     #* A B C D E
#     for j in range(ord("A"),ord(("F"))-i):               #* A B C D 
#         print(chr(j),end=" ")                            #* A B C 
#     print()                                              #* A B  
                                                           #* A                     
#! Same Answer
# #^ logic-2
# for i in range(69,64,-1):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()    

# #! Same Answer
# #^ logic-3
# for i in range(1,6):
#     for j in range(65,71-i):
#         print(chr(j),end=" ")
#     print()    
#! Same Answer
#^ logic-4




#?========================================================
#!IMP LOGIC
# num=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num,end=" ")    
#         num=num+1
#         # print(num)
#     print()    



#?========================================================
#! IMP LOGIC
# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 or j==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()    

#! IMP LOGIC
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5:
#             print("*",end=" ")
#         else:
#             print("-" ,end=" ")    
#     print()    

# for i in range(1,6):
#     # print(i,end=" ")
#     for i in range(1,6):
#         print(j,end=" ")
#     print()    

# for i in range(1,6):
#     # print(i,end=" ")
#     for j in range(1,6):
#         print(j,end=" ")
#     print()    

#?========================================================
# for i in range(1,6):
#     print(i,"|",end=" ")
#     for j in range(1,3):
#         print(j,end=" ")
#     print()    

#?========================================================
spaces=4
for i in range(1,6):
    for s in range(1,spaces+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    spaces=spaces-1
    print()    

# spaces=4
# for i in range(1,6):
#     for s in range(spaces-1,1,-1):
#         print(end="-")
#     for j in range(i-1,1,-1):
#         print("*",end=" ")    
#     spaces=spaces-1    
#     print()


#?========================================================




















































