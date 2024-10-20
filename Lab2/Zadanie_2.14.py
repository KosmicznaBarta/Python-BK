def max_word(line):
    words = line.split()
    longest = max(words, key=len)
    return longest

def length_max_word(line):
    words = line.split()
    return len(max(words, key=len)) 

line = "Super długie zdanie dla krótkich słów"
result_max = max_word(line)
result_length = length_max_word(line)

print(f"Zdanie: {line}")
print(f"Najdłuższe słowo: {result_max}")
print(f"Długość najdłuższego słowa: {result_length}")
