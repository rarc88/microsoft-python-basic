from unicodedata import numeric


pi = 3.14159
print(pi)

first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

days_in_feb = 28
print(str(days_in_feb) + ' days in February')

first_num = '6'
second_num = '2'
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

first_num = numeric(input('Please enter a number: '))
second_num = numeric(input('Please enter another number: '))
print(first_num + second_num)
