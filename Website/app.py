from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__) 


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


if __name__ == "__main__": 

    app.run(debug=True)