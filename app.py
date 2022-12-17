from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='python'

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        fm=request.form
        a=fm['sname']
        b=fm['semail']
        c=fm['scontact']
        d=fm['sdob']
        cursor=mysql.connection.cursor()
        q="insert into student(name,email,contact,dob) values('"+a+"','"+b+"','"+c+"','"+d+"')"
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/show')
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show')
def show():
    cursor=mysql.connection.cursor()
    q="select * from student"
    res=cursor.execute(q)
    if res>0:
        details=cursor.fetchall()
        return render_template('show.html',det=details)    
    else:
        return render_template('show.html')

@app.route('/delete/<string:did>')
def delete(did):
    cursor=mysql.connection.cursor()
    q="delete from student where id='"+did+"'"
    cursor.execute(q)
    mysql.connection.commit()
    return redirect('/show')

@app.route('/edit/<string:eid>')
def edit(eid):
    cursor=mysql.connection.cursor()
    q="select * from student where id='"+eid+"'"
    res=cursor.execute(q)
    if res>0:
        details=cursor.fetchall()
        return render_template('edit.html',det=details)    
    
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        fm=request.form
        e=fm['editid']
        a=fm['sname']
        b=fm['semail']
        c=fm['scontact']
        d=fm['sdob']
        cursor=mysql.connection.cursor()
        q="update student set name='"+a+"',email='"+b+"',contact='"+c+"',dob='"+d+"' where id='"+e+"'"
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/show')

app.run(debug=True)