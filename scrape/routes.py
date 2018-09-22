from flask import Flask, redirect, request, render_template, url_for
from server import app



@app.route('/', methods=['GET', 'POST'])
def homePage():
	return render_template('base.html')