# Restaurant System
The Restaurant System is a Python application that manages customers, restaurants, and their reviews.

## Built With:
![Static Badge](https://img.shields.io/badge/python-orange)

Table of Contents
Built With
Classes
Customer
Restaurant
Reviews
Example
Contributing

## Built With:
![Static Badge](https://img.shields.io/badge/python-orange)

Classes
Customer
The Customer class represents a customer who can leave reviews for restaurants.

Attributes:

first_name: The first name of the customer.
last_name: The last name of the customer.
reviews: A list of reviews left by the customer.
Methods:

add_review(review): Add a review to the customer's list of reviews.
reviews(): Get a list of all reviews left by the customer.
restaurants(): Get a list of all restaurants reviewed by the customer.
num_negative_reviews(): Get the number of negative reviews left by the customer.
has_reviewed_restaurant(restaurant): Check if the customer has reviewed a specific restaurant.
Restaurant
The Restaurant class represents a restaurant that can receive reviews from customers.

Attributes:

name: The name of the restaurant.
reviews: A list of reviews received by the restaurant.
Methods:

add_review(review): Add a review to the restaurant's list of reviews.
reviews(): Get a list of all reviews received by the restaurant.
customers(): Get a list of all customers who reviewed the restaurant.
average_star_rating(): Get the average star rating of the restaurant.
top_two_restaurants(): Get the top two restaurants based on their average star ratings.
Reviews
The Reviews class represents a review left by a customer for a restaurant.

Attributes:

customer: The customer who left the review.
restaurant: The restaurant being reviewed.
rating: The rating given in the review.
Example
Here's an example of how you can use the Restaurant Review System:

python
Copy code
# Create some customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create some restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Create some reviews
review1 = Reviews(customer1, restaurant1, 5)
review2 = Reviews(customer2, restaurant1, 4)
review3 = Reviews(customer1, restaurant2, 3)

# Add reviews to the customers' lists
customer1.add_review(review1)
customer1.add_review(review3)
customer2.add_review(review2)

# Test the methods
print("John Doe's reviews:")
for review in customer1.reviews():
    print(f"- Restaurant: {review.restaurant.name} - Rating: {review.rating}")

print("\nRestaurants reviewed by John Doe:")
for restaurant in customer1.restaurants():
    print(f"- {restaurant.name}")

print("\nNumber of negative reviews by John Doe:", customer1.num_negative_reviews())
print("Has John Doe reviewed Restaurant B?", customer1.has_reviewed_restaurant(restaurant2))

## Contributing
If you'd like to contribute to the Restaurant Review System, feel free to fork the repository and submit a pull request with your changes.

## License
The Restaurant System is open source software licensed under the MIT License.

