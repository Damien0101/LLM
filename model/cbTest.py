from google import genai
from google.genai import types
import json

with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']


client = genai.Client(api_key=API_KEY)

def gen_prompt():
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents='Explain how ai works',
        config=types.GenerateContentConfig(
            max_output_tokens=100,
            temperature=0.5
        ))
    return response.text


