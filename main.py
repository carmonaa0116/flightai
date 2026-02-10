"""
main.py
-------
PASO 4: Integración en el Chat
Chatbot completo con function calling usando Gemini.
Ahora soporta MÚLTIPLES HERRAMIENTAS (Práctica 2).
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
from tool_schema import tools
from handler import handle_tool_call


# System message
SYSTEM_MESSAGE = "I am a helpful assistant for an Airline called FlightAI."


def setup_gemini():
    """Configura la API de Gemini"""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError(
            "ERROR: No se encontró GEMINI_API_KEY en el archivo .env\n"
            "Crea un archivo .env con: GEMINI_API_KEY=tu_api_key"
        )
    
    genai.configure(api_key=api_key)
    
    # ✅ INTENTAR CON DIFERENTES NOMBRES DE MODELO
    model_names_to_try = [
        "gemini-1.5-flash",           # Opción 1
        "gemini-1.5-pro",             # Opción 2
        "models/gemini-1.5-flash",    # Opción 3 (con prefijo)
        "models/gemini-1.5-pro",      # Opción 4 (con prefijo)
    ]
    
    for model_name in model_names_to_try:
        try:
            print(f"🔄 Intentando con modelo: {model_name}")
            model = genai.GenerativeModel(
                model_name=model_name,
                tools=tools,
                system_instruction=SYSTEM_MESSAGE
            )
            print(f"✅ Modelo cargado exitosamente: {model_name}\n")
            return model
        except Exception as e:
            print(f"❌ Falló {model_name}: {str(e)[:50]}...")
            continue
    
    raise ValueError(
        "❌ No se pudo cargar ningún modelo.\n"
        "Ejecuta 'python check_models.py' para ver modelos disponibles."
    )

def chat():
    """Loop principal del chatbot"""
    print("\n" + "="*70)
    print("✈️  FLIGHTAI - CHATBOT CON MÚLTIPLES HERRAMIENTAS")
    print("="*70)
    print("\nPRUEBAS DE LA PRÁCTICA 2:")
    print("1. Regresión: 'How much is a ticket to Tokyo?'")
    print("2. Nueva funcionalidad: 'Is flight FA202 on time?'")
    print("3. Combinada: 'Check status of FA303 and price to Berlin'")
    print("\nEscribe 'exit' para salir\n")
    print("="*70 + "\n")
    
    try:
        model = setup_gemini()
    except ValueError as e:
        print(f"❌ {e}")
        return
    
    chat_session = model.start_chat(enable_automatic_function_calling=False)
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['exit', 'quit', 'salir']:
            print("\n👋 ¡Hasta luego!\n")
            break
        
        try:
            response = chat_session.send_message(user_input)
            
            # Verificar si hay tool calls
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                
                print(f"\n🔧 Tool {function_call.name} called")
                print(f"📝 Args: {dict(function_call.args)}")
                
                # Ejecutar la función
                result = handle_tool_call(function_call)
                
                print(f"✅ Result: {result}\n")
                
                # Enviar resultado a Gemini
                function_response = genai.protos.Content(
                    parts=[
                        genai.protos.Part(
                            function_response=genai.protos.FunctionResponse(
                                name=function_call.name,
                                response=result
                            )
                        )
                    ]
                )
                
                response = chat_session.send_message(function_response)
            
            print(f"\nFlightAI: {response.text}\n")
            
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    chat()