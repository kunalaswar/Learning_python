# def dispstudinfo(sno,sname,smark):
#     print(f"{sno} {sname} {smark}")

# dispstudinfo(100,"sag",70)    
# dispstudinfo(200,"kun",80)  
  
#!
# def dispstudinfo(sno,sname,smarks,crs):
#     print(f"\t{sno}\t{sname}\t{smarks}\t{crs}")


# print(f"\tsno\tsname\tsmarks\tcourse")
# print("-------------------------------------------------")
# dispstudinfo(100,"sag",70,"python")
# dispstudinfo(100,"sag",70,"java")
# dispstudinfo(200, "kun",70,"python")

#!

# def dispstudinfo(sno,sname,smarks):
#     print(sno ,sname ,smarks)
    
# #*main program
# print("sno sname smarks")
# dispstudinfo(100,"ss",70)
# dispstudinfo(200,"ks",80)
# dispstudinfo(smarks=90,sname="hs",sno=300)


# def dispstudinfo(sno,sname,smarks,crs="python"):
#     print(sno, sname, smarks, crs)

# # print("\tsno\tsname\tsmarks\tcrs")
# dispstudinfo(100,"ss",60,"python") #positional auguments   
# dispstudinfo(sname="prath",sno=200,smarks=70,crs="java") #keyword arguments    
# dispstudinfo(500,"huhhbj",70)
#?=====================================================================================================

#!positional Arguments
# def student(sno,sname,smark,course):
#     print(f"\t{sno}\t{sname}\t{smark}\t{course}")

# #main program
# print("\tsno\tsname\tsmark\tcourse") #* positional arguments
# student(100,"har",90,"python")

#!defult Arguments
# def student(sno=100,sname="kunal",smark=80,course="python"):#* Default arguments
#     print(f"\t{sno}\t{sname}\t{smark}\t{course}")

# #main program
# print("\tsno\tsname\tsmark\tcourse")
# student(100,"harshal",90,"python")
# student()

#!keywords Arguments
# def student(sno,sname,smark,course):
#     print(f"\t{sno}\t{sname}\t{smark}\t{course}")

# #main program
# print("\tsno\tsname\tsmark\tcourse")
# student(100,"harshal",90,"python")
# # student()
# student(sno=500,sname="ankit",smark=90,course="python") #*keyword argument


#! variable length Arguments
# def student(*vals):
#     print(vals)

# student(100,"kunal",70,"python")



#!Program for Demonstrating Default arguments
#*DefaultArgsEx1.py
# def dispstudinfo(sno,sname,marks,crs="PYTHON"):
# 	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

# #Main Program
# print("*"*50)
# print("\tSNO\tNAME\tMARKS\tCOURSE")
# print("*"*50)
# dispstudinfo(100,"RS",45.67) # Function Call with Pos Args
# dispstudinfo(200,"TR",75.67) # Function Call with Pos Args
# dispstudinfo(300,"KV",15.67) # Function Call with Pos Args
# dispstudinfo(400,"DR",75.97) # Function Call with Pos Args
# dispstudinfo(500,"SS",45.97,crs="java" ) # Function Call with Pos Args

# print("*"*50)

#!Program for Demonstrating the Need of Variable Length Arguments
#*PureVarArgsEx3.py
# def  calculate(sno,sname,*vals):  # Here *val is called Variable Length Parameter and vals type is <class,tuple>
# 	print("----------------------------------------------------")
# 	print("Student Number:{}".format(sno))
# 	print("Student Name:{}".format(sname))
# 	print("----------------------------------------------------")
# 	if(len(vals)==0):pass
# 	else:	
# 		s=0
# 		for val in vals:
# 			print("\t{}".format(val))
# 			s+=val
# 		print("----------------------------------------------------")
# 		print("Sum={}".format(s))
# 		print("----------------------------------------------------")

# #Main Program
# calculate(100,"RS",10, 20, 30, 40,50)
# calculate(200,"TR",10,20,30,40)
# calculate(300,"DR",10,20,30)
# calculate(400,"DR",10,20)
# calculate(500,"SR",10)
# calculate(600,"SS",1.2,2.2,3.3,4.4,5.5,6.6)
# calculate(700,"KV")

