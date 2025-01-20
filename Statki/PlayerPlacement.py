import tkinter as tk
from RandomPlacement import RandomShips
from tkinter import messagebox
          
class ShipPlacement:
    def __init__(self, selection_window, game_window, board_size=10, ship_sizes=None):
        self.selection_window = selection_window
        self.selection_window.title("Gra w statki")
        self.game_window = game_window
        self.selection_window.resizable(False, False)
        self.selection_window.protocol("WM_DELETE_WINDOW", self.exit_game)
        self.board_size = board_size
        self.ship_sizes = ship_sizes or [5, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]
        self.remaining_ships = {size: self.ship_sizes.count(size) for size in set(self.ship_sizes)}
        self.selected_ship_size = None
        self.current_ship_positions = []
        self.selected_ship_to_remove = []
        self.ship_buttons = {}
        self.board = [[0] * board_size for _ in range(board_size)]
        self.buttons = []

        self.selection_window.grid_columnconfigure(0, weight=1)
        self.selection_window.grid_columnconfigure(2, weight=1)
        self.selection_window.grid_rowconfigure(0, weight=1)

        self.instruction_label = tk.Label(self.selection_window, text="Naciśnij jeden z poniższych przycisków z numerami, aby wybrać odpowiedni rozmiar statku. Następnie kliknij na planszę, aby umieścić statek o wybranej długości.", font=("Arial", 14), wraplength=600)
        self.instruction_label.grid(row=0, column=1, columnspan=self.board_size, pady=(5, 10), sticky="n")

        self.status_label = tk.Label(self.selection_window, text="Wybierz położenie swoich statków.", font=("Arial", 14))
        self.status_label.grid(row=1, column=1, columnspan=self.board_size, pady=(5, 10), sticky="n")

        self.remaining_label = tk.Label(self.selection_window, text=self.get_remaining_text(), font=("Arial", 12))
        self.remaining_label.grid(row=2, column=1, columnspan=self.board_size, pady=(10, 0), sticky="n")

        self.create_ship_selection_buttons()
        self.create_ship_board()

        button_frame = tk.Frame(self.selection_window)
        button_frame.grid(row=self.board_size + 4, column=1, pady=10, columnspan=self.board_size, sticky="n")

        self.random_ships = RandomShips(board_size, ship_sizes=self.ship_sizes)
        self.random_button = tk.Button(button_frame, text="Losuj", command=self.randomize_ships, width=12, height=2)
        self.random_button.grid(row=0, column=0, padx=10)

        self.undo_button = tk.Button(button_frame, text="Cofnij", command=self.undo_ship, state="disabled", width=12, height=2)
        self.undo_button.grid(row=0, column=1, padx=10)

        self.confirm_button = tk.Button(button_frame, text="Zatwierdź", command=self.confirm_ships, state="disabled", width=12, height=2)
        self.confirm_button.grid(row=0, column=2, padx=10)

        empty_frame = tk.Frame(self.selection_window, height=10)
        empty_frame.grid(row=self.board_size + 5, column=1, pady=0, columnspan=self.board_size, sticky="n")

        self.center_window()

    def exit_game(self):
        if messagebox.askyesno("Zamknięcie gry", "Czy na pewno chcesz zakończyć grę?"):
            if self.selection_window.winfo_exists():
                self.selection_window.destroy()
            if self.game_window.winfo_exists():
                self.game_window.destroy()

    def center_window(self):
        self.selection_window.update_idletasks()
        width = self.selection_window.winfo_width()
        height = self.selection_window.winfo_height()
        x = (self.selection_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.selection_window.winfo_screenheight() // 2) - (height // 2)
        self.selection_window.geometry(f"{width}x{height}+{x}+{y}")

    def create_ship_selection_buttons(self):
        frame = tk.Frame(self.selection_window)
        frame.grid(row=3, column=1, columnspan=self.board_size, pady=10, sticky="n")

        for idx, size in enumerate(sorted(set(self.ship_sizes))):
            button = tk.Button(frame, text=f"{size}", command=lambda s=size: self.select_ship_size(s), width=4, height=2)
            button.grid(row=0, column=idx, padx=10)
            self.ship_buttons[size] = button

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

    def create_ship_board(self):
        self.selection_window.grid_columnconfigure(0, weight=1, minsize=30)
        self.selection_window.grid_columnconfigure(self.board_size + 1, weight=1, minsize=30)

        letters_frame = tk.Frame(self.selection_window)
        letters_frame.grid(row=4, column=1, columnspan=self.board_size, pady=(10, 0), sticky="n")

        blank_label = tk.Label(letters_frame, text="", font=("Arial", 12), width=2)
        blank_label.grid(row=0, column=0, sticky="nsew")

        board_frame = tk.Frame(self.selection_window)
        board_frame.grid(row=5, column=1, columnspan=self.board_size, pady=5, sticky="n")

        button_size = 40

        for i in range(self.board_size):
            letter_label = tk.Label(letters_frame, text=chr(65 + i), font=("Arial", 12))
            letter_label.grid(row=0, column=i + 1, padx=12)

            row_buttons = []
            for j in range(self.board_size):
                number_label = tk.Label(board_frame, text=str(j + 1), font=("Arial", 12), width=2)
                number_label.grid(row=j + 1, column=0, sticky="e")
                button = tk.Button(board_frame, width=button_size // 10, height=button_size // 20, bg="lightblue",
                                    command=lambda x=i, y=j: self.place_or_select_ship(x, y))
                button.grid(row=i + 1, column=j + 1, sticky="nsew", padx=1, pady=1)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        for i in range(self.board_size):
            board_frame.grid_rowconfigure(i + 1, weight=1)
            board_frame.grid_columnconfigure(i + 1, weight=1)

    def select_ship_size(self, size):
        self.cancel_incomplete_ship()

        for ship_size, button in self.ship_buttons.items():
            if self.remaining_ships[ship_size] > 0:
                button.config(bg="#f0f0f0")

        self.ship_buttons[size].config(bg="lightgrey")
        self.selected_ship_size = size
        self.status_label.config(text=f"Wybrano statek o długości {size}.")

    def place_or_select_ship(self, x, y):
        if self.board[x][y] == 1:
            self.select_ship_to_remove(x, y)
            return

        if not self.selected_ship_size:
            self.status_label.config(text="Najpierw wybierz rozmiar statku!")
            return

        self.cannot_place_ship(x, y)

    def randomize_ships(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j] = 0
                self.buttons[i][j].config(bg="lightblue")

        self.random_ships.place_ships_with_shapes(self.board)
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == 1:
                    self.buttons[x][y].config(bg="darkblue")

        self.remaining_ships = {size: 0 for size in self.remaining_ships.keys()}
        self.update_remaining_label_button()
        self.status_label.config(text="Wylosowano pozycję statków.")
        self.check_ready_to_confirm_button()

    def select_ship_to_remove(self, x, y):
        ship_positions = self.find_connected_ship(x, y)
        if not ship_positions or any(pos in self.current_ship_positions for pos in ship_positions):
            return

        if self.selected_ship_to_remove == ship_positions:
            for sx, sy in self.selected_ship_to_remove:
                self.buttons[sx][sy].config(bg="darkblue")
            self.selected_ship_to_remove = []
            self.undo_button.config(state="disabled")
            return

        if self.selected_ship_to_remove:
            for sx, sy in self.selected_ship_to_remove:
                self.buttons[sx][sy].config(bg="darkblue")

        self.selected_ship_to_remove = ship_positions
        for sx, sy in self.selected_ship_to_remove:
            self.buttons[sx][sy].config(bg="green")

        self.undo_button.config(state="normal")

    def find_connected_ship(self, x, y):
        if self.board[x][y] != 1:
            return []

        ship_positions = []
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) not in ship_positions and self.board[cx][cy] == 1:
                ship_positions.append((cx, cy))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                        stack.append((nx, ny))

        return ship_positions

    def cannot_place_ship(self, x, y):
        if not self.selected_ship_size:
            return

        if not self.can_place_ship(x, y):
            self.status_label.config(text="Nie możesz położyć statku obok innego statku!")
            return

        self.place_ship(x, y)
        self.check_ready_to_confirm_button()

    def place_ship(self, x, y):
        self.current_ship_positions.append((x, y))
        self.board[x][y] = 1
        self.buttons[x][y].config(bg="grey")

        if len(self.current_ship_positions) == self.selected_ship_size:
            for sx, sy in self.current_ship_positions:
                self.buttons[sx][sy].config(bg="darkblue")
            self.remaining_ships[self.selected_ship_size] -= 1
            self.current_ship_positions = []
            self.update_remaining_label_button()

            if self.remaining_ships[self.selected_ship_size] <= 0:
                self.status_label.config(text=f"Postawione zostały wszystkie statki o długości {self.selected_ship_size}.")
                self.ship_buttons[self.selected_ship_size].config(bg="SystemButtonFace")
                self.selected_ship_size = None

    def cancel_incomplete_ship(self):
        if self.current_ship_positions:
            for x, y in self.current_ship_positions:
                self.board[x][y] = 0
                self.buttons[x][y].config(bg="lightblue")
            self.current_ship_positions = []

    def undo_ship(self):
        if not self.selected_ship_to_remove:
            return

        for x, y in self.selected_ship_to_remove:
            self.board[x][y] = 0
            self.buttons[x][y].config(bg="lightblue")

        ship_size = len(self.selected_ship_to_remove)
        self.remaining_ships[ship_size] += 1
        self.update_remaining_label_button()

        self.selected_ship_to_remove = []
        self.undo_button.config(state="disabled")
        self.status_label.config(text=f"Pomyślnie cofnięto położenie statku o długości {ship_size}.")

    def can_place_ship(self, x, y):
        if self.board[x][y] == 1:
            return False

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size: 
                    if (nx, ny) not in self.current_ship_positions and self.board[nx][ny] == 1:
                        return False

        if len(self.current_ship_positions) == 0:
            return True

        for segment_x, segment_y in self.current_ship_positions:
            if abs(segment_x - x) + abs(segment_y - y) == 1:
                return True

        return False

    def update_remaining_label_button(self):
        self.remaining_label.config(text=self.get_remaining_text())

        for ship_size, button in self.ship_buttons.items():
            if self.remaining_ships[ship_size] > 0:
                button.config(state="normal")
            else:
                button.config(state="disabled")

    def get_remaining_text(self):
        if all(count == 0 for count in self.remaining_ships.values()):
            return "Postawiono wszystkie statki!"
        return "Pozostałe statki do postawienia: " + ", ".join(f"{size}: {count}" for size, count in self.remaining_ships.items() if count > 0)

    def check_ready_to_confirm_button(self):
        if all(count == 0 for count in self.remaining_ships.values()):
            self.confirm_button.config(state="normal")
        else:
            self.confirm_button.config(state="disabled")

    def confirm_ships(self):
        self.selection_window.destroy()