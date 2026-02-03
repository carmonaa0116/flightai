import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ No se encontró GEMINI_API_KEY en .env")
    exit(1)

client = genai.Client(api_key=api_key)

print("\n🔍 Modelos disponibles:\n")
for model in client.models.list():
    print(f"✅ {model.name}")