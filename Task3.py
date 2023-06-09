# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input("Введите шестизначный номер билета: "))

num1 = number // 1000
num2 = number % 1000

sum1 = 0
sum2 = 0

while num1 > 0 and num2 > 0:
  n1 = num1 % 10 
  n2 = num2 % 10 
  sum1 += n1
  sum2 += n2
  num1 //=10
  num2 //=10

if sum1 == sum2:
  print("Поздравляю, этот билет СЧАСТЛИВЫЙ!")
else:
  print("Увы, это не счастливый билет.")

