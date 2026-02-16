# import csv
# with open("CSVFILE\\Employee.csv","r")as rp:
#     filedata=csv.DictReader(rp)
#     print(filedata,type(filedata)) #<csv.DictReader object at 0x000001DAFA4B0710> <class 'csv.DictReader'>
    # for record in filedata:
        # print(record)
#         for k,v in record.items():
#             print(f"{k}--->{v}")


# import csv
# with open("Employee.csv") as rp:
#     csvrd=csv.DictReader(rp)
#     # print(filedata)
#     for record in csvrd:
#         for k,v in record.items():
#             # print(val,end="\n")
#             print(f"{k}--->{v}")
#     print()        
#^----------------------------------------------------------------------------------------------------

#! Program for Reading the Data from CSV File without using csv module
#CSVDictReadEx2.py 
# import csv
# with open("Employee.csv","r") as rp:
#     recdr=csv.DictReader(rp)
#     recno=1
#     for record in recdr:
#         for k,v in record.items():
#             print(f"{k}--->{v}")



# import csv
# with open("CSVFILE\\Employee.csv","r") as rp:
#     csvrdic=csv.DictReader(rp)
#     # print(csvrdic)       #<csv.DictReader object at 0x000002698C4723F0>
#     for dictrec in csvrdic:
#         # print(dictrec)
#         for k,v in dictrec.items():
#             print(f"\t{k}--->{v}",end="")        
#         print()    


import csv
with open("CSVFILE\\Student.csv","r") as rp:
    csvdic=csv.DictReader(rp)
    for dictrec in csvdic:
        for k,v in dictrec.items():
            print(f"\t{k}--->{v}")
        print()    






















