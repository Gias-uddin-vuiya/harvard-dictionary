
from flask import Flask, flash, redirect, render_template, session, request
from flask_session import Session
import sqlite3
from project import get_entry, register_user, login_user, add_topic, add_word
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


@app.route("/manage_vocab", methods=["GET"])
def manage_vocab():
    # get topics 
    connect = sqlite3.connect("dictionary.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM topics")
    topics = cursor.fetchall()
    # format topics
    topics = [{"id": topic[0], "name": topic[1], "image": topic[2]} for topic in topics]
  
    
    connect.close()
    return render_template("manage_vocab.html", topics=topics)


@app.route("/add_topic", methods=["POST"])
def add_topic_name():
    """Render the manage vocabulary page."""
    if request.method == "POST":
        name = request.form.get("topic_name").strip()
        image = request.form.get("image_url").strip()
        if not name:
            flash("Topic name is required.", "error")
            return redirect("/manage_vocab")
        
        result = add_topic(name, image)
        if result["status"] != "success":
            flash(f"Error adding topic: {result.get('message', 'Unknown error')}", "error")
            return redirect("/manage_vocab")
        return redirect("/manage_vocab")

@app.route('/add_word', methods=['POST'])
def add_words():
    if request.method == "POST":
        topics_id = request.form.get('topic_id').strip()
        word = request.form.get('word').strip()
        difinition = request.form.get('difinition').strip()
        part_of_speech = request.form.get('part_of_speech').strip()
        ipa_us = request.form.get('ipa_us').strip()
        ipa_uk = request.form.get('ipa_uk').strip()
        sound_us = request.form.get('sound_us').strip()
        sound_uk = request.form.get('sound_uk').strip()
        level = request.form.get('level').strip()

        if not word:
            flash("Word is required.", "error")
            return redirect("/manage_vocab") 
        # Check if the word already exists
        result = add_word(topics_id, word, difinition, part_of_speech, ipa_us, ipa_uk, sound_us, sound_uk, level)
       
        if result["status"] == "success":
            flash(f"Word '{word}' added successfully!", "success")
            return redirect("/manage_vocab")
        else:
            flash(f"Error adding word: {result.get('message', 'Unknown error')}", "error")
            return redirect("/manage_vocab")    


@app.route("/topics")
def show_topics():
    """Render the topics page."""
    conn = sqlite3.connect("dictionary.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM topics")
    topics = cur.fetchall()
    conn.close()

    return render_template("topics.html", topics=topics)

@app.route("/topic/<int:topic_id>")
def show_topic_word(topic_id):
    """Render a specific topic page."""
    conn = sqlite3.connect("dictionary.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    topic = cur.fetchone()
    
    if not topic:
        flash("Topic not found.", "error")
        return redirect("/topics")

    cur.execute("SELECT * FROM vocabulary WHERE topic_id = ?", (topic_id,))
    words = cur.fetchall()
    
    conn.close()

    return render_template("topic_words.html", topic=topic, words=words)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user."""
    if request.method == "POST":
        fname = request.form.get("fname").strip()
        lname = request.form.get("lname").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        confirm_password = request.form.get("confirm_password").strip()
        

        if not fname or not lname or not email or not password:
            flash("All fields are required.", "error")
            return redirect("/register")
        
        if password != confirm_password:
            flash("Passwords do not match.", "error")
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """Render the login page."""
    if request.method == "POST":
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()
        print(f"Logging in user: {email, password}")

        if not email or not password:
            flash("Email and password are required.", "error")
            return redirect("/login")

        result = login_user(email, password)

        if result["status"] == "success":
            session["user_id"] = result["user_id"]
            flash("Login successful!", "success")
            return redirect("/")
        else:
            flash(result.get("message", "Login failed."), "error")
            return redirect("/login")
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out the user."""
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect("/")    
