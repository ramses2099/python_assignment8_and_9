from dataclasses import dataclass

@dataclass
class Product:
    """
    Product is a base class with three attributes:

    name: a string representing the product's name.
    price: a float representing the product's price.
    discountPercent: an integer representing the discount percentage.
    """
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        """Calculates the discount amount based on the price and discount percent."""
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        """Returns the price after applying the discount."""
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        """Returns the product's name."""
        return self.name

@dataclass   
class Media(Product):
     format:str =""    

@dataclass
class Book(Media):
    """
    Book is a subclass of Product with an additional attribute:

    author: a string representing the book's author.
    """
    author:str = ""
   

    def getDescription(self):
        """Returns a string that includes the book's name and author."""
        return f"{Product.getDescription(self)} by {self.author}"

@dataclass        
class Movie(Media):
    """
    Movie is a subclass of Product with an additional attribute:

    year: an integer representing the movie's release year.
    movieFormat: an string representing the format of the movie
    """
    year:int = 0   
   
   
    def getDescription(self):
        """Returns a string that includes the movie's name and release year."""
        return f"{Product.getDescription(self)} ({self.year})"

@dataclass
class Album(Media):
    """
    Album is a subclass of Product with an additional attribute:

    artist: an string representing the artist.
    albumFormat: an string representing the album format
    """
    artist:str =""
    

    def getDescription(self):
        """Returns a string that includes the Album's artist and format."""
        return f"{Product.getDescription(self)} ({self.artist})"
    

