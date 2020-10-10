a = input("Результат спортсмена за первый день:")
b = input("Какой результат нужен: ")
numberofdays = 1
res = a
while res < b:
    res *= 1.1
    numberofdays += 1
print("Результат не менее " + b + " будет достигнут на " + numberofdays + "день.")
