from flask import Flask, render_template, send_from_directory
from data import gallery

app = Flask(__name__)

my_works = gallery()
@app.route('/')

def index():

	return render_template('home.html')

@app.route('/gallery')

def gallery():

	# works here points out to te variable that is equal gallery() function
	
	return render_template('gallery.html', works = my_works) 

@app.route('/about')

def about():

	return render_template('about.html')

@app.route('/work/<string:id>')
def work(id):

	return render_template('work.html', id = id)

if __name__=='__main__':

	app.run(debug=True)