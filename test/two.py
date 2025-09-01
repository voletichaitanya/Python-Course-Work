class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display_info(self):
        print(f"Title : {self.title} Author : {self.author} Price = {self.price}")


b = Book("The Alchemist","Paulo Coelho",299)
b.display_info()