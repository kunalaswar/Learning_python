
#! files  
#todo -        For  Normal file 
#^======================================================================================================
#! writing the data to the  Text files
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit.txt","w") as fp:
#     fp.write("1.0 2.0 3.0\n 4.0 5.0 6.0\n 7.0 8.0 9.0 ")
#     print("Text File Created abd data saved to the file :")
    

#^======================================================================================================

#! read the data from file 
#* we can read the data from file 
# try:
#     with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit.txt","r") as fp:
            
#         filedata = fp.read()
#         print("File data ")
#         print(filedata)
# except FileNotFoundError:

#     print("File Not found Error")

#^======================================================================================================
#& read the Data from text File by using numpy.loadtxt()
# import numpy as np
# try:     
#     filedata = np.loadtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit.txt")
#     print("File data ")
#     print(filedata,type(filedata))
# except FileNotFoundError:
#     print("file not found  ")

#^======================================================================================================

#&  Program for Demonstrating Writing the ndarray object data to text file
# import numpy as np
# a = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print(" Given Ndarray Data :")
# print(a,type(a))

#^======================================================================================================
#! savetxt()  numpy ndarray data to save the data 
#^======================================================================================================
#& Program for Demonstrating Writing the ndarray object data to text file
#* data into the file float scientfic notation 
#* 

# import numpy as np
# arr = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("Given Ndarray data ")
# print(arr,type(arr))
# np.savetxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\1.txt",arr)
# print("Nd Array Data saved into Text file")

#^======================================================================================================
#& Program for Demonstrating Writing the ndarray object data to text file
# import numpy as np
# a=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("Given Ndarray object")
# print(a)
# print("-------------------------------------")
# np.savetxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\2.txt",a,delimiter=" ",fmt="%1.1f")
# print("Nd array Data saved in text file")

#^======================================================================================================
#! loadtxt() Use to read the data from file
#^======================================================================================================
#* read the data from text file by using numpy.loadtxt()
# import numpy as np
# # filedata = np.loadtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\1.txt")
# filedata = np.loadtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\2.txt")
# print("File data ")
# print(filedata,type(filedata))

#^======================================================================================================
#! save() to save the data to the Binary file
#! Binary file
#todo - .npy extension 

#& Program for Demonstrating Writing the ndarray object data to Binary file
#^======================================================================================================
# import numpy as np
# arr = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
# print("Given Ndarray data ")
# print(arr)
# print("--------------------------------")
# np.save("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy",arr)
# print("Ndarray data saved in Binary File ---Verify")


#^======================================================================================================
   #! load() reading the data to the Binary file 
#^======================================================================================================
#& Program for Demonstrating Reading data from Binary file into ndarray object
# import numpy as np
# filedata = np.load("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy")
# print("File data ")
# print(filedata,type(filedata))

#^======================================================================================================
#& Program for Demonstrating Reading data from Binary file into ndarray object
#todo - perticular data to file How to access with the help of slicing

# import numpy as np
# filedata = np.load("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy")
# print("File data ")
# print(filedata[0:1,::],type(filedata))
# # print(filedata[0:2,::],type(filedata))

#^======================================================================================================

#& Program for Demonstrating Reading data from Binary file into ndarray object
#* Binary file data read with numpy.nditer() function 
# import numpy as np
# filedata = np.load("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy")
# print("File data read by nditer() function ")
# for val in np.nditer(filedata):
#     print(val)

# import numpy as np
# filedata = np.load("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy")
# print("file data ")
# for val in np.ndenumerate(filedata):
#     print(f"{val[0]} --->{val[1]}")

# import numpy as np
# filedata = np.load("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\3.npy")
# print("file data ")
# for index,value in np.ndenumerate(filedata):
#     print(f"{index} --->{value}")


#^======================================================================================================
#! .csv extension 
#^======================================================================================================

#& writing the data to the CSV File 
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit5.csv","w")as fp:
#     fp.write("1.0 2.0 3.0\n 4.0 5.0 6.0\n 7.0 8.0 9.0")
#     print("CSV file Created and Data Saved in File :")
#^======================================================================================================
#& Reading  the Data from the CSV File
# import numpy as np
# filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit5.csv")
# print(filedata,type(filedata))

#^======================================================================================================
#& Writing the Data to the CSV File
# import numpy as np
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit6.csv","w") as fp:
#     fp.write("1.0,2.0,3.0\n 4.0,5.0,6.0\n7.0,8.0,9.0")    
#     print("CSV file Created and data Saved in file :")

