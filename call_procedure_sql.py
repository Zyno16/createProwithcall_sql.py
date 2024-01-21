import mysql.connector
try:
    conn = mysql.connector.connect(
        
        host ="localhost",
        user ="userpython",
        passwd = "123456",
        database ="arabicinfo"
        )
    cur =conn.cursor()
    
    cur.callproc("all_emp")
    sr = cur.stored_results()
    r =""
    for x in sr: r = x.fetchall()

    for z in r:
        print(z)

except mysql.connector.Error as e:
    print(e)
                
   
