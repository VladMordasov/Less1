a = float(input("Результат спортсмена за первый день:"))
b = float(input("Какой результат нужен: "))
numberofdays = 1
res = a
while res < b:
    res *= 1.1
    numberofdays += 1
print("Результат не менее " + str(b) + " будет достигнут на " + str(numberofdays) + " день.")
