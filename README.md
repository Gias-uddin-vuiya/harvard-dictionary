# Harvard Dictionary 🏛️

![Status: Completed](https://img.shields.io/badge/Status-Completed-green)
![Built with HTML](https://img.shields.io/badge/Built%20with-HTML-red)
![Built with CSS](https://img.shields.io/badge/Built%20with-CSS-blue)
![Bundler: Python](https://img.shields.io/badge/Bundler-python-white)
![Bundler: SQL](https://img.shields.io/badge/Bundler-SQL-black)
![Bundler: Flask](https://img.shields.io/badge/Bundler-Flask-magenta)
![Design Pattern: Functional](https://img.shields.io/badge/Design%20Pattern-Functional-blue)
![Deployment: Vercel](https://img.shields.io/badge/Deployment-Versal-lightgrey)
![Deployments: No Deploys](https://img.shields.io/badge/Deployments-No%20Deploys-lightgrey)

> **Harvard Dictionary** is a web-based dictionary application designed specifically for Harvard University students and language learners. It provides powerful search capabilities and topic-based vocabulary learning, making it easier to explore, understand, and master academic and subject-specific vocabulary. This project was developed as the final submission for Harvard's CS50P (Introduction to Programming with Python) course.

--- 
## 💻 Technologies Used

| **Category**     | **Technologies**                                     |
|-------------------|-----------------------------------------------------|
| **Backend**      | Python, Flask                                       |
| **Frontend**     | HTML, CSS, Bootstrap                    |
| **Database**     | SQLite                                             |
| **Other Tools**  | JSON for structured data storage, Flask sessions for user management |

--- 
## 🌐 Video link
Check out the video presentation of Harvard Dictionary [click here](https://youtu.be/U8X7OWDzpXI)

---
```base
harvard-dictionary/
├── 🐍 project.py              # Core logic and main() function
├── 🧪 test_project.py         # Unit tests for custom functions
├── 🔥 app.py                 # Flask app runner (calls logic from project.py)
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md               # Project documentation
├── 🗄️ dictionary.db           # SQLite database
├── 📁 templates/              # HTML templates (Jinja2)
│   ├── add_topics.html
│   ├── add_vocabulary.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── topic_words.html
│   └── topics.html
├── 🎨 static/                 # Static files
│   ├── style.css             # Custom CSS
│   └── images/               # Image assets
└── 🧠 flask_session/          # Flask session folder (if used)
```

## 🚀 Features & CS50P Compliance

This project meets all the CS50P final project requirements and provides a practical, real-world application. Below is a breakdown of its core features and how it aligns with the course expectations:

--- 

### ✅ Python Requirements Fulfilled

- `project.py` includes:
  - A `main()` function (entry point of the program)
  - 3+ custom functions: modular, reusable, and non-nested
- `test_project.py` includes:
  - Unit tests for each custom function using `pytest`
- `requirements.txt` lists necessary dependencies (`Flask`, etc.)

--- 

### 📚 Dictionary Features (Public)

- **Word Search**  
  Search for any word and retrieve:
  - Part of Speech
  - IPA symbol
  - Pronunciation (sound)
  - Definitions
  - Example sentences
  - Synonyms and antonyms
 
 --- 

### 🔐 Authenticated User Features

- **User Registration & Login System**  
  Allows users to securely create accounts and log in.

- **Topic-Based Vocabulary Learning**  
  Users can:
  - Browse vocabulary by topics (e.g., Science, History, Medicine)
  - Click on a topic to view related words
  - Search within a specific topic

--- 

### 🛠 Developer/Admin Features

- **Add New Topics**  
  Developers can create new vocabulary topics from a form interface.

- **Add Words to Topics**  
  Easily associate words with a topic and store them in the database.

- All data is managed using **Flask**, **SQLite**, and **Python functions**, ensuring separation of logic and maintainability.


