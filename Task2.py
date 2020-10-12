time = int(input("Time in seconds: "))
h = time // 3600
m = time % 3600 // 60
s = time % 3600 % 60
print("%002d:%002d:%002d" % (h, m, s))
