class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    @property
    def name(self):
        return self.__name
        
    @property
    def kind(self):
        return self.__kind
        
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @kind.setter
    def kind(self, new_kind):
        self.__kind = new_kind
        
    def move(self, direction, speed, time):
        #go a given direction at a given speed for a given time
        
    def make_noise(self, call):
        print(call)
        
class Book:
    def __init__(self, title, author, genre, pages, isbn, hardcover):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.isbn = isbn
        self.hardcover = hardcover
        
    #pretend there's getters and setters for everything here - this is just practice and I didn't feel like writing them all out
    
class Vehicle:
    def __init__(self, make, model, vehicle_type, year):
        self.make = make
        self.model = model
        self.vehicle_type = vehicle_type
        self.year = year
        
    #getters and setters go here
    
    def drive(self, direction, speed, time):
        #drive a given direction at a given speed for a given time