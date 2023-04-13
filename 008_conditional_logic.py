addTaxBefore = 1.00
taxRate = .12

inputPrice = input('Price: ')
price = float(inputPrice)


if price >= addTaxBefore:
    tax = price * (taxRate)
else:
    tax = 0

print(f'Tax: {tax}')

total = price + tax
print(f'Total: {total}')

print()
country = input('Where are you from? ')
if country.lower() == 'canada':
    print('You are from Canada')
else:
    print('You are not from Canada')
