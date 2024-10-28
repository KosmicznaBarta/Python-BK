#Metoda 1
roman_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

#Metoda 2
roman_keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic_values = [1, 5, 10, 50, 100, 500, 1000]

roman_to_arabic = dict(zip(roman_keys, arabic_values))

#Funkcja
def roman2int(roman):
    roman_to_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_to_arabic[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total 

print(roman2int("III")) #3
print(roman2int("IX")) #9
print(roman2int("LVIII")) #58
print(roman2int("MCMXCIV")) #1994