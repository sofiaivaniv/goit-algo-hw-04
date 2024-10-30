def total_salary(path: str) -> tuple[float, float]:
    '''Calculates the total and average salary of all developers'''
    try:
        total = 0
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            for el in lines:
                _, salary = el.split(',')
                total += float(salary)
            average= total/len(lines)
        return total, average
    except FileNotFoundError:
        return f"Файл не знайдено"
    except UnicodeDecodeError:
        return "Неможливо прочитати файл через проблеми з кодуванням"
    except Exception as e:
        return f"Виникла помилка: {e}"
        
result = total_salary("D:/my_repor/goit-algo-hw-04/salary_file.txt")
if isinstance(result, tuple):
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
    print(result)