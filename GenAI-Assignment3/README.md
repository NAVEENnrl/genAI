# Assignment 3 - Functions


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
    

## Task 1 - Basic Function : Price after Discount


```python
def apply_discount(price,discount_percent=5):
    if discount_percent>60:
        return "Max docount price exceed, please make it below 60%"
    else:
        return price-(price*discount_percent/100)


```


```python
print(apply_discount(1000,10))
print(apply_discount(500))
print(apply_discount(1000,70))
```

    900.0
    475.0
    Max docount price exceed, please make it below 60%
    

## Task 2 - Recursive Function : Factorial Utility


```python
def fact(n):
    result=1
    if n<0:
        result="Value is not correct"
       
    elif n==0 or n==1:
        result=1
       
    for i in range(1,n+1):
           result *=i
    return result   

```


```python
print(fact(5))
print(fact(0))
print(fact(-3))
```

    120
    1
    Value is not correct
    

## Task 3: Lambda Function-GST Calculator


```python
gst=lambda price:price+(0.18*price)
print(gst(100))
```

    118.0
    


```python
# include price and percentage of discount
discounted_price=lambda price,discount: (price-(price*discount/100))*0.18+(price-(price*discount/100))
print(discounted_price(100,5))
```

    112.1
    

## Task 4: using map():Apply GST to list of Prices


```python
prices=[100,250,400,1200,50]
gst_price=list(map(gst,prices))
print("Orginal price:",prices)
print("Price after GST",gst_price)
```

    Orginal price: [100, 250, 400, 1200, 50]
    Price after GST [118.0, 295.0, 472.0, 1416.0, 59.0]
    

## Task 5: Using Filter - Filter Expensive Product


```python
prices=[100,250,400,1200,50,2000,850]
exp_prices=list(filter(lambda price:price>500,prices))
lower_prices=list(filter(lambda prices:prices<=500,prices))
print("Expensive Prices:",exp_prices)
print("Lower Prices:",lower_prices)
```

    Expensive Prices: [1200, 2000, 850]
    Lower Prices: [100, 250, 400, 50]
    

## Task 6: Combined Utility Function


```python
def process_price(prices):
    dis_price=list(map(lambda price:price-price*10/100,prices))
    filter_price=list(filter(lambda price:price>300,dis_price))
    return dis_price,filter_price
```


```python
dis_price,filter_price=process_price([100,500,900,50,750])
print("Discounted price:", dis_price)
print("Filtered Price:",filter_price)
```

    Discounted price: [90.0, 450.0, 810.0, 45.0, 675.0]
    Filtered Price: [450.0, 810.0, 675.0]
    

## Task 7:Mini Problem - Menu using Function


```python
prices_list=[]

def add_price(prices_list,price):
    prices_list.append(price)

def get_average_price(prices_list):
    if len(prices_list)==0:
        return 0
    return sum(prices_list)/len(prices_list)
    
def get_max_price(prices_list):
    if len(prices_list)==0:
        return 0
    return max(prices_list)


# menu using loop:

while True:
    print("1 -> Add price")
    print("2 -> Show average price")
    print("3 -> Show highest price")
    print("q -> Quit")

    select_menu=input("Choose your menu Ex:1,2,q:")

    if select_menu=="1":
        price=int(input("Enter yout Price"))
        add_price(prices_list,price)
    
    elif select_menu=="2":
        avg_price=get_average_price(prices_list)
        print("Average Price:",avg_price)
    
    elif select_menu=="3":
        max_price=get_max_price(prices_list)
        print("Maximum Price:",max_price)
    
    elif select_menu=="q":
        print("Exit the loop")
        break
    else:
        print("input is not valid select again:")
        continue



```

    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    Average Price: 460.0
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    Maximum Price: 800
    1 -> Add price
    2 -> Show average price
    3 -> Show highest price
    q -> Quit
    Exit the loop
    


```python

```
