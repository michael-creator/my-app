from flask import Flask, render_template

app = Flask(__name__)

post = [{
    'author': 'nill blake',
    'title':'Example of pitches',
    'content': 'contents',
    'date': 'jan 17 2010'
},
{
    'author': 'booterkn boika',
    'title': 'Usefull pitches',
    'content': 'contents',
    'date': 'jan 17 2010'
  
},
{
    'author': 'boot camp',
    'title': 'short pitches',
    'content': 'contents',
    'date': 'jan 17 2010'
  
}
]
@app.route('/')
def home():
    return render_template("home.html",post=post)


@app.route('/about')
def about():
    return render_template("about.html",post=post)


if __name__ == '__main__':
    app.run(debug = True)