#^======================================================================================================
#& reading the data from the CSV File 
# filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit6.csv",delimiter=",")
# print(filedata,type(filedata))

#^======================================================================================================
#!10-02-2025

#& Reading  the Data from the CSV File where It contains str data

# import numpy as np
# filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit6.csv",delimiter=",")
# print(filedata,type(filedata))

# import numpy as np
# try :
#    filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit6.csv",delimiter=",")
#    print(filedata,type(filedata))
# except FileNotFoundError:
#    print("File not Found Error ")   

#^======================================================================================================

#& save the data to the csv file

# import numpy as np
# arr = ([1, 'GUIDO ROSSUM', 95.5],
#     [2, 'TRAVIS OLIPHANT', 90.0],
#     [3, 'DENNIS RITCHE', 80.0],
#     [4, 'JHON HUNTER', 91.5])

# filedata = np.savetxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit7.csv",arr,fmt="%s",delimiter=",")    
# print(filedata,type(filedata))


#^======================================================================================================

# #& save the data to the csv file
import numpy as np
# arr = [['big','sam','raj'],['read','the','book'],['read','the','python']]
# filedata = np.savetxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit8.csv",arr,fmt="%s")
# print(filedata,type(filedata))

#^======================================================================================================

# filedataread = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit8.csv",dtype =str)
# filedataread = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit8.csv",dtype =str)
# print(filedataread)
# print("file data from file sussessfully")

#^======================================================================================================
#& Read the data from csv file

# import numpy as np
# filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit7.csv",delimiter=",",dtype=str)    
# print(filedata,type(filedata))

#^======================================================================================================
#& Reading  the Data from the CSV File where It contains str data  
# import numpy as np
# arr =np.array([['Rossum','Travis'] ,['Hunter' ,'Gosling']])
# np.savetxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit9.csv",arr,fmt= "%s",delimiter=",")
# print("Data saved file successfully ")
# # print(filedata,type(filedata))

# import numpy as np
# filedata = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\nit9.csv",delimiter=",",dtype=str)
# print(filedata,type(filedata))

#^======================================================================================================

#& Create a NumPy array with both numeric and string data
# import numpy as np
# a = np.array([
#     [1, 'GUIDO ROSSUM', 95.5],
#     [2, 'TRAVIS OLIPHANT', 90.0],
#     [3, 'DENNIS RITCHE', 80.0],
#     [4, 'JHON HUNTER', 91.5]
# ], dtype=object)
# print("content of ndarray")
# print(a,type(a))
# #& write the above ndarray data to csv file
# import numpy as np
# import csv
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit10.csv","w") as fp:
#    csvwr = csv.writer(fp)
#    print(csvwr,type(csvwr))
#    csvwr.writerows(a) #* Here a is an Ndarray object
#    print("ND Array data written to the csv file --verify ")

#^======================================================================================================

# import numpy as np
# import csv
# #& create a numpy array with both numeric and string
# a = np.array([
#     [1, 'GUIDO ROSSUM', 95.5],
#     [2, 'TRAVIS OLIPHANT', 90.0],
#     [3, 'DENNIS RITCHE', 80.0],
#     [4, 'JHON HUNTER', 91.5]], dtype=object)
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit11.csv","w") as fp:
#    csvwr = csv.writer(fp)
#    print(csvwr,type(csvwr))
#    for row in a:
#       csvwr.writerow(row)
# print("ND array data written to the File--verify")      
# #*OR to written multiple data at a time
#    ##csvwr.writerows(a)
# ##print("data written")   

#^======================================================================================================

#& Most IMP
#& : This Reads the Data from CSV File where It Contains Different Col names with Diff type

# import numpy as np
# #todo - define the path to the csv file
# csv_file_path ="D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit11.csv"
# #todo - define the datatype for each column
# dtype = [("id" ,"i4"),("name","U10"),("Score","f4")]

# #todo - Read the CSV file into a structured Numpy array 
# sa = np.genfromtxt(csv_file_path,delimiter=",",dtype=dtype,names=True)

# #todo - print the Structured numpy array
# print(sa,type(sa))

#^======================================================================================================
#& Most IMP: This Reads the Data from CSV File where It Contains Different Col names with Diff type
#^======================================================================================================
# import numpy as np
# #todo - define the file path 
# csv_file_path = "D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit11.csv"

# #todo - define datatypes for Each column
# dtype = [("id","i4"),("Name","U10"),("score","f4")] #* U10 aahe manun sting fakt 10 gete

