from models.library import Library
from models.employee import Employee
from models.book import Book
from models.student import Student
from models.order import Order

library1 = Library("London", "west street", 33880, "8-16", 6765818)
library2 = Library("Cambridge", "east street", 32133, "8-16", 7658978)

book1 = Book(library1, "12.08.1996", "Stanisław", "Lem", 128)
book2 = Book(library2, "30.05.1992", "John", "Flanagan", 220)
book3 = Book(library1, "12.06.2001", "Andrzej", "Sapkowski", 231)

employee1 = Employee("Jan", "Kowalski", "12.04.2019", "12.12.1976", "London", "South Street", 12343, 987323278)
employee2 = Employee("Adam", "Nowak", "30.04.2003", "12.12.1990", "London", "That Street", 123132, 131323)
student1 = Student("Marek", 30)

order1 = Order(employee2, student1, book1, "12.03.18")
order2 = Order(employee1, student1, book3, "27.08.19")

print(order1)
print(order2)
