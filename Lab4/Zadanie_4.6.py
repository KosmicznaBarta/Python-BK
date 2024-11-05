def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
        
    return total

def test_sum_seq():
    assert sum_seq([]) == 0, "Test 1 nie przeszedł"
    assert sum_seq([1, 2, 3]) == 6, "Test 2 nie przeszedł"
    assert sum_seq([1, [2, 3], 4]) == 10, "Test 3 nie przeszedł"
    assert sum_seq([1, [2, [3, 4]], 5]) == 15, "Test 4 nie przeszedł"
    assert sum_seq((1, (2, (3, 4)), 5)) == 15, "Test 5 nie przeszedł"
    assert sum_seq([1, [2, [3, [4, 5]]]]) == 15, "Test 6 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie")

test_sum_seq()