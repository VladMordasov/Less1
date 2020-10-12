var1 = int(input("Целое положительное число: "))
MaxDigit = 0
while var1 > 0:
    if var1 % 10 > MaxDigit:
        MaxDigit = var1 % 10
    var1 = var1 // 10
print(MaxDigit)
