def create_rectangle(height, width):
    line_up = '+---' * width + '+'
    line_middle = "|   " * width + '|'

    rectangle = ""
    for _ in range(height):
        rectangle += line_up + '\n' + line_middle + '\n'
    rectangle += line_up

    return rectangle

height = int(input("Podaj wysokość prostokąta: "))
width = int(input("Podaj szerokość prostokąta: "))
print(create_rectangle(height, width))