class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.first_name = None
        self.last_name = None
        self.reviews = []
        

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

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews if review.rating in [1, 2])
    def has_reviewed_restaurant(self, restaurant):
        return (reviews.restaurant == restaurant for reviews in self.reviews)


class Restaurant:

    def __init__(self, name):
      self.name = name
      self.reviews = []

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

    def average_start_rating(self):
        if not self.reviews:
            return 0.0
        total_ratings = sum(review.rating for review in self.reviews)
        average_rating = total_ratings / len(self.reviews)
        return round(average_rating, 1)
    
    @classmethod
    def top_two_restaurants(cls):
        if not cls.members:
            return None
        sorted_restaurants = sorted(cls.members, key = lambda restaurant: restaurant.average_star_rating(), reverse = True)
        return sorted_restaurants[:2]

class Reviews:

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