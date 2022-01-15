# Import necessary libraries
from googletrans import Translator

# Define a translator
translator = Translator()

# I'm gonna use simple input command to take our message and translate it to english
text = str(input("Type your text in any language, I'll translate it to english: "))

# Translate our message and save it to "translated" variable
translated = translator.translate(text)

# Print our original and translated messages
print(f"Original text: {text}")
print(f"Translated text: {translated}")