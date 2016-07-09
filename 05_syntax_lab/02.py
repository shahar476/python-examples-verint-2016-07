sum = 0
for i in range (0,7):
    sum += i
print "Total = %d" % sum
if sum % 7 ==0:
    print "boom"
else:
    print "not boom"