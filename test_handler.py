"""
test_handler.py
---------------
Tests para el módulo handler.py
Ejecutar con: python test_handler.py
"""

from handler import handle_tool_call


class MockToolCall:
    """Mock de un tool_call de Gemini para testing"""
    def __init__(self, name, args):
        self.name = name
        self.args = args


def test_handle_valid_call():
    """Test 1: Manejar llamada válida"""
    print("=" * 50)
    print("TEST 1: Llamada Válida")
    print("=" * 50)
    
    # Simular tool_call de Gemini
    mock_call = MockToolCall(
        name="get_ticket_price",
        args={"destination_city": "Paris"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Función: {mock_call.name}")
    print(f"Args: {mock_call.args}")
    print(f"Resultado: {result}")
    
    assert result == "$899"
    print("✅ TEST PASADO\n")


def test_handle_unknown_city():
    """Test 2: Manejar ciudad desconocida"""
    print("=" * 50)
    print("TEST 2: Ciudad Desconocida")
    print("=" * 50)
    
    mock_call = MockToolCall(
        name="get_ticket_price",
        args={"destination_city": "Madrid"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Función: {mock_call.name}")
    print(f"Args: {mock_call.args}")
    print(f"Resultado: {result}")
    
    assert result == "Unknown"
    print("✅ TEST PASADO\n")


def test_handle_case_insensitive():
    """Test 3: Manejar diferentes mayúsculas"""
    print("=" * 50)
    print("TEST 3: Case Insensitive")
    print("=" * 50)
    
    test_cases = ["Berlin", "berlin", "BERLIN"]
    
    for city in test_cases:
        mock_call = MockToolCall(
            name="get_ticket_price",
            args={"destination_city": city}
        )
        result = handle_tool_call(mock_call)
        print(f"Ciudad: {city} → Resultado: {result}")
        assert result == "$499"
    
    print("✅ TEST PASADO\n")


def test_handle_invalid_function():
    """Test 4: Manejar función inválida"""
    print("=" * 50)
    print("TEST 4: Función Inválida")
    print("=" * 50)
    
    mock_call = MockToolCall(
        name="funcion_inexistente",
        args={"param": "valor"}
    )
    
    result = handle_tool_call(mock_call)
    
    print(f"Función: {mock_call.name}")
    print(f"Resultado: {result}")
    
    assert "Error" in result
    assert "funcion_inexistente" in result
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE handler.py\n")
    
    try:
        test_handle_valid_call()
        test_handle_unknown_city()
        test_handle_case_insensitive()
        test_handle_invalid_function()
        
        print("=" * 50)
        print("🎉 TODOS LOS TESTS DE handler.py PASARON")
        print("=" * 50)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)