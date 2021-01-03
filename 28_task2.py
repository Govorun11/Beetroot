'''
Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock
'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_items = {}
total_price = 0
for key, value in stock.items() and prices.items():
    total_items[key] = prices.get(key, 0) * stock.get(key, 0)
    total_price += total_items[key]
print(f'Total price for every key of stock: {total_items}')
print(f'Total price of stock: {total_price}.')