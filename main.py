from  library import Library
library = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        book = input("Enter Book Name: ")
        library.add_book(book)

    elif choice == 2:
        library.show_books()

    elif choice == 3:
        book = input("Enter Book Name to Issue: ")
        library.issue_book(book)

    elif choice == 4:
        book = input("Enter Book Name to Return: ")
        library.return_book(book)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")