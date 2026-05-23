# Python Data Structure

### Task 1: Product Collection (List & Tuple)


```python
products=["Book","Eraser","Pen","Pencil","Tiffin","Beg"]
sample_product=("Book",200,"science")

print("Second Product:"+products[1])
print("Last Product:"+products[-1])
```

    Second Product:Eraser
    Last Product:Beg
    


```python

products.append("Sharpner")
products.append("Scale")
for prod in products:
    print(prod)
```

    Book
    Eraser
    Pen
    Pencil
    Tiffin
    Beg
    Sharpner
    Scale
    


```python

sample_list=list(sample_product)
print(type(sample_list))

sample_list[1]=500
print(sample_list)

sample_product=tuple(sample_list)
print(type(sample_product))
```

    <class 'list'>
    ['Book', 500, 'science']
    <class 'tuple'>
    

## Task 2: Categories (Sets)


```python
product_categories=["study","stationary","stationary","stationary","lunch","school"]
categories_set=set(product_categories)
print(type(categories_set))
categories_set.add("lunch")
categories_set.add("library")
print(categories_set)

print("category in set :", "study" in categories_set)
print("total category in set:",len(categories_set))


```

    <class 'set'>
    {'lunch', 'stationary', 'study', 'school', 'library'}
    category in set : True
    total category in set: 5
    

## Task 3: Product Pricing(Dictoniries)



```python
price_dict={"Book":500,"Eraser":5,"Pen":20,"Pencil":10,"Tiffin":300,"Beg":800}
print(price_dict)
price_dict["Scale"]=5
price_dict["Pen"]=15
print(price_dict)


```

    {'Book': 500, 'Eraser': 5, 'Pen': 20, 'Pencil': 10, 'Tiffin': 300, 'Beg': 800}
    {'Book': 500, 'Eraser': 5, 'Pen': 15, 'Pencil': 10, 'Tiffin': 300, 'Beg': 800, 'Scale': 5}
    


```python
prod_name=input("Type the Product You want to remove:")
if prod_name in price_dict:
    del price_dict[prod_name]
    print(price_dict)
else:
    print("Product not found")

```

    {'Book': 500, 'Eraser': 5, 'Pen': 15, 'Pencil': 10, 'Tiffin': 300, 'Beg': 800}
    


```python
price_average=sum(price_dict.values())/len(price_dict)
print(price_average)
```

    271.6666666666667
    


```python
min_price=min(price_dict,key=price_dict.get)
print("Minimum price product:",min_price)
max_price=max(price_dict,key=price_dict.get)
print("Maximum Price product:",max_price)
```

    Minimum price product: Eraser
    Maximum Price product: Beg
    

## Task 4:Combined Operations


```python
catalog=[]

for i in range(len(products)):
    catalog.append((products[i],price_dict[products[i]],product_categories[i]))
    
print(catalog)
```

    [('Book', 500, 'study'), ('Eraser', 5, 'stationary'), ('Pen', 15, 'stationary'), ('Pencil', 10, 'stationary'), ('Tiffin', 300, 'lunch'), ('Beg', 800, 'school')]
    


```python
category_to_product={}
product_1=[]

for product, price, category in catalog:
    if category not in category_to_product:
        category_to_product[category]=[]
    category_to_product[category].append(product)
print(category_to_product)
```

    {'study': ['Book'], 'stationary': ['Eraser', 'Pen', 'Pencil'], 'lunch': ['Tiffin'], 'school': ['Beg']}
    


```python
max_count=0
cat=""
for category in category_to_product:
    count1=len(category_to_product[category])

    if count1>max_count:
        max_count=count1
        cat=category
print("max category is:",cat," with count :",max_count)
```

    max category is: stationary  with count : 3
    


```python

```
