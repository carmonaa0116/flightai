"""
test_handler.py
---------------
Tests para handler.py (Práctica 1 + 2)
"""

from handler import handle_tool_call


class MockToolCall:
    """Mock de un tool_call de Gemini"""
    def __init__(self, name, args):
        self.name = name
        self.args = args


# ============================================================================
# TESTS DE LA HERRAMIENTA DE PRECIOS (PRÁCTICA 1)
# ============================================================================

def test_handle_price_tokyo():
    """PRUEBA 1 PRÁCTICA 2: Regresión - Precio de Tokyo"""
    print("=" * 60)
    print("TEST 1: Handle Price - Tokyo")
    print("=" * 60)
    
    mock_call = MockToolCall(
        name="get_ticket_price",
        args={"destination_city": "Tokyo"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Función: {mock_call.name}")
    print(f"Args: {mock_call.args}")
    print(f"Resultado: {result}")
    
    assert result["destination_city"] == "Tokyo"
    assert result["price"] == "$1400"
    
    print("✅ TEST PASADO\n")


def test_handle_price_unknown():
    """Manejar ciudad desconocida"""
    print("=" * 60)
    print("TEST 2: Handle Price - Ciudad Desconocida")
    print("=" * 60)
    
    mock_call = MockToolCall(
        name="get_ticket_price",
        args={"destination_city": "Madrid"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Resultado: {result}")
    
    assert result["destination_city"] == "Madrid"
    assert result["price"] == "Unknown"
    
    print("✅ TEST PASADO\n")


# ============================================================================
# TESTS DE LA HERRAMIENTA DE ESTADOS (PRÁCTICA 2)
# ============================================================================

def test_handle_status_fa202():
    """PRUEBA 2 PRÁCTICA 2: Nueva Funcionalidad - FA202"""
    print("=" * 60)
    print("TEST 3: Handle Status - FA202")
    print("=" * 60)
    
    mock_call = MockToolCall(
        name="get_flight_status",
        args={"flight_number": "FA202"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Función: {mock_call.name}")
    print(f"Args: {mock_call.args}")
    print(f"Resultado: {result}")
    
    assert result["flight_number"] == "FA202"
    assert result["status"] == "Delayed 2 hours"
    
    print("✅ TEST PASADO\n")


def test_handle_status_unknown():
    """Manejar vuelo desconocido"""
    print("=" * 60)
    print("TEST 4: Handle Status - Vuelo Desconocido")
    print("=" * 60)
    
    mock_call = MockToolCall(
        name="get_flight_status",
        args={"flight_number": "FA999"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Resultado: {result}")
    
    assert result["flight_number"] == "FA999"
    assert result["status"] == "Status Unknown"
    
    print("✅ TEST PASADO\n")


def test_handle_all_flight_statuses():
    """Verificar todos los estados de vuelos"""
    print("=" * 60)
    print("TEST 5: Todos los Estados de Vuelos")
    print("=" * 60)
    
    test_cases = [
        ("FA101", "On Time"),
        ("FA202", "Delayed 2 hours"),
        ("FA303", "Cancelled"),
        ("FA404", "Boarding"),
    ]
    
    for flight_num, expected_status in test_cases:
        mock_call = MockToolCall(
            name="get_flight_status",
            args={"flight_number": flight_num}
        )
        
        result = handle_tool_call(mock_call)
        print(f"{flight_num} → {result['status']}")
        
        assert result["status"] == expected_status
    
    print("✅ TEST PASADO\n")


# ============================================================================
# TESTS DE SELECCIÓN DINÁMICA (IF/ELIF)
# ============================================================================

def test_handler_selects_correct_function():
    """Verificar que el handler elige la función correcta"""
    print("=" * 60)
    print("TEST 6: Selección Dinámica de Función")
    print("=" * 60)
    
    # Llamada a precios
    price_call = MockToolCall(
        name="get_ticket_price",
        args={"destination_city": "Berlin"}
    )
    price_result = handle_tool_call(price_call)
    
    assert "price" in price_result
    assert "destination_city" in price_result
    assert "status" not in price_result  # No debe tener campos de vuelos
    print("✅ get_ticket_price ejecuta la lógica correcta")
    
    # Llamada a estados
    status_call = MockToolCall(
        name="get_flight_status",
        args={"flight_number": "FA101"}
    )
    status_result = handle_tool_call(status_call)
    
    assert "status" in status_result
    assert "flight_number" in status_result
    assert "price" not in status_result  # No debe tener campos de precios
    print("✅ get_flight_status ejecuta la lógica correcta")
    
    print("✅ TEST PASADO\n")


def test_handler_invalid_function():
    """Verificar manejo de función inválida"""
    print("=" * 60)
    print("TEST 7: Función Inválida")
    print("=" * 60)
    
    mock_call = MockToolCall(
        name="funcion_inexistente",
        args={"param": "valor"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Resultado: {result}")
    
    assert "error" in result
    assert "funcion_inexistente" in result["error"]
    
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE handler.py (Práctica 1 + 2)\n")
    
    try:
        # Tests Práctica 1 (regresión)
        test_handle_price_tokyo()
        test_handle_price_unknown()
        
        # Tests Práctica 2 (nueva funcionalidad)
        test_handle_status_fa202()
        test_handle_status_unknown()
        test_handle_all_flight_statuses()
        
        # Tests de integración
        test_handler_selects_correct_function()
        test_handler_invalid_function()
        
        print("=" * 60)
        print("🎉 TODOS LOS TESTS DE handler.py PASARON")
        print("=" * 60)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)