from AuthorObjectsNew import Book, Author, Authors
import os

def main():
    os.system("clear")
    print("The Authors Tester program")
    print()
    
    author1 = Author("Mark", "Twain")
    author2 = Author("Charles", "Warner")
    authors = Authors()
    authors.add(author1)
    authors.add(author2)
    book = Book("The Gilded Age", authors)

    # display the book data
    print("BOOK DATA - SINGLE LINE")
    print(book)
    print()

    print("BOOK DATA - MUTLIPLE LINES")
    print("Title:   ", book.title)
    print("Authors: ",  book.authors)
    
    print("BOOK DATA - MULTIPLE LINES")
    print("Title:   ", book.title)
    print("Author:  " if authors.count == 1 else "Authors: ", book.authors)
    
    print("\nAUTHORS")
    for author in authors:
        print(author)
    
        
if __name__ == "__main__":
    main()
