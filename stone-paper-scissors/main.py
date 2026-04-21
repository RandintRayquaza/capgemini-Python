import random

def comp():
    return random.choice(["stone", "paper", "scissors"])

def win(u, c):
    if u == c:
        return "Draw"
    elif (u == "stone" and c == "scissors") or \
         (u == "paper" and c == "stone") or \
         (u == "scissors" and c == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\n--- SPS Game ---")
    print("1. Play")
    print("2. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        u = input("stone / paper / scissors: ").lower()

        if u not in ["stone", "paper", "scissors"]:
            print("Invalid input!")
            continue

        c = comp()
        print(f"Computer: {c}")
        print(win(u, c))

    elif ch == "2":
        print("Game exited.")
        break
    else:
        print("Invalid choice.")