from Productobjects import Product, Book, Movie

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
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

def main():
    print("The Product Viewer program")
    print()
    
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Michael Lewis"),
                Movie("The Holy Grail - DVD", 14.99, 68, 1975))
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        number = int(input("Enter product number: "))
        print()

        product = products[number-1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
