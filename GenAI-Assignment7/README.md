# Assignment 7: Object Oriented Programming (OOP)

## Requirements

- Python 3.13.12
- Jupyter Notebook

## How to Run

### Option 1: Jupyter Notebook

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Install Jupyter Notebook if not already installed:

```bash
pip install notebook
```

4. Start Jupyter Notebook:

```bash
jupyter notebook
```

5. Open `Assignment6_ExceptionHandling.ipynb`.
6. Run the cells one by one using:
   - **Shift + Enter**, or
   - **Run → Run All Cells**
### Option 2: VS Code

1. Open the project folder in VS Code.
2. Install the **Python** and **Jupyter** extensions.
3. Open the `.ipynb` file.
4. Click **Run All** or execute cells individually.

### Task 1: Basic Class and Object Creation


```python
class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
        print(f"Name of the product {self.name} and price of product is: {self.price} and category of product is:{self.category}")
    
    ## Optional Work
    def apply_discount(self,percent):
        discounted_price=self.price-(self.price*percent/100)
        return discounted_price
    
```


```python
## Creating two Objects

product1=Product("Laptop",60000,"Electronics")
product2=Product("Headphones",2000,"Accessories")

product2.get_info()

## Discounted Methods
print("Laptop price after 10% discount:",product1.apply_discount(10))
print("Headphone Price after 20% discount:",product2.apply_discount(20))
```

    Name of the product Headphones and price of product is: 2000 and category of product is:Accessories
    Laptop price after 10% discount: 54000.0
    Headphone Price after 20% discount: 1600.0
    

### Task 2: Constructr & Encapsulation


```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price      # Private attribute
        self.category = category

    # Getter method
    def get_price(self):
        return self.__price

    # Setter method
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully.")
        else:
            print("Price must be greater than 0.")

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)
        
```


```python
product = Product("Laptop", 50000, "Electronics")
```


```python
# Display original details
product.get_info()

```

    Name: Laptop
    Price: 50000
    Category: Electronics
    


```python
# Get price using getter
print("Current Price:", product.get_price())
```

    Current Price: 50000
    


```python
# Update price using setter
product.set_price(55000)
```

    Price updated successfully.
    


```python
# Check updated price
print("Updated Price:", product.get_price())

# Test invalid price
product.set_price(-1000)
```

    Updated Price: 55000
    Price must be greater than 0.
    

### Task 3: Inheritance (Single Level)


```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Child class inherit the property of parent class
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # Method Overriding
    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("Warranty:", self.warranty_years, "Years")


# Create object of child class
electronic_item = ElectronicProduct(
    "Laptop",
    50000,
    "Electronics",
    2
)

# Call overridden method
electronic_item.get_info()
```

    Name: Laptop
    Price: 50000
    Category: Electronics
    Warranty: 2 Years
    

### Task 4: Polymorphism


```python
## Grand Parent Class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print("Product:", self.name)
        print("Price:", self.price)

## Parent Class
class Laptop(Product):
    def get_info(self):
        print("Laptop Details")
        print("Name:", self.name)
        print("Price:", self.price)
       
## Child Class
class Mobile(Product):
    def get_info(self):
        print("Mobile Details")
        print("Name:", self.name)
        print("Price:", self.price)
        


# Create objects
laptop = Laptop("Dell Inspiron", 60000)
mobile = Mobile("Samsung Galaxy", 25000)

# Store objects in a list
products = [laptop, mobile]

# Polymorphism
for product in products:
    product.get_info()
```

    Laptop Details
    Name: Dell Inspiron
    Price: 60000
    Mobile Details
    Name: Samsung Galaxy
    Price: 25000
    

### Task 5 : Abstraction using Abstraction base class


```python
## Import abstract method from Abc 
from abc import ABC, abstractmethod


# Abstract Class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Class 1 to implement abstract method
class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Credit Card Payment of ₹{amount} processed successfully.")


# class 2 to implement abstract method
class UPIPayment(Payment):

    def process_payment(self, amount):
        print(f"UPI Payment of ₹{amount} processed successfully.")


# Create objects for both the classes
credit_card = CreditCardPayment()
upi = UPIPayment()

# Test classes
credit_card.process_payment(5000)
upi.process_payment(2500)
```

    Credit Card Payment of ₹5000 processed successfully.
    UPI Payment of ₹2500 processed successfully.
    

### Task 6: Magic Methods and operator overloading


```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic Method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator Overloading
    def __add__(self, other):
        return self.price + other.price


# Create two product objects
product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Mobile", 25000, "Electronics")

# Test __str__()
print(product1)
print(product2)

# Test __add__() operator
total_price = product1 + product2
print("Total Combined Price:", total_price)
```

    Product(Laptop, 50000, Electronics)
    Product(Mobile, 25000, Electronics)
    Total Combined Price: 75000
    

### Task 7: Mini Project: Simple Inventory System


```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(name, "removed successfully.")
                return
        print("Product not found.")

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print("Store Name:", self.store_name)
        print("Products:")

        self.inventory.show_all_products()

        print("Total Inventory Value:",
              self.inventory.get_total_value())


# Create Store
store = Store("Naveen Gen AI Store")

# Add 3 Products
store.add_new_product("Laptop", 50000, "Electronics")
store.add_new_product("Mobile", 25000, "Electronics")
store.add_new_product("Headphones", 3000, "Accessories")

# Show Summary
store.show_summary()

# Test __add__()
print("Using Operator Overloading:")

product1 = store.inventory.products[0]
product2 = store.inventory.products[1]

print("Combined Price:", product1 + product2)
```

    Store Name: Naveen Gen AI Store
    Products:
    Product(Laptop, 50000, Electronics)
    Product(Mobile, 25000, Electronics)
    Product(Headphones, 3000, Accessories)
    Total Inventory Value: 78000
    Using Operator Overloading:
    Combined Price: 75000
    


```python

```