#! program gives an Error 
    #^disp(10,20,30,40,50)
#^ TypeError: disp() takes 1 positional argument but 5 were given
#! this is Not a correct way 
# def disp(a,b,c,d,e):
#     print(a,b,c,d,e)

# def disp(a,b,c,d):
#     print(a,b,c,d)

# def disp(a,b,c):
#     print(a,b,c)

# def disp(a,b):
#     print(a,b)

# def disp(a):
#     print(a)

# disp(10,20,30,40,50)
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
# disp(10)

#!# NOTE : In General If we have n-Function Calls then Python Programmer Must Define n-Function Defintions . This is Process is Time consuming Process.

#!NOTE : let Us have n-Function Calls with Variable Length args then by using By using Var Length args concept
#!we define Single Function Definition.
 
# def disp(a,b,c,d,e):
#     print(a,b,c,d,e)
# disp(10,20,30,40,50)    
# #---------------------------------------
# def disp(a,b,c,d):
#     print(a,b,c,d)
# disp(10,20,30,40)    
# #---------------------------------------
# def disp(a,b,c):
#     print(a,b,c)
# disp(10,20,30)    
# #---------------------------------------
# def disp(a,b):
#     print(a,b)
# disp(10,20)    
# #---------------------------------------
# def disp(a):
#     print(a)
# disp(10)    
# #---------------------------------------

# #! PureVarArgsEx1.py
# def disp(*kvr):
#     print(kvr,type(kvr),len(kvr))

#*main function
# disp(10,20,30,40,50)
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
# disp(10)
# disp()
# disp([],(),{})
# disp(set())
# disp(str(),tuple(),set(),list(),dict())
# disp("kvr","python",1.2,2+3j,True)

# #!#PureVarArgsEx2.py
# def disp(*kvr):
#     print("Number of values=",len(kvr))
#     for val in kvr:
#         print(f"\t{val}")
#     print("-------------------------")    

# #*main function
# disp(10,20,30,40,50)
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
# disp(10)
# disp()
# disp([],(),{})
# disp(set())
# disp(str("HI"),tuple(),set(),list(),dict())
# disp("KVR","PYTHON",1.2,2+3j,True)

# def dispvalues(sno,sname,marks):
#     print(sno,sname,marks)

# dispvalues(100,"RS",45.67)

#!keyword parameter or Arguments
# def dispvalues(sno,sname,marks):
#     print(sno,sname,marks)

# dispvalues(sno=200,sname="TS",marks=60.67)

#!Default parameter or Arguments
# def dispvalues(sno,sname,marks,city="HYD") :
#     print(sno,sname,marks,city)

# dispvalues(100,"KS",70.88)
# dispvalues(100,"KS",70.88)

#! Positional parameter or Arguments
# def dispvalues(sno,sname,marks):
#     print(sno,sname,marks)

# dispvalues(100,"kunal",80)


#! varible length or Arguments
# def dispvalues(*value):
#     print(value) 
#     for val in value:
#         print(val)

# dispvalues(10,20,30)
    
#!keyword varible length Arguments
# def dispvalues(**value):
#     print(value)
#     for keys,val in value.items():
#         print(f"{keys}--->{val}")

# dispvalues(sno=10,sname="sagar",cls="x")

#!
# def findtotalmarks(sno,sname,cls,*vals,city="HYD",**submarks):
#     for val in vals:
#         print(f"{val}")

#     for keys,value in submarks.items():
#         print(f"{keys}--->{value}")    
# findtotalmarks(100,"ankit","XII",10,20,30,city="akola",history=50,geo=60,science=90)        


#!
# def findtotalmarks(sno,sname,cls, city="HYD",**submarks):
#     print("\tStudent Number:{}".format(sno))
#     print(f"\tstudent Name:{sname}")
#     print(f"\tstudent city:{cls}")
#     print(f"\tstudent City:{city}")
#     if(len(submarks)==0):
#         pass
#     else:
#         totalmarks=0
#         for subject,marks in submarks.items():
#             print(f"\t{subject}\t\t{marks}")
#             totalmarks=totalmarks + marks
#     print("Total marks :",totalmarks)        

# findtotalmarks(50,"harsh","X",city="Akola",history=60,science=70,Eco=80,Geo=90)








































































































