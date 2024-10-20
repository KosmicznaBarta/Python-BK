def count_words(line):
    words = line.split()
    return len(words)

line = "Ania   idzie  do      \nsklepu \n\nzoologicznego."
result = count_words(line)

print(f"Zdanie: {line}")
print(f"Liczba wyrazów w zdaniu: {result}")
