
import requests


def main():
    print("This is the main function of the project module.")


def fetch_definition(word):
    # faching data
    try:
        url = f"https://dictionaryapi.com/api/v3/references/learners/json/{word}?key=af7a50c6-6a2f-4855-89b0-34938adbd8b4"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Handle suggestions (if result is just a list of strings)
        if not data or isinstance(data[0], str):
            return {
                "word": word,
                "definition": "No exact match found. Did you mean: " + ", ".join(data[:5]),
                "example": "",
                "part_of_speech": "",
                "ipa": "",
                "audio_url": "",
                "status": "suggestion"
            }

        entry = data[0]

        # Word
        actual_word = entry.get("hwi", {}).get("hw", word)

        # Part of speech
        part_of_speech = entry.get("fl", "")

        # IPA pronunciation
        ipa = entry.get("hwi", {}).get("prs", [{}])[0].get("ipa", "")

        # Audio
        audio_code = entry.get("hwi", {}).get("prs", [{}])[0].get("sound", {}).get("audio", "")
        audio_url = (
            f"https://media.merriam-webster.com/audio/prons/en/us/mp3/{audio_code[0]}/{audio_code}.mp3"
            if audio_code else ""
        )

        # Definition
        definitions = []
        examples = []

        if "def" in entry:
            senses = entry["def"][0]["sseq"]
            for s in senses:
                for item in s:
                    sense = item[1]

                    definition = ""
                    local_examples = []

                    for dt in sense.get("dt", []):
                        if dt[0] == "text":
                            cleaned_def = dt[1].replace("{bc}", "").strip()
                            definitions.append(cleaned_def)
                        elif dt[0] == "vis":
                            for ex in dt[1]:
                                cleaned_ex = ex.get("t", "").replace("{it}", "").replace("{/it}", "").replace("{phrase}", "").replace("{/phrase}", "")
                                local_examples.append(cleaned_ex)

                    examples.extend(local_examples)

        return {
            "word": actual_word,
            "part_of_speech": part_of_speech,
            "ipa": ipa,
            "definition": definitions,
            "example": examples,
            "audio_url": audio_url,
            "status": "success"
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "word": word,
            "definition": "Definition not found.",
            "example": "",
            "part_of_speech": "",
            "ipa": "",
            "audio_url": "",
            "status": "error"
        }
    
def translate_bengali(word):
    # Call LibreTranslate API
    pass

def mark_word(word, status, memory):
    # Mark as memorized or ignored
    pass