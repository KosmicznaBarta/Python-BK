def replace(line):
    return line.replace("GvR", "Guido van Rossum")

line = "Twórcą Pythona jest GvR"
result = replace(line)

print(f"Zdanie: {line}")
print(f"Poprawione zdanie: {result}")
