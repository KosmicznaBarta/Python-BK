while True:
    user_input = input("Podaj liczbę rzeczywistą (wpisanie 'stop' zamknie program): ")

    if user_input.lower() == "stop":
        print("Zakończono działanie programu")
        break

    try:
        x = float(user_input)
        print(f"Trzecia potęga wpisanej liczby {x} to: {x**3}")
    except ValueError:
        print("Błąd: Wpisana wartość nie jest liczbą rzeczywistą.")