from flask import Flask,render_template,redirect,url_for,flash,request
from flask_mysqldb import MySQL
from asdforms import Register,Login,Admin

app=Flask(__name__)
app.config['SECRET_KEY']='12345678asdfgh'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQl_DB']='asdlab'

mysql=MySQL(app)
SNo=0
Sno=0

@app.route('/',methods=['GET','POST'])
def login():
    cur = mysql.connection.cursor()
    data=[]
    asdform=Login()
    if asdform.validate_on_submit():
        email=asdform.email.data
        password=asdform.password.data
        query='SELECT * FROM asdlab.login WHERE email=%s AND pass_word=%s'
        cur.execute(query,(email,password))
        data=cur.fetchone()
        if data:
            global Sno
            Sno=data[0]
            flash("LoggedIn Iucessfully",'sucess')
            return redirect(url_for('view'))
        else:
            flash('Incorrect Email or Password','danger')
        cur.close()
    return render_template('asdlogin.html',title='LOGINPAGE',asdform=asdform)

@app.route('/registerpage',methods=['GET','POST'])
def register():
    
    asdform=Register()
    if asdform.validate_on_submit():#used to check the registration is sucessfull not
       email=asdform.email.data
       password=asdform.password.data
       cur= mysql.connection.cursor()
       query='INSERT INTO asdlab.login(email,pass_word) VALUES (%s,%s)'
       cur.execute(query,(email,password))
       mysql.connection.commit()
       query='SELECT sno FROM asdlab.login WHERE email=%s AND pass_word=%s'
       cur.execute(query,(email,password))
       data=cur.fetchone()
       global SNo
       SNo=data[0]
       cur.close()
       flash('Account Created Enter your details','sucess')
       return redirect(url_for('edit'))
    return render_template('asdregister.html',title='REGISTERPAGE',asdform=asdform)


@app.route('/admin',methods=['GET','POST'])
def admin():
    asdform=Admin()
    if asdform.validate_on_submit():#used to check the registration is sucessfull not
        if asdform.userid.data=="admin123" and asdform.password.data=="password":
            flash('WELCOME ','sucess')
            return redirect(url_for('all'))
    return render_template('adminlogin.html',title='ADMIN',asdform=asdform)

@app.route('/view',methods=['GET','POST'])
def view():
    
    cur = mysql.connection.cursor()
    data=[]
    query='SELECT * FROM asdlab.login WHERE sno=%s'
    cur.execute(query,(Sno,))
    data=cur.fetchone()
    global SNo
    SNo=Sno
    cur.close()
    if request.method=='POST':
        flash('You Can Edit Your Details')
        return redirect(url_for('sedit'))
    return render_template('asdview.html',title='VIEW',form=data)

@app.route('/edit',methods=['GET','POST'])
def edit():
    cur= mysql.connection.cursor()
    if request.method=='POST':
        sregno=request.form.get('stdregno')
        sname=request.form.get('stdname')
        spname=request.form.get('stdpname')
        sage=request.form.get('stdage')
        sdob=request.form.get('stddob')
        sdept=request.form.get('stddept')
        ssem=request.form.get('stdpresem')
        savggpa=request.form.get('stdavgpa')
        spho=request.form.get('stdphone')
        sadd=request.form.get('stdaddres')
        scity=request.form.get('stdcity')
        sstate=request.form.get('stdstate')
        spin=request.form.get('stdpin')

        query='UPDATE asdlab.login SET regno=%s,name=%s,pname=%s,age=%s,DOB=%s,depat=%s,psem=%s,avggpa=%s,pnum=%s,addr=%s,city=%s,state=%s,PIN=%s WHERE sno=%s'
        cur.execute(query,(sregno,sname,spname,sage,sdob,sdept,ssem,savggpa,spho,sadd,scity,sstate,spin,SNo))
        mysql.connection.commit()
        cur.close()

        flash('Details have been Saved')
        return redirect(url_for('login'))
    return render_template('asdedit.html',title='EDIT')

@app.route('/sedit',methods=['GET','POST'])
def sedit():
    cur= mysql.connection.cursor()
    data=[]
    query='SELECT * FROM asdlab.login WHERE sno=%s'
    cur.execute(query,(Sno,))
    data=cur.fetchone()
    if request.method=='POST':
        sregno=request.form.get('stdregno')
        sname=request.form.get('stdname')
        spname=request.form.get('stdpname')
        sage=request.form.get('stdage')
        sdob=request.form.get('stddob')
        sdept=request.form.get('stddept')
        ssem=request.form.get('stdpresem')
        savggpa=request.form.get('stdavgpa')
        sadd=request.form.get('stdaddres')
        scity=request.form.get('stdcity')
        sstate=request.form.get('stdstate')
        spin=request.form.get('stdpin')

        query='UPDATE asdlab.login SET regno=%s,name=%s,pname=%s,age=%s,DOB=%s,depat=%s,psem=%s,avggpa=%s,addr=%s,city=%s,state=%s,PIN=%s WHERE sno=%s'
        cur.execute(query,(sregno,sname,spname,sage,sdob,sdept,ssem,savggpa,sadd,scity,sstate,spin,SNo))
        mysql.connection.commit()
        cur.close()

        flash('Details have been Saved')
        return redirect(url_for('login'))
    cur.close()
    return render_template('sedit.html',title='EDIT',form=data)

@app.route('/all',methods=['GET','POST'])
def all():
    cur=mysql.connection.cursor()
    data=[]
    query='SELECT * FROM asdlab.login'
    cur.execute(query)
    data=cur.fetchall()
    sregno=request.form.get('stdregno')
    if request.method=='POST':
        query2='DELETE FROM asdlab.login WHERE regno=%s'
        cur.execute(query2,(sregno,))
        mysql.connection.commit()
        return redirect(url_for('all'))
    cur.close()
    return render_template('adminview.html',title='Full Details',forms=data)

if __name__ == "__main__":
    app.run(debug=True)
