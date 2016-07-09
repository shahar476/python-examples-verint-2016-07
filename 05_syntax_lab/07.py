from random import randint
num = randint(1,100)
guess = int(raw_input())
if guess < num:
    print "Smaller"
elif guess > num:
    print "Bigger"