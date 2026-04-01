x = 5
y = 5
<<<<<<< HEAD
# Počáteční pozice
=======
# Počát
>>>>>>> efbeae4 (hiugz)

while True:
    print("Player position:", x, y)
    move = input("Move (w=up, s=down, a=left, d=right, q=quit): ")

# Posunutí o jeden pixel
    if move == "w":
<<<<<<< HEAD
        y = y - 1
    elif move == "s":
        y = y + 1
=======
        y = y + 1
    elif move == "s":
        y = y - 1
>>>>>>> efbeae4 (hiugz)
    elif move == "a":
        x = x - 1
    elif move == "d":
        x = x + 1
    elif move == "q":
        print("Game Over!")
        break
    else:
        print("Invalid input!")

    # Na hranice mapy
    if x < 0:
        x = 0
    if x > 10:
        x = 10
    if y < 0:
        y = 0
    if y > 10:
        y = 10