def check_cred_user(cur,username,password):
    if password:
        query = "SELECT * FROM userdetails WHERE username = %s AND password = %s"
        values = (username, password)
        cur.execute(query, values)
        result = cur.fetchone()
        if result:
            return True
        else:
            return False
    else:
        query = "SELECT * FROM userdetails WHERE username = %s"
        values = (username,)
        cur.execute(query, values)
        result = cur.fetchone()
        if result:
            return True
        else:
            return False


def check_cred_admin(cur,username,password):
    query = "SELECT * FROM admindetails WHERE username = %s AND password = %s"
    values = (username, password)
    cur.execute(query, values)
    result = cur.fetchone()
    if result:
        return True
    else:
        return False


def check_valid(password,cnfpassword):
    if password==cnfpassword:
        return 0
    else:
        return 1


def add_user(cur,username,password,email):
    query="INSERT INTO userdetails values(%s,%s,%s)"
    values=(username,password,email)
    cur.execute(query,values)


def check_flight(cur,flino):
    query = "SELECT * FROM flightdetails WHERE flightno = %s"
    values = (flino,)
    cur.execute(query, values)
    result = cur.fetchone()
    if result:
        return True
    else:
        return False


def add_flight(cur,flino,date,time,st,dest):
    query="INSERT INTO flightdetails values(%s,%s,%s,%s,%s,60)"
    values=(flino,date,time,st,dest)
    cur.execute(query,values)


def del_flight(cur,flino):
    query="DELETE FROM flightdetails WHERE flightno= %s"
    values=(flino,)
    cur.execute(query,values)
    query="DELETE FROM bookings WHERE flightno= %s"
    values=(flino,)
    cur.execute(query,values)


def view_bookings(cur,flightno):
    cur.execute('SELECT username,flightno,date,time,start,destination from bookings natural join flightdetails where flightno = %s',(flightno,))
    rows = cur.fetchall()
    return rows


def search(cur,date,dept,dest,nos):
    query='SELECT * from flightdetails where date=%s and start=%s and destination=%s and availableseats >= %s'
    values=(date,dept,dest,nos)
    cur.execute(query,values)
    rows=cur.fetchall()
    return rows


def book_seats(cur,username,flightno,nos):
    query="INSERT INTO bookings values(%s,%s)"
    values=(username,flightno)
    for i in range(int(nos)):
        cur.execute(query,values)


def my_bookings(cur,uname):
    cur.execute('SELECT flightno,date,time,start,destination from bookings natural join flightdetails where username = %s',(uname,))
    rows=cur.fetchall()
    return rows