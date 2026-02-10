from google.generativeai.types import FunctionDeclaration, Tool


# ============================================================================
# PRÁCTICA 1: HERRAMIENTA DE PRECIOS
# ============================================================================

# 3. Definición de la herramienta para Gemini (price_function)
get_ticket_price_func = FunctionDeclaration(
    name="get_ticket_price",
    description=(
        "Get the price of a return ticket to the destination city. "
        "Call this whenever you need to know the ticket price."
    ),
    parameters={
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to"
            }
        },
        "required": ["destination_city"]
    }
)


# ============================================================================
# PRÁCTICA 2: HERRAMIENTA DE ESTADO DE VUELOS
# ============================================================================

# Definición de la herramienta para Gemini (status_function)
get_flight_status_func = FunctionDeclaration(
    name="get_flight_status",
    description="Get the current status of a specific flight",
    parameters={
        "type": "object",
        "properties": {
            "flight_number": {
                "type": "string",
                "description": (
                    "The flight number to check (e.g., 'FA101', 'FA202'). "
                    "Flight numbers are case-sensitive."
                )
            }
        },
        "required": ["flight_number"]
    }
)


# ============================================================================
# LISTA DE HERRAMIENTAS HABILITADAS
# ============================================================================

# Lista de herramientas habilitadas
# Equivalente a:
# tools = [
#     {"type": "function", "function": price_function},
#     {"type": "function", "function": status_function}
# ]
tools = [
    Tool(function_declarations=[
        get_ticket_price_func,
        get_flight_status_func
    ])
]


# ============================================================================
# NOTA IMPORTANTE SOBRE LA ESTRUCTURA
# ============================================================================