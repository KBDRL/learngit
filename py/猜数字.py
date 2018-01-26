import string


def isWordGuessed(secretWord, lettersGuessed):
    '''如果所猜字符在秘密单词中返回True'''
    for i in secretWord:
        if i in lettersGuessed:
            return True
    return False

def getGuessedWord(secretWord, lettersGuessed):

    m = ''
    for i in secretWord:
        if i not in lettersGuessed:
            m += ' _ '
        else:
            m += i
    return m

def getAvailableLetters(lettersGuessed):
    s = string.ascii_lowercase
    for i in lettersGuessed:
        if i in s:
            s = s.replace(i,' ')
    return s

def hangman(secretWord):
    import string
    secretWord = secretWord.lower()
    count = 8
    guess = ''
    s = string.ascii_lowercase
    L = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %s letters long.' % len(secretWord))
    while count > 0:
        print('------------')
        print('You have %s guesses left.' % count)
        print('Available letters: %s' % s)
        guess = input('Please guess a letter:')
        L.append(guess)
        g = getGuessedWord(secretWord, L)
        if isWordGuessed(secretWord, guess) and guess in s:
            print('Good guess:%s' % g)
            if g == secretWord:
                print('------------')
                print('Congratulations, you won!')
                return
            s = s.replace(guess, '')

        elif guess not in s:
            print('------------')
            print("Oops! You've already guessed that letter: %s" % g)
        else:
            s = s.replace(guess, ' ')
            count -= 1
            print('Oops! That letter is not in my word: %s' % g)


    print('------------')
    print('Sorry, you ran out of guesses. The word was else. ')
    return
a = 'sea'
hangman(a)
