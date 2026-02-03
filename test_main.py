"""
test_main.py
------------
Tests para el módulo main.py
Ejecutar con: python test_main.py
"""

import os
from unittest.mock import patch


def test_imports():
    """Test 1: Verificar imports"""
    print("=" * 50)
    print("TEST 1: Imports")
    print("=" * 50)
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai importado")
        
        from dotenv import load_dotenv
        print("✅ dotenv importado")
        
        from main import setup_gemini, SYSTEM_PROMPT
        print("✅ main.py importado")
        
        print("✅ TEST PASADO\n")
        return True
        
    except ImportError as e:
        print(f"❌ Error: {e}")
        return False


def test_system_prompt_exists():
    """Test 2: Verificar que existe el system prompt"""
    print("=" * 50)
    print("TEST 2: System Prompt")
    print("=" * 50)
    
    from main import SYSTEM_PROMPT
    
    assert SYSTEM_PROMPT
    assert len(SYSTEM_PROMPT) > 50
    assert "FlightAI" in SYSTEM_PROMPT
    
    print(f"✅ System prompt existe ({len(SYSTEM_PROMPT)} caracteres)")
    print(f"✅ Menciona 'FlightAI'")
    print("✅ TEST PASADO\n")


def test_system_prompt_content():
    """Test 3: Verificar contenido del system prompt"""
    print("=" * 50)
    print("TEST 3: Contenido del System Prompt")
    print("=" * 50)
    
    from main import SYSTEM_PROMPT
    
    prompt_lower = SYSTEM_PROMPT.lower()
    
    # Debe mencionar que es un asistente
    assert "assistant" in prompt_lower or "ayudante" in prompt_lower
    print("✅ Se identifica como asistente")
    
    # Debe mencionar FlightAI
    assert "flightai" in prompt_lower
    print("✅ Menciona FlightAI")
    
    # Debe mencionar no inventar precios
    assert "never" in prompt_lower or "not" in prompt_lower
    print("✅ Contiene restricciones")
    
    print("✅ TEST PASADO\n")


def test_env_file_missing():
    """Test 4: Verificar comportamiento sin .env"""
    print("=" * 50)
    print("TEST 4: Archivo .env Faltante")
    print("=" * 50)
    
    from main import setup_gemini
    
    # Simular que no hay GEMINI_API_KEY
    with patch.dict(os.environ, {}, clear=True):
        try:
            setup_gemini()
            print("❌ Debería haber lanzado ValueError")
            assert False
        except ValueError as e:
            assert "GEMINI_API_KEY" in str(e)
            print(f"✅ Lanza ValueError correcto: {e}")
    
    print("✅ TEST PASADO\n")


def test_setup_with_mock_key():
    """Test 5: Verificar setup con API key mockeada"""
    print("=" * 50)
    print("TEST 5: Setup con API Key Mock")
    print("=" * 50)
    
    from main import setup_gemini
    
    # Simular API key
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key_for_testing"}):
        with patch('google.generativeai.configure'):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                model = setup_gemini()
                print("✅ setup_gemini() ejecutado sin errores")
    
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE main.py\n")
    
    try:
        if not test_imports():
            print("\n❌ ABORTADO: Faltan dependencias\n")
            exit(1)
        
        test_system_prompt_exists()
        test_system_prompt_content()
        test_env_file_missing()
        test_setup_with_mock_key()
        
        print("=" * 50)
        print("🎉 TODOS LOS TESTS DE main.py PASARON")
        print("=" * 50)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)