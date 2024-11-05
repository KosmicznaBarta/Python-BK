def odwracanie_iteracyjnie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def test_odwracanie_iteracyjnie():
    L = [1, 2, 3, 4, 5]
    odwracanie_iteracyjnie(L, 1, 3)
    assert L == [1, 4, 3, 2, 5], "Test 1 nie przeszedł"

    L = [1, 2, 3, 4, 5]
    odwracanie_iteracyjnie(L, 0, 4)
    assert L == [5, 4, 3, 2, 1], "Test 2 nie przeszedł"

    L = [10, 11, 12, 13, 14, 15]
    odwracanie_iteracyjnie(L, 1, 4)
    assert L == [10, 14, 13, 12, 11, 15], "Test 3 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie dla iteracji")

test_odwracanie_iteracyjnie()



def odwracanie_rekurencyjnie(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjnie(L, left + 1, right - 1)

def test_odwracanie_rekurencyjnie():
    L = [1, 2, 3, 4, 5]
    odwracanie_rekurencyjnie(L, 1, 3)
    assert L == [1, 4, 3, 2, 5], "Test 1 nie przeszedł"

    L = [1, 2, 3, 4, 5]
    odwracanie_rekurencyjnie(L, 0, 4)
    assert L == [5, 4, 3, 2, 1], "Test 2 nie przeszedł"

    L = [10, 11, 12, 13, 14, 15]
    odwracanie_rekurencyjnie(L, 1, 4)
    assert L == [10, 14, 13, 12, 11, 15], "Test 3 nie przeszedł"
    print("Wszystkie testy przeszły pomyślnie dla rekurencji")

test_odwracanie_rekurencyjnie()