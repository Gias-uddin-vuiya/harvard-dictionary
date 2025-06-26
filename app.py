
from flask import Flask, flash, redirect, render_template, session, request
from flask_session import Session
from project import get_entry, register_user
# configure application
app = Flask(__name__)

# configue session to ensure filesystem (insted of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



# Ensuser that users get up to date data
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search", methods=["POST"])
def search():
    word = request.form.get("word").strip().lower()
    print(f"Searching for: {word}")  # Debugging output
    if not word:
        return "Please enter a word.", 400
    result = get_entry(word)  # Get word definition, etc.
    print(result)
    return render_template("home.html", word=word, result=result)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    if request.method == "POST":
        fname = request.form.get("fname").strip()
        lname = request.form.get("lname").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        print(f"Registering user: {fname} {lname}, Email: {email}")

        if not fname or not lname or not email or not password:
            flash("All fields are required.", "error")
            return redirect("/register")

        result = register_user(fname, lname, email, password)

        if result["status"] == "success":
            # session["user_id"] = result["user_id"]
            flash("Registration successful!", "success")
            return redirect("/login")
        else:
            flash(result.get("message", "Registration failed."), "error")
            return redirect("/register")

    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")

