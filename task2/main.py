from pathlib import Path

def get_cats_info(path):
    cat_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": int(cat_age)  # Convert age to an integer
                }
                cat_list.append(cat_info)

    except FileNotFoundError:
        print(f'Файл {path} не існує')
    except Exception as e:
        print(f"Виникла помилка при читанні файла: {e}")

    return cat_list

FILENAME = Path(__file__).parent / "cats_files.txt"
cats_info = get_cats_info(FILENAME)
print(cats_info)
