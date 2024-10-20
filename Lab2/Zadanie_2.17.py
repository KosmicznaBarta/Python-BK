def sort_alphabetically(line):
    words = line.split()
    return sorted(words)

def sort_length(line):
    words = line.split()
    return sorted(words, key=len)

line = "Ania postanowiła pójść do lasu pozbierać grzyby"
result_alphabetically = sort_alphabetically(line)
result_length = sort_length(line)

print(f"Zdanie: {line}")
print(f"Słowa posortowane alfabetycznie: {result_alphabetically}")
print(f"Słowa posortowane pod względem długości: {result_length}")
