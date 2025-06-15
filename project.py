
import requests


def main():
    print("This is the main function of the project module.")


def fetch_definition(word):
    try:
        # 1. Get definition and example
        dict_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(dict_url)
        response.raise_for_status()  # Raises an error for 4xx/5xx responses
        data = response.json()
        
        # Extract info from first meaning/definition
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', 'No example available.')


        return {
            "definition": definition,
            "example": example,
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "definition": "Definition not found.",
            "example": "Example not found.",
        }
def translate_bengali(word):
    # Call LibreTranslate API
    pass

def mark_word(word, status, memory):
    # Mark as memorized or ignored
    pass