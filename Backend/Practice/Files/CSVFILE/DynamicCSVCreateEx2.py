# #Program for Creating CSV File Dynamically by reading the Dict of List Values from KBD
# #DynamicCSVCreateEx2.py
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
#                 record= {} # for adding Record value in the form Dict
#                 for j in range(len(colnames)):
#                     val=input("Enter Value for {}:".format(colnames[j]))
#                     record[colnames[j]]=val # Adding (Key,value) to dict obj
#                 else:
#                     records.append(record) # Adding Dict object to List
#             else:
#                 while(True):
#                     csvfilename=input("Enter CSV File Name with an extension .csv:")
#                     if(csvfilename.endswith(".csv")):
#                         with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\"+csvfilename,"a") as fp:
#                             csvdwr=csv.DictWriter(fp,fieldnames=colnames)
#                             csvdwr.writeheader()
#                             csvdwr.writerows(records)
#                             print("CSV File Created and Records Saved Dynamically-Verify")
#                             break
#                     else:
#                         print("Invalid CSV File Name-try Again")




#Program for Creating CSV File Dynamically by reading the Dict of List Values from KBD
#DynamicCSVCreateEx2.py
import csv
#Take Column Names--Step-1
noc=int(input("Enter How Many Columns u Have:"))
if(noc<=0):
    print("Invaid input plaese try again ")
else:
    colname=[]    
    for i in range(1,noc+1):
        val=input(f"Enter {i} COl name :")
        colname.append(val)
# print(colname)
    else:
        nor=int(input("Enter How many Row U have to Enter "))
        if nor<=0:
            print("Invalid input please try---Again")
        else:
            Main_record=[]    
            for i in range(1,nor+1):
                print(f"Enter {i} records :")
                print("-"*50)
                records={}
                for k in range(len(colname)):
                    val=input(f"Enter {colname[k]}: ")
                    # records.append(record)
                    records[colname[k]]=val
                else:
                    Main_record.append(records)    
# print(Main_record)                    
            else:
                while(True):
                    filename=input("Enter File Name here :")    
                    if filename.endswith(".csv"):
                        with open(filename,"w") as wp:
                            csvdwr=csv.DictWriter(wp,fieldnames=colname)
                            csvdwr.writeheader()
                            csvdwr.writerows(Main_record)
                            print("CSV File Created and Records Saved Dynamically-Verify")
                            break
                    else:
                        print("Invalid CSV file Try again")    



                    