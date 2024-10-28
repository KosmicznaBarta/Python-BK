def sum_sequence(sequences):
    return [sum(sequence) for sequence in sequences]

sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = sum_sequence(sequence)

print("Suma liczb w sekwencjach:", result)