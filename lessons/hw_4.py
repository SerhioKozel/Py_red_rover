#списки
# items = [1, 2, 3, 4, 5, "Hello", True, None, False, [1,2,3]]
#
# print(items)
from operator import add

# items = [1, 2, 3, 4, 5, "Hello", True] #индексы 0 1 2 3 4...
#
# a = (items[0]) #1
# b = (items[6]) #True
# items[1] = 99
# print(a, b)


# items = [1, 2, 3, 4, 5, "Hello", True] #индексы 0 1 2 3 4...
# items[1] = 99
# print(items)

# items = [1, 2, 3, 4, 5, "Hello", True] #индексы 0 1 2 3 4...
# del items[6]
# print(items)


# items = [1, 2, 3, 4, 5, "Hello", True] #индексы 0 1 2 3 4...
#
# items.append(6)
# items.append("text")
# print(items) #[1, 2, 3, 4, 5, 'Hello', True, 6, 'text']

# numbers = [1, 2, 3, 4, 5, "Hello", True, 45, 45, 124,66]
# print(numbers[-1]) #обратная индексация

# numbers = [1, 2, 3, 4, 5, "Hello", True, 45, 45, 124,66]
# print(numbers[2:6]) #старт/стоп среза невключительно

# numbers = [1, 2, 3, 4, 5]
# a = numbers.pop(2) #3
#
# print(numbers, a)


# numbers = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# a = len(numbers)
#
# print(a)

# numbers = [1, 2, 3, 4, 5, 44 ,21, 45, 66]
# sorted_numbers = sorted(numbers) #сортировка с новым списком
# print(sorted_numbers)

# numbers = [1, 2, 3, 4, 5, 44 ,21, 45, 66]
#
# print(sum(numbers))


# items = [1, 2, 3, 4, 5, "Hello", True]
# numbers = []
# for item in items:
#     if type(item) == int:
#         numbers.append(item)
#
# print(numbers)

nums = [1,2,3]
nums2 = nums.copy() #копия изменяемого объекта

nums.append(4)

print(nums)
print(nums2)








#1 задание
# numbers = [x for x in range(101) if x % 2 == 0 and x % 3 == 0]
# print(numbers)

# numbers = []
#
# for x in range(101):
#     if x % 2 == 0 and x % 3 == 0:
#         numbers.append(x)
#
# print(numbers)

#2 задание
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# numbers = [x for x in items if isinstance(x, (int, float))]
#
# print(sum(numbers))

# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
#
# numbers = []
#
# for x in items:
#     if isinstance(x, (int, float)):
#         numbers.append(x)
#
# print(sum(numbers))


#3 задание
# messages = []
#
# while True:
#     message = input("Введите сообщение: ")
#
#     messages.append(message)
#
#     if len(messages) > 5:
#         messages.pop(0)
#
#     if message == "Пока":
#         print("Ну ладно, пока!")
#         print(messages)
#         break

#Рефакторинг
#
# age = 16
# admin = True
#
# if age > 18 and admin == True:
#     print("closed")
# else:
#     print("opened")
#
#     исправлено на:
# age = 16
# admin = True
#
# if age >= 18 or admin:
#     print("opened")
# else:
#     print("closed")