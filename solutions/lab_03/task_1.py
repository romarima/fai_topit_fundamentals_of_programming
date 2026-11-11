import sys

result = int(input("Введите результат студента: "))
if not(0 <= result <= 100):
    print("Недопустимый диапазон результатов")
    sys.exit(0)

work_type = input("Введите тип работы студента: ").strip().lower()

absences = int(input("Введите количество пропусков студента: "))
if not(0 <= absences <= 5):
    print("Недопустимый диапазон пропусков")
    sys.exit(0)

level_table = ["Недостаточный", "Удовлетворительный", "Хороший", "Отличный"]
level_num = 0
type_translate = ""

def get_student_level(score: int, absences: int) -> str:
    if 90 <= score <= 100:
        lvl = 3
    elif 75 <= score <= 89:
        lvl = 2
    elif 60 <= score <= 74:
        lvl = 1
    else:
        lvl = 0

    if absences > 3:
        lvl = max(0, lvl - 1)

    return level_table[lvl]

match work_type:
    case "exam":
        type_translate = "Экзаменационная работа"
    case "project":
        type_translate = "Проектная работа"
    case "practice":
        type_translate = "Практическая работа"
    case _:
        type_translate = "Неизвестный тип работы"

level_name = get_student_level(result, absences)

print("====================")
print("Статистика студента")
print("====================")
print(f"Результат: {result}")
print(f"Тип работы: {type_translate}")
print(f"Пропуски: {absences}")
print(f"Оценка уровня: {level_name}")

# Практическое расширение
students_batch = [
    (100, "exam", 0),
    (90, "project", 1),
    (89, "practice", 2),
    (75, "exam", 4),
    (74, "project", 1),
    (60, "practice", 5),
    (59, "exam", 0),
    (0, "project", 2),
    (95, "practice", 4),
    (68, "exam", 1),
]

level_counts = {lvl: 0 for lvl in level_table}

print("====================")
print("Список студентов")
print("====================")
for s_score, s_type, s_abs in students_batch:
    lvl = get_student_level(s_score, s_abs)
    level_counts[lvl] += 1
    print(
        f"Результат: {s_score}, Тип: {s_type}, Пропуски: {s_abs} -> Уровень: {lvl}"
    )
print("\nИтоговая сводка:", level_counts)
