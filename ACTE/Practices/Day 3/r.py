rows = 10
for i in range(rows):
    # 1️⃣ spaces
    print(" " * (rows - i - 1), end="")

    # 2️⃣ reverse alphabets
    for j in range(i, -1, -1):
        print(chr(65 + j), end="")

    # 3️⃣ forward alphabets
    for j in range(1, i + 1):
        print(chr(65 + j), end="")

    print()
    