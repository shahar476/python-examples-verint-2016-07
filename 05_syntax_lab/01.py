print "Enter 10 numbers"
max = int(raw_input())
for i in range (1,10):
    number = int(raw_input())
    if number > max: 
        high = number
print "The biggeset number is: %d" % max