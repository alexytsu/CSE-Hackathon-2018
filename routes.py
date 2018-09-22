from flask import Flask, redirect, request, render_template, url_for
from server import app
from scrape.parse import get_all_prequisites, convert_names_to_courses, Timetable


tt = Timetable()

@app.route('/', methods=['GET', 'POST'])
def homePage():
	if request.method == 'POST':
		course = request.form['search_course']
		prereqs = get_all_prequisites(course)
		prereqs = convert_names_to_courses(prereqs)

		prereqselected = None
		try:
			prereqselected = request.form["prereq"]
			prereqselected = convert_names_to_courses([prereqselected])[0]
		except Exception:
			prereqselected = None

		try:
			tablesubmitted = request.form["clicked_table"]
			slot = request.form["slot"]
			year = int(int(slot)/10)
			trim = (int(slot) % 10 ) % 3 
			print("year, ", year, "trim ", trim)
			prereqselected = request.form["prereqselected"]
			tt.set_course(prereqselected, year, trim)
		except Exception:
			tablesubmitted = None

		return render_template('home.html', tt=tt, tablesubmitted=tablesubmitted, prereqselected=prereqselected, course=course, prereqList=prereqs, search=True, timetable=tt)
	return render_template('home.html')

