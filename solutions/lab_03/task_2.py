import random

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

summ = 0
maximum = 0
minimum = float("inf")
evens = 0

for i in measurements:
    summ += i
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
    if i % 2 == 0:
        evens += 1
print(f"Сумма: {summ}")

print(f"Сумма: {summ}")
print(f"Минимум: {minimum}")
print(f"Максимум: {maximum}")
print(f"Количество четных: {evens}")

mid = summ / len(measurements)
count_gt_mid = 0

for x in measurements:
    if x > mid:
        count_gt_mid += 1

print(f"Количество больше среднего ({mid:.2f}): {count_gt_mid}")

user_input = int(input("Введите число - "))

def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1
print(linear_search(measurements, user_input))

arr1 = list(range(10))
arr2 = list(range(100))
arr3 = list(range(1000))

def selection_sort(arr: list) -> int:
    n = len(arr)
    count = 0
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
            count += 1
        arr[i], arr[m] = arr[m], arr[i]
    return count

def binary_search(arr: list, target: int) -> int:
    l, r = 0, len(arr) - 1
    count = 0
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return count
        count += 1
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        count += 1
    return count

print("Selection sort")
for i in [arr1, arr2, arr3]:
    print(f"Длина - {len(i)}, Кол-во сравнений - {selection_sort(i)}")
print("Binary search")
for i in [arr1, arr2, arr3]:
    print(f"Длина - {len(i)}, Кол-во сравнений - {binary_search(i, random.randint(0, len(i)))}")

# Проверка простоты положительного целого числа (до sqrt(n))
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print("Проверка на простоту:")
for num in [2, 7, 15, 18, 29]:
    print(f"{num}: {is_prime(num)}")

# Линейный поиск со счетчиком сравнений
def linear_search_count(arr: list, target: int) -> int:
    count = 0
    for x in arr:
        count += 1
        if x == target:
            return count
    return count

# Сравнительная таблица линейного и бинарного поиска
print("\nСравнение числа сравнений (Linear vs Binary):")
print("Длина | Искомое | Linear | Binary")
for arr in [list(range(10)), list(range(100)), list(range(1000))]:
    target = random.choice(arr)
    lin_cnt = linear_search_count(arr, target)
    bin_cnt = binary_search(arr, target)
    print(f"{len(arr)} | {target} | {lin_cnt} | {bin_cnt}")
