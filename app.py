from flask import Flask , render_template , request
from db import new_task, get_tasks , delete_task , search_tasks
app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html" , tasks = get_tasks())

@app.route('/create')
def create():
    new_task(description = request.args['description'] , date = request.args['date'] , category =request.args['category'])
    return home()

@app.route('/search' ,methods = ['POST'])
def search():
    return render_template("home.html", tasks = search_tasks(request.form['search']))

@app.route('/delete' , methods = ['POST' , 'GET'])
def delete():
    delete_task(request.form['deleteid'])
    return home()

