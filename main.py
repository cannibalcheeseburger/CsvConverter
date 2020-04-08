import sqlite3
import pandas as pd

dbname = input("Enter name of Database:")
conn = sqlite3.connect("./DBS"+dbname+".db")
c = conn.cursor()

path = input("Enter name of file:")
df = pd.read_csv("./csv/"+path,index_col = [0])

columns = df.columns



for i in range(len(columns)):
    if " " in columns[i]:
        columns[i] = columns[i].replace(" ","_")

types =[]
table = input("Enter name of table:")
for i in df.dtypes:
    if "int" in str(i):
        types.append("INTEGER")

    elif "float" in str(i):
        types.append("REAL")

    else :   
        types.append("TEXT")
        
execute_create ="CREATE TABLE "+ table + " ("

for i in range(len(types)-1):
    execute_create = execute_create + columns[i]+" " +types[i]+","



execute_create = execute_create+ columns[len(types)-1]+" "+types[len(types)-1]+")"
print(execute_create)
c.execute(execute_create)
conn.commit()

execute = "INSERT INTO "+table +" VALUES ("
for index,row in df.iterrows():
    execute_insert = execute
    for i in range(len(columns)-1):
        if types[i] == "TEXT":
            execute_insert = execute_insert + "'" + str(row[columns[i]].replace("'","`"))+"',"
        else:
            execute_insert = execute_insert +str(row[columns[i]])+","
    execute_insert = execute_insert + str(row[columns[len(columns)-1]])+")"
    print(execute_insert)
    #c.execute(execute_insert)    
    #conn.commit()    

c.close()
conn.close()