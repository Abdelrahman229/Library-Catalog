library = {}

# Create Menu
def menu():
  print("""
  Menu:
  1- Add Book
  2- Check Out Book
  3- Check In Book
  4- List Books
  5- Exit
  """)
  choice = int(input("Enter your choice: "))

# Create Add Book
def add_book():
  while True:
    isbn = input("Please enter ISBN: ")
    title = input("Please enter the title: ")
    auther = input("Please enter the auther: ")
  
    library[isbn] = {"title":title, "auther":auther, "available":True}
    print(
      f"Book '{title}' by '{auther}' added to the catalog with ISBN '{isbn}'")
  
    choice = input("\nDo you want to add another book? (Y/N): ").lower()
    if choice != "y":
      break

# Create Check Out Book
def check_out():
  while True:
    isbn = input("Enter ISBN to check out: ")
    if isbn in library:
      if library[isbn]['available']:
        library[isbn]["available"] = False
        print(f"Book {library[isbn]['title']} checked out successfully")
      else:
        print("Sorry, the book is currently checked out.")

    else:
      print("This ISBN not found in Catalog")

    choice = input("Do you want to check out another book? (Y/N): ").lower()
    if choice != "y":
      break

# Create Check In Book
def check_in():
  while True:
    isbn = input("Enter ISBN to check in: ")
    if isbn in library:
      if not library[isbn]['available']:
        library[isbn]['available'] = True
        print(f"Book {library[isbn]['title']} checked in successfully.")
      else:
        print("This book already in catalog")
    else:
      print("Book not found in catalog.")

    choice = input("Do you want to check out another book? (Y/N): ").lower()
    if choice != "y":
      break

# Create view list
def view_list():
  while True:
    print("Library Catalog")
    for isbn in library:
      book_info = library[isbn]
      print(f"ISBN: {isbn}, Title: {book_info['title']}, Auther: {book_info['auther']}, Available: {book_info['available']} ")
  
    choice = input("Do you want to go back to the main menu? (Y/N): ").lower()
    if choice == "y":
      break

while True:
  print("""
  Menu:
  1- Add Book
  2- Check Out Book
  3- Check In Book
  4- List Books
  5- Exit
  """)
  choice = int(input("Enter your choice: "))

  if choice == 1:
    add_book()
    
  elif choice == 2:
    check_out()

  elif choice == 3:
    check_in()

  elif choice == 4:
    view_list()

  elif choice == 5:
    print("Exiting ... ")
    break

  else:
    print("\nInvalid choice, Please enter a number between (1:5). \n")