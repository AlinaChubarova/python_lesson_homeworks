time = int(input('Enter time in seconds'))
hour = time // 3600
minute = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'Your time is {hour:02}:{minute:02}:{seconds:02}')