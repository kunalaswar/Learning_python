

#! DataFrame Object Creation Examples
# import numpy as np,pandas as pd
# a = 10
# print(a,type(a))
# # df = pd.DataFrame(a)   #* Error
# # print(df)
# df =pd.DataFrame ([a])
# print(df,type(df))

#^=======================================================================================================
#& We can't create DataFrame Object with Fundamental Traditional Python Object.
#& We must Fundamental Traditional Python Object into Iterable Objects by using Type Casting Functions

#!int
# import pandas as pd
# a = 10
# df = pd.DataFrame([a])
# print(df)

#!float
# import pandas as pd
# a = 10.2
# df = pd.DataFrame([a])
# print(df,type(df))

#! bool
# import pandas as pd
# a = True
# df = pd.DataFrame([a])
# print(df,type(df))

#! complex
# import pandas as pd
# a = 2+3j
# df = pd.DataFrame([a])
# print(df,type(df))   

#           0
# 0  2.0+3.0j <class 'pandas.core.frame.DataFrame'> 

#^=======================================================================================================
#!str
# import pandas as pd
# a = "python"
# df = pd.DataFrame([a])
# print(df,type(df))

#! bytes
# import pandas as pd
# a = bytes(10)
# df = pd.DataFrame([a])
# print(df,type(df))

#!bytesarray

# import pandas as pd
# a = bytearray(10)
# df = pd.DataFrame([a])
# print(df,type(df))


#^=======================================================================================================
#! Create an object of DataFrame By using range

# import pandas as pd
# r = range(10,21,2)
# df = pd.DataFrame(r)
# print("COntent of DataFrame")
# print(df,type(df))

#! Create an object of DataFrame By using list
# import pandas as pd
# lst = [100,200,300,400,500,600]
# df = pd.DataFrame([lst])
# print("Content of Dataframe")
# print(df,type(df))

#^=======================================================================================================
#! Create an object of DataFrame By using list
# import pandas as pd
# lst  =  [100,"Rossum",45.67,"python"]
# df  = pd.DataFrame(lst)
# print("Content of DataFrame ")
# print(df,type(df))

#^=======================================================================================================
#! Create an object of DataFrame By using list
# import pandas as pd
# lst = [100,200,300,400,500,600]
# df = pd.DataFrame(lst,dtype=float)
# print("Content of DataFrame")
# print(df,type(df))

#^=======================================================================================================
#! Create an object of DataFrame By using list with Giving To name 

# import pandas as pd
# lst  =  [100,"Rossum",45.67,"python"]
# df = pd.DataFrame(lst,index=["id","Name","Marks","Subject "])
# print("Content of dataframe ")
# print(df,type(df))

#^=======================================================================================================
#!  Create an object of DataFrame By using list  only With column name   
# import pandas as pd    
# lst  =  [100,"Rossum",45.67,"python"]
# df = pd.DataFrame(lst,columns=["Record"])
# print("Content of DataFrame ")
# print(df,type(df))

#^=======================================================================================================
#! Create an object of DataFrame By using list Both column name and  Row name
#todo  - madatalya value le dataset manatat
# import pandas as pd
# lst  =  [100,"Rossum",45.67,"python"]
# df = pd.DataFrame(lst,index=["Id ","Name","marks","Subject"],columns=["Records"])
# print("Content of Dataframe ")
# print(df,type(df))

#^=======================================================================================================
#! tto find the Dimesion and shape of an DataFrame 
# import pandas as pd
# lst  =  [100,"Rossum",45.67,"python"]
# df = pd.DataFrame(lst,index=["Id","Name","Marks","Subject"],columns=["Record"])
# print("Content of dataFrame ")
# print(df,type(df))
# print(df.ndim)
# print(df.shape)

#^=======================================================================================================
#todo -  It Consider as a row data Name

# import pandas as pd
# lst  = [[100],["Rossum"],[45.67],["python"]]
# df = pd.DataFrame(lst)
# print(df,type(df))

#todo -  It Consider as a column data Name 
# import pandas as pd
# lst = [[100,"Rossum",45.67,"python"]]
# # print(lst)
# df = pd.DataFrame(lst)
# print(df,type(df))

#^=======================================================================================================
#todo  - 
# import pandas as pd
# lst = [[100,"Rossum",45.67,"python"]]
# df = pd.DataFrame(lst,index=["Record"],columns=["Id","Name","Marks","Subject "])
# print(df,type(df))


#^=======================================================================================================
#todo -  Giving your own index and Column name     

# import pandas as pd
# lst =[[100,"Rossum",45.67,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"MatplotLib"]]
# df = pd.DataFrame(lst,index=["Record1","Record2","Record3"],columns=["Id","name","Marks","Subject "])   
# print("Content of Dataframe ")
# print(df,type(df))

# print("Dimension of DataFrame = ",df.ndim)
# print("Shape of dataFrame = ",df.shape)

#^=======================================================================================================

#todo - not to give your own index and Column name 
# import pandas as pd
# lst =[[100,"Rossum",45.67,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"MatplotLib"]]
# df = pd.DataFrame(lst) #* It Take Bydefault data
# print(df,type(df))

#^=======================================================================================================

#! for getting the Row value easily it do sir
# import pandas as pd
# lst =[[100,"Rossum",45.67,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"MatplotLib"]]
# df = pd.DataFrame(lst,index=["rec" + str(i) for i in range(1,len(lst)+1) ]) #* concat the String
# print(df,type(df))

#^=======================================================================================================