# #todo -read the csv file a structured array
# sa = np.genfromtxt(csv_file_path,delimiter=",",dtype= dtype,names=True)

# #todo - print the structured Numpy array

# print(sa,type(sa))
# print("------------------------------")
# for row in sa :
#     print(row)

#^-------------------------------------------------------------------------------------------------------

# for row in sa:
#    for val in row:
#         print(f"\t{val},",end= "\t")
#    print()    


#^======================================================================================================
#& Most IMP: This Reads the Data from CSV File where It Contains Different Col names with Diff type
# import numpy as np
# #todo - define the path to the csv file
# # csv_file_path = 

# #todo - Define the data type for each column
# # dtype = 

# #todo - Read the CSV file into a structured numpy array
# sa = np.genfromtxt("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit11.csv",delimiter=",",dtype = [("id","i4"),("name","U15"),("score","f4")],names= True)

# #print the structured numpy array
# print(sa,type(sa))

#^======================================================================================================

#& Most Imp: Writing the Ndarray object data to text File and Reading the Text File Data
# import numpy as np
# #todo -Create a numpy array

# data_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(data_array.dtype)
# #todo - Define the path to the text file
# text_file_path = "D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\ndnit112.csv"

# #todo - # Save the NumPy array to a text file with space as the delimiter
# np.savetxt(text_file_path,data_array)
# print("----------------------------------------")
# print("ndarray object data saved in text file")
# print("-----------------------------------")
# #todo - Read the text file back into a NumPy array

# # read the data to file 
# loaded_array = np.loadtxt(text_file_path)

# #todo - Print the original and loaded NumPy arrays
# print("Original numpy array ")
# print(data_array)



# #^======================================================================================================

# print("Original Numpy array ")
# print(data_array)
# print(data_array.dtype)

# #^======================================================================================================

# print("Original Numpy Array with float")
# loaded_array = loaded_array.astype(float)
# print(loaded_array.dtype)

# #^======================================================================================================
# print("Original numpy array with int ")
# loaded_array = loaded_array.astype("i4")
# print(loaded_array.dtype)

# #^======================================================================================================

# print("Original numpy array with float ")
# loaded_array = loaded_array.astype("i2")
# print(loaded_array)
# print(loaded_array.dtype)
# #^======================================================================================================
#&  json file 
#todo       .json extension
# #^======================================================================================================
# import numpy as np
# import json
# employee = ' {"id":"09", "name": "Rossum", "department":"IT"} ' #* put into the str double cot ""
# #& Here we are convert Json data into str data
# dictemp =json.loads(employee)
# print(dictemp,type(dictemp))


#todo -Save the dict object into Json file
# import json
# dictobj =  ' {"id":"09", "name": "Rossum", "department":"IT"} ' #* put into the str double cot ""
# with open( "D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\json1.json","w")as fp:
#    json.dump(dictobj,fp)
#    print("Dict data saved into json file---Verify ") 
   
# #^======================================================================================================

#& Read the json Data into Ndarray object
# import numpy as np
# import json
# with open( "D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\json1.json","r")as fp:
#    jsondata = json.load(fp)
#    #* Here Json data is of type <class,dict>
#    #* convert the dict type data into the Ndarray data by using array()
#    a = np.array(jsondata)
#    print(a,type(a))

#^======================================================================================================
#todo -write the json file data 
# import json 
# import numpy as np
# dictdata = {'Title': "The Cuckoo's Calling", 'Author': 'Robert Galbraith', 'Genre': 'classic crime novel', 'Detail': {'Publisher': 'Little Brown', 'Publication_Year': 2013, 'ISBN-13': 9781408704004, 'Language': 'English', 'Pages': 494}, 'Price': [{'type': 'Hardcover', 'price': 16.65}, {'type': 'Kidle Edition', 'price': 7.03}]} #<class 'numpy.ndarray'>

# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\json2.json","w")as fp:
#    json.dump(dictdata,fp)
#    print("Data loaded into the file json file ---verify json2. ")




#^======================================================================================================
# #& Read Json File Data into ndarray object
# import json
# import numpy as np
# with open("D:\\PYTHON FULL STACK\\LibraryPrograms\\Numpy\\Files\\json2.json","r")as fp:
#     jsondata = json.load(fp)
#     #* Here json data is of type <class,dict'
#     #* Convert dict type data into ndarray object data by using array()
#     a = np.array(jsondata)
#     print(a,type(a))


#^======================================================================================================







    


#^======================================================================================================
   


































