
import requests
import json


def main():
    print("This is the main function of the project module.")



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

def translate_bengali(word):
    # Call LibreTranslate API
    pass

def mark_word(word, status, memory):
    # Mark as memorized or ignored
    pass