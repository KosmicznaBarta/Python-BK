def with_underscore(word):
    return '_'.join(word)

word = "Słowo w słowo"
result = with_underscore(word)

print(f"Zdanie: {word}")
print(f"Zdanie ze znakami \'_\': {result}")