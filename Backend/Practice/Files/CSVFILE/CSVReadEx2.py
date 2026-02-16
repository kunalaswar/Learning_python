# import csv
# with open("Employee.csv","r") as rp:
#     csrv=csv.reader(rp)
#     for record in csrv:
#         for val in record:
#             print(val)


import csv
with open("Employee.csv","r") as rp:
    csvr=csv.reader(rp)
    for record in csvr:
        for val in record:
            print(val)
    print()