from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import time

app = Flask(__name__) 

DB = "user.db" 
DB2 = "messages.db"
 
def init_db(): 
    conn = sqlite3.connect(DB) 
    conn.execute("""CREATE TABLE IF NOT EXISTS users ( 
                        id INTEGER PRIMARY KEY, 
                        name TEXT NOT NULL, 
                        email TEXT NOT NULL, 
                        password TEXT NOT NULL)""") 
    conn.commit() 
    conn.close() 

init_db() 

def init_db2(): 
    conn = sqlite3.connect(DB2) 
    conn.execute("""CREATE TABLE IF NOT EXISTS messages ( 
                        id INTEGER PRIMARY KEY, 
                        name TEXT NOT NULL,  
                        message TEXT NOT NULL,
                        posted_at NOT NULL)""") 
    conn.commit() 
    conn.close() 

init_db2() 


def get_db(): 
    conn = sqlite3.connect(DB) 
    conn.row_factory = sqlite3.Row 
    return conn


def get_db2(): 
    conn = sqlite3.connect(DB2) 
    conn.row_factory = sqlite3.Row 
    return conn


@app.route("/") 
def index(): 
    return render_template("index.html") 


@app.route("/learn") 
def learn(): 
    return render_template("learn.html") 


@app.route("/about") 
def about(): 
    return render_template("about.html") 


@app.route("/form") 
def form(): 
    return render_template("form.html") 


@app.route("/form_post", methods=["POST"]) 
def form_post(): 
    name = request.form["Uname"].strip()
    email = request.form["email"].strip()
    password = request.form["Password"].strip()
    conn = get_db()
    conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()
    return redirect("form")


@app.route("/message_post", methods=["POST"]) 
def message_post(): 
    name = request.form["Name"].strip()
    message = request.form["Message"].strip()
    conn = get_db2()
    posted_at = time.strftime("%Y-%m-%d %H:%M")
    conn.execute("INSERT INTO messages (name, message, posted_at) VALUES (?, ?, ?)", (name, message, posted_at))
    conn.commit()
    conn.close()
    return redirect("contact")



@app.route("/contact") 
def contact(): 
    conn = get_db2() 
    messages = conn.execute("SELECT * FROM messages ORDER BY id DESC").fetchall() 
    conn.close() 
    return render_template("contact.html", messages=messages) 


if __name__ == "__main__": 

    app.run(debug=True)