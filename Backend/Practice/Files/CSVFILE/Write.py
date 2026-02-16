# #! Program for Creating CSV File
# import csv
# colnames=["SNO","SNAME","MARKS","COLNAME"]
# records=[
#             [100,"RS",90,"CLG"],    
#             [200,"SN",89,"ALG"],
#             [300,"TS",70,"RTS"],
#             [400,"ER",60,"AQT"],
#             ]
# with open("CSVFILE\\col.csv","a") as wp:
#     csvwr=csv.writer(wp)
#     csvwr.writerow(colnames)
#     csvwr.writerows(records)
#     print("CSV file Created---Verify")
#^----------------------------------------------------------------------------------------------------
# #! program for adding rows in CSV files
#CSVWriteEx2.py
# import csv
# records =[500,"CS",88,"KTR"]
# with open("CSVFILE\\col.csv","a") as wp:
#     csvr=csv.writer(wp)
#     # print(csvr)
#     csvr.writerow(records)
#     print("Record Added to CSV File ---Verify")  

#!      
#Program for Adding the Record to CSV File
#CSVWriteEx2.py
# import csv
# record=[106,"Rossum",9.6,"NLU"]
# with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","a") as fp:
#     csvwr=csv.writer(fp)
#     csvwr.writerow(record)
#     print("Record addded to CSV File--verity")

#^----------------------------------------------------------------------------------------------------
 # #!Program for Creating CSV File with Dict Data.
#CSVDictWriteEx1.py

# import csv # Step-1
# colnames=["TNO","NAME","SUBJECT"] # Step-2
# records=[{"TNO":1000,"NAME":"ROSSUM","SUBJECT":"PYTHON"},
#          {"TNO":2000,"NAME":"TRAVIS","SUBJECT":"NUMPY"},
#          {"TNO":3000,"NAME":"HUNTER","SUBJECT":"MATPLOTLIB"},
#          {"TNO":4000,"NAME":"DENNIS","SUBJECT":"C"},
#          {"TNO":5000,"NAME":"JGOSLING","SUBJECT":"JAVA"} ] # Step-3
# with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\teacher.csv","a") as fp: # Step-4
#      csvdwr=csv.DictWriter(fp,fieldnames=colnames) # Step-5
#      csvdwr.writeheader() # Step-6
#      csvdwr.writerows(records) # Step-7
#      print("CSV File Created with Dict Data---verify")


# import csv
# colnames=["TNO","NAME","SUBJECT"]
# records=[
#         {"TNO":100,"NAME":"harshal","SUBJECT":"python"},
#         {"TNO":200,"NAME":"paa","SUBJECT":"java"},
#         {"TNO":300,"NAME":"path","SUBJECT":"c++"},
#         {"TNO":400,"NAME":"SKV","SUBJECT":"c"},
#          ]
# with open("CSVFILE\\Dictcol.csv","a") as wp:
#     csvr=csv.DictWriter(wp,fieldnames=colnames)
#     csvr.writeheader()
#     csvr.writerows(records)
#     print("CSV file Created with dict data--verity")

#^----------------------------------------------------------------------------------------------------
#!#Program for Creating CSV File Dynamically from Read the List Values from KBD
#DynamicCSVCreateEx1.py
import csv





