from typing import *

# Question-1. Create an object-oriented program that allows you to enter data for customers and  employees. 

# Create a Person class that provides attributes for first name, last name, and email address.
# This class  should provide a property or method that returns the person’s full name. 
class Person:
    """
    Person Class: This base class has attributes for first name, last name, and email.
    It also includes a property full_name that returns the person's full name.
    """
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
# Create a Customer class that inherits the Person class. This class should add an attribute for a  customer number.
class Customer(Person):
    """
    Customer Class: Inherits from Person and adds a customer_number attribute.
    """
    def __init__(self, first_name: str, last_name: str, email: str, customer_number: int) -> None:
        super().__init__(first_name, last_name, email)
        self.customer_number = customer_number
#Create an Employee class that inherits the Person class. This class should add an attribute for a social  security number (SSN).
class Employee(Person):
    """
    Employee Class: Inherits from Person and adds an ssn attribute.
    """
    def __init__(self, first_name: str, last_name: str, email: str, ssn: str) -> None:
        super().__init__(first_name, last_name, email)
        self.ssn = ssn

def main():
    while True:
        role = input("Customer or employee? (c/e): ").strip().lower()
        if role not in ['c', 'e']:
            print("Invalid input. Please enter 'c' for customer or 'e' for employee.")
            continue
        
        print("DATA ENTRY")
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        email = input("Email: ").strip()

        if role == 'c':
            customer_number = input("Number: ").strip()
            person = Customer(first_name, last_name, email, customer_number)
            print("CUSTOMER")
        else:
            ssn = input("SSN: ").strip()
            person = Employee(first_name, last_name, email, ssn)
            print("EMPLOYEE")
        
        print(f"Name: {person.full_name}")
        print(f"Email: {person.email}")

        if isinstance(person, Customer):
            print(f"Number: {person.customer_number}")
        else:
            print(f"SSN: {person.ssn}")

        continue_entry = input("Continue? (y/n): ").strip().lower()
        if continue_entry != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
