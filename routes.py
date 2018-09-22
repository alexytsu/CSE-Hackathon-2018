from flask import Flask, redirect, request, render_template, url_for
from server import app
from scrape.parse import get_all_prequisites

@app.route('/', methods=['GET', 'POST'])
def homePage():
	if request.method == 'POST':
		course = request.form['search_course']
		print("Course:" ,course)
		prereqs = get_all_prequisites(course)
		print(prereqs)

	return render_template('home.html')

