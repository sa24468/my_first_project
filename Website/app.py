from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__) 

DB = "user.db" 

 
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


@app.route("/contact") 
def contact(): 
    return render_template("contact.html") 


@app.route("/form_post", methods=["POST"]) 
def form_post(): 
    name = request.form["Uname"] 
    email = request.form["email"] 
    password = request.form["Password"] 
    print(email)
    print(name)  
    print(password)
    return redirect("form")


if __name__ == "__main__": 

    app.run(debug=True)