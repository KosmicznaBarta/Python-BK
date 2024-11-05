def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorical():
    assert factorial(0) == 1, "Test 1 nie przeszedł"
    assert factorial(1) == 1, "Test 2 nie przeszedł"
    assert factorial(5) == 120, "Test 3 nie przeszedł"
    assert factorial(6) == 720, "Test 4 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie")

test_factorical()