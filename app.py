from flask import Flask , render_template , request , session , redirect , jsonify
from db import new_task, get_tasks , delete_task , update_task , get_task , get_users
app = Flask(__name__)

app.secret_key = "kjdbkjsdbkjjsldjdsbn"
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home/<username>' , methods = ['POST' , 'GET'])
def home(username):
    if username in session:
        if request.method == 'GET':
            return render_template("home.html" , tasks = get_tasks(username) , username = username , users =  get_users())
        if session[username] == request.form['password']:
            return render_template("home.html" , tasks = get_tasks(username) , username = username , users = get_users())
        else:
            return render_template("login.html" , message = "wrong password")
    else:
        session[username] = request.form['password']
        return render_template("home.html" , tasks = get_tasks(username) , username = username , users = get_users())

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

@app.route('/share/<task_id>/<username>')
def share_task(task_id , username):
    task = get_task(task_id)
    task.username = username
    new_task(task.description , task.date , task.category , task.username)
    return ""