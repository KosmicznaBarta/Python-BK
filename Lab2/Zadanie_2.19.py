def three_blocks(L):
    return ''.join(str(num).zfill(3) for num in L)

L = [7, 24, 123, 5, 99, 104, 50]
result = three_blocks(L)

print(f"Lista liczb: {L}")
print(f"Napis z trzycyfrowych bloków: {result}")