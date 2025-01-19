README: Gra w Statki
Autor: Bartosz Kosmala

O czym jest program?:
Program to aplikacja stworzona w Pythonie z wykorzystaniem biblioteki tkinter, która umożliwia rozgrywanie strategicznej gry w statki przeciwko komputerowi. Gracz rozmieszcza swoje statki na planszy, a następnie próbuje zniszczyć flotę komputera poprzez oddawanie strzałów na wybrane współrzędne planszy przeciwnika.

Jak uruchomić program?:
Aby uruchomić grę, w terminalu należy użyć komendy:
python RunGame.py

Opis plików programu:
1. PlayerPlacement.py - Klasa ShipPlacement
Moduł odpowiedzialny za rozmieszczanie statków przez gracza na planszy z przyciskami. Umożliwia manualne umieszczanie statków o rozmiarach 1, 2, 3 i 5 pól w różnych kierunkach. Dodatkowo umożliwia losowe rozmieszczenie statków z wykorzystaniem klasy RandomShips. Klasa weryfikuje poprawność rozmieszczenia statków oraz informuje gracza o błędach i poprawności rozmieszczenia.

2. GameShips.py - Klasa BattleshipGame
Główna klasa odpowiedzialna za przebieg rozgrywki. Klasa zapewnia inicjalizację planszy dla gracza i komputera, obsługę strzałów, obsługę tur, weryfikację trafień i zatopień, aktualizację wyników w czasie rzeczywistym, sprawdzanie stanu gry i kończenie rozgrywki oraz mechanizm restartowania gry.

3. RandomPlacement.py - Klasa RandomShips
Moduł odpowiedzialny za losowe rozmieszczanie statków na planszy. Zapewnia rozmieszczanie statków gracza i komputera w sposób zgodny z zasadami gry, obsługuje zarówno proste, jak i nieregularne kształty statków oraz weryfikuje, czy statki nie nachodzą na siebie i są rozmieszczone poprawnie.

4. RunGame.py
Plik startowy gry. Uruchamia aplikację i inicjuje główne okno aplikacji i moduł główny gry BattleshipGame.

Zasady gry w Statki:
1. Każdy gracz dysponuje planszą o wymiarach 10x10.
2. Flota każdego gracza składa się z: 1 statku o rozmiarze 5 pól, 2 statków o rozmiarze 3 pól, 3 statków o rozmiarze 2 pól, 5 statków o rozmiarze 1 pola.
3. Statki mogą być rozmieszczane w dowolnym kierunku (nie tylko poziomo/pionowo) o dowolnym kształcie. Statki muszą być oddzielone od siebie co najmniej jednym polem.
4. Gracz oddaje strzały na planszy przeciwnika, próbując trafić w jego statki. Trafienie w statek oznaczane jest kolorem czerwonym, a pudło kolorem szarym. Po każdym strzale, niezależnie czy trafionym czy nie, tura przechodzi do przeciwnika.
5. Każdy trafiony strzał dodaje do przelicznika ‘Trafiony’ punkt. Gdy Gracz trafi we wszystkie pola danego statku, do przelicznika ‘Zatopiony’ dodawany jest jeden punkt.
6. Wygrywa gracz, który jako pierwszy zatopi wszystkie statki przeciwnika. Gra kończy się komunikatem z możliwością rozpoczęcia nowej rozgrywki.
7. Istnieje możliwość zakończenia gry walkowerem. Wystarczy w trakcie gry z komputerem nacisnąć przycisk F12.


