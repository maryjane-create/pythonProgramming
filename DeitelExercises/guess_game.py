import  random
import  sys

answer= random.randrange(1,  3)

guess=int(input('please enter number'))
while guess!=answer:
    if guess>answer:print('number too high')
    # guess = int(input('please enter number'))
    elif guess<answer:print('number is too low')
    guess=int(input('please enter number'))
if guess == answer:
        print('correct!')
        sys.exit()


