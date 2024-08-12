#Day_13: Abstract Classes
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): 
        pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')
        
title=input("Enter the Title of the Book: ")
author=input("Enter the Author Name: ")
price=int(input("Enter Price: "))
new_novel=MyBook(title,author,price)
new_novel.display()