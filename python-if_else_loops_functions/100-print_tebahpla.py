#!/usr/bin/python3
s = ""
for i in range(90, 64, -1):
    if i % 2 == 0:
        s += chr(i)
    else:
        s += chr(i + 32)

    
print("{}".format(s))
