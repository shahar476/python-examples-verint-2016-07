from random import randint
while True:
    x = randint(1,1000000)
    if x % 7 == 0 and x % 13 == 0 and x % 15 == 0:
        print x
        break