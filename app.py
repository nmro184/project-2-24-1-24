from flask import Flask , render_template , request , session , redirect , jsonify
from db import new_task, get_tasks , delete_task , update_task , get_task
app = Flask(__name__)

app.secret_key = "kjdbkjsdbkjjsldjdsbn"
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home/<username>' , methods = ['POST' , 'GET'])
def home(username):
    get_task(2)
    if username not in session:
        session[username] = username
    return render_template("home.html" , tasks = get_tasks(username) , username = username)

@app.route('/create/<username>' , methods = ['POST' , 'GET'])
def create(username):
    new_task(description = request.form['description'] , date = request.form['date'] , category =request.form['category'] , username = username)
    return redirect (f"/home/{username}")

@app.route('/delete/<username>' , methods = ['POST'])
def delete(username):
    delete_task(request.form['deleteid'] , username)
    return redirect(f'/home/{username}')

@app.route('/update/<username>' , methods = ['POST'])
def update(username):
    update_task(new_description= request.form['description'] , new_date= request.form['date'] , new_category= request.form['category'] , updateid= request.form['updateid'] , username = username)
    return redirect(f'/home/{username}')

@app.route('/api/task/<task_id>')
def get_task_api(task_id):
    task = get_task(task_id)
    return jsonify(task.to_dict())