from googletrans import Translator

def translate_persian_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='fa', dest='en')
    return translation.text

# Example usage:
persian_text = "سلام، چطوری؟"
english_translation = translate_persian_to_english(persian_text)
print(f"Original (Persian): {persian_text}")
print(f"Translation (English): {english_translation}")