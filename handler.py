
from tools import get_ticket_price, get_flight_status


def handle_tool_call(tool_call):
    # Obtener el nombre de la función que la IA quiere ejecutar
    function_name = tool_call.name
    
    # Obtener los argumentos
    arguments = dict(tool_call.args)
    
    # Variable para guardar el resultado
    response_content = {}
    
    # ========================================================================
    # PRÁCTICA 2 - PASO 5: GESTIÓN DE MÚLTIPLES HERRAMIENTAS
    # ========================================================================
    
    # 1. Si pide PRECIOS
    if function_name == "get_ticket_price":
        city = arguments.get('destination_city')
        price = get_ticket_price(city)
        response_content = {
            "destination_city": city,
            "price": price
        }
    
    # 2. Si pide ESTADO DE VUELO
    elif function_name == "get_flight_status":
        # Extraer el número de vuelo de los argumentos
        flight_number = arguments.get('flight_number')
        
        # Llamar a la función get_flight_status
        status = get_flight_status(flight_number)
        
        # Guardar el resultado en response_content
        response_content = {
            "flight_number": flight_number,
            "status": status
        }
    
    # 3. Función desconocida (manejo de errores)
    else:
        response_content = {
            "error": f"Unknown function: {function_name}"
        }
    
    return response_content
