import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# The SDK automatically uses the GEMINI_API_KEY environment variable
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)  # No need to pass api_key if using env var

model = genai.GenerativeModel('gemini-2.5-flash')  # Or 'gemini-1.5-pro' if available in free tier

topic = input("Enter a topic: ")

prompt = f"Write a haiku about {topic} in 5-7-5 syllables"
response = model.generate_content(prompt)

print(response.text)