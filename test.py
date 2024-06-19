import time

start_time = time.time()
stop = ''

job = input('Enter job: ')
print('Enter s to stop: ')

# while stop.lower() != 's':
    # stop = input()/
    # num = (round((time.time() - start_time), 2))
num = int(input())

if num >= 3600:
     num /= 60
     num /= 60

print(round(num, 2))
