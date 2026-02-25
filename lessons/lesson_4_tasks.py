### 🟡 Уровень 2 — Средний

#Задание 2.1: Есть смешанный список. Создай два новых списка: один только с числами, другой только со строками.

# mixed = [1, "hello", 3.14, True, "world", 42, None, "python"]
# numbers = []
# strings = []
# Напиши цикл for с проверкой типов

#с проверкой на bool
# mixed = [1, "hello", 3.14, True, "world", 42, None, "python"]
# numbers = []
# strings = []
#
# for item in mixed:
#     if isinstance(item, bool):  # bool — подкласс int, проверяем первым
#         pass
#     elif isinstance(item, (int, float)):
#         numbers.append(item)
#     elif isinstance(item, str):
#         strings.append(item)
#
# print("Числа:", numbers)   # [1, 3.14, 42]
# print("Строки:", strings)  # ['hello', 'world', 'python']
#
# #без проверки на bool
# mixed = [1, "hello", 3.14, True, "world", 42, None, "python"]
# numbers = []
# strings = []
#
# for item in mixed:
#     if isinstance(item, (int, float)):
#         numbers.append(item)
#     elif isinstance(item, str):
#         strings.append(item)
#
# print("Числа:", numbers)   # [1, 3.14, True, 42]
# print("Строки:", strings)  # ['hello', 'world', 'python']



#Задание 2.2: Создай словарь с данными о себе (имя, возраст, город). Затем:

# - Выведи только имя
# - Измени возраст на любое другое число
# - Добавь новый ключ "hobby"
# - Удали ключ "city"

# person = {
#     "name": "Sergey",
#     "age": 25,
#     "city": "Minsk"
# }
#
# # Выведи только имя
# print(person["name"])  # Алексей
#
# # Измени возраст
# person["age"] = 40
#
# # Добавь новый ключ
# person["hobby"] = "Python"
#
# # Удали ключ "city"
# del person["city"]
#
# print(person)  # {'name': 'Sergey', 'age': 40, 'hobby': 'Python'}

#Задание 2.3: Объясни разницу в результатах и исправь второй вариант:

# Вариант 1
# a = [1, 2, 3]
# b = a
# a.append(4)
# print(a)  # [1, 2, 3, 4]
# print(b)  # [1, 2, 3, 4] - b тоже изменился!

# Вариант 2 — исправь, чтобы b не менялся
# a = [1, 2, 3]
# b = a   # ← что нужно изменить?
# a.append(4)
# print(b)  # должно быть [1, 2, 3]

# a = [1, 2, 3]
# b = a.copy()   #  создаём настоящую копию
# a.append(4)
# print(a)  # [1, 2, 3, 4]
# print(b)  # [1, 2, 3]  ✓


###  Уровень 3 — Продвинутый (применение в тестировании)

#Задание 3.1: Анализ тестовых данных** Есть список словарей с результатами тестов. Найди все упавшие тесты:

# test_results = [
#     {"name": "test_login", "status": "passed", "time": 1.2},
#     {"name": "test_signup", "status": "failed", "time": 0.8},
#     {"name": "test_cart", "status": "passed", "time": 2.1},
#     {"name": "test_payment", "status": "failed", "time": 3.5},
#     {"name": "test_logout", "status": "passed", "time": 0.5},
# ]

# Напиши код, который:
# 1. Выводит имена всех упавших тестов
# 2. Считает количество passed и failed
# 3. Выводит имя самого медленного теста

# # 1. Имена упавших тестов
# print("Упавшие тесты:")
# for test in test_results:
#     if test["status"] == "failed":
#         print(" --", test["name"])
#
# # 2. Количество passed и failed
# passed = 0
# failed = 0
# for test in test_results:
#     if test["status"] == "passed":
#         passed += 1
#     else:
#         failed += 1
#
# print(f"\nПройдено: {passed}, Упало: {failed}")
#
# # 3. Самый медленный тест
# slowest = test_results[0]
# for test in test_results:
#     if test["time"] > slowest["time"]:
#         slowest = test
#
# print(f"Самый медленный тест: {slowest['name']} ({slowest['time']}s)")

#упавшие в 1 строку
# for test in test_results:
#     if test["status"] == "failed":
#         print(test["name"], end=" ")  # вместо \n ставит пробел
# test_signup test_payment


#Задание 3.2: Список URL для проверки** Проверь список URL и создай два словаря: валидные и невалидные:
# print("Валидные:", valid)
# print ("Невалидные:", invalid)
# URL валидный, если начинается с "https://"

# urls = [
#     "https://google.com",
#     "http://insecure.com",
#     "https://api.service.com",
#     "ftp://old-server.com",
#     "https://valid-site.org",
# ]
#
# valid = []
# invalid = []
#
# for url in urls:
#     if url.startswith("https://"):
#         valid.append(url)
#     else:
#         invalid.append(url)
#



# Задание 3.3: Работа с вложенным словарём** Есть структура данных API-ответа. Достань и выведи нужные поля:

# api_response = {
#     "status": "success",
#     "data": {
#         "user": {
#             "id": 12345,
#             "name": "Denis",
#             "email": "denis@test.com"
#         },
#         "permissions": ["read", "write", "delete"]
#     }
# }
# # Выведи: имя пользователя, email, второй permission
#
# # Имя пользователя
# print(api_response["data"]["user"]["name"])
#
# # Email
# print(api_response["data"]["user"]["email"])
#
# # Второй permission (индекс 1)
# print(api_response["data"]["permissions"][1])