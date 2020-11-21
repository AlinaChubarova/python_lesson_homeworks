number = int(input('Input the number '))
biggest_number = 0
updated_number = number
while updated_number > 0:
    comparison_number = updated_number % 10
    updated_number = updated_number // 10
    if comparison_number > biggest_number:
        biggest_number = comparison_number
        if biggest_number == 9:
            break
print(f'The biggest number is {biggest_number}')

