with open("books.txt") as books_file:
    for line in books_file:
     books = line.strip()
     print(books)