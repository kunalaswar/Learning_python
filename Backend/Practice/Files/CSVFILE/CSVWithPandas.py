
# import pandas as pd
# df=pd.read_csv("Employee.csv")
# print(df)


# import pandas as pd
# df=pd.read_csv("Student.csv")
# print(df[df["MARKS"]>3][["NAME","MARKS"]])
# print("---------------------------------------")
# print(df[df["MARKS"]<3][["NAME","MARKS"]])


import pandas as pd
df=pd.read_csv("Student.csv")
print(df[df["MARKS"]>3][["NAME","MARKS"]])
print("---------------------------------------")
print(df[df["MARKS"]<3][["NAME","MARKS"]])
