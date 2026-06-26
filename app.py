import json
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__) # instantiates the Flask application
app.secret_key = "tem_key"

def load_user():
    with open("user.json", "r") as file:
        return json.load(file)

@app.route('/')
def home():
    if "logged_in" not in session:
        return redirect(url_for("login"))
    return render_template('index.html')

@app.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == "POST":
        saved_user = load_user()
        username = request.form["username"]
        password = request.form["password"]
        if username == saved_user["username"] and password == saved_user["password"]:
            session["logged_in"] = True
            return redirect(url_for("home"))
        
        return "Login Fail!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)