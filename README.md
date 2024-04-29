# Restaurant System
We will be building out a Python application that builds out a database relational model of a database.

## Table of Contents
Built With
Classes
Customer
Restaurant
Reviews
Contributing

## Built With:
![Static Badge](https://img.shields.io/badge/python-orange)

## Classes
1. Customer
The Customer class represents a customer who can leave reviews for restaurants.

### Attributes:
Should have first_name and last_name of the customer
reviews: A list of reviews left by the customer.

### Methods:

add_review(review): Add a review to the customer's list of reviews.
reviews(): Get a list of all reviews left by the customer.
restaurants(): Get a list of all restaurants reviewed by the customer.
num_negative_reviews(): Get the number of negative reviews left by the customer.
has_reviewed_restaurant(restaurant): Check if the customer has reviewed a specific restaurant.

2. Restaurant
The Restaurant class represents a restaurant that can receive reviews from customers.

### Attributes:

name: The name of the restaurant.
reviews: A list of reviews received by the restaurant.
Methods:

add_review(review): Add a review to the restaurant's list of reviews.
reviews(): Get a list of all reviews received by the restaurant.
customers(): Get a list of all customers who reviewed the restaurant.
average_star_rating(): Get the average star rating of the restaurant.
top_two_restaurants(): Get the top two restaurants based on their average star ratings.

3. Reviews
The reviews represents a review left by a customer for a restaurant.

### Attributes:

customer: The customer who left the review.
restaurant: The restaurant being reviewed.
rating: The rating given in the review.

## Contributing
If you'd like to contribute to the Restaurant System, feel free to fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License

