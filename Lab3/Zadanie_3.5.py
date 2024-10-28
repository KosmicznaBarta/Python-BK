def create_measure(length):
    measure = '|'
    for i in range(length):
        measure += '....|'

    numbers = '0'
    for i in range(1, length + 1):
        numbers += f'{i:>5}'

    return measure + '\n' + numbers

length = int(input("Podaj długość miarki: "))
print(create_measure(length))