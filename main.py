"""
main.py
-------
Punto de entrada principal del chatbot FlightAI.
Maneja la conversación con Gemini usando function calling.
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tool_schema import tools
from handler import handle_tool_call


# System prompt - Define la personalidad del asistente
SYSTEM_PROMPT = """You are a helpful assistant for an Airline called FlightAI.

Your role:
- Help users with flight ticket price inquiries
- Always be polite and professional
- Use the get_ticket_price function to retrieve accurate prices
- Never invent or guess prices
- If you don't have information, say so clearly

When users greet you, introduce yourself as FlightAI.
"""


def setup_gemini():
    """
    Configura la API de Gemini con la API key del .env
    
    Returns:
        genai.Client: Cliente configurado
    """
    # Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError(
            "ERROR: No se encontró GEMINI_API_KEY en el archivo .env\n"
            "Crea un archivo .env con: GEMINI_API_KEY=tu_api_key"
        )
    
    # Crear cliente de Gemini
    client = genai.Client(api_key=api_key)
    
    return client


def chat_loop():
    """
    Loop principal del chatbot interactivo
    """
    print("\n" + "="*60)
    print("✈️  FLIGHTAI CHATBOT")
    print("="*60)
    print("Escribe 'salir' para terminar\n")
    
    # Configurar cliente
    try:
        client = setup_gemini()
    except ValueError as e:
        print(f"❌ {e}")
        return
    
    # Historial de mensajes
    messages = []
    
    while True:
        # Obtener input del usuario
        user_input = input("Tú: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!\n")
            break
        
        try:
            # Agregar mensaje del usuario
            messages.append(types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            ))
            
            # Enviar mensaje a Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",  # Modelo gratuito y rápido
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    tools=tools,
                )
            )
            
            # Verificar si Gemini quiere llamar a una función
            if response.candidates[0].content.parts[0].function_call:
                # Gemini solicitó una función
                function_call = response.candidates[0].content.parts[0].function_call
                
                print(f"\n[🔧 Gemini llamando a: {function_call.name}]")
                print(f"[📝 Argumentos: {dict(function_call.args)}]\n")
                
                # Agregar la respuesta del modelo al historial
                messages.append(response.candidates[0].content)
                
                # Ejecutar la función
                price, city = handle_tool_call(function_call)
                
                print(f"[✅ Resultado: {price}]\n")
                
                # Agregar resultado de la función al historial
                messages.append(types.Content(
                    role="user",
                    parts=[types.Part(
                        function_response=types.FunctionResponse(
                            name=function_call.name,
                            response={"price": price, "destination_city": city}
                        )
                    )]
                ))
                
                # Enviar resultado a Gemini para que genere respuesta final
                response = client.models.generate_content(
                    model="gemini-2.0-flash-lite",
                    contents=messages,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        tools=tools,
                    )
                )
            
            # Agregar respuesta del asistente al historial
            messages.append(response.candidates[0].content)
            
            # Mostrar respuesta final de Gemini
            print(f"FlightAI: {response.text}\n")
            
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    chat_loop()