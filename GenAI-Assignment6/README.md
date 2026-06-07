# Assignment 6: Exception Handling

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

### Task 1: Safe Division Utility


```python
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")
```

    Result: 5.0
    Operation Complete
    

### Task 2: Bill Calculator with Error Handling


```python
prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Not a number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

    except TypeError:
        print(f"Skipped '{price}' - Invalid price")

    except ValueError as e:
        print(f"Skipped {price} - {e}")

    print("Running Total:", total)

print("Final Total:", total)
```

    Running Total: 120
    Running Total: 470
    Skipped 'abc' - Invalid price
    Running Total: 470
    Running Total: 970
    Skipped -200 - Negative price not allowed
    Running Total: 970
    Running Total: 1770
    Final Total: 1770
    

### Task 3: Custom Exception - Age Validator


```python
def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Valid age")

except ValueError as e:
    print("Error:", e)
```

    Valid age
    

### Task 4: File Reader with Exception Handling


```python
try:
    filename = input("Enter filename: ")

    file = open(filename, "r")

    print("First 3 lines of the file:")
    for i in range(3):
        print(file.readline(), end="")

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("\nFile operation attempted.")
```

    First 3 lines of the file:
    Hello, This is my test file
    my age is 35
    this is the test program for File Exception Handling
    
    File operation attempted.
    

### Task 5: Safe Shopping Cart


```python
cart = []

while True:
    item = input("Enter price (or 'q' to quit): ")

    if item.lower() == 'q':
        break

    try:
        price = float(item)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

print("Total items:", len(cart))
print("Total bill:", sum(cart))
```

    Total items: 6
    Total bill: 7745.0
    


```python

```
