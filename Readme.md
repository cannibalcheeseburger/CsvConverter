# CSV to SQLite DB convertor

Not good enough code to convert csv files into SQLite databases.
Might work but most likely won't. It was made to understand sqlite3 library.


## Installation 
----
Installing dependencies:
```
python -m pip install -r requirements.txt
```

To run :
```
python main.py
```

## How to use:
---
Place your csv file in /csv folder then run main.py .  

 - Enter Name of Database(without extension) you want to create. 

 - Then name of csv file(without extension) you want to convert.

 - Then the name of table you want to insert values in

## Example
---
```
Enter name of Database:example
Enter name of csv file:ccsv
Enter name of table:yas
```
## OUTPUT
---
The database will be created in /DBs folder.