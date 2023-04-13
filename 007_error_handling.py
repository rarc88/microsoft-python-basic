x = 10
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, division by zero not allowed')
else:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
