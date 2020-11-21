a = float(input('Please enter your start result - '))
b = float(input('Please enter your finish result - '))
day_counter = 1
while a < b:
    a = a * 1.1
    day_counter += 1
print(f'Your target result will be accessible on {day_counter} day')
