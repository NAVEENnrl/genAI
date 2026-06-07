# Assignment 5: Importing, creating modules and packages

# Task 1: Creating Simple module (Math_utils.py)
# import the function from math_utils file
import math_utils
from math_utils import square
# Task 2
import string_utils
# Task 3
from shop_package import (
    apply_discount,
    flat_discount,
    calculate_total,
    apply_tax
)

# Task 4 : import packages
import shop_package.discount as disc
from shop_package.billing import calculate_total

# call and print the result

print(math_utils.add(10, 5))
print(math_utils.sub(10, 5))
print(square(6))

# Task 2:Create another module

text = "hello Naveen Hooda"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))

# Task 3: Create a Simple Package (Shop package)
print("Discounted Price:", apply_discount(1000, 10))
print("Flat Discount Price:", flat_discount(1000))

prices = [100, 200, 300]
total = calculate_total(prices)

print("Total Bill:", total)
print("Bill With Tax:", apply_tax(total))


# Task 4: Importing the Packages
print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))

prices = [100, 200, 300]
total = calculate_total(prices)

print(total)
print(apply_tax(total))