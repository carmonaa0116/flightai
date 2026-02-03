"""
test_tool_schema.py
-------------------
Tests para el módulo tool_schema.py
"""


def test_imports():
    """Test 1: Verificar que las importaciones funcionan"""
    print("=" * 60)
    print("TEST 1: Importaciones")
    print("=" * 60)
    
    try:
        from google.genai import types
        print("✅ google.genai.types importado")
        
        from tool_schema import tools, get_ticket_price_func
        print("✅ tool_schema importado")
        
        print("✅ TEST PASADO\n")
        return True
        
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("💡 Ejecuta: pip install google-genai")
        return False


def test_function_name():
    """Test 2: Verificar nombre de función"""
    print("=" * 60)
    print("TEST 2: Nombre de Función")
    print("=" * 60)
    
    from tool_schema import get_ticket_price_func
    
    assert get_ticket_price_func.name == "get_ticket_price"
    print(f"✅ Nombre: {get_ticket_price_func.name}")
    print("✅ TEST PASADO\n")


def test_function_description():
    """Test 3: Verificar descripción"""
    print("=" * 60)
    print("TEST 3: Descripción")
    print("=" * 60)
    
    from tool_schema import get_ticket_price_func
    
    assert get_ticket_price_func.description
    assert len(get_ticket_price_func.description) > 20
    print(f"✅ Descripción presente ({len(get_ticket_price_func.description)} caracteres)")
    print("✅ TEST PASADO\n")


def test_parameters():
    """Test 4: Verificar parámetros"""
    print("=" * 60)
    print("TEST 4: Parámetros")
    print("=" * 60)
    
    from tool_schema import get_ticket_price_func
    
    params = get_ticket_price_func.parameters
    
    # Verificar estructura
    assert params["type"] == "object"
    print("✅ Tipo: object")
    
    # Verificar destination_city existe
    assert "destination_city" in params["properties"]
    print("✅ Parámetro 'destination_city' existe")
    
    # Verificar tipo de destination_city
    assert params["properties"]["destination_city"]["type"] == "string"
    print("✅ Tipo de destination_city: string")
    
    # Verificar que es requerido
    assert "destination_city" in params["required"]
    print("✅ destination_city es requerido")
    
    print("✅ TEST PASADO\n")


def test_tools_list():
    """Test 5: Verificar lista de herramientas"""
    print("=" * 60)
    print("TEST 5: Lista de Herramientas")
    print("=" * 60)
    
    from tool_schema import tools
    from google.genai import types
    
    assert isinstance(tools, list)
    assert len(tools) == 1
    print(f"✅ tools es una lista con {len(tools)} elemento(s)")
    
    # Verificar que el primer elemento es un Tool
    assert isinstance(tools[0], types.Tool)
    print("✅ tools[0] es un objeto Tool")
    
    # Verificar que tiene function_declarations
    assert hasattr(tools[0], 'function_declarations')
    assert len(tools[0].function_declarations) > 0
    print(f"✅ Tiene {len(tools[0].function_declarations)} function_declaration(s)")
    
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE tool_schema.py\n")
    
    try:
        if not test_imports():
            print("\n❌ ABORTADO: Faltan dependencias\n")
            exit(1)
        
        test_function_name()
        test_function_description()
        test_parameters()
        test_tools_list()
        
        print("=" * 60)
        print("🎉 TODOS LOS TESTS DE tool_schema.py PASARON")
        print("=" * 60)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)