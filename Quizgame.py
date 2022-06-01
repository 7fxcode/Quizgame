import os
import time
from colorama import Fore

points = 0

os.system('cls')
print(Fore.BLUE + '''
 ██████╗ ██╗   ██╗██╗███████╗ ██████╗  █████╗ ███╗   ███╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║   ██║██║   ██║██║  ███╔╝ ██║  ███╗███████║██╔████╔██║█████╗  
██║▄▄ ██║██║   ██║██║ ███╔╝  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝██║███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝''')
print('')
print(Fore.BLUE + 'Press Enter to play a quiz!')
cont = input('')
os.system('cls')
print(Fore.BLUE + 'Question 1\n\nWho painted the Mona Lisa??')
print(Fore.BLUE + 'a) Leonardo da Vinci')
print(Fore.BLUE + 'b) James Bond')
print(Fore.BLUE + 'c) Vincent Van Gogh')
q1 = input('> ')
time.sleep(0.5)
print(Fore.BLUE + 'Checking answer...')
time.sleep(2)
if q1 == 'a':
    points +=25
    print(Fore.BLUE + 'Correct, congrats!')
    print(Fore.BLUE + '+25 Points, you now have {} Points!'.format(points))
else:
    print(Fore.BLUE + 'Wrong, sad!')
    print(Fore.BLUE + '+0 Points, you now have {} Points!'.format(points))

time.sleep(1)
print(Fore.BLUE + 'Loading question 2...')
time.sleep(1)
os.system('cls')
print(Fore.BLUE + 'Question 2\n\nWhen did the Eiffeltower get build?')
print(Fore.BLUE + 'a) 17. October 1901')
print(Fore.BLUE + 'b) 28. January 1887')
print(Fore.BLUE + 'c) 19. June 1851')
q2 = input('> ')
time.sleep(0.5)
print(Fore.BLUE + 'Checking answer...')
time.sleep(2)
if q2 == 'b':
    points +=25
    print(Fore.BLUE + 'Correct, congrats!')
    print(Fore.BLUE + '+25 Points, you now have {} Points!'.format(points))
else:
    print(Fore.BLUE + 'Wrong, sad!')
    print(Fore.BLUE + '+0 Points, you now have {} Points!'.format(points))
time.sleep(1)
print(Fore.BLUE + 'Loading question 3...')
time.sleep(1)
os.system('cls')
print(Fore.BLUE + 'Question 3\n\nWho made the popular programming language Python?')
print(Fore.BLUE + 'a) Guido van Rossum')
print(Fore.BLUE + 'b) Alexander Triskow')
print(Fore.BLUE + 'c) Daniel Rick')
q3 = input('> ')
time.sleep(0.5)
print(Fore.BLUE + 'Checking answer...')
time.sleep(2)
if q3 == 'a':
    points +=25
    print(Fore.BLUE + 'Correct, congrats!')
    print(Fore.BLUE + '+25 Points, you now have {} Points!'.format(points))
else:
    print(Fore.BLUE + 'Wrong, sad!')
    print(Fore.BLUE + '+0 Points, you now have {} Points!'.format(points))
time.sleep(1)
print(Fore.BLUE + 'Loading question 4...')
time.sleep(1)
os.system('cls')
print(Fore.BLUE + 'Question 4\n\nWhat made Java so popular?')
print(Fore.BLUE + 'a) Minecraft uses Java')
print(Fore.BLUE + 'b) Platform independence')
print(Fore.BLUE + 'c) Syntax of the code')
q4 = input('> ')
time.sleep(0.5)
print(Fore.BLUE + 'Checking answer...')
time.sleep(2)
if q4 == 'b':
    points +=25
    print(Fore.BLUE + 'Correct, congrats!')
    print(Fore.BLUE + '+25 Points, you now have {} Points!'.format(points))
else:
    print(Fore.BLUE + 'Wrong, sad!')
    print(Fore.BLUE + '+0 Points, you now have {} Points!'.format(points))
time.sleep(1)
print(Fore.BLUE + 'Loading question 5...')
time.sleep(1)
os.system('cls')
print(Fore.BLUE + 'Question 5\n\nWhat language is the most popular in the world?')
print(Fore.BLUE + 'a) Javascript')
print(Fore.BLUE + 'b) C++')
print(Fore.BLUE + 'c) Python')
q5 = input('> ')
time.sleep(0.5)
print(Fore.BLUE + 'Checking answer...')
time.sleep(2)
if q5 == 'c':
    points +=25
    print(Fore.BLUE + 'Correct, congrats!')
    print(Fore.BLUE + '+25 Points, you now have {} Points!'.format(points))
else:
    print(Fore.BLUE + 'Wrong, sad!')
    print(Fore.BLUE + '+0 Points, you now have {} Points!'.format(points))
    time.sleep(3)
    print(Fore.BLUE + 'Calculating result...')
    time.sleep(2)
if points > 75:
    print(Fore.BLUE + 'You`ve reached {} Points and won the quizgame!'.format(points))
    exita = input('')
elif points < 75:
    print(Fore.BLUE + 'You`ve reached {} Points and lost the quizgame, sad!'.format(points))
    print(Fore.RED + 'Press Enter to exit!')
exita = input('')
exit()
