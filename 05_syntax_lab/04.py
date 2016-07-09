line = raw_input()
x = ""
while len(line) > 0:
    x = line + "\n" + x
    line = raw_input()
print x