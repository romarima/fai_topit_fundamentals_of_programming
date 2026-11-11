students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

def mean(values: list[int]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def minimum(values: list[int]) -> int:
    if not values:
        return None
    minimum = float("inf")
    for i in values:
        if i < minimum:
            minimum = i
    return minimum

def maximum(values: list[int]) -> int:
    if not values:
        return None
    maximum = float("-inf")
    for i in values:
        if i > maximum:
            maximum = i
    return maximum

def classify(score: float | None) -> str:
    if score is None:
        return "Нет данных"
    if score >= 90:
        return "Отличный"
    elif score >= 75:
        return "Хороший"
    elif score >= 60:
        return "Удовлетворительный"
    else:
        return "Недостаточный"

def student_summary(name: str, results: list[int]) -> dict:
    if not results:
        return {"name": name, "results": [], "mean": None, "min": None, "max": None, "category": "Нет данных"}
    avg = mean(results)
    return {"name": name, "results": results, "mean": avg, "min": minimum(results), "max": maximum(results), "category": classify(avg)}

def find_top_students(students: dict[str, list[int]]) -> list[str]:
    best = -1.0
    top = []
    for name, res in students.items():
        if not res:
            continue
        avg = mean(res)
        if avg > best:
            best = avg
            top = [name]
        elif avg == best:
            top.append(name)
    return top

def group_summary(students: dict[str, list[int]]) -> dict:
    summaries = [student_summary(name, res) for name, res in students.items()]
    all_scores = [s for res in students.values() for s in res]
    categories = {"Отличный": 0, "Хороший": 0, "Удовлетворительный": 0, "Недостаточный": 0, "Нет данных": 0}
    for s in summaries:
        categories[s["category"]] = categories.get(s["category"], 0) + 1
    ranking = sorted(summaries, key=lambda s: s["mean"] if s["mean"] is not None else -1, reverse=True)
    return {
        "count": len(students),
        "mean": mean(all_scores),
        "categories": categories,
        "top": find_top_students(students),
        "ranking": ranking,
        "students": summaries,
    }

def format_report(students_data: list, group_data: dict) -> str:
    lines = ["=== СВОДКА ГРУППЫ ==="]
    for s in students_data:
        m = f"{s['mean']:.2f}" if s["mean"] is not None else "-"
        lines.append(f"{s['name']}: {s['results']} | ср: {m} | {s['category']}")
    lines.append(f"\nВсего студентов: {group_data['count']}, Общий средний балл: {group_data['mean']:.2f}")
    lines.append(f"Лидер(ы): {', '.join(group_data['top']) or 'нет'}")
    lines.append(f"Категории: {group_data['categories']}")
    lines.append("Рейтинг: " + ", ".join(f"{s['name']} ({s['mean']:.2f})" for s in group_data['ranking'] if s['mean']))
    return "\n".join(lines)

# Запуск на основных данных
res = group_summary(students)
print(format_report(res["students"], res))

# 6 тестовых сценариев
print("\n--- 6 Сценариев ---")
scenarios = [
    ("1. Обычный", students),
    ("2. Один студент", {"Ольга": [85, 90]}),
    ("3. Несколько лидеров", {"Алексей": [90], "Мария": [90], "Иван": [70]}),
    ("4. Пустая группа", {}),
    ("5. Без результатов", {"Анна": [80], "Олег": []}),
    ("6. Границы", {"59": [59], "60": [60], "75": [75], "90": [90]}),
]
for title, data in scenarios:
    r = group_summary(data)
    print(f"{title:<20} -> Студентов: {r['count']}, Лидер: {r['top']}, Ср. балл: {r['mean']:.2f}")
