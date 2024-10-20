def total_length(line):
    words = line.split()
    return sum(len(word) for word in words)

def last_letters(line):
    words = line.split()
    return ''.join([word[-1] for word in words])

line = "Perfekcyjny przykład zdania"
result = total_length(line)

print(f"Zdanie: {line}")
print(f"Łączna długość: {result}")