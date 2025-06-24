import pytest
from project import get_entry

@pytest.mark.parametrize("search_word", ["Pneumonoultramicroscopicsilicovolcanoconiosis", "computer", "university", 'education', 'knowledge', 'python', 'programming'])
def test_word_accuracy_from_api(search_word):
    result = get_entry(search_word)
  
    #  1. Check that API returned successfully
    assert result["status"] == "success", f"API failed for word: {search_word}"

    assert result["word"].lower() == search_word.lower(), (
        f"Mismatch: searched for '{search_word}', but API returned '{result['word']}'"
    )
    
    assert isinstance(result["definition"], str) and result["definition"].strip() != "", (
        f"No valid definition found for '{search_word}'"
    )

    assert "part_of_speech" in result and isinstance(result["part_of_speech"], str), (
        f"Missing or invalid part of speech for '{search_word}'"
    )

    assert "ipa" in result, f"IPA not provided for '{search_word}'"
    assert "audio_url" in result, f"Audio URL missing for '{search_word}'"

    # Optional: Make sure synonyms/antonyms, if exist, are lists
    assert isinstance(result.get("synonyms", []), list), f"Synonyms is not a list for '{search_word}'"
    assert isinstance(result.get("antonyms", []), list), f"Antonyms is not a list for '{search_word}'"
