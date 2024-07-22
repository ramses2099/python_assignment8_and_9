from typing import *
from objects import Product, Book, Movie, Album, Media
import os

# Question-3. Enhance the Product Viewer program so it provides one more type of product: 
# a music  album. When you enter the product number for a music album,
# it should print the data to the console like  this: 
# Enter product number: 4 
# PRODUCT DATA  
# Name: Rubber Soul 
# Artist: The Beatles 
# Format: CD 
# Discount price: 10.00 



def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()



def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    if isinstance(product, Album):
        print(f"{'Author:':{w}}{product.artist}")
    if isinstance(product, Media):
        print(f"{'Format:':{w}}{product.format}")
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()


def main():
    print()
    print("The Product Viewer program")
    print()
    
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book(name="The Big Short",price=15.95, discountPercent=34, author="Michael Lewis",format="ebook"),
                Movie(name="The Holy Grail", price=14.99, discountPercent=68, year=1975, format="DVD"),
                Album(name="Flesh Of My Fleshblood Of My Blood", artist="DMX", price=15.99, discountPercent=18, format="DVD"),
                Album(name="Grateful", artist="DJ Khaled", price=15.99, discountPercent=0, format="DVD"),
                Album(name="Strange Clouds ", artist="B.o.B", price=15.99, discountPercent=18,  format="Streaming"),
                Album(name="COMMON - ELECTRIC CIRCUS ", artist="COMMON", price=5.99, discountPercent=1,  format="DVD"),)
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                raise ValueError("Product number out of range.")
            print()

            product = products[number-1]
            show_product(product)

        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid product number.")
            continue

        while True:
            choice = input("View another product? (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()

