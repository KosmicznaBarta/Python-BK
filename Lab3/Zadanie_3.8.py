def find_common_and_all(table1, table2):
    common = sorted(list(set(table1) & set(table2)))
    all = sorted(list(set(table1) | set(table2)))

    return common, all

table1 = [1, 4, 60, 201, 34]
table2 = [4, 18, 201, 57, 9]

common, all = find_common_and_all(table1, table2)

print("Wspólne elementy:", common)
print("Wszystkie elementy:", all)