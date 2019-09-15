import pymysql
import threading
b = 0
flag = 0
db = pymysql.connect("localhost","root","","databasename" )
cursor = db.cursor()
def thread_1():
    global flag
    global b
    while(True):
        if (flag == 0): 
            a = input("nhap x:")    
            if (a == "exit"):
                flag = 3
                break
            else:
                b = int(a)
                flag = 1;
        if (flag == 4):
            sql = """INSERT INTO ngay3(x)
                        VALUES ('%d')""" %(b)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
            print("da them x = " + a + " vao bang")
            flag = 0

def thread_2():
    global b
    global flag
    while (True):
        if (flag == 3):
            break
        if (flag == 1):
            sql = """ select x from ngay3
            where x = '%d' """ %(b)
            try:
                # Execute the SQL command
                cursor.execute(sql)
                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                #x = None
                #for row in results:
                #    x = row[0]
                if (len(results) != 0):
                    print("da ton tai trong bang")
                else:
                    print("x chua ton tai trong bang")
            except:
                print ("Error: unable to fetch data")
            flag = 4

thread1 = threading.Thread(target=thread_1)
thread2 = threading.Thread(target=thread_2)
thread1.start()
thread2.start()