from google import genai
import json

with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']



client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Explain how ai works')

print(response.text)