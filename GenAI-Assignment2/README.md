# Assignment 2-Control Flow
## Task 1: Discount Rule


```python
order_amount=input("please enter order amount:")

if order_amount.isdigit():
    order_amount=int(order_amount)
    if order_amount>=2000:
        discount=order_amount*15/100
    elif order_amount>=1500:
        discount=order_amount*10/100
    elif order_amount>=1000:
        discount=order_amount*7/100
    else:
        discount=0
    discount_price=order_amount-discount
    tax=(discount_price)*5/100
    total_amount=discount_price+tax

    
    print("The price after Discount:",discount_price)
    print("Total Amount after Tax:",total_amount)
else:
    print("not int")

```

    The price after Discount: 930.0
    Total Amount after Tax: 976.5
    

## Task 2: Process Multiple Order


```python
order=[1200,2500,800,1750,3000]
total_rev=0
discount_orders=0
for order_amount in order:
    if order_amount>=2000:
        discount=order_amount*15/100
    elif order_amount>=1500:
        discount=order_amount*10/100
    elif order_amount>=1000:
        discount=order_amount*7/100
    else:
        discount=0

    discount_price=order_amount-discount
    total_rev=total_rev+discount_price
    if discount>0:
        discount_orders=discount_orders+1
    
print("Total Revenue:",total_rev)
print("Total Discounted Orders:",discount_orders)
    
```

    Total Revenue: 8166.0
    Total Discounted Orders: 4
    

## Task 3: User Menu


```python
order_list=[]

while True:
    print("1. Add order")
    print("2. show All orders")
    print("q. Exit the menu ")

    select_menu=input("Choose your menu Ex:1,2,q:")

    if select_menu=="1":
        order_amount=int(input("Enter yout order amount"))
        order_list.append(order_amount)
    
    elif select_menu=="2":
        total_rev=0
        discount_orders=0
        for order_amount in order_list:
            if order_amount>=2000:
                 discount=order_amount*15/100
            elif order_amount>=1500:
                discount=order_amount*10/100
            elif order_amount>=1000:
                discount=order_amount*7/100
            else:
                discount=0

            discount_price=order_amount-discount
            total_rev=total_rev+discount_price
            if discount>0:
                discount_orders=discount_orders+1
    
        print("Total Revenue:",total_rev)
        print("Total Discounted Orders:",discount_orders)
    
    elif select_menu=="q":
        print("Exit the loop")
        break
    else:
        print("input is not valid select again:")
        continue

```

    1. Add order
    2. show All orders
    q. Exit the menu 
    1. Add order
    2. show All orders
    q. Exit the menu 
    1. Add order
    2. show All orders
    q. Exit the menu 
    Total Revenue: 2630.0
    Total Discounted Orders: 2
    1. Add order
    2. show All orders
    q. Exit the menu 
    input is not valid select again:
    1. Add order
    2. show All orders
    q. Exit the menu 
    Exit the loop
    

## Task 4: Loop Control with condition


```python
daily=[200,150,0,400,50,-1,300]

total_sales=0

for sales in daily:
    if sales==-1:
        print("corrupted data")
        break
    elif sales==0:
        print("No Sales")
        continue
    else:
        total_sales=total_sales+sales
        print("total Sales running:",total_sales)
print("Final sales :",total_sales)

```

    total Sales running: 200
    total Sales running: 350
    No Sales
    total Sales running: 750
    total Sales running: 800
    corrupted data
    Final sales : 800
    


```python

```
