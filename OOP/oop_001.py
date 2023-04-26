class Book():
    def __init__(self, age = 0, auth = 'Winston', name = 'sigar'):
        self.age = age
        self.auth = auth
        self.name = name



my_book_1 = Book(age = 1934) 
print(my_book_1.auth)