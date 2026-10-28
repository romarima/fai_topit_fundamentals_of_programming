import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print(f"Сборщик мусора включен: {gc.isenabled()}")
print(f"Пороги поколений (thresholds): {gc.get_threshold()}")
print(f"Текущая статистика поколений (count): {gc.get_count()}")

id_f = id(first)
id_s = id(second)
print(id_f, id_s)

del first
del second

coll = gc.collect()
print(coll)

# Отключение сборщика

gc.disable()
print(f"Сборщик мусора включен: {gc.isenabled()}")

for _ in range(10):
    a = []
    b = []
    a.append(b)
    b.append(a)
    del a
    del b

coll2 = gc.collect()
print(coll2)

gc.enable()
print(f"Сборщик мусора включен: {gc.isenabled()}")

node1 = {"id": 1, "test": [], "name": "name1"}
node2 = {"id": 2, "test": [], "name": "name2"}
node3 = {"id": 3, "test": [], "name": "name3"}
node4 = {"id": 4, "test": [], "name": "name4"}

node1["test"].append(node2)
node2["test"].append(node3)
node3["test"].append(node1)

print("Связи графа сформированы:")
print(f"Node 1 -> {node1['test'][0]['name']}")
print(f"Node 2 -> {node2['test'][0]['name']}")
print(f"Node 3 -> {node3['test'][0]['name']}")

gc.collect()
coll3 = gc.collect()
print(coll3)

del node1
del node2
del node3

coll4 = gc.collect()
print(f"До удаления графа {coll3}")
print(f"После удаления графа {coll4}")

print(f"Независимый узел {node4['name']} (id: {node4['id']})")