#Initializers and Properties
class Customer:

    all= []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
         return self._first_name
    
    @first_name.setter
    def first_name(self, value):
         if not isinstance(value, str):
              raise TypeError('Names must be of type str')
         if not 1<= len(value) <= 25:
             raise TypeError('Names must be between 1 and 25 characters')
         self.first_name = value
         
    @property
    def second_name(self):
         return self._second_name
    
    @second_name.setter
    def second_name(self, value):
         if not isinstance(value, str):
              raise TypeError('Names must be of type string')
         if not 1 <= len(value) <= 25:
             raise TypeError('Names must be between 1 and 25 characters')
         self.second_name = value


class Restaurant:

    all = []

    def __init__(self, name):
      self.name = name

    @property
    def restaurant(self):
        return self._restaurant
    
    @restaurant.setter
    def restaurant(self, value):
        if not isinstance(value, str):
            raise TypeError('Names must be of type string')
        if not 1 <= len(value) <= 100:
            raise TypeError("Names must be 1 or more characters")
        self._restaurant = value

class Reviews:
    
    all = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    @property
    def rating(self):
        self._rating

    @rating.setter
    def rating (self, value):
        if not isinstance(value, int):
            raise TypeError('Ratings must be of type integer')
        if not 1 <= len(value) <= 5:
            raise TypeError("Ratings must be between 1 and 5")
        
# Object Relationship Methods and Properties