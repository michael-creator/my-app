from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

post = [{
    'author': 'nill blake',
    'title':'Example of pitches',
    'content': 'contents',
    'date':'jan 17 2010'
}
]
@app.route('/')
def home():
    return render_template("homepage.html",post=post)
@app.route('/homepage')
def homepage():
    return render_template("pitches.html",post=post)
@app.route('/pitches')
def pitches():
    return render_template("pitches.html",post=post)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.method == 'POST'
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        print('# form = UserCreationForm()')
    return render_template( 'signup.html')
if __name__ == '__main__':
    app.run(debug = True)