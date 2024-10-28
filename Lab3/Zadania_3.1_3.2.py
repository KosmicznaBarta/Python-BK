#*Zadanie 3.1*

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Kod jest składniowo poprawny, ale w pythonie znaki średnika ";" są zbędne

for i in "axby": if ord(i) < 100: print (i)

#Kod nie jest składniowo poprawny, ponieważ instrukcja "if" powinna znaleźć się w nowej linii po "for"

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#Kod jest składniowo poprawny


#*Zadanie 3.2*

L = [3, 5, 4] ; L = L.sort()

#L = L.sort() zamiast zwrócić posortowaną tablicę zwróci None. Poprawnie powinno wyglądać L.sort()

x, y = 1, 2, 3

#Liczba zmiennych po lewej stronie nie jest równa liczbie wartości po prawej
#Albo usuwamy wartość 3, albo dodajemy zmienną z

X = 1, 2, 3 ; X[1] = 4

#X zwróci błąd, ponieważ dla X nie możemy zmienić elementów. Najlepiej wartości umieścić w tablicy X = [1, 2, 3]

X = [1, 2, 3] ; X[3] = 4

#Indeks w tablicy zaczyna się od 0 (w przykładzie indeksy [0, 1, 2]), więc nie możemy zamienić wartości 3 indeksu, ponieważ on nie istnieje w tablicy X

X = "abc" ; X.append("d")

#Nie możemy mutować obiektów string, a ciągi znaków nie mają metody append()

L = list(map(pow, range(8)))

#Funkcja pow() wymaga dwóch argumentów: podstawy i wykładnika