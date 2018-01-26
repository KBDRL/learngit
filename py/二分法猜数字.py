'''这是个二分法猜数字游戏'''
#print('Is your secret number:')
print("Please think of a number between 0 and 100!")
h = 100
z = 0
while 1:
    m = round((h+z)/2)
    print('Is your secret number ' + str(m) + "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    n = input()
    if n == 'c':
        print('Game over. Your secret number was: ' + str(m))
        break
    elif n == 'h':
        h = m
    elif n == 'l':
        z = m
        print(z)
        pass
    else:
        print('Sorry, I did not understand your input.')
