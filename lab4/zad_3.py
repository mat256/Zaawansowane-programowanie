class Property:

    def __init__(self, area: int, rooms: int, price: int, adress: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adress = adress

    def __str__(self):
        return f'Location: {self.adress},  Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}'


class House(Property):

    def __init__(self, plot: int, area: int, rooms: int, price: int, adress: str):
        super().__init__(area, rooms, price, adress)
        self.plot = plot

    def __str__(self):
        return f'Location: {self.adress}, Plot: {self.plot}, Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}'


class Flat(Property):

    def __init__(self, floor: int, area: int, rooms: int, price: int, adress: str):
        super().__init__(area, rooms, price, adress)
        self.floor = floor

    def __str__(self):
        return f'Location: {self.adress}, Floor: {self.floor}, Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}'


house1 = House(20, 12, 3, 20000, 'Street 12')
flat1 = Flat(3, 13, 4, 12000, "Street 32")
print(house1)
print(flat1)
