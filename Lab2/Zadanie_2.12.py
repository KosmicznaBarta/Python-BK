def first_letters(line):
    words = line.split()
    return ''.join([word[0] for word in words])

def last_letters(line):
    words = line.split()
    return ''.join([word[-1] for word in words])

line = "Perfekcyjny przykład dla perfekcyjnych słów w zdaniu"
result_first = first_letters(line)
result_last = last_letters(line)

print(f"Zdanie: {line}")
print(f"Słowo z pierwszymi znakami: {result_first}")
print(f"Słowo z ostatnimi znakami: {result_last}")