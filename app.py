import functions as fun
import mysql.connector
from flask import Flask, render_template, request, redirect,flash

app = Flask(__name__)
app.secret_key = '111'
username=""

try:
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'
        )
    cur = cnx.cursor()

except mysql.connector.Error as error:
    print("Error connecting to the database:", error)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/usersignup', methods=['GET', 'POST'])
def usersignup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cnfpassword = request.form['cnfpassword']
        mail=request.form['mail']
        if fun.check_cred_user(cur,username,""):
            flash('username already taken')
            return redirect('/usersignup')
        elif fun.check_valid(password,cnfpassword):
            flash('password miss match')
            return redirect('/usersignup')
        else:
            fun.add_user(cur,username,password,mail)
            cnx.commit()
        return redirect('/userlogin')
    return render_template('usersignup.html')


@app.route('/userlogin', methods=['GET', 'POST'])
def userlogin():
    global username
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if fun.check_cred_user(cur,username,password):
                return redirect('/userdash')
        else:
            flash('invalid username or password','error')
            return redirect('/userlogin')
    else:
        username=""
        return render_template('userlogin.html')
    

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if fun.check_cred_admin(cur,name,password):
            return redirect('/admindash')
        else:
            flash('invalid username or password')
            return redirect('/adminlogin')       
    return render_template('adminlogin.html')


@app.route('/admindash',methods=['GET','POST'])
def admindash():
    
    return render_template('admindash.html')


@app.route('/addflight',methods=['GET','POST'])
def addflight():
    if request.method == 'POST':
        flightno = request.form['flightno']
        date = request.form['date']
        time = request.form['time']
        start = request.form['start']
        dest = request.form['destination']
        if fun.check_flight(cur,flightno):
            flash('flight number already taken!!')
            return redirect('/addflight')
        fun.add_flight(cur,flightno,date,time,start,dest)
        cnx.commit()
        flash('flight added successfully!!')
        return redirect('/admindash')
    return render_template('addflight.html')


@app.route('/removeflight',methods=['GET','POST'])
def removeflight():
    if request.method == 'POST':
        flightno = request.form['flightno']
        date = request.form['date']
        time = request.form['time']
        if fun.check_flight(cur,flightno):
            fun.del_flight(cur,flightno)
            cnx.commit()
            flash('flight successfully removed!!')
            return redirect('/admindash')
        else:
            flash('flight doesnot exist')
            return redirect('/removeflight')
    return render_template('removeflight.html')


@app.route('/view',methods=['GET','POST'])
def view():
    if request.method == 'POST':
        flightno = request.form['flightno']
        date = request.form['date']
        time = request.form['time']
        if fun.check_flight(cur,flightno):
            global tup
            tup=fun.view_bookings(cur,flightno)
            return redirect('/dataview')
        else:
            flash('flight doesnot exist')
            return redirect('/view')
    return render_template('view.html')


@app.route('/dataview',methods=['GET','POST'])
def display_data():
    global tup
    return render_template('dataview.html', rows=tup)


@app.route('/userdash',methods=['GET','POST'])
def userdash():
    global username
    if username=="":
        return redirect('/userlogin')
    return render_template('userdash.html')


@app.route('/search',methods=['GET','POST'])
def search():
    global username
    if request.method =='POST':
        date=request.form['date']
        dept=request.form['dept']
        dest=request.form['dest']
        nos=request.form['nos']
        global resrows
        resrows=fun.search(cur,date,dept,dest,nos)
        if not resrows:
            flash('No available flights for the given details')
            return redirect('/search')
        else:
            return redirect('/results')
    if username =="":
        return redirect('/userlogin')
    return render_template('search.html')


@app.route('/results',methods=['GET','POST'])
def display_result():
    global username
    if request.method == 'POST':
        flightno=request.form['flightno']
        nos=request.form['nos']
        fun.book_seats(cur,username,flightno,nos)
        cnx.commit()
        flash('tickets successfully booked!!')
        return redirect('/userdash')
    global resrows
    return render_template('results.html', rows=resrows)


@app.route('/mybook',methods=['GET','POST'])
def my_book():
    global username
    if not username:
        return redirect('/userlogin')
    else:
        res=fun.my_bookings(cur,username)
    return render_template('mybook.html',rows=res)


if __name__ == '__main__':
    app.run(debug=True)
