
import requests
import json
from flask import Flask
import sqlite3

app = Flask(__name__)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()



def get_entry(word):
   
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if not data:
            return {"status": "error", "message": "No data found for the word."}
        
        word = data[0].get("word", "")
        definition = data[0].get("meanings", [{}])[0].get("definitions", [{}])[0].get("definition", "")
        examples = data[0].get("meanings", [{}])[0].get("definitions", [{}])[0].get("example", "")
        part_of_speech = data[0].get("meanings", [{}])[0].get("partOfSpeech", [{}])
        synonyms = data[0].get("meanings", [{}])[0].get("synonyms", [])
        antonyms = data[0].get("meanings", [{}])[0].get("antonyms", [])
        ipa = data[0].get("phonetic", "")
        audio_url = data[0].get("phonetics", [{}])[0].get("audio", "")
        try:
            
            return {
                "word": word,
                "definition": definition,
                "examples": examples,
                "part_of_speech": part_of_speech,
                "synonyms": synonyms,
                "antonyms": antonyms,
                "ipa": ipa,
                "audio_url": audio_url,
                "status": "success"
            }
        except Exception as e:
            return {"status": f"error parsing data: {e}"}
    else:
        return {
            "status": f"API Error {response.status_code}",
            "message": response.text
        }


def register_user(fname, lname, email, password):
    try:
        conn = sqlite3.connect("dictionary.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO users (fname, lname, email, password)
            VALUES (?, ?, ?, ?)
        """, (fname, lname, email, password))
        
        conn.commit()

        # Fetch the last inserted user's id
        user_id = cur.lastrowid
        conn.close()

        return {"status": "success", "user_id": user_id}
    except sqlite3.IntegrityError as e:
        return {"status": "error", "message": f"Email already exists or integrity error: {e}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

