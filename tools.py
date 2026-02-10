# Base de datos ficticia de precios
ticket_prices = {
    "london": "$799",
    "paris": "$899",
    "tokyo": "$1400",
    "berlin": "$499"
}

# Función para obtener el precio del billete
def get_ticket_price(destination_city):
    """
    Obtiene el precio de un billete de vuelta a la ciudad de destino.
    
    Args:
        destination_city (str): Ciudad de destino
        
    Returns:
        str: Precio del billete o "Unknown" si no existe
    """
    print(f"🔧 Tool get_ticket_price called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

# Base de datos simulada de estados de vuelos
flight_status_db = {
    "FA101": "On Time",
    "FA202": "Delayed 2 hours",
    "FA303": "Cancelled",
    "FA404": "Boarding"
}

# Función para obtener el estado de un vuelo
def get_flight_status(flight_number):

    print(f"🔧 Tool get_flight_status called for {flight_number}")
    
    return flight_status_db.get(flight_number, "Status Unknown")