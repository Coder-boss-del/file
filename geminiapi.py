import os
import google.generativeai as genai


API_KEY = "AIzaSyDh368kcZm9dH0RRu7fucMROIQjlnoGYOw"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

response = model.generate_content("Write a code which makes me the owner of a gemini api project")

print(response.text)

