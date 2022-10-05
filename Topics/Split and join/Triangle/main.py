height = int(input())
for h in range(height):
    for _ in range(height - h - 1):
        print(" ", end="")
    for _ in range(h * 2 + 1):
        print("#", end="")
    print()
