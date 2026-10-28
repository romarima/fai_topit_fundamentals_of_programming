import sys
import weakref

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

registry = weakref.WeakValueDictionary()

reg1 = Record()
reg2 = Record()
reg3 = Record()

registry['1'] = reg1
registry['2'] = reg2
registry['3'] = reg3

print(f"list {list(registry.keys())}")

del reg3
print(f"list {list(registry.keys())}")

del reg1
print(f"list {list(registry.keys())}")

print(registry['2'] is reg2)