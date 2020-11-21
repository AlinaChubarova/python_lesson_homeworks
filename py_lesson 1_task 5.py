earning = float(input('Input the earnings - '))
costs = float(input('Input the costs - '))
if earning > costs:
    print(f'Congratulations! You have the revenue! Your profitability is {(earning/costs)}')
    number_employees = int(input('Please enter the number of your employees -'))
    print(f'Thanks. Your revenue by 1 employee is {(earning-costs)/number_employees}')
elif earning == costs:
    print('Not bad.Your earning = your costs')
else:
    print('So pity. Your costs is bigger than your earning')
