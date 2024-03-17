import re
from pathlib import Path

def total_salary(path):
    with open(path) as reader:
        employees_list = [el.strip() for el in reader.readlines()]
        total = 0
        for employee in employees_list:
            employee = employee.split(",")
            emp_sal = int(employee[1])
            total += emp_sal
        average = int(total / len(employees_list))
    return total, average

total, average = total_salary("mod_4_1\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")