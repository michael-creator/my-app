from flask import render_template
from app import app

# Views
@app.route('/myapp/<myapp_id>')
def myapp(myapp_id):

    '''
    View myapp page function that returns the myapp details page and its data
    '''
    return render_template('myapp.html',id = myapp_id)