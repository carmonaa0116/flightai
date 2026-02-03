"""
tool_schema.py
--------------
Define el schema (esquema) de las herramientas disponibles para Gemini.
Este schema le dice al modelo qué funciones existen y cuándo usarlas.
"""

from google.genai import types


# Declaración de la función get_ticket_price para Gemini
get_ticket_price_func = types.FunctionDeclaration(
    name="get_ticket_price",
    description=(
        "Get the price of a flight ticket to a specific destination city. "
        "Use this function when the user asks about ticket prices, costs, "
        "or how much a flight to a city costs."
    ),
    parameters={
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": (
                    "The destination city for the flight ticket. "
                    "Example: 'London', 'Paris', 'Tokyo', 'Berlin'"
                )
            }
        },
        "required": ["destination_city"]
    }
)


# ✅ CORRECCIÓN: Envolver en Tool con function_declarations
tools = [
    types.Tool(
        function_declarations=[get_ticket_price_func]
    )
]