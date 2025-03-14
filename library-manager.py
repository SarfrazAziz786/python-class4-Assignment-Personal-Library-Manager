import json # use for json file handling data save and load
import os # os use for file handling and system operations file read write etc


data_file = "library.txt"

def load_library():
    if os.path.exists(data_file): # check if file exists
        with open(data_file, "r") as file: # open file in read mode and file varibale is used to access file
            return json.load(file)  # load json data from file 
    return []


def save_library(library):
    with open(data_file, "w") as file: # open file in write mode
        json.dump(library, file) # Convert Python list into JSON and save it

def add_book (library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")   
    year = input("Enter book year: ")
    genre = input("Enter book genre: ") #book type
    read = input("Have you read the book? (yes / no):  ").lower() == "yes"

    # create a dictionary to store book details
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    
    library.append(new_book) # add book to library

    save_library(library) # save library to file
    
    print(f"Book {title} added successfully.")


def remove_book(library):
    title = input("Enter book title to remove from the library: ").lower()
    initial_length = len(library)
    
    new_library = []
    for book in library:
        if book["title"].lower() != title:
            new_library.append(book)
    library = new_library


    # # This line uses a list comprehension to create a new library list that includes all books except the one with the title matching the user's input.
    # library = [book for book in library if book["title"].lower() != title]

    

    if len(library) < initial_length:
        save_library(library) # save updated library to file
        print(f"Book {title} removed successfully")
    else:
        print(f"Book {title} not found in the library")

    
def search_library(library):
    search_by = input("Search by title or author: ").lower()
    search_term = input(f"Enter the {search_by}: ").lower()
    
    # results = [book for book in library if search_term in book[search_by].lower()]

    results = []
    for book in library:
        if search_term in book[search_by].lower():
            results.append(book)


    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No results found.")


def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("Library is empty")

def display_statistics (library):
    total_books = len(library) # get total number of books in library
    total_read_books = len([book for book in library if book["read"]]) # get total number of read books
    persentage_read = (total_read_books / total_books) * 100

    total_unread_books = total_books - total_read_books
    persentage_unread = (total_unread_books / total_books) * 100


    print(f"Total books: {total_books}")
    print(f"Total read books: {total_read_books}")
    print(f"Percentage read books: {persentage_read:.2f}%")

    print(f"Total unread books: {total_unread_books}")
    print(f"Percentage unread books: {persentage_unread:.2f}%")


def main():
    library = load_library() # load library from file
    while True:
        print("Menu")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

    
if __name__ == "__main__":
    main()

