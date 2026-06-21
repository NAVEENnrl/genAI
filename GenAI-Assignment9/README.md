## Assignment 9 - NumPy 

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

5. Open `numpy.ipynb`.
6. Run the cells one by one using:
   - **Shift + Enter**, or
   - **Run → Run All Cells**
### Option 2: VS Code

1. Open the project folder in VS Code.
2. Install the **Python** and **Jupyter** extensions.
3. Open the `.ipynb` file.
4. Click **Run All** or execute cells individually.

#### Task 1: Creating NumPy array


```python
## Import Numpy
import numpy as np
```


```python
arr1 = np.arange(1, 11)
arr2 = np.arange(1, 10).reshape(3, 3)
arr3 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("Array 2:", arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("Array 3:", arr3)
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
```

    Array 1: [ 1  2  3  4  5  6  7  8  9 10]
    Shape: (10,)
    Data Type: int64
    Array 2: [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape: (3, 3)
    Data Type: int64
    Array 3: [10 20 30 40 50]
    Shape: (5,)
    Data Type: int64
    

#### Task 2: Important Mathematical Operations


```python
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("A + B =", A + B)
print("A - B =", A - B)
print("A * B =", A * B)
print("A / B =", A / B)
print("A ** 2 =", A ** 2)
```

    A + B = [11 22 33 44]
    A - B = [ 9 18 27 36]
    A * B = [ 10  40  90 160]
    A / B = [10. 10. 10. 10.]
    A ** 2 = [ 100  400  900 1600]
    


```python
ary_add=np.add(A,B)
ary_sub=np.subtract(A,B)
print("Add()",ary_add)
print("subtract()",ary_sub)
```

    Add() [11 22 33 44]
    subtract() [ 9 18 27 36]
    

#### Task 3: Important NumPy Mathematical Formulas


```python
values = np.array([2, 4, 6, 8, 10])

# 1. Square root of each element
sqrt_values = np.sqrt(values)

# 2. Exponential of each element
exp_values = np.exp(values)

# 3. Natural logarithm of each element
log_values = np.log(values)

# 4. Sum of all elements
sum_values = np.sum(values)

# 5. Cumulative sum of elements
cumsum_values = np.cumsum(values)

print("Values:", values)
print("Square Root:", sqrt_values)
print("Exponential:", exp_values)
print("Natural Logarithm:", log_values)
print("Sum:", sum_values)
print("Cumulative Sum:", cumsum_values)
```

    Values: [ 2  4  6  8 10]
    Square Root: [1.41421356 2.         2.44948974 2.82842712 3.16227766]
    Exponential: [7.38905610e+00 5.45981500e+01 4.03428793e+02 2.98095799e+03
     2.20264658e+04]
    Natural Logarithm: [0.69314718 1.38629436 1.79175947 2.07944154 2.30258509]
    Sum: 30
    Cumulative Sum: [ 2  6 12 20 30]
    

#### Task 4: Aggregation Operations


```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1. Row-wise sum
row_sum = np.sum(data, axis=1)

# 2. Column-wise sum
column_sum = np.sum(data, axis=0)

# 3. Minimum value
min_value = np.min(data)

# 4. Maximum value
max_value = np.max(data)

# 5. Overall mean
mean_value = np.mean(data)

print("Array:", data)
print("row-wise Sum:", row_sum)
print("Column-wise Sum:", column_sum)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Overall Mean:", mean_value)
```

    Array: [[10 20 30]
     [40 50 60]
     [70 80 90]]
    row-wise Sum: [ 60 150 240]
    Column-wise Sum: [120 150 180]
    Minimum Value: 10
    Maximum Value: 90
    Overall Mean: 50.0
    

#### Task 5: Statistical Operations 


```python
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])


mean_marks = np.mean(marks)
median_marks = np.median(marks)
variance_marks = np.var(marks)
std_marks = np.std(marks)
min_marks = np.min(marks)
max_marks = np.max(marks)
range_marks = np.ptp(marks)   

print("Mean:", mean_marks)
print("Median:", median_marks)
print("Variance:", variance_marks)
print("Standard Deviation:", std_marks)
print("Minimum:", min_marks)
print("Maximum:", max_marks)
print("Range:", range_marks)
```

    Mean: 79.25
    Median: 81.5
    Variance: 134.1875
    Standard Deviation: 11.583932838203095
    Minimum: 60
    Maximum: 95
    Range: 35
    

#### Task 6: Percentiles & Sorting


```python
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

# Sort the array
sorted_marks = np.sort(marks)

# Percentiles
p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)

# Average marks
avg_marks = np.mean(marks)

# Count students above average
above_avg_count = np.sum(marks > avg_marks)

print("Sorted Marks:", sorted_marks)
print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)
print("Average Marks:", avg_marks)
print("Students Above Average:", above_avg_count)
```

    Sorted Marks: [60 66 72 78 85 88 90 95]
    25th Percentile: 70.5
    50th Percentile: 81.5
    75th Percentile: 88.5
    Average Marks: 79.25
    Students Above Average: 4
    

#### Task 7: Mini use Case: Sales Analysis


```python
# Daily sales data
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# 1. Total weekly sales
total_sales = np.sum(sales)

# 2. Average daily sales
average_sales = np.mean(sales)

# 3. Highest and lowest sales day
highest_sales = np.max(sales)
lowest_sales = np.min(sales)

# 4. Standard deviation of sales
std_sales = np.std(sales)

# 5. Identify days where sales were above average
above_average_days = np.where(sales > average_sales)[0] + 1
above_average_sales = sales[sales > average_sales]

print("Total Weekly Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation of Sales:", std_sales)
print("Days with Above Average Sales:", above_average_days)
print("Sales on Above Average Days:", above_average_sales)
```

    Total Weekly Sales: 10700
    Average Daily Sales: 1528.5714285714287
    Highest Sales: 2000
    Lowest Sales: 900
    Standard Deviation of Sales: 345.2298849598449
    Days with Above Average Sales: [4 5 6 7]
    Sales on Above Average Days: [2000 1800 1700 1600]
    


```python

```
