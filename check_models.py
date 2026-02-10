"""
check_models.py
---------------
Verifica qué modelos están disponibles con tu API key
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ No se encontró GEMINI_API_KEY en .env")
    exit(1)

genai.configure(api_key=api_key)

print("\n" + "="*70)
print("📋 MODELOS DISPONIBLES CON TU API KEY")
print("="*70 + "\n")

models_found = False

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        models_found = True
        print(f"✅ {model.name}")
        print(f"   Display name: {model.display_name}")
        print(f"   Soporta: {', '.join(model.supported_generation_methods)}")
        print()

if not models_found:
    print("❌ No se encontraron modelos disponibles")
    print("Verifica que tu API key sea válida")

print("="*70)