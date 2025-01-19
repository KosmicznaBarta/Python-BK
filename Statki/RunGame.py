import tkinter as tk
from GameShips import BattleshipGame
          
if __name__ == "__main__":
    game_window = tk.Tk()
    BattleshipGame(game_window)
    game_window.mainloop()