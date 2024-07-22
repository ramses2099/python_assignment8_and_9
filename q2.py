from typing import *
import random

#  Question-2. Create an object-oriented program that uses a custom list object to automatically  
# generate and work with a series of random integers. 



# • Create a RandomIntList class that inherits the list class. 
# This class should allow a programmer to create  a list of random integers from 1 to 100 by writing a single line of code.
# For example, a programmer  should be able to create a custom list that stores 12 random integers with 
# this line of code: int_list = RandomIntList(12)
class RandomIntList(list):
    """
    Class RandomIntList Inherits from list class
    """
    def __init__(self, count) -> None:
        super().__init__()
        for _ in range(count):
            self.append(random.randint(1, 100))
    
    @property
    def count(self):
        return len(self)
    
    @property
    def total(self):
        return sum(self)
    
    @property
    def average(self):
        return self.total / self.count if self.count > 0 else 0
    
    def __str__(self):
        return ', '.join(map(str, self))

def main():
    print()
    print("Random Integer List")
    while True:
        try:
            num_integers = int(input("How many random integers should the list contain?: "))
            if num_integers <= 0:
                raise ValueError("Number of integers must be positive.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
        
        int_list = RandomIntList(num_integers)
        print("\nRandom Integers")
        print("===============")
        print(f"Integers: {int_list}")
        print(f"Count: {int_list.count}")
        print(f"Total: {int_list.total}")
        print(f"Average: {int_list.average:.1f}")

        while True:
            cont = input("Continue? (y/n): ").strip().lower()
            if cont == 'y':
                break
            elif cont == 'n':
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
