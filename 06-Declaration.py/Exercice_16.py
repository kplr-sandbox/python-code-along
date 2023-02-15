amount_store = int(input('In stock:'))
error = amount_store < 50 or amount_store > 300
print('Stock error:', error)