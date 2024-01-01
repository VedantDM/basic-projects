import random
random_num = int(input('enter random number:'))

guess = None
attempt = 0
while guess!= random_num:
    guess = int(input('enter number:'))
    attempt += 1

    if guess<random_num:
        print('too low')
    elif guess>random_num:
        print('too high')

print(f'u guessed it {random_num} is the random number in {attempt} attempts')