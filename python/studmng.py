#MENUDRIVEN PROGRAMM WITH MYSQL

import pymysql
import sys
myConnection = pymysql.connect( host="localhost", user="root", passwd="root", db="studmng" )
#if myConnection:
#	print "Connection successfully..."

cursor1 = myConnection.cursor()

def insert():

	stud_name = raw_input("\n\tEnter student name :: \n\t => ")
	stud_std = raw_input("\n\tEnter studnet standard (only digit allow) :: \n\t => ")
	
	#args = (stud_name, stud_std)

	query = " INSERT INTO stud(sname,sstd) VALUES(%s,%s)"	
	cursor1.execute(query,[(stud_name),(stud_std),])
	myConnection.commit()
	print "\n---------------RECORD WAS SUCCESSFULLY INSERTED--------------------\n"	
	view()
	

def update():
	view()

	stud_id = raw_input("\n\tEnter student id (only digit allow) :: \n\t => ")
	stud_name = raw_input("\n\tENTER UPDATE student name :: \n\t => ")
	stud_std = raw_input("\n\tENTER UPDATE studnet standard (only digit allow) :: \n\t => ")
	
	#args = (stud_name, stud_std)

	query = "UPDATE stud SET sname = %s, sstd = %s WHERE sid = %s"	
	cursor1.execute(query,[(stud_name),(stud_std),(stud_id),])
	myConnection.commit()
	print "\n---------------RECORD WAS SUCCESSFULLY UPDATED--------------------\n"	
	view()


def delete():
	view()
	
	stud_id = raw_input("\n\tEnter student id (only digit allow):: \n\t => ")
	
	#args = (stud_name, stud_std)

	query = "DELETE FROM stud WHERE sid = %s"	
	cursor1.execute(query,[(stud_id),])
	myConnection.commit()
	print "\n---------------RECORD WAS SUCCESSFULLY DELETED--------------------\n"	
	view()



def search():
	print "\n"
	
	stud_id = raw_input("\n\tEnter student name :: \n\t => ")
	#args = (stud_name, stud_std)

	query = " select * from stud WHERE sname = %s"	
	res = cursor1.execute(query,[(stud_id),])
	row = cursor1.fetchone()
	while row is not None:
    		print "\t",row
    		row = cursor1.fetchone()
	print "\n-----------------THANK YOU HAVE A NICE DAY-----------------------\n"	
	print "\n-----------------------------END----------------------------------\n"



def view():
	print "\n"
	
	
	#args = (stud_name, stud_std)

	query = " select * from stud"	
	res = cursor1.execute(query)
	row = cursor1.fetchone()
	print "\tSID  NAME  STD\n"
	while row is not None:
    		print "\t",row
    		row = cursor1.fetchone()
	print "\n-----------------THANK YOU HAVE A NICE DAY------------------------"	
	print "\n-----------------------------END----------------------------------\n"
	


def data():
	
	print "\n"
		
	#args = (stud_name, stud_std)

	query = " select * from stud"	
	res = cursor1.execute(query)
	row = cursor1.fetchone()
	
	stud_data = open("studdata.txt","wa+")
		
	stud_data.write("========STUDENT INFORMATION========\n\nSID  NAME  STD\n")

	while row is not None:
    		stud_data.write('\t\t\n'+str(row)+'\t')
    		row = cursor1.fetchone()

	stud_data.write("\n\n========END STUDENT INFORMATION========\n")
	stud_data.close()


	
	



print "\n--------------------------START MENU-------------------------------\n"
print "\tWELCOME TO THE SCHOOL MANAGEMENT SYSTEM\n"
print "\tSELECT 1 FOR :: INSERT A NEW STUDENT :: "
print "\tSELECT 2 FOR :: VIEWS ALL STUDENTS :: "
print "\tSELECT 3 FOR :: UPDATE STUDENT INFORMATION :: "
print "\tSELECT 4 FOR :: DELETE STUDENT INFORMATION :: "
print "\tSELECT 5 FOR :: SEARCH STUDENT INFORMATION :: "
print "\tSELECT 6 FOR :: GENARATE ALL STUDENT INFORMATION FILE :: "
print "\tENTER ANY KEY TO EXIT :: "
print "\n--------------------------END MENU-------------------------------\n"
choice = raw_input("\tCHOOSE ANY ONE OPTION :: => ")



if choice == "1":
	insert()
elif choice == "2":
	view()
elif choice == "3":
	update()
elif choice == "4":
	delete()
elif choice == "5":
	search()
elif choice == "6":
	data()
else:
	print "\n-----------------THANK YOU HAVE A NICE DAY------------------"
	print "\n--------------------------END-------------------------------\n"
	sys.exit()







