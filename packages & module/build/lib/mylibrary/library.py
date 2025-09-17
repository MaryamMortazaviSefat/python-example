class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return f"book name:   {self.title}  --> author: {self.author}"    


class Library:
    def __init__(self):
        self.books=[]


    def search_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"{title} is'nt exists")
        return -1

    def add_book(self,title, author):
        new_book=Book(title,author)
        if self.search_book(new_book.title) == -1:
            self.books.append(new_book)
            print(f"{new_book.title} is added")
        else:
            print(f"{new_book} was exist")

    def remove_book(self,title):
        book=self.search_book(title)
        if book != -1:
            self.books.remove(book)
            print(f"{title} is remove from this library")
        

    def __str__(self):
        return "\n".join(str(book) for book in self.books)
    

    def show_books(self):
        print(str(self))

            

