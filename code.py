from abc import ABC, abstractclassmethod
from enum import Enum

class Enum:
    Book: 1
    CD: 2
    DVD: 3
    Magazine: 4


class Catalog:
    def search(self, src, name):
        """
        src int:
            Book: 1
            CD: 2
            DVD: 3
            Magazine: 4
        """
        if not isinstance(src, int):
            raise ValueError(f"src is int type, but get {type(src)}")

        


class LibraryItem(ABC):
    def __init__(self, Title, UPC, Subject, Contributor):
        self.Title = Title
        self.UPC = UPC
        self.Subject = Subject
        self.Contributor = Contributor
        
    @abstractclassmethod
    def Locate(self):
        pass


class Contributor:
    def __init__(self, name):
        self.name = name


class ContibutorWithType:
    def __init__(self, Contirbutor, Type):
        self.contributor = Contirbutor
        self.Type = Type


class Book(LibraryItem):
    def __init__(self, Title, UPC, Subject, Contributor, ISBN, DDS):
        super().__init__(Title, UPC, Subject, Contributor)
        self.ISBN = ISBN
        self.DDS = DDS

    def Locate(self):
        return f"This book is with DDS:{self.DDS}, ISBN:{self.ISBN}"

    
class CD(LibraryItem):
    def __init__(self, Title, UPC, Subject, Contributor):
        super().__init__(Title, UPC, Subject, Contributor)

    def Locate(self):
        return ""

class DVD(LibraryItem):
    def __init__(self, Title, UPC, Subject, Contributor, Genre):
        super().__init__(Title, UPC, Subject, Contributor)
        self.Genre = Genre

    def Locate(self):
        return f"This DVD is {self.Genre}, {self.Title}"

class Magazine(LibraryItem):
    def __init__(self, Title, UPC, Subject, Contributor, volume, issue):
        super().__init__(Title, UPC, Subject, Contributor)
        self.volume = volume
        self.issue = issue
    
    def Locate(self):
        return f"This DVD is {self.volume}, {self.issue}"

contributor = Contributor(name='Phillips')
author = ContibutorWithType(contributor, 'yes')
a_book = Book(Title='OOP Design Pattern', UPC='know', Subject='language', Contributor=author, ISBN='0000033689', DDS='4681')
print(a_book.Locate())