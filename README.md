# Tiny Flask Password App

This project shows a very small password login app.

It uses:

```text
Python
Flask
HTML templates
one JSON file
sessions
a browser cookie
```

This is a teaching example. It is not a secure production login system yet.

## What this app does

The app has one saved password in `user.json`.

The user types a password into the login form.

Flask checks the typed password against the saved password.

If the password is correct, Flask creates a session.

The session lets Flask remember that the user has logged in.

In this simple Flask app, the session is stored in a browser cookie.

## File structure

Create this structure:

```text
password-app1/
    app.py
    user.json
    templates/
        index.html
        login.html
```

## Step 1: Create the project folder

```bash
mkdir password-app1
cd password-app1
```

## Step 2: Create the templates folder

```bash
mkdir templates
```

## Step 3: Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on Mac:

```bash
source venv/bin/activate
```

When the virtual environment is active, the terminal should show:

```text
(venv)
```

## Step 4: Install Flask

```bash
pip install flask
```

Check Flask is installed:

```bash
python -m flask --version
```

## Step 5: Create `user.json`

Create a file called `user.json`.

This file goes next to `app.py`.

```json
{
    "password": "secret"
}
```

For this lesson, the password is written directly in the JSON file.

This is only to make the login logic easy to see.

In a real app, the plain password should not be stored like this.

## Step 6: Create `templates/index.html`

Create `index.html` inside the `templates` folder.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Home page</h1>

    <p>You are logged in.</p>

    <a href="/logout">Log out</a>
</body>
</html>
```

## Step 7: Create `templates/login.html`

Create `login.html` inside the `templates` folder.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Log in</title>
</head>
<body>
    <h1>Log in</h1>

    <form method="POST">
        <label for="password">Password</label>
        <input id="password" name="password" type="password">

        <button type="submit">Log in</button>
    </form>
</body>
</html>
```

The important part is:

```html
<form method="POST">
```

This sends the password inside the request body.

Without `method="POST"`, the password can appear in the browser URL.

The other important part is:

```html
name="password"
```

Flask uses this name to grab the password from the form.

## Step 8: Create `app.py`

Create `app.py` in the main project folder.

```python
import json
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)  # creates the Flask application

app.secret_key = "temporary_secret_key"


def load_user():
    with open("user.json", "r") as file:
        return json.load(file)


@app.route("/")
def home():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        saved_user = load_user()
        password = request.form["password"]

        if password == saved_user["password"]:
            session["logged_in"] = True
            return redirect(url_for("home"))

        return "Login failed"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
```

## Step 9: Run the app

```bash
python app.py
```

Open this in the browser:

```text
http://127.0.0.1:5000
```

The app should send you to the login page.

Use this password:

```text
secret
```

After login, the app should send you to the home page.

## What the important lines mean

This line reads the password typed into the form:

```python
password = request.form["password"]
```

It works because the HTML input has:

```html
name="password"
```

This line checks the typed password against the saved password in `user.json`:

```python
if password == saved_user["password"]:
```

This line creates the session:

```python
session["logged_in"] = True
```

It means:

```text
Remember that this browser has logged in.
```

This line protects the home page:

```python
if "logged_in" not in session:
    return redirect(url_for("login"))
```

It means:

```text
If the browser has not logged in, send it back to the login page.
```

This line logs the user out:

```python
session.clear()
```

It means:

```text
Forget the session.
```

## What is `app.secret_key`?

This line is needed because the app uses sessions:

```python
app.secret_key = "temporary_secret_key"
```

The secret key is not the login password.

Flask uses it to protect the session cookie.

## Where is the cookie?

After logging in, Flask creates a session cookie.

The cookie is stored in the browser.

To see it in Chrome:

```text
Right click the page
Click Inspect
Click Application
Click Cookies
Click http://127.0.0.1:5000
Look for a cookie called session
```

## Simple summary

```text
user.json stores the saved password.

The login form sends the typed password to Flask.

Flask checks the typed password against the saved password.

If the password is correct, Flask creates a session.

The session is stored in a browser cookie.

The cookie helps Flask remember that the browser has logged in.
```
