#The items in a shopping cart can be modelled in a dictionary. Write a program 
#that can add a new item, remove an item, update an item's 

shopping_cart = {'item1': "clothes", 'item2': "groceries", 'item3': "fruits", 'item4': "beverages"}

def add():
    shopping_cart['item5'] = "food"
    return shopping_cart

print(add())

def remove():
    del shopping_cart['item2']
    return shopping_cart

print(remove())

def update():
    shopping_cart['item5'] = "shoes"
    return shopping_cart

print(update())
