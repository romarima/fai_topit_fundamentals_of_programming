def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name:
        return ""
    return " ".join(part.capitalize() for part in name.split())


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if not results:
        return f"{prefix}: {normalize_name(student)} — нет данных"
    avg = arithmetic_mean(results)
    return f"{prefix}: {normalize_name(student)}, средний: {avg:.{precision}f}, оценки: {results}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    seen = set()
    cleaned = []
    for tag in tags:
        t = tag.strip().lower() if lowercase else tag.strip()
        if t and t not in seen:
            seen.add(t)
            cleaned.append(t)
    return tuple(cleaned)


# 1. Проверки assert
assert arithmetic_mean([1, 2, 3]) == 2.0
assert arithmetic_mean([]) == 0.0
assert arithmetic_mean([5]) == 5.0

assert normalize_name("  вася   васянов  ") == "Вася Васянов"
assert normalize_name("ВАСЯ") == "Вася"
assert normalize_name("") == ""

assert "нет данных" in build_report("борис", [])
assert "5.0" in build_report("анна", [5, 5], precision=1)
assert "Результат" in build_report("иван", [4, 5])

assert collect_tags("Python", "  python  ", "Lab") == ("python", "lab")
assert collect_tags("AI", "ai", lowercase=False) == ("AI", "ai")
assert collect_tags() == ()

# 2. Вызовы и распаковка * и **
args_list = ["Python", "Git", "python"]
print("Распаковка *:", collect_tags(*args_list))

params = {"precision": 3, "prefix": "Отчет"}
print("Распаковка **:", build_report("сергей смирнов", [4, 5, 5], **params))

# 3. LEGB и nonlocal
course = "Основы (Global)"
def outer():
    course = "Python (Enclosing)"
    def inner():
        nonlocal course
        course = "Advanced (Enclosing изменен)"
        print("Внутри inner:", course)
    inner()
    print("Внутри outer:", course)
outer()
print("Глобальная:", course)

# 4. Ошибка изменяемого значения по умолчанию
def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

print("add_result(1):", add_result(1))
print("add_result(2):", add_result(2))

# 5. Практическое расширение
def apply_to_results(operation, values):
    return [operation(x) for x in values]

def make_threshold_checker(threshold):
    def check(score):
        return score >= threshold
    return check

print("apply_to_results:", apply_to_results(lambda x: x + 1, [3, 4, 5]))
check_pass = make_threshold_checker(60)
check_honors = make_threshold_checker(90)
print("75 сдал (>=60):", check_pass(75))
print("75 отлично (>=90):", check_honors(75))
