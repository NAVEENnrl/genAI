# Assignment 4: File Handling (Read, Write, Append, Mode)


```python
import sys
import platform

print("Python Version:", sys.version)
print("Python Executable:", sys.executable)
print("Platform:", platform.system())
print("Platform Release:", platform.release())
print("Processor:", platform.processor())
```

    Python Version: 3.13.12 | packaged by Anaconda, Inc. | (main, Feb 24 2026, 16:05:56) [MSC v.1942 64 bit (AMD64)]
    Python Executable: c:\Users\navee\miniconda3\python.exe
    Platform: Windows
    Platform Release: 11
    Processor: Intel64 Family 6 Model 140 Stepping 2, GenuineIntel
    

### Task 1: Write Sales Record to a File


```python
# List of Sale Amount
sales=[1200,450,980,1500,3000]
# write sales in file
with open("sales_data.txt","w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

```


```python
# open file and print
 
with open("sales_data.txt","r") as file:
    print(file.read()) 
```

    1200
    450
    980
    1500
    3000
    
    


```python
with open("sales_data.txt", "w") as file:
     file.write(",".join(map(str,sales)))
```


```python
with open("sales_data.txt","r") as file:
    print(file.read())
```

    1200,450,980,1500,3000
    

### Task 2: Read file in different Ways


```python
# using read() function
with open("sales_data.txt", "r") as file:
    data = file.read()

print(data)
```

    1200,450,980,1500,3000
    


```python
# using readline()
with open("sales_data.txt", "r") as file:
    first_line = file.readline().strip()

print(first_line)
```

    1200,450,980,1500,3000
    


```python
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = [int(line.strip()) for line in lines]

print(sales)
```

    [1200, 450, 980, 1500, 3000]
    

### Task 3: Append New Sales


```python
new_sales = [5000, 2500, 1700]

# Append data
with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(f"{sale}\n")

# Read and print 
with open("sales_data.txt", "r") as file:
    print(file.read())
```

    1200
    450
    980
    1500
    3000
    5000
    2500
    1700
    
    


```python
# read tota lines
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))
```

    Total lines: 8
    

### Task 4: Generate Summery Report from File


```python
with open("sales_data.txt", "r") as file:
    sales = [int(line.strip()) for line in file]

# Calculate summary
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Print report
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)
```

    Total Sales: 16330
    Highest Sale: 5000
    Lowest Sale: 450
    Average Sale: 2041.25
    

### Task 5 : Create Product Info File


```python
with open("products.txt", "w") as file:
    for i in range(3):
        name = input(f"Enter product {i+1} name: ")
        price = float(input(f"Enter {name} price: "))

        file.write(f"{name} | {price}\n")

# Read file
print("\nProduct List:")
with open("products.txt", "r") as file:
    for line in file:
        product, price = line.strip().split(" | ")
        print(f"Product: {product}, Price: ₹{price}")
```

    
    Product List:
    Product: ac, Price: ₹25000.0
    Product: fridge, Price: ₹12000.0
    Product: tv, Price: ₹30000.0
    

### Task 6: Read File Safely


```python
import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found. Please check the filename.")
```

    ac | 25000.0
    fridge | 12000.0
    tv | 30000.0
    
    

### Task 7: Mini Project - Export Discounted Prices


```python
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

total_discounted = 0

with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")

    for product, price in prices.items():
        discounted_price = price - (price * discount / 100)

        file.write(
            f"{product} | {price} | {discounted_price:.2f}\n"
        )

        total_discounted += discounted_price

    
    average_discounted = total_discounted / len(prices)

    file.write("\n")
    file.write(f"Total Items: {len(prices)}\n")
    file.write(
        f"Average Discounted Price: {average_discounted:.2f}\n"
    )

# print the file
with open("discount_report.txt", "r") as file:
    print(file.read())
```

    Product | Original Price | Discounted Price
    Mouse | 500 | 450.00
    Keyboard | 800 | 720.00
    Monitor | 7000 | 6300.00
    Pendrive | 400 | 360.00
    Camera | 5000 | 4500.00
    
    Total Items: 5
    Average Discounted Price: 2466.00
    
    


```python

```
