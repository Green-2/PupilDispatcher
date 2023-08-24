from flask import Flask, request

from variables import *

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/addpupil', methods=['POST'])
def addpupil():
    if request.method == 'POST':
        name = request.form['name']
        pupil_list.append(name)

    else:
        return "Error: Not a POST request", 400


@app.route('/addmatch', methods=['POST'])
def addmatch():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        pupil_mustmatch[name1] = name2

    else:
        return "Error: Not a POST request", 400


@app.route('/addseparation', methods=['POST'])
def addseparation():
    if request.method == 'POST' and request.form['name1'] != request.form['name2'] and request.form['name1'] in pupil_list and request.form['name2'] in pupil_list and request.form['name1'] not in pupil_mustmatch and request.form['name2'] not in pupil_mustmatch:
        name1 = request.form['name1']
        name2 = request.form['name2']
        pupil_separated[name1] = name2

    else:
        return "Error: Not a POST request", 400
