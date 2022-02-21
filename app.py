import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_job(job_id):
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?',
                        (job_id,)).fetchone()
    conn.close()
    if job is None:
        abort(404)
    return job

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/<int:job_id>')
def job(job_id):
    job = get_job(job_id)
    return render_template('job.html', job=job)