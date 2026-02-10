# ✈️ FlightAI -- Práctica 1 + 2: Múltiples Herramientas

Asistente de aerolínea con **Function Calling** usando Google Gemini.

## 🎯 Funcionalidades

### Práctica 1: Consulta de Precios

-   Consultar precios de billetes a diferentes ciudades
-   Ciudades disponibles: `London`, `Paris`, `Tokyo`, `Berlin`

### Práctica 2: Consulta de Estados de Vuelos

-   Consultar el estado de vuelos en tiempo real
-   Vuelos disponibles: `FA101`, `FA202`, `FA303`, `FA404`

------------------------------------------------------------------------

## 📋 Pruebas del Sistema

### 🧪 PRÁCTICA 1

#### 1. Prueba de Éxito (Berlin)

``` text
You: How much is a ticket to Berlin?

🔧 Tool get_ticket_price called
FlightAI: A return ticket to Berlin costs $499.
```

#### 2. Prueba de Dato No Disponible (Madrid)

``` text
You: How much is a ticket to Madrid?

🔧 Tool get_ticket_price called
FlightAI: I'm sorry, I don't have price information for Madrid.
```

#### 3. Prueba de Personalidad

``` text
You: Who are you?

FlightAI: I am a helpful assistant for an Airline called FlightAI.
```

------------------------------------------------------------------------

### 🧪 PRÁCTICA 2

#### 4. Prueba de Regresión (Tokyo)

``` text
You: How much is a ticket to Tokyo?

🔧 Tool get_ticket_price called
FlightAI: A return ticket to Tokyo costs $1400.
```

#### 5. Nueva Funcionalidad (FA202)

``` text
You: Is flight FA202 on time?

🔧 Tool get_flight_status called
FlightAI: No, flight FA202 is delayed 2 hours.
```

#### 6. Prueba Combinada (Avanzada)

``` text
You: Check the status of flight FA303 and tell me the price to Berlin.

🔧 Tool get_flight_status called
🔧 Tool get_ticket_price called
FlightAI: Flight FA303 is cancelled. A ticket to Berlin costs $499.
```

------------------------------------------------------------------------

## 🚀 Instalación

``` bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar API Key
echo "GEMINI_API_KEY=tu_api_key" > .env

# 3. Ejecutar tests
python run_all_tests.py

# 4. Ejecutar chatbot
python main.py
```

------------------------------------------------------------------------

## 📁 Estructura del Proyecto

``` text
flightai/
│
├── tools.py               # Base de datos + funciones (precios + vuelos)
├── test_tools.py
│
├── tool_schema.py         # Schemas de ambas herramientas
├── test_tool_schema.py
│
├── handler.py             # Manejador con if/elif dinámico
├── test_handler.py
│
├── main.py                # Chat integrado
├── test_main.py
│
├── .env
├── requirements.txt
├── run_all_tests.py
└── README.md
```

------------------------------------------------------------------------

## 🎯 Datos Disponibles

### 💰 Precios de Billetes

  Ciudad   Precio
  -------- --------
  London   \$799
  Paris    \$899
  Tokyo    \$1400
  Berlin   \$499

### ✈️ Estados de Vuelos

  Vuelo   Estado
  ------- -----------------
  FA101   On Time
  FA202   Delayed 2 hours
  FA303   Cancelled
  FA404   Boarding

------------------------------------------------------------------------

## 🔍 Diferencias Técnicas: OpenAI vs Gemini

### Registro de Herramientas

**OpenAI**

``` python
tools = [
    {"type": "function", "function": price_function},
    {"type": "function", "function": status_function}
]
```

**Gemini**

``` python
tools = [
    Tool(
        function_declarations=[
            get_ticket_price_func,
            get_flight_status_func
        ]
    )
]
```

------------------------------------------------------------------------

### Handler Dinámico

``` python
def handle_tool_call(tool_call):
    function_name = tool_call.name

    if function_name == "get_ticket_price":
        pass
    elif function_name == "get_flight_status":
        pass
```

------------------------------------------------------------------------

## 📚 Referencias

-   [Google Gemini API](https://ai.google.dev/)
-   [Function Calling](https://ai.google.dev/docs/function_calling)
-   Práctica 1: `Practica_Vuelo_01.pdf`
-   Práctica 2: `Practica_Vuelo_02.pdf`

------------------------------------------------------------------------

## ▶️ Ejecutar Tests

``` bash
python run_all_tests.py
```

Salida esperada:

``` text
🎉 TODOS LOS TESTS PASARON
```
