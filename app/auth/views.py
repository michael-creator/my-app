from flask imports Blueprint, render_template,url_for,redirect
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')
# @authh.route('/login', methods=[POST])
# def login_post():
@auth.route('/signup')
def signup(): 
    return render_template('signup.html')
@auth.route('/logout')
def logout():
    return redirect(url_for('homepage.html'))