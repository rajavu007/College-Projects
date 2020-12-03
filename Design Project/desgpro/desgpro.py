from flask import Flask,render_template,request
from flask import redirect,flash,url_for

from form import Login,Register,Admin

app=Flask(__name__)
app.config['SECRET_KEY']='12345678asdfghjkl'

@app.route('/')
def home():
    return render_template('home.html',title='Home')

@app.route('/login',methods=['GET','POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        if form.email.data=="rp@gmail.com" and form.password.data=="password":
            flash("Loged in sucessfully",'sucess')
            return redirect(url_for('view'))
        else:
            flash('In correct userid or password','danger')
    return render_template('login.html',title='LOGINPAGE',asdform=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form=Register()
    if form.validate_on_submit():
        return redirect(url_for('edit'))   
    return render_template('register.html',title='REGISTERPAGE',asdform=form)

@app.route('/admin',methods=['GET','POST'])
def admin():
    form=Admin()
    if form.validate_on_submit():
        if form.userid.data=="Libraryian" and form.password.data=="password":
            flash('Admin Welcome ','sucess')
            return redirect(url_for('allbooks'))
    return render_template('adminlogin.html',title='ADMIN',asdform=form)

@app.route('/allbooks',methods=['GET','POST'])
def allbooks():
    if request.method=='POST':
        return redirect(url_for('allusers'))
    return render_template('all.html',title='DetailsOfFullBooks')

@app.route('/allusers',methods=['GET','POST'])
def allusers():
    if request.method=='POST':
        return redirect(url_for('allbooks'))
    return render_template('user.html',title='USERS DETAILS')

@app.route('/adventure',methods=['GET','POST'])
def adventure():
    return render_template('adventure.html',title='Advenuture Books')

@app.route('/view',methods=['GET','POST'])
def view():
    if request.method=='POST':
        flash('LoggedOut Sucessfully')
        return redirect(url_for('home'))
    return render_template('view.html',title='Your Details')

@app.route('/edit',methods=['GET','POST'])
def edit():
    if request.method=='POST':
        flash('Details Entered Sucessfully ! Login')
        return redirect(url_for('login'))
    return render_template('edit.html',title='Enter Your Details')

if __name__ == "__main__":
    app.run(debug=True)