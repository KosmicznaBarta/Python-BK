def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def test_fibonacci():
    assert fibonacci(0) == 0, "Test 1 nie przeszedł"
    assert fibonacci(1) == 1, "Test 2 nie przeszedł"
    assert fibonacci(5) == 5, "Test 3 nie przeszedł"
    assert fibonacci(10) == 55, "Test 4 nie przeszedł"
    assert fibonacci(15) == 610, "Test 5 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie")

test_fibonacci()