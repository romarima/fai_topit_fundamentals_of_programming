from copy import deepcopy

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]
print(first, second)
print(id(first), id(second))
print(first == second, first is second)

second.append(40)
print(first, second)

# =========================
# Практическое задание

config_1 = {
    "project name": "Пышки",
    "members": ["Roman", "Vlad", "Vasya"],
    "params": [["par1", "par2"], ["par3", "par4"]],
}
config_2 = config_1
config_2["project name"] = "Булки"
config_2["params"][0].append("test")

print("После нежелательного изменения")
print(f"Конфиг 1 - {config_1}")
print(f"Конфиг 2 - {config_2}")
print(f"Общий ли словарь {config_1 is config_2}")
print(f"Общий ли список параметров {config_1["params"] is config_2["params"]}")

config_1 = {
    "project name": "Пышки",
    "members": ["Roman", "Vlad", "Vasya"],
    "params": [["par1", "par2"], ["par3", "par4"]],
}

config_3 = deepcopy(config_1)
config_3["project name"] = 'Булки'
config_3["members"].append("Vitaliy")

print("Создание независимой конфигурации")
print(f"config_1 - {config_1}")
print(f"config_3 - {config_3}")

assert config_1 is not config_3, 'Словари должны быть разными объектами'
assert config_3["project name"] is not config_1["project name"]
assert config_3["members"] is not config_1["members"]

print("Итоговый тест")
print(f"Общий ли словарь {config_1 is config_3}")
print(f"Общий ли список параметров {config_1["params"] is config_3["params"]}")
