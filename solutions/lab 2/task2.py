import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

def print_state(step_name):
    print(f"\n--- {step_name} ---")
    print(f"original: {original}")
    print(f"alias:    {alias}")
    print(f"shallow:  {shallow}")
    print(f"deep:     {deep}")
    print("\nИдентификаторы внешних списков:")
    print(f"  id(original): {id(original)}")
    print(f"  id(alias):    {id(alias)}")
    print(f"  id(shallow):  {id(shallow)}")
    print(f"  id(deep):     {id(deep)}")
    print("Идентификаторы первого вложенного списка [0]:")
    print(f"  id(original[0]): {id(original[0])}")
    print(f"  id(alias[0]):    {id(alias[0])}")
    print(f"  id(shallow[0]):  {id(shallow[0])}")
    print(f"  id(deep[0]):     {id(deep[0])}")
    print("Идентификаторы первой оценки [0][1]:")
    print(f"  id(original[0][1]): {id(original[0][1])}")
    print(f"  id(alias[0][1]):    {id(alias[0][1])}")
    print(f"  id(shallow[0][1]):  {id(shallow[0][1])}")
    print(f"  id(deep[0][1]):     {id(deep[0][1])}")

print_state("Начальное состояние")
original.append(["Databases", 5])
print_state("После original.append(['Databases', 5])")

original[0][1] = 3
print_state("После original[0][1] = 3")



# Матрицы

wrong_matrix = [[0] * 3] * 3
print(wrong_matrix)
print(f"Айди строк мариц {[id(x) for x in wrong_matrix]}")

wrong_matrix[0][0] = 1
print("После преобразований - ", wrong_matrix)


correct_matrix = [[0] * 3 for _ in range(3)]
print(f"Айди строк мариц {[id(x) for x in correct_matrix]}")
correct_matrix[0][0] = 1
print("Корректная матрица - ", correct_matrix)