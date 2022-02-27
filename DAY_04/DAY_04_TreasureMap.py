row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to place your treasure?\n")

horizontal_pos = int(position[0])
vertical_pos = int(position[1])

map[vertical_pos - 1][horizontal_pos - 1] = "X "

print(f"{row1}\n{row2}\n{row3}")
