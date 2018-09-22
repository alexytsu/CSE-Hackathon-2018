from flask import Flask, redirect, request, render_template, url_for
from server import app
from scrape.parse import get_all_prequisites, convert_names_to_courses, Timetable


tt = Timetable()

@app.route('/', methods=['GET', 'POST'])
def homePage():
	if request.method == 'POST':
		if 'reset' in request.form:
			return render_template('home.html')
		course = request.form['search_course']
		prereqs = get_all_prequisites(course)
		prereqs = convert_names_to_courses(prereqs)

		## update tt

		return render_template('home.html', course=course, prereqList=prereqs, search=True, timetable=tt)
	return render_template('home.html')

