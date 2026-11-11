submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

all_students = set()
all_labs = set()
for i in submissions:
    all_students.add(i[0])
    all_labs.add(i[1])
print(all_students)
print(all_labs)

students_try = {}
for i in submissions:
    if i[0] not in students_try:
        students_try[i[0]] = []
    students_try[i[0]].append((i[1], i[2]))
print(students_try)

labs_try = {}
for i in submissions:
    key = (i[0], i[1])
    if key not in labs_try or i[2] > labs_try[key]:
        labs_try[key] = i[2]
print(labs_try)

count_try = {}
for i in submissions:
    key = (i[0], i[1])
    if key not in count_try:
        count_try[key] = 1
    else:
        count_try[key] += 1
print(count_try)

lab1 = {name for name, lab, grade in submissions if lab == 'lab_01'}
lab2 = {name for name, lab, grade in submissions if lab == 'lab_02'}
both_labs = lab1 & lab2
print(both_labs)

# Добавление новой записи без полного перестроения
new_sub = ("daria", "lab_02", 5)
submissions.append(new_sub)
all_students.add(new_sub[0])
all_labs.add(new_sub[1])
if new_sub[0] not in students_try:
    students_try[new_sub[0]] = []
students_try[new_sub[0]].append((new_sub[1], new_sub[2]))
key = (new_sub[0], new_sub[1])
if key not in labs_try or new_sub[2] > labs_try[key]:
    labs_try[key] = new_sub[2]
if key not in count_try:
    count_try[key] = 1
else:
    count_try[key] += 1

# Текстовые запросы
def handle_query(query: str):
    parts = query.split()
    if not parts:
        return
    match parts[0]:
        case "student" if len(parts) >= 2:
            print(students_try.get(parts[1], "не найден"))
        case "best" if len(parts) >= 3:
            print(labs_try.get((parts[1], parts[2]), "не найден"))
        case "attempts" if len(parts) >= 3:
            print(count_try.get((parts[1], parts[2]), 0))
        case "completed" if len(parts) >= 2:
            print([s for (s, l) in labs_try if l == parts[1]])
        case _:
            print("неизвестная команда или недостаточно параметров")

print("\nТекстовые запросы:")
for q in ["student anna", "best anna lab_01", "attempts boris lab_02", "completed lab_01"]:
    print(f"{q}:", end=" ")
    handle_query(q)
