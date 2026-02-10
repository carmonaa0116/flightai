"""
test_tools.py
-------------
Tests para tools.py (Práctica 1 + Práctica 2)
"""

from tools import (
    get_ticket_price, 
    ticket_prices,
    get_flight_status,
    flight_status_db
)


# ============================================================================
# TESTS DE LA PRÁCTICA 1 (PRECIOS)
# ============================================================================

def test_price_database_exists():
    """Verificar que la base de datos de precios tiene las 4 ciudades"""
    print("=" * 60)
    print("TEST 1: Base de Datos de Precios")
    print("=" * 60)
    
    required_cities = ["london", "paris", "tokyo", "berlin"]
    
    for city in required_cities:
        assert city in ticket_prices, f"❌ Falta la ciudad: {city}"
        print(f"✅ {city}: {ticket_prices[city]}")
    
    print("✅ TEST PASADO\n")


def test_get_ticket_price_tokyo():
    """PRUEBA 1 PRÁCTICA 2: Prueba de Regresión - Tokyo"""
    print("=" * 60)
    print("TEST 2: Regresión - Precio de Tokyo")
    print("=" * 60)
    
    result = get_ticket_price("Tokyo")
    
    assert result == "$1400", f"❌ Esperado '$1400', obtenido '{result}'"
    print(f"Resultado: {result}")
    print("✅ TEST PASADO: Tokyo devuelve $1400\n")


def test_get_ticket_price_unknown():
    """Verificar que ciudades desconocidas devuelven Unknown"""
    print("=" * 60)
    print("TEST 3: Ciudad Desconocida")
    print("=" * 60)
    
    result = get_ticket_price("Madrid")
    
    assert result == "Unknown", f"❌ Esperado 'Unknown', obtenido '{result}'"
    print(f"Madrid → {result}")
    print("✅ TEST PASADO\n")


# ============================================================================
# TESTS DE LA PRÁCTICA 2 (ESTADOS DE VUELOS)
# ============================================================================

def test_flight_status_database_exists():
    """Verificar que la base de datos de vuelos tiene los 4 vuelos"""
    print("=" * 60)
    print("TEST 4: Base de Datos de Vuelos")
    print("=" * 60)
    
    required_flights = ["FA101", "FA202", "FA303", "FA404"]
    
    for flight in required_flights:
        assert flight in flight_status_db, f"❌ Falta el vuelo: {flight}"
        print(f"✅ {flight}: {flight_status_db[flight]}")
    
    print("✅ TEST PASADO\n")


def test_get_flight_status_fa202():
    """PRUEBA 2 PRÁCTICA 2: Nueva Funcionalidad - FA202"""
    print("=" * 60)
    print("TEST 5: Estado del Vuelo FA202")
    print("=" * 60)
    
    result = get_flight_status("FA202")
    
    assert result == "Delayed 2 hours", f"❌ Esperado 'Delayed 2 hours', obtenido '{result}'"
    print(f"FA202 → {result}")
    print("✅ TEST PASADO: FA202 está retrasado 2 horas\n")


def test_get_flight_status_unknown():
    """Verificar que vuelos desconocidos devuelven Status Unknown"""
    print("=" * 60)
    print("TEST 6: Vuelo Desconocido")
    print("=" * 60)
    
    result = get_flight_status("FA999")
    
    assert result == "Status Unknown", f"❌ Esperado 'Status Unknown', obtenido '{result}'"
    print(f"FA999 → {result}")
    print("✅ TEST PASADO\n")


def test_all_flight_statuses():
    """Verificar todos los estados de vuelos"""
    print("=" * 60)
    print("TEST 7: Todos los Estados de Vuelos")
    print("=" * 60)
    
    expected = {
        "FA101": "On Time",
        "FA202": "Delayed 2 hours",
        "FA303": "Cancelled",
        "FA404": "Boarding"
    }
    
    for flight, expected_status in expected.items():
        result = get_flight_status(flight)
        print(f"{flight}: {result}")
        assert result == expected_status
    
    print("✅ TEST PASADO\n")


def test_flight_number_case_sensitive():
    """Los códigos de vuelo son case-sensitive"""
    print("=" * 60)
    print("TEST 8: Case Sensitivity de Vuelos")
    print("=" * 60)
    
    # FA101 existe, fa101 NO
    result_upper = get_flight_status("FA101")
    result_lower = get_flight_status("fa101")
    
    print(f"FA101 → {result_upper}")
    print(f"fa101 → {result_lower}")
    
    assert result_upper == "On Time"
    assert result_lower == "Status Unknown"
    
    print("✅ TEST PASADO: Los códigos son case-sensitive\n")


if __name__ == "__main__":
    print("\n🧪 TESTS DE tools.py (Práctica 1 + 2)\n")
    
    try:
        # Tests Práctica 1
        test_price_database_exists()
        test_get_ticket_price_tokyo()
        test_get_ticket_price_unknown()
        
        # Tests Práctica 2
        test_flight_status_database_exists()
        test_get_flight_status_fa202()
        test_get_flight_status_unknown()
        test_all_flight_statuses()
        test_flight_number_case_sensitive()
        
        print("=" * 60)
        print("🎉 TODOS LOS TESTS DE tools.py PASARON")
        print("=" * 60)
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}\n")
        exit(1)