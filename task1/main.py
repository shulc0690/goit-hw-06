import os.path
from pathlib import Path
from data import load_data, load_salary


def total_salary(path: str):
    sum_salary = 0
    avg_salary = 0

    if not os.path.exists(path):
        print(f'Файл {path} не існує')
        return sum_salary,avg_salary
    try:
        lines = load_data(path)
        all_salary = load_salary(lines)
        sum_salary = sum(all_salary)
        avg_salary = sum(all_salary)//len(all_salary)
    except Exception as e:
        print(f"Помилка в данних: {e}")
    
    return sum_salary, avg_salary


FILENAME = Path(__file__).parent / "salary.txt"
total, average = total_salary(FILENAME)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")