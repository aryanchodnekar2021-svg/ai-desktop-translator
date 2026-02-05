from googletrans import Translator

# 1. Initialize the AI Translator
ai_translator = Translator()

# 2. Define the text and target language
text_to_translate = "Hello, I am learning how to build AI!"
target_language = 'es' # 'es' is for Spanish, 'fr' for French, 'hi' for Hindi

# 3. Perform the translation
result = ai_translator.translate(text_to_translate, dest=target_language)

# 4. Show the results
print(f"Original: {result.origin}")
print(f"Translation ({result.dest}): {result.text}")