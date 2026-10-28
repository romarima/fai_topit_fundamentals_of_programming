import tracemalloc
import sys

data = []
data.append({"name": "Тест 1"})

tracemalloc.start()

numbers = list(range(100_000))

data[0]["cur_memory"], data[0]["peak_memory"] = tracemalloc.get_traced_memory()
data[0]["size"] = sys.getsizeof(numbers)
data[0]["count"] = len(numbers)
tracemalloc.stop()

data.append({"name": "Тест 2"})

tracemalloc.start()

numbers2 = range(100000)

data[1]["cur_memory"], data[1]["peak_memory"] = tracemalloc.get_traced_memory()
data[1]["size"] = sys.getsizeof(numbers2)
data[1]["count"] = len(numbers2)
tracemalloc.stop()

for i in data:
    print("Название:", i["name"])
    print("Число элементов:", i["count"])
    print("Размер:", i["size"])
    print("Текущий объем:", i["cur_memory"] / 1024, "KB")
    print("Пиковый объект:", i["peak_memory"] / 1024, "KB")

print("Отношение пикового объема двух сценариев:", data[0]['peak_memory'] / data[1]['peak_memory'])
