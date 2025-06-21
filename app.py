
from flask import Flask, flash, redirect, render_template, session, request
from flask_session import Session
from project import get_entry 
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