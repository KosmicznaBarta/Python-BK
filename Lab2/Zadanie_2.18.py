def find_zeros(number):
    return str(number).count('0')

number = 10420039040751091201
result = find_zeros(number)

print(f"Liczba: {number}")
print(f"Liczba zer: {result}")
