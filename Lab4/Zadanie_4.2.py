def make_ruler(n):
    measure = '|'
    for i in range(n):
        measure += '....|'

    numbers = '0'
    for i in range(1, n + 1):
        numbers += f'{i:>5}'

    return measure + '\n' + numbers

def test_make_ruler():
    assert make_ruler(1) == '|....|\n0    1', "Test 1 nie przeszedł"
    assert make_ruler(2) == '|....|....|\n0    1    2', "Test 2 nie przeszedł"
    assert make_ruler(5) == '|....|....|....|....|....|\n0    1    2    3    4    5', "Test 3 nie przeszedł"
    
    print("Wszystkie testy przeszły pomyślnie dla miarki")

test_make_ruler()



def make_grid(rows, cols):
    line_up = '+---' * cols + '+'
    line_middle = "|   " * cols + '|'

    rectangle = ""
    for _ in range(rows):
        rectangle += line_up + '\n' + line_middle + '\n'
    rectangle += line_up

    return rectangle

def test_make_grid():
    assert make_grid(1, 1) == "+---+\n|   |\n+---+", "Test 1 nie przeszedł"
    assert make_grid(2, 2) == "+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+", "Test 2 nie przeszedł"
    assert make_grid(3, 1) == "+---+\n|   |\n+---+\n|   |\n+---+\n|   |\n+---+", "Test 3 nie przeszedł"
    
    print("Wszystkie testy przeszły pomyślnie dla prostokąta")

test_make_grid()