"""
test_tool_schema.py
-------------------
Tests para tool_schema.py (Práctica 1 + 2)
"""


def test_imports():
    """Verificar importaciones"""
    print("=" * 60)
    print("TEST 1: Imports")
    print("=" * 60)
    
    try:
        from google.generativeai.types import FunctionDeclaration, Tool
        print("✅ google.generativeai.types")
        
        from tool_schema import (
            tools, 
            get_ticket_price_func, 
            get_flight_status_func
        )
        print("✅ tool_schema")
        
        print("✅ TEST PASADO\n")
        return True
        
    except ImportError as e:
        print(f"❌ Error: {e}")
        return False


# ============================================================================
# TESTS DE LA HERRAMIENTA DE PRECIOS (PRÁCTICA 1)
# ============================================================================

def test_price_function_name():
    """Verificar nombre de la función de precios"""
    print("=" * 60)
    print("TEST 2: Nombre de get_ticket_price")
    print("=" * 60)
    
    from tool_schema import get_ticket_price_func
    
    assert get_ticket_price_func.name == "get_ticket_price"
    print(f"✅ Nombre: {get_ticket_price_func.name}")
    print("✅ TEST PASADO\n")


def test_price_function_parameter():
    """Verificar parámetro destination_city"""
    print("=" * 60)
    print("TEST 3: Parámetro destination_city")
    print("=" * 60)
    
    from tool_schema import get_ticket_price_func
    
    params = get_ticket_price_func.parameters
    
    assert "destination_city" in params["properties"]
    assert params["properties"]["destination_city"]["type"] == "string"
    assert "destination_city" in params["required"]
    
    print("✅ destination_city existe, es string y es requerido")
    print("✅ TEST PASADO\n")


# ============================================================================
# TESTS DE LA HERRAMIENTA DE ESTADOS (PRÁCTICA 2)
# ============================================================================

def test_status_function_name():
    """Verificar nombre de la función de estados"""
    print("=" * 60)
    print("TEST 4: Nombre de get_flight_status")
    print("=" * 60)
    
    from tool_schema import get_flight_status_func
    
    assert get_flight_status_func.name == "get_flight_status"
    print(f"✅ Nombre: {get_flight_status_func.name}")
    print("✅ TEST PASADO\n")


def test_status_function_description():
    """Verificar descripción de get_flight_status"""
    print("=" * 60)
    print("TEST 5: Descripción de get_flight_status")
    print("=" * 60)
    
    from tool_schema import get_flight_status_func
    
    desc = get_flight_status_func.description.lower()
    
    assert "status" in desc, "❌ Debe mencionar 'status'"
    assert "flight" in desc, "❌ Debe mencionar 'flight'"
    
    print(f"Descripción: {get_flight_status_func.description}")
    print("✅ Menciona 'status' y 'flight'")
    print("✅ TEST PASADO\n")


def test_status_function_parameter():
    """Verificar parámetro flight_number"""
    print("=" * 60)
    print("TEST 6: Parámetro flight_number")
    print("=" * 60)
    
    from tool_schema import get_flight_status_func
    
    params = get_flight_status_func.parameters
    
    # Verificar que existe
    assert "flight_number" in params["properties"], \
        "❌ Falta el parámetro 'flight_number'"
    print("✅ Parámetro 'flight_number' existe")
    
    # Verificar tipo
    assert params["properties"]["flight_number"]["type"] == "string", \
        "❌ flight_number debe ser string"
    print("✅ Tipo: string")
    
    # Verificar que es requerido
    assert "flight_number" in params["required"], \
        "❌ flight_number debe ser requerido"
    print("✅ Marcado como requerido")
    
    print("✅ TEST PASADO\n")


# ============================================================================
# TESTS DE LA LISTA DE HERRAMIENTAS
# ============================================================================

def test_tools_list_structure():
    """Verificar que tools tiene ambas funciones"""
    print("=" * 60)
    print("TEST 7: Lista de Herramientas")
    print("=" * 60)
    
    from tool_schema import tools
    
    assert isinstance(tools, list)
    assert len(tools) == 1  # En Gemini, todas las funciones van en UN Tool
    print("✅ tools es una lista con 1 objeto Tool")
    
    # Verificar que el Tool tiene 2 function_declarations
    tool = tools[0]
    assert len(tool.function_declarations) == 2
    print("✅ El Tool contiene 2 function_declarations")
    
    # Verificar nombres de las funciones
    function_names = [f.name for f in tool.function_declarations]
    assert "get_ticket_price" in function_names
    assert "get_flight_status" in function_names
    
    print("✅ Contiene get_ticket_price y get_flight_status")
    print("✅ TEST PASADO\n")


def test_both_functions_registered():
    """Verificar que ambas funciones están correctamente registradas"""
    print("=" * 60)
    print("TEST 8: Ambas Funciones Registradas")
    print("=" * 60)
    
    from tool_schema import tools
    
    tool = tools[0]
    functions = {f.name: f for f in tool.function_declarations}
    
    # Verificar get_ticket_price
    assert "get_ticket_price" in functions
    price_func = functions["get_ticket_price"]
    assert "destination_city" in price_func.parameters["properties"]
    print("✅ get_ticket_price registrada correctamente")
    
    # Verificar get_flight_status
    assert "get_flight_status" in functions
    status_func = functions["get_flight_status"]
    assert "flight_number" in status_func.parameters["properties"]
    print("✅ get_flight_status registrada correctamente")
    
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE tool_schema.py (Práctica 1 + 2)\n")
    
    try:
        if not test_imports():
            print("\n❌ ABORTADO: Faltan dependencias\n")
            exit(1)
        
        # Tests Práctica 1
        test_price_function_name()
        test_price_function_parameter()
        
        # Tests Práctica 2
        test_status_function_name()
        test_status_function_description()
        test_status_function_parameter()
        
        # Tests de integración
        test_tools_list_structure()
        test_both_functions_registered()
        
        print("=" * 60)
        print("🎉 TODOS LOS TESTS DE tool_schema.py PASARON")
        print("=" * 60)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)