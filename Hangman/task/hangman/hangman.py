# import random
#
#
# def loadWords():
#     # word_list = ['javascript']
#     word_list = ['python', 'kotlin', 'java', 'javascript']
#     return random.choice(word_list)
#
#
# word = loadWords()
#
#
# def isWordGuessed(secretWord, lettersGuessed):
#     c = 0
#     for i in lettersGuessed:
#         if i in secretWord:
#             c += 1
#     if c == len(secretWord):
#         return True
#     else:
#         return False
#
#
# def getGuessedWord(secretWord, lettersGuessed):
#     s = []
#     for i in secretWord:
#         if i in lettersGuessed:
#             s.append(i)
#     ans = ''
#     for i in secretWord:
#         if i in s:
#             ans += i
#         else:
#             ans += '-'
#     return ans
#     print(ans)
#
#
# def getAvailableLetters(lettersGuessed):
#     import string
#     ans = list(string.ascii_lowercase)
#     for i in lettersGuessed:
#         ans.remove(i)
#     return ''.join(ans)
#     print(ans)
#
#
# def hangman(secretWord):
#     print("H A N G M A N")
#     print()
#     hidden = len(word)
#     hint = "-" * hidden
#     print(hint)
#     # print("Welcome to the game, Hangman!")
#     # print("I am thinking of a word that is", len(secretWord), "letters long.")
#     #
#     global letters_guessed
#     turns = 0
#     letters_guessed = []
#
#     while 8 - turns > 0:
#         turns += 1
#         if isWordGuessed(secretWord, letters_guessed):
#             # 	print(word)
#             # 	print("Congratulations, you won!")
#             # 	break
#             continue
#
#         else:
#             # print("-------------")
#             # print("You have", 8 - mistakeMade, "guesses left.")
#             # print("Available letters:", getAvailableLetters(lettersGuessed))
#             guess = str(input("Input a letter: ")).lower()
#             # if guess in lettersGuessed:
#             # 	print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
#
#             if guess in secretWord and guess not in letters_guessed:
#                 # x = guess in secretWord and guess not in lettersGuessed
#                 if guess in letters_guessed:
#                     print('No improvements')
#                 letters_guessed.append(guess)
#                 print(getGuessedWord(secretWord, letters_guessed))
#             else:
#                 letters_guessed.append(guess)
#                 print("That letter doesn't appear in the word.")
#                 if 8 - turns > 0:
#                     print(getGuessedWord(secretWord, letters_guessed))
#
#         if 8 - turns == 0:
#             # print(word)
#             print('No improvements')
#             print('You lost!')
#             print("Thanks for playing!")
#             print("We'll see how well you did in the next stage")
#             break
#
#         else:
#             continue
#
#
# secretWord = word.lower()
# hangman(secretWord)

# import random
# # Write your code here
# random_list = ['python', 'java', 'kotlin', 'javascript']
# word = random.choice(random_list)
# hidden_word = list('-' * len(word))
# print("H A N G M A N")
# for _ in range(8):
#     if ''.join(hidden_word) == word:
#         break
#     while True:
#         print()
#         print(''.join(hidden_word))
#         if ''.join(hidden_word) == word:
#             break
#         letter = input("Input a letter: ")
#         if letter in word and letter not in ''.join(hidden_word):
#             for x in range(len(word)):
#                 if letter == word[x]:
#                     hidden_word[x] = letter
#         elif letter in hidden_word:
#             print("No improvements")
#             break
#         else:
#             print("That letter doesn't appear in the word")
#             break
# if ''.join(hidden_word) == word:
#     print("You guessed the word!")
#     print("You survived!")
# else:
#     print("You lost!")
# import random
#
#
# def answer(letters, used_letters, hidden):
#     if letters == used_letters:
#         print(*hidden, sep='')
#         print('''You guessed the word!
#     You survived!''')
#         exit()
#
#
# def play():
#     words = ['python', 'java', 'kotlin', 'javascript']
#     tries = 8
#     choice = random.choice(words)
#     # a = choice[0:3]
#     # b = (len(choice) - 3) * '-'
#     hidden = list(len(choice) * '-')
#     letters = set(choice)
#     used_letters = []
#     symbols = '1234567890!@#$%^&*()_-{[}]:;"\'<,|\\>.?/~=+`'
#
#     while tries > 0:
#         answer(letters, used_letters, hidden)
#         print('\n', *hidden, sep='')
#
#         letter = input('Input a letter:')
#         if letter in used_letters:
#             print('You already typed this letter')
#             continue
#         if len(letter) != 1:
#             print('You should input a single letter')
#             continue
#         if letter.isupper() or letter in symbols:
#             print('It is not an ASCII lowercase letter')
#             continue
#         if letter not in used_letters:
#             used_letters.append(letter)
#
#         if letter in letters:
#             for x in range(len(choice)):
#                 if letter == choice[x]:
#                     hidden.pop(x)
#                     hidden.insert(x, letter)
#                     print()
#         else:
#             tries -= 1
#             print('No such letter in the word')
#     else:
#         print('You are hanged!')
#
#
# def menu():
#     choose = input('Type "play" to play the game, "exit" to quit:')
#     if choose == 'play':
#         play()
#     elif choose == 'exit':
#         exit()
#     else:
#         menu()
#
#
# print('H A N G M A N')
# menu()
#
import random
from string import ascii_lowercase
print('H A N G M A N')


while True:
    print('Type "play" to play the game, "exit" to quit:')
    choice = input()
    if choice == 'play':
        word = random.choice(['python', 'java', 'kotlin', 'javascript'])
        # word = random.choice(['java'])
        s = set()
        w = set()
        lives = 8
        while lives > 0:
            print()
            for k in word:
                if k in s:
                    print(k, end='')
                else:
                    print('-', end='')
            print()
            print('Input a letter: ', end='')
            n = input()
            if n not in word and n not in w and n in ascii_lowercase:
                print('That letter doesn\'t appear in the word')
                lives -= 1
                w.add(n)
            elif n in w:
                print('You\'ve already guessed this letter')
                lives -= 0
            elif n in s:
                print('You\'ve already guessed this letter')
                lives -= 0
            elif len(n) > 1:
                print('You should input a single letter')
                lives -= 0
            elif n not in ascii_lowercase:
                print('Please enter a lowercase English letter')
                lives -= 0
            else:
                s.add(n)
            if set(word) == s:
                print('You guessed the word ' + word +'!\nYou survived!')
                break
        else:
            print('You lost!')
    else:
        break