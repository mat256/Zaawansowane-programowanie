class Library:

    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library located in {self.city} {self.zip_code} on {self.street}. Open hours {self.open_hours}. Phone: {self.phone}'


class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f' {self.employee}. {self.student} ordered {self.books} on {self.order_date}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Author: {self.author_name} {self.author_surname}. Library: {self.library}'


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name}'

    def is_passed(self):
        return self.marks > 50


library1 = Library("London", "west street", 33880, "8-16", 6765818)
library2 = Library("Cambridge", "east street", 32133, "8-16", 7658978)

book1 = Book(library1, "12.08.1996", "Stanisław", "Lem", 128)
book2 = Book(library2, "30.05.1992", "John", "Flanagan", 220)
book3 = Book(library1, "12.06.2001", "Andrzej", "Sapkowski", 231)

employee1 = Employee("Jan", "Kowalski", "12.04.2019", "12.12.1976", "London", "South Street", 12343, 987323278)
employee2 = Employee("Adam", "Nowak", "30.04.2003", "12.12.1990", "London", "That Street", 123132,131323)
student1 = Student("Marek", 30)



order1 = Order(employee2, student1, book1, "12.03.18")
order2 = Order(employee1, student1, book3, "27.08.19")

print(order1)
print(order2)
