time = int(input("Time in seconds"))
print(str(time // 3600) + " часов, " + str((time % 3600) // 60) + " минут, " + str(time % 3600 % 60) + " секунд.")
