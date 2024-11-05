def flatten(sequence):
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
        
    return flat_list

def test_flatten():
    assert flatten([]) == [], "Test 1 nie przeszedł"
    assert flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9], "Test 2 nie przeszedł"
    assert flatten([1, [2, [3, [4, 5]]]]) == [1, 2, 3, 4, 5], "Test 3 nie przeszedł"
    assert flatten([(1, 2), [3, 4], 5]) == [1, 2, 3, 4, 5], "Test 4 nie przeszedł"
    assert flatten([[], [1, [], [2, [3]]], 4]) == [1, 2, 3, 4], "Test 5 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie")

test_flatten()