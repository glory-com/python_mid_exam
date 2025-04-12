# F 图书馆管理系统library
# 图书馆管理系统：
# 有一个父类 Book，具有属性 title 和方法 describe()。其中，describe() 方法打印出 "This is a book."

# 有两个子类：Fiction 和 NonFiction。它们继承自 Book 类，并且都具有一个额外的方法 read()。其中，Fiction 类的 describe() 方法输出 "This is a fiction book."，read() 方法输出 "{TITLE} is being read."；NonFiction 类类似。

# 现在，有一个 Library 类，管理所有书籍的实例。该类具有以下方法：

# add_book(book:Book)：将一本书的实例添加到该类self.books列表属性中。
# show_books()：显示所有添加到图书馆中的书籍的标题和类型（小说或非小说）。
# 要求：

# 请你填写如下 Python 代码，采用面向对象方法，使其能够顺利运行，满足上述要求。

class Book(object):
    def __init__(self, title):
        self.__title = title

    def describe(self):
        print("This is a book.")

class Fiction(Book):
    def __init__(self, title):
        super(Fiction, self).__init__(title)
        self.__genre = 'Fiction'
        self.title = title 

    def describe(self):
        print("This is a fiction book.")

    def read(self):
        print(f"{self.title} is being read.")

class NonFiction(Book):
    def __init__(self, title):
        super(NonFiction, self).__init__(title)
        self.__genre = 'NonFiction'
        self.title = title 

    def describe(self):
        print("This is a non-fiction book.")

    def read(self):
        print(f"{self.title} is being read.")

class Library(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books :
            print(f"{book.title} is {book.__class__.__name__}.")


def testing_Library(book_dict):
    library = Library()
    for genre, title in book_dict.items():
        genre = genre.split("_")
        if genre[0] == "Fiction":
            fiction = Fiction(title)
            fiction.describe()
            fiction.read()
            library.add_book(fiction)
        elif genre[0] == "NonFiction":
            non_fiction = NonFiction(title)
            non_fiction.describe()
            non_fiction.read()
            library.add_book(non_fiction)
        else:
            print("Incorrect dict keys!")
    library.show_books()


testing_Library({"Fiction_1":"To Kill a Mockingbird", "NonFiction_1":"A Brief History of Time", "Fiction_2":"Pride and Prejudice"})
