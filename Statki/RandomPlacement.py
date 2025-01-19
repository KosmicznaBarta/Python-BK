import random

class RandomShips:  
    def __init__(self, board_size, ship_sizes):
        self.board_size = board_size
        self.ship_sizes = ship_sizes

    def place_ships_with_shapes(self, board):
        for size in self.ship_sizes:
            placed = False
            while not placed:
                layout_type = random.choices([0, 1], weights=[25, 75])[0]

                # prosty (0), nieregularny (1)
                if layout_type == 0:
                    # Orientacja: (0 - poziomo, 1 - pionowo)
                    orientation = random.choice([0, 1])
                    if orientation == 0:
                        x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - size)
                    else:
                        x, y = random.randint(0, self.board_size - size), random.randint(0, self.board_size - 1)

                    if self.can_place_ship(board, x, y, size, orientation, place=True):
                        placed = True

                # Nieregularny układ
                else:
                    start_x = random.randint(0, self.board_size - 1)
                    start_y = random.randint(0, self.board_size - 1)

                    if self.is_space_around_empty(board, start_x, start_y):
                        ship_coordinates = [(0, 0)]
                        for _ in range(size - 1):
                            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                            random.shuffle(directions)
                            extended = False

                            for dx, dy in directions:
                                nx, ny = ship_coordinates[-1][0] + dx, ship_coordinates[-1][1] + dy
                                if (nx, ny) not in ship_coordinates:
                                    ship_coordinates.append((nx, ny))
                                    extended = True
                                    break

                            if not extended:
                                break
                        # Rotacja: 0°, 90°, 180°, 270°
                        if len(ship_coordinates) == size:
                            angle = random.choice([0, 90, 180, 270])
                            rotated_coordinates = self.rotate_coordinates(ship_coordinates, angle)

                            final_coordinates = [
                                (start_x + x, start_y + y) for x, y in rotated_coordinates
                            ]

                            if all(
                                0 <= x < self.board_size and 0 <= y < self.board_size and self.is_space_around_empty(board, x, y)
                                for x, y in final_coordinates
                            ):
                                for x, y in final_coordinates:
                                    board[x][y] = 1
                                placed = True

    def rotate_coordinates(self, coordinates, angle):
        if angle == 0:
            return coordinates
        elif angle == 90:
            return [(y, -x) for x, y in coordinates]
        elif angle == 180:
            return [(-x, -y) for x, y in coordinates]
        elif angle == 270:
            return [(-y, x) for x, y in coordinates]

    def can_place_ship(self, board, x, y, size, orientation, place=False):
        for i in range(size):
            nx, ny = (x, y + i) if orientation == 0 else (x + i, y)
            if not self.is_space_around_empty(board, nx, ny):
                return False
        if place:
            for i in range(size):
                nx, ny = (x, y + i) if orientation == 0 else (x + i, y)
                board[nx][ny] = 1
        return True

    def is_space_around_empty(self, board, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                    if board[nx][ny] != 0:
                        return False
        return True