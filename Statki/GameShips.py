import tkinter as tk
from tkinter import messagebox
import random
from PlayerPlacement import ShipPlacement
from RandomPlacement import RandomShips

class BattleshipGame:
    def __init__(self, game_window):
        try:
            if not game_window.winfo_exists():
                return 
        
            self.game_window = game_window
            self.game_window.title("Gra w statki")
            self.game_window.protocol("WM_DELETE_WINDOW", self.exit_game)
            self.game_window.resizable(False, False)

            self.game_window.bind("<F12>", self.end_game_walkover)

            self.board_size = 10
            self.ship_sizes = [5, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]

            self.player_board = self.get_player_board()
            self.computer_board = [[0] * self.board_size for _ in range(self.board_size)]
            self.computer_hits = []
            self.is_player_turn = True

            self.player_buttons = []
            self.computer_buttons = []

            self.player_score = {"Trafione": 0, "Zatopione": 0}
            self.computer_score = {"Trafione": 0, "Zatopione": 0}
            self.current_turn = "Gracz"

            self.status_label = tk.Label(self.game_window, text="Gracz 1 zaczyna rozgrywkę", font=("Arial", 14))
            self.status_label.grid(row=0, column=0, columnspan=self.board_size * 2 + 4)

            self.score_label = tk.Label(self.game_window, text="", font=("Arial", 14))
            self.score_label.grid(row=self.board_size + 4, column=0, columnspan=self.board_size * 2 + 4)

            self.create_boards()
            self.random_ships = RandomShips(self.board_size, self.ship_sizes)
            self.random_ships.place_ships_with_shapes(self.computer_board)
            self.center_window()
        except tk.TclError:
            pass

    def exit_game(self):
        if messagebox.askyesno("Zamknięcie gry", "Czy na pewno chcesz zakończyć grę?"):
            self.game_window.destroy()

    def end_game_walkover(self, event):
        if not self.game_window.winfo_exists():
            return
        
        result = messagebox.askquestion("Koniec Gry!", "Walkower!\nGracz zakończył grę wcześniej.\nCzy chcesz rozpocząć nową grę?", type="yesno")
            
        if result == "yes":
            self.restart_game()
        else:
            self.game_window.destroy()

    def center_window(self):
        self.game_window.update_idletasks()
        width = self.game_window.winfo_width()
        height = self.game_window.winfo_height()
        x = (self.game_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.game_window.winfo_screenheight() // 2) - (height // 2)
        self.game_window.geometry(f"{width}x{height}+{x}+{y}")

    def get_player_board(self):
        try:
            setup_root = tk.Toplevel(self.game_window)
            self.game_window.withdraw()
            placement = ShipPlacement(setup_root, self.game_window, self.board_size, self.ship_sizes)
            setup_root.wait_window()
            self.game_window.deiconify()
            return placement.board
        except tk.TclError:
            return [[0] * self.board_size for _ in range(self.board_size)]

    def create_boards(self):
        tk.Label(self.game_window, text="Twoja plansza", font=("Arial", 16), anchor="center").grid(row=1, column=0, columnspan=self.board_size, pady=(0, 5), padx=(72, 0))
        for i in range(self.board_size):
            row_buttons = []
            for j in range(self.board_size):
                bg_color = "yellow" if self.player_board[i][j] == 1 else "lightblue"
                button = tk.Button(self.game_window, width=4, height=2, bg=bg_color)
                button.grid(row=i + 3, column=j + 1)
                row_buttons.append(button)
            self.player_buttons.append(row_buttons)

        separator_frame = tk.Frame(self.game_window, width=20)
        separator_frame.grid(row=3, column=self.board_size + 1, rowspan=self.board_size)

        tk.Label(self.game_window, text="Plansza przeciwnika", font=("Arial", 16), anchor="center").grid(row=1, column=self.board_size + 3, columnspan=self.board_size, pady=(0, 5), padx=(0, 0))
        for i in range(self.board_size):
            row_buttons = []
            for j in range(self.board_size):
                button = tk.Button(self.game_window, width=4, height=2, bg="lightblue",
                                command=lambda x=i, y=j: self.player_guess(x, y))
                button.grid(row=i + 3, column=j + self.board_size + 3)
                row_buttons.append(button)
            self.computer_buttons.append(row_buttons)

        tk.Label(self.game_window, text=" ", font=("Arial", 16)).grid(row=1, column=self.board_size * 2 + 3, rowspan=self.board_size, padx=(0, 10))

        for i in range(self.board_size):
            tk.Label(self.game_window, text=chr(65 + i), font=("Arial", 10)).grid(row=2, column=i + 1)
            tk.Label(self.game_window, text=i + 1, font=("Arial", 10)).grid(row=i + 3, column=0, padx=(20, 0))
            tk.Label(self.game_window, text=chr(65 + i), font=("Arial", 10)).grid(row=2, column=self.board_size + 3 + i)
            tk.Label(self.game_window, text=i + 1, font=("Arial", 10)).grid(row=i + 3, column=self.board_size + 2)

        score_frame = tk.Frame(self.game_window)
        score_frame.grid(row=self.board_size + 4, column=0, columnspan=self.board_size * 2 + 4)

        tk.Label(self.game_window, text="", font=("Arial", 4)).grid(row=self.board_size + 3, column=0, columnspan=self.board_size * 2 + 4)
        tk.Label(self.game_window, text="", font=("Arial", 4)).grid(row=self.board_size + 5, column=0, columnspan=self.board_size * 2 + 4)
        
        tk.Label(score_frame, text="Gracz 1:", font=("Arial", 14)).grid(row=0, column=0)
        self.player_score_label = tk.Label(score_frame, text="", font=("Arial", 14))
        self.player_score_label.grid(row=0, column=1, padx=(0, 40))

        self.score_label.grid(row=self.board_size + 5, column=0, columnspan=self.board_size * 2 + 4)
        tk.Label(self.game_window, text="|", font=("Arial", 14)).grid(row=self.board_size + 4, column=self.board_size + 1)

        tk.Label(score_frame, text="Gracz 2:", font=("Arial", 14)).grid(row=0, column=2, padx=(70, 0))
        self.computer_score_label = tk.Label(score_frame, text="", font=("Arial", 14))
        self.computer_score_label.grid(row=0, column=3)

        self.status_label.grid(row=0, column=0, columnspan=self.board_size * 2 + 4)
        self.score_label.grid(row=self.board_size + 4, column=0, columnspan=self.board_size * 2 + 4)

        self.update_score()

    def toggle_buttons(self, is_player_turn):
        for row in self.player_buttons:
            for button in row:
                button.config(state="disabled" if not is_player_turn else "normal")

        for row in self.computer_buttons:
            for button in row:
                button.config(state="normal" if is_player_turn else "disabled")

    def is_adjacent_to_sunk_ship(self, x, y, board):
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size and board[nx][ny] == -1:
                return True
        return False
    
    def mark_neighbors_as_checked(self, x, y, board):
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if random.random() < 0.1:
                    continue
                if board[nx][ny] == 0:
                    board[nx][ny] = -2

    def player_guess(self, x, y):
        if not self.is_player_turn or self.computer_buttons[x][y]["state"] == "disabled":
            return
        
        if self.computer_buttons[x][y]["bg"] in ["red", "grey"]:
            return
        
        self.toggle_buttons(is_player_turn=False) 
        self.is_player_turn = False 

        if self.computer_board[x][y] == 1:
            self.computer_buttons[x][y].config(bg="red")
            self.computer_board[x][y] = -1
            self.player_score["Trafione"] += 1
            self.status_label.config(text="Trafiony!")
            if self.check_if_sunk(x, y, self.computer_board, self.ship_sizes, is_computer=True):
                self.status_label.config(text="Trafiony! Zatopiony!")
        if self.computer_board[x][y] == 0:
            self.computer_buttons[x][y].config(bg="grey")
            self.computer_board[x][y] = -2
            self.status_label.config(text="Pudło!")

        self.computer_buttons[x][y]["state"] = "disabled"
        self.update_score()

        self.end_game()

        self.game_window.after(1000, lambda: self.status_label.config(text="Ruch Gracza 2..."))
        self.game_window.update()
        self.current_turn = "Computer"
        self.game_window.after(2000, self.computer_turn)

    def computer_turn(self):
        self.toggle_buttons(is_player_turn=False)
        self.game_window.update()

        move_made = False            

        while not move_made:
            if self.computer_hits:
                x, y = self.computer_hits[-1]
                found_next_target = False
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                        if self.player_board[nx][ny] == 1:
                            self.player_buttons[nx][ny].config(bg="red")
                            self.player_board[nx][ny] = -1
                            self.computer_score["Trafione"] += 1
                            self.computer_hits.append((nx, ny))
                            self.status_label.config(text="Trafiony!")
                            if self.check_if_sunk(nx, ny, self.player_board, self.ship_sizes, is_computer=False):
                                self.status_label.config(text="Trafiony! Zatopiony!")
                                for px, py in self.computer_hits:
                                    self.mark_neighbors_as_checked(px, py, self.player_board)
                                self.computer_hits.clear()
                            found_next_target = True
                            move_made = True
                            break
                
                if not found_next_target:
                    self.computer_hits.pop()

            else:
                x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
                if self.player_board[x][y] == 0:
                    self.player_buttons[x][y].config(bg="grey")
                    self.player_board[x][y] = -2
                    self.status_label.config(text="Pudło!")
                    move_made = True
                elif self.player_board[x][y] == 1:
                    self.player_buttons[x][y].config(bg="red")
                    self.player_board[x][y] = -1
                    self.computer_score["Trafione"] += 1
                    self.computer_hits.append((x, y))
                    self.status_label.config(text="Trafiony!")
                    if self.check_if_sunk(x, y, self.player_board, self.ship_sizes, is_computer=False):
                        self.status_label.config(text="Trafiony! Zatopiony!")
                        self.mark_neighbors_as_checked(x, y, self.player_board)
                        self.computer_hits.clear()
                    move_made = True

        self.game_window.update()
        self.game_window.after(1000, lambda: self.status_label.config(text="Ruch Gracza 1..."))
        self.is_player_turn = True
        self.current_turn = "Player"
        self.toggle_buttons(is_player_turn=True)
        self.update_score()
        
        self.end_game()

    def check_if_sunk(self, x, y, board, ship_sizes, is_computer):
        def find_ship(x, y):
            ship_coordinates = []
            queue = [(x, y)]
            visited = set()

            while queue:
                cx, cy = queue.pop(0)
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))

                if 0 <= cx < self.board_size and 0 <= cy < self.board_size and board[cx][cy] in [1, -1]:
                    ship_coordinates.append((cx, cy))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.append((cx + dx, cy + dy))

            return ship_coordinates

        ship_coordinates = find_ship(x, y)
        all_hit = all(board[cx][cy] == -1 for cx, cy in ship_coordinates)

        if all_hit:
            if is_computer:
                self.player_score["Zatopione"] += 1
            else:
                self.computer_score["Zatopione"] += 1
                for cx, cy in ship_coordinates:
                    self.mark_neighbors_as_checked(cx, cy, board)

            return True
        
        return False

    def update_score(self):
        self.player_score_label.config(text=f"Trafione = {self.player_score['Trafione']}, Zatopione = {self.player_score['Zatopione']}")
        self.computer_score_label.config(text=f"Trafione = {self.computer_score['Trafione']}, Zatopione = {self.computer_score['Zatopione']}")

        if self.status_label.cget("text") == "Gracz 1 zaczyna rozgrywkę":
            return
    
        if self.current_turn == "Computer":
            self.status_label.config(text="Ruch Gracza 2...")
        elif self.current_turn == "Gracz" and "Trafiony" not in self.status_label.cget("text") and "Pudło" not in self.status_label.cget("text"):
            self.status_label.config(text="Ruch Gracza 1...")

    def end_game(self):
        total_ship_cells = sum(self.ship_sizes)
        if (self.player_score["Trafione"] == total_ship_cells or self.computer_score["Trafione"] == total_ship_cells) and \
           (self.player_score["Zatopione"] == len(self.ship_sizes) or self.computer_score["Zatopione"] == len(self.ship_sizes)):
            
            winner = "Gracz 1" if self.player_score["Trafione"] == total_ship_cells else "Gracz 2"
            result = messagebox.askquestion("Koniec Gry", f"Gratulacje!!! Wygrał {winner}! Czy chcesz rozpocząć nową grę?", type="yesno")

            if result == "yes":
                self.restart_game()
            else:
                self.game_window.destroy()

    def restart_game(self):
        if not self.game_window.winfo_exists():
            return

        for widget in self.game_window.winfo_children():
            widget.destroy()

        try:
            self.__init__(self.game_window)
        except tk.TclError:
            pass