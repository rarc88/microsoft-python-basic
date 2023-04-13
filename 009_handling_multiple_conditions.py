print('Are you Canadian? ')
print('(y)es')
print('(n)o')
isCanadian = input('Choose an option: ')

if isCanadian.lower() in ('y', 'yes'):
    print('Where province/state are you from? ')
    print('1. Alberta')
    print('2. Nunavut')
    print('3. Ontario')
    print('4. Other')
    option = input('Choose an option: ')

    # if option == '1':
    #     taxRate = 0.05
    # elif option == '2':
    #     taxRate = 0.05
    # if option == '1' or option == '2':
    #     taxRate = 0.05
    if option in ('1', '2'):
        taxRate = 0.05
    elif option == '3':
        taxRate = 0.13
    else:
        taxRate = 0.15
else:
    taxRate = 0

print(f'TaxRate: {taxRate}')
