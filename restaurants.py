class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = None
        self.last_name = None
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        
    @property
    def first_name(self):
         return self._first_name
    
    @first_name.setter
    def first_name(self, value):
         if not isinstance(value, str):
              raise TypeError('Names must be of type string')
         if not 1 <= len(value) <= 25:
             raise TypeError('Names must be between 1 and 25 characters')
         self.first_name = value
         
    @property
    def last_name(self):
         return self._last_name
    
    @last_name.setter
    def last_name(self, value):
         if not isinstance(value, str):
              raise TypeError('Names must be of type string')
         if not 1 <= len(value) <= 25:
             raise ValueError('Names must be between 1 and 25 characters')
         self.last_name = value

    def add_review(self, review):
        if not isinstance(review, Reviews):
            raise TypeError("Reviews must be of type Review")
        self._add_reviews.append(review)

    def reviews(self):
        return self._reviews

    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews if review.rating in [1, 2])
    
    def has_reviewed_restaurant(self, restaurant):
        return (reviews.restaurant == restaurant for reviews in self.reviews)


class Restaurant:

    def __init__(self, name):
      self.name = None
      self.name = name
      self.reviews = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def restaurant(self, value):
        if not isinstance(value, str):
            raise TypeError('Names must be of type string')
        if not 1 <= len(value) <= 100:
            raise ValueError("Names must be 1 or more characters")
        self._restaurant = value

    def add_review(self, review):
        if not isinstance(review, Reviews):
            raise TypeError("Reviews must be of type Review")
        self._reviews.append(review)

    def reviews(self):
        return self._reviews
    
    def customers(self):
        return list({review.customer for review in self.reviews})

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
        self.customer = None
        self.restaurant = None
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating (self, value):
        if not isinstance(value, int):
            raise TypeError('Ratings must be of type integer')
        if not 1 <= value <= 5:
            raise ValueError("Ratings must be between 1 and 5")
        self._rating = value

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be type of Customer")
        self._customer = value

    @property
    def restaurant(self):
        return self._restaurant
    
    @restaurant.setter
    def restaurant (self, value):
        if not isinstance(value, Restaurant):
            raise TypeError("Restaurant must be type of Restaurant")
        self._restaurant = value

#Example
if __name__ == "__main__":
    # Create some customers
    customer1 = Customer("Salma", "Njeri")
    customer2 = Customer("Joseph", "Brown")

    # Create some restaurants
    restaurant1 = Restaurant("KFC")
    restaurant2 = Restaurant("Chicken Inn")

    # Create some reviews
    review1 = Reviews(customer1, restaurant1, 5)
    review2 = Reviews(customer2, restaurant1, 2.2)
    review3 = Reviews(customer1, restaurant2, 4)

    # Add reviews to the customers' lists
    customer1.add_review(review1)
    customer1.add_review(review3)
    customer2.add_review(review2)

    # Test the methods
    print("Salma Njeri's reviews:")
    for review in customer1.get_reviews():
        print(f"- Restaurant: {review.restaurant.name} - Rating: {review.rating}")

    print("\nRestaurants reviewed by Salma Njeri:")
    for restaurant in customer1.restaurants():
        print(f"- {restaurant.name}")

    print("\nNumber of negative reviews by Salma Njeri:", customer1.num_negative_reviews())
    print("Has Salma Njeri reviewed Chicken Inn?", customer1.has_reviewed_restaurant(restaurant2))