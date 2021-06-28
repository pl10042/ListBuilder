# AI that Guesses the numbers in a randomly generated list
import random

# ylist = []
# while len(ylist) < 5:
#     if len(ylist) < 5:
#         y = random.randint(0,10)
#         ylist.append(y)
#
#
# for x in xlist:
#     if x < len(xlist):
#         ylist.append(x)

# print(ylist)
#
# xylist = (xlist + ylist)


xlist = []
# range1 = int(input(f'How big should the list be?\n'))
# range2 = int(input(f'What should the maximum number in the list be?\n'))
randoTest = random.randint(0,100)
randoTest2 = random.randint(0,100)
#creates a list from size 0 to 100 with numbers 0 to 100
while len(xlist) < randoTest:
    if len(xlist) < randoTest:
        x = random.randint(0, randoTest2)
        xlist.append(x)
print(f'O: {xlist}')
print()

guess = random.randint(0,randoTest2)

newList = []
#Guesses each number in xlist
for x in xlist:
    while guess != x:
        if guess < x:
            guess += 1
        elif guess > x:
            guess -= 1
    if guess == x:
        newList.append(guess)
print(f'C: {newList}')


