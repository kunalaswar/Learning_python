# import csv
# with open("D:\\PYTHON FULL STACK\\Practice\\CSVFILE\\Student.csv","r") as rp:
#     csvr=csv.reader(rp)
#     print(csvr)
#     for record in csvr:
#         # print(record,type(record))
#         for val in record:
#             print(val)
#     print()    
    

# import csv
# with open("Student.csv","r") as rp:
#     csvr=csv.reader(rp)    
#     # print(csvr)  #<_csv.reader object at 0x0000024CF8D3E7A0>
#     for record in csvr:
#         # print(record)
#         for val in record:
#             print(val,end="\n")
#     # print()        


# import csv
# with open("Employee.csv","r") as rp:
#     csvr=csv.reader(rp)
#     for record in csvr:
#         for val in record:
#             print(val)


# import csv
# with open("CSVFILE\\Student.csv","r") as rp:
#     csvr=csv.reader(rp)
#     for dictrec in csvr:
#         print(dictrec,"\t")
#         for val in dictrec:
#             print(val)

#Program for Reading the Data from CSV File without using csv module
#CSVReadEx1.py
# import csv
# with open("CSVFILE\\Employee.csv","r") as fp:
#     csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
#     for record in csvr: # here record is an object of <class, list>
#         for val in record:
#             print("\t{}".format(val),end="\t")
#         print()


# import csv
# with open("CSVFILE\\Student.csv","r") as rp:
#     csvr=csv.reader(rp)
#     for record in csvr:
#         # print(record)
#         for val in record:
#             print(val,"\t")
#         # print()    


# import csv
# with open("CSVFILE\\Students.csv","r") as rp:
#     csvr=csv.reader(rp)
#     for record in csvr:
#         # print(record)
#         for val in record:
#             print("\t{}".format(val),end="\t")
#         print()

#Program for Reading the Data from CSV File without using csv module
#CSVReadEx1.py
# import csv
# with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","r") as fp:
#     csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
#     for record in csvr: # here record is an object of <class, list>
#         for val in record:
#             print("\t{}".format(val),end="\t")
#         print()


# import csv
# with open("CSVFILE\\Employee.csv","r") as rp:
#     csvr=csv.reader(rp) 
#     for record in csvr:
#         # print(record)
#         for val in record:
#             print(f"\t{val} ",end="\t")
#         print()
















