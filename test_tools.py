"""
test_tools.py
-------------
Tests para el módulo tools.py
Ejecutar con: python test_tools.py
"""

from tools import get_ticket_price


def test_case_insensitive():
    """Test 1: Verificar que 'Berlin' y 'berlin' funcionan igual"""
    print("=" * 50)
    print("TEST 1: Case Insensitive")
    print("=" * 50)
    
    result_berlin = get_ticket_price("Berlin")
    result_berlin_lower = get_ticket_price("berlin")
    result_berlin_upper = get_ticket_price("BERLIN")
    
    print(f"get_ticket_price('Berlin')  → {result_berlin}")
    print(f"get_ticket_price('berlin')  → {result_berlin_lower}")
    print(f"get_ticket_price('BERLIN')  → {result_berlin_upper}")
    
    assert result_berlin == "$499"
    assert result_berlin_lower == "$499"
    assert result_berlin_upper == "$499"
    
    print("✅ TEST PASADO\n")


def test_unknown_city():
    """Test 2: Verificar que una ciudad inexistente devuelve 'Unknown'"""
    print("=" * 50)
    print("TEST 2: Ciudad Inexistente")
    print("=" * 50)
    
    result_madrid = get_ticket_price("Madrid")
    result_barcelona = get_ticket_price("Barcelona")
    
    print(f"get_ticket_price('Madrid')     → {result_madrid}")
    print(f"get_ticket_price('Barcelona')  → {result_barcelona}")
    
    assert result_madrid == "Unknown"
    assert result_barcelona == "Unknown"
    
    print("✅ TEST PASADO\n")


def test_all_known_cities():
    """Test 3: Verificar que todas las ciudades conocidas devuelven precios correctos"""
    print("=" * 50)
    print("TEST 3: Ciudades Conocidas")
    print("=" * 50)
    
    expected_results = {
        "london": "$799",
        "paris": "$899",
        "tokyo": "$1400",
        "berlin": "$499"
    }
    
    for city, expected_price in expected_results.items():
        result = get_ticket_price(city)
        print(f"get_ticket_price('{city}')  → {result}")
        assert result == expected_price
    
    print("✅ TEST PASADO\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE tools.py\n")
    
    try:
        test_case_insensitive()
        test_unknown_city()
        test_all_known_cities()
        
        print("=" * 50)
        print("🎉 TODOS LOS TESTS DE tools.py PASARON")
        print("=" * 50)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)