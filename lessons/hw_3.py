        ###2
day = input()

if day == "суббота" or day == "воскресенье":
    print("Сегодня выходной!")
elif day == "среда":
    print("Мне сегодня к стоматологу в 15:30")
else:
    print("Сегодня обычный день.")


        ###1
n = int(input())

if n % 2 == 0:
    print("четное")
else:
    print("нечетное")


        ###3
n = int(input())
text = input()

for _ in range(n):
    print(text)

        ###4
message = input()
vowels = "аеёиоуыэюя"

count = 0
for i in message.lower():
    if i in vowels:
        count += 1 #сокращение count = count + 1

print(count)


        ###5
total = 0  # переменная для суммы

while True:
    n = int(input("Введите число: "))  # ввод числа
    if n < 0:  # если число отрицательное, выход из цикла
        break
    total += n  # добавляем число к сумме

print("Сумма введённых чисел:", total)





age = 14

if age <= 12:
    print("Ребенок")
elif age <= 17:
    print("Подросток")
else:
    print("Взрослый")

###
age = 5
is_citizen = True

if age >= 18 and is_citizen == True:
    print("Голосовать!")
else:
    print("НЕ Голосовать!")





count = 1

if count:
    print(f"на вашем счету {count}")
else:
    print("У вас нет денег")



for i in range(10):
    print("Hello World")



for letter in "Яблоко":
    print(letter)

