import pandas as pd
import numpy
from pandas import ExcelWriter
from pandas import ExcelFile
import MySQLdb

def create_table():
	df = pd.read_excel('w.xlsx', sheetname='Sheet1')
	l=[]
	for x in  df.columns:
		l.append(x)
	
	
	con=MySQLdb.connect("localhost","root","root","ifet")
   	obj=con.cursor() 
	table_name = "table_name"
	createsqltable = "CREATE TABLE IF NOT EXISTS "  + table_name + " (" + " varchar(250),".join(l) + " varchar(250))"
	print createsqltable
	obj.execute(createsqltable)
	con.commit()
def insert_table():
	df = pd.read_excel('w.xlsx', sheetname='Sheet1')
	l=[]
	ll=[]
	con=MySQLdb.connect("localhost","root","root","ifet")
   	obj=con.cursor() 
	for x in  df.columns:
		l.append(x)
	
	values = df.values
	for x in values:
		ll.append(x)
	table_name = "table_name"
   	e="'%s',"*len(l)
	e=e[0:len(e)-1]
	y=" VALUES("+e+")"
	for x in ll:
		q=tuple(x)
		ta="INSERT INTO "  + table_name + " (" + ", ".join(l) + ")" +y %(q)
		obj.execute(ta)
		con.commit()
if __name__=="__main__":
	create_table()
	insert_table()