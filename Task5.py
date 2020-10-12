Earnings = float(input("Выручка:"))
Expences = float(input("Издержки:"))
if Earnings > Expences:
    print("Фирма прибыльна. Рентабельность составила " + "{:.1f}".format((Earnings - Expences) / Earnings * 100) + "%")
    numberofemploees = int(input("Количество сотрудников фирмы: "))
    print("Прибыль на каждого сотрудника %.1f" % ((Earnings - Expences) / numberofemploees))
else:
    print("Фирма уботычна.")
