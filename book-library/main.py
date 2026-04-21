books = {
    "python": "available",
    "math": "available",
    "science": "available"
}

issued = {}

def show_books():
    print("\nBooks List:")
    for b in books:
        print(b, "-", books[b])

def issue_book():
    name = input("Enter your name: ")
    book = input("Enter book name: ").lower()
    days = int(input("For how many days: "))

    if book in books and books[book] == "available":
        books[book] = "issued"
        issued[book] = {
            "name": name,
            "days": days,
            "used_days": 0
        }
        print("Book issued successfully")
    else:
        print("Book not available")

def return_book():
    book = input("Enter book name: ").lower()

    if book in issued:
        data = issued[book]
        used_days = int(input("Enter how many days you kept the book: "))
        allowed_days = data["days"]

        fine = 0
        extra = used_days - allowed_days

        if extra > 0:
            if extra <= 7:
                fine = extra * 10
            elif extra <= 14:
                fine = extra * 20
            else:
                fine = extra * 60

        print("Returned by:", data["name"])
        print("Days used:", used_days)
        print("Fine: ₹", fine)

        books[book] = "available"
        del issued[book]
    else:
        print("Book was not issued")

while True:
    print("\n--- Library Menu ---")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        show_books()
    elif ch == "2":
        issue_book()
    elif ch == "3":
        return_book()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")