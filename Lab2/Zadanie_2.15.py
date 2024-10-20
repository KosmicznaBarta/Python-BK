def create_string(L):
    return ''.join(str(num) for num in L)

L = [123, 45, 6789, 1000, 966]
result = create_string(L)

print(f"Lista liczb: {L}")
print(f"Ciąg cyfr: {result}")