#! for Geitng the Row and Cloumn name easily it do sir
# import pandas as pd
# lst =[[100,"Rossum",45.67,"Python"],[200,"Travis",56.78,"Numpy"],[300,"Hunter",33.33,"MatplotLib"]]
# df = pd.DataFrame(lst,index=["rec" +str(i) for i in range(1,len(lst)+1)],columns=["Col"+str(j)for j in range(1,len(lst[0])+1)])
# print(df,type(df))

#^=======================================================================================================

#todo  - Tuple In tuple of Value 
#* It Automatically remove the Tuple of Tuple 
# import pandas as pd
# tpl = ((10,"Rs"),(20,"DR"),(30,"JH"),(40,"ss"))
# # print(tpl)
# df   = pd.DataFrame(tpl)
# print(df)

#^=======================================================================================================

# import pandas as pd
# tpl = ((10,"Rs"),(20,"DR"),(30,"JH"),(40,"ss"))
# df = pd.DataFrame(tpl,index=["Rec"+str(i) for i in range(1,len(tpl)+1)],columns=["Id","Name"])
# print(df,type(df))

#^=======================================================================================================

#todo - consider as the row 
# import pandas as pd
# tpl = [[10,20,30,40],["TR","DR","SS","JH"]]
# df = pd.DataFrame(tpl)
# print(df,type(df))

#* 0   1   2   3
#* 0  10  20  30  40
#* 1  TR  DR  SS  JH <class 'pandas.core.frame.DataFrame'>
#^=======================================================================================================

#* Implement the Following  with dataframe object

#*		      CL		HL		PL
#* SBI		8.2		7.8		11.2 
#* HDFC      7.8		8.8		12.4
#* ICICI		8.5		8.7		10.5

# import pandas as pd
# loans=[[8.2,7.8,11.2],[7.8,8.8,12.4],[8.5,8.7,10.5]]
# df = pd.DataFrame(loans,index=["SBI","HDFC","ICICI"],columns=["CL","HL","PL"])
# print(df,type(df))

#^=======================================================================================================
#todo - We can convert the set in list and tuple in lst and list in lst 
#todo -BUT we can never convert the list of set
# import pandas as pd
# loans=[{8.2,7.8,11.2},(7.8,8.8,12.4),[8.5,8.7,10.5]]
# df = pd.DataFrame(loans,index=["SBI","HDFC","ICICI"],columns=["CL","HL","PL"])
# print(df)

#^======================================================================================================
#! Converting set object into DataFrame
# import pandas as pd
# s={8.2,7.8,11.2}
# df = pd.DataFrame(s)
# print(df)
#^=======================================================================================================
#! Converting frozenet  object into DataFrame
# import pandas as pd
# s = frozenset({8.2,7.8,11.2})
# df = pd.DataFrame(s)
# print(df)
#^=======================================================================================================

#! Converting Dict  object into DataFrame
#todo - Key Go the Column name 
#todo - But in Series it takeing the name as Row name
# import pandas as pd
# dictobj={"Python":1,"C":2,"C++":3,"Java":4}
# # df = pd.DataFrame(dictobj)  #*ValueError: If using all scalar values, you must pass an index
# df = pd.DataFrame(dictobj,index=[1])
# print(df)
#&    OR
#?======================================================================================================
# import pandas as pd
# dictobj = {"Python": 1, "C": 2, "C++": 3, "Java": 4}
# df = pd.DataFrame([dictobj])  # Wrap the dictionary in a list
# print(df)
#?======================================================================================================
#^=======================================================================================================
#! Converting Dict  object into DataFrame
#todo - Key Go the Column name 
#todo - But in Series it takeing the name as Row name
# import pandas as pd
# dictobj = {"ID":[100,200,300],"Name":["Rossumn","Travis","Hunter "],"Age":[99,78,88]}
# df = pd.DataFrame(dictobj)
# print(df,type(df))

#^=======================================================================================================

#! Converting Dict  object into DataFrame

# import pandas as pd
# dictobj={"ID":[100,200,300],"NAME":["Rossum","Travis","Hunter"],"AGE":[99,78,88]}
# df = pd.DataFrame(dictobj,index=["Rec1","Rec2","Rec3"])
# print(df,type(df))

#^=======================================================================================================
#! Create DataFrame Object from Series Object

# import pandas as pd
# lst = [100,200,300,400,500,600]
# s = pd.Series(lst)
# print("Series of Data ")
# print(s,type(s))
# print("-----------------------------------------")
# df = pd.DataFrame(s)
# print(df,type(df))
#^=======================================================================================================

#! Create DataFrame Object from ndarray Object
# import numpy as np,pandas as pd
# lst = [100,200,300,400,500]
# a = np.array(lst)
# print("Content of Ndarray ")
# print(a,type(a))
# print("-----------------")
# df = pd.DataFrame(a)
# print("Content of DataFrame ")
# print(df,type(df))


#^=======================================================================================================
#&.CSV Extension
# !Create NDArray Object by using CSV File
# import pandas as pd,numpy as np
# # df = pd.read_csv("D:\\PYTHON FULL STACK\\Practice\\Files\\CSVFILE\\Student.csv")

# df = pd.read_csv("D:\\PYTHON FULL STACK\\Practice\\Files\\CSVFILE\\Students.csv")
# print(df)


#^=======================================================================================================
# #todo  - it Give the SNAME  into the CSV file
# print(df["SNAME"])

# print(df["SNAME"],type(df["SNAME"]))

#^=======================================================================================================








