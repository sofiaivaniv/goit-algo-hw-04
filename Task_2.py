def get_cats_info(path: str) -> list[dict]:
    '''Returns a list of dictionaries with information about each cat'''
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            for el in lines:
                info = el.split(',')
                cat_info = {'id': info[0], 'name': info[1], 'age': info[2]}
                cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        return f"Файл не знайдено"
    except UnicodeDecodeError:
        return "Неможливо прочитати файл через проблеми з кодуванням"
    except Exception as e:
        return f"Виникла помилка: {e}"
    
print(get_cats_info('D:\my_repor\goit-algo-hw-04\cats_file.txt'))