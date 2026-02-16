# #Program for Creating CSV File Dynamically from Read the List Values from KBD
# #DynamicCSVCreateEx1.py
# import csv
# #Take Column Names--Step-1
# noc=int(input("Enter How Many Columns u Have:"))
# if(noc<=0):
#     print("{} is Invalid Number of Columns".format(noc))
# else:
#     #Accept the column names
#     colnames=[] # create an empty list for adding col names
#     for i in range(1,noc+1):
#         colname=input("Enter {} Col Name:".format(i))
#         colnames.append(colname)
#     else:
#         nor=int(input("Enter How Many Records u Have:"))
#         if(nor<=0):
#             print("{} Invalid Number of Records:".format(nor))
#         else:
#             records = []  # empty outer list for adding inner list values
#             for i in range(1,nor+1):
#                 print("-"*50)
#                 print("Enter {} Record".format(i))
#                 print("-" * 50)
#                 record=[] # for adding Record value
#                 for j in range(len(colnames)):
#                     val=input("Enter Value for {}:".format(colnames[j]))
#                     record.append(val)
#                 else:
#                     records.append(record)
#             else:
#                 while(True):
#                     csvfilename=input("Enter CSV File Name with an extension .csv:")
#                     if(csvfilename.endswith(".csv")):
#                         with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\"+csvfilename,"a") as fp:
#                             csvwr=csv.writer(fp)
#                             csvwr.writerow(colnames)
#                             csvwr.writerows(records)
#                             print("CSV File Created and Records Saved Dynamically-Verify")
#                             break
#                     else:
#                         print("Invalid CSV File Name-try Again")


# import csv
# nocol=int(input("Enter How many column you Want to generate:"))
# if nocol<=0:
#     print("Invalid column number ")
# else:
#     maincolnames=[]    
#     for i in range(1,nocol+1):
#         colname=input(f"Enter a column {i} :")
#         maincolnames.append(colname)
#     else:
#         nor=int(input("Enter How many RECORDS you Wnat to Enter:"))
#         if nor<=0:
#             print("Invalid input for Number of Rows :")
#         else:

#             records=[]
#             for i in range(1,nor+1):
#                 print("Enter {} Record".format(i))
#                 record=[]
#                 for j in range(len(maincolnames)):
                    
#                     val=input("Enter Value for {}:".format(maincolnames[j]))
#                     record.append(val)
#                 else:
#                     records.append(record)
# # print(records)    
#             else:
#                 while(True):
#                     filename=input("Enter file Name:")
#                     if filename.endswith(".csv"):
#                         with open("D:\\PYTHON FULL STACK\\Practice\\CSVFILE\\"+filename,"a") as fp:
#                             csvr=csv.writer(fp)
#                             csvr.writerow(  maincolnames)
#                             csvr.writerows(records)
#                             print("Successful ---Verify")
#                             break
#                     else:
#                         print("Invalid input for File name wite properly file name ")        
                
                




























#!Program for Creating CSV File Dynamically from Read the List Values from KBD
#DynamicCSVCreateEx1.py
# import csv
# noc=int(input("Enter How many Column you want: "))
# if noc<=0:
#     print("Invalid Column Name")
# else:
#     #Accept the column name
#     colnames=[]
#     for i in range(1,noc+1):
#         colname=input(f"Enter {i} column Name :")
#         colnames.append(colname)
#     else:
#           nor=int(input("Enter how Many Records u Have:"))  
#           if nor<=0:
#                print(f"{nor} Invalid number of records")
#           else:
#                records=[]     
#                for i in range(1,nor+1):
#                     print(f"Enter {i} Record :")
#                     # records.append()
#                     record=[]
#                     for j in range(len(colnames)):
#                          val=input(f"Enter Value for {colnames[j]}")
#                          record.append(val)
#                     else:
#                          records.append(record)     
#                 else:
#                     while(True):
#                         csvfilename=input("Enter file name with Extension .csv :")
#                         if csvfilename.endswith(".csv"):
#                              with open("","a") as fp:
                                  
                                  













