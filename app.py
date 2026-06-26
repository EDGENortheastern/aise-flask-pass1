import json
from flask import Flask, render_template, request

app = Flask(__name__) # instantiates the Flask application

def load_user():
    with open("user.json", "r") as file:
        return json.load(file)

@app.route('/')
def home():
    return render_template('index.html')
    # saved_user = load_user()
    # return saved_user["username"]
    

@app.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return username
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)