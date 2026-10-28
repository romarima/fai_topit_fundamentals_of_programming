import sys
import tracemalloc

print("Размер пустого списка:", sys.getsizeof([]))
print("Размер списка из десяти целых чисел:", sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("Размер кортежа из десяти целых чисел:", sys.getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)))
print("Размер строки из десяти символов", sys.getsizeof("1234567890"))
print("Размер целого числа:", sys.getsizeof(1))
print("Размер объекта None:", sys.getsizeof(None))

# Часть 2

test_list = []
size = sys.getsizeof(test_list)

for n in range(100):
    test_list.append(n)
    s = sys.getsizeof(test_list)
    if s != size:
        print(len(test_list), s)
        size = s


tracemalloc.start()
numbers = list(range(100_000))
cur1, peak1 = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("list(range):", cur1 / 1024, "KB,", peak1 / 1024, "KB")

tracemalloc.start()
numbers2 = range(100_000)
cur2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("range:", cur2 / 1024, "KB,", peak2 / 1024, "KB")