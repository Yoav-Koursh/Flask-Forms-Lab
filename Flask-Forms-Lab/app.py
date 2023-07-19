from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


usernames_and_passwords= {"a":"123","b":"456"}
facebook_friends=["yoav","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		usercheck = request.form["username"]
		passwordcheck = request.form["password"]
		if usernames_and_passwords[usercheck] == passwordcheck:
			return redirect(url_for('home'))
	return render_template('login.html')

	
@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html', freindslist= facebook_friends)


@app.route('/friends_exists/<string:name>')
def freinds(name):
	return render_template('friend_exists.html', n = name, freindslist=facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)