import os
import pymongo
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DBNAME = os.getenv('DB_NAME')

app = Flask(__name__)

connection = pymongo.MongoClient(MONGO_URI)
db = connection[MONGO_DBNAME]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        return redirect(url_for('show_tasks'))
    return render_template('login.html')


@app.route('/')
def show_tasks():
    all_tasks = db.tasks.find({})
    return render_template('tasks.html', tasks=all_tasks)

@app.route('/create')
def create_task_page():
    return render_template('create_task.html')

@app.route('/add', methods=['POST'])
def add_task():
    new_task = {
        "user_id": request.form.get('user_id'),
        "task_title": request.form.get('task_title'),
        "date": request.form.get('date'),
        "reminder_frequency": request.form.get('reminder_frequency')
    }
    db.tasks.insert_one(new_task)
    return redirect(url_for('show_tasks'))


@app.route('/update/<task_id>', methods=['POST'])
def update_task(task_id):
    updated_data = {
        "user_id": request.form.get('user_id'),
        "task_title": request.form.get('task_title'),
        "date": request.form.get('date'),
        "reminder_frequency": request.form.get('reminder_frequency')
    }
    db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": updated_data})
    return redirect(url_for('show_tasks'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    db.tasks.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for('show_tasks'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)