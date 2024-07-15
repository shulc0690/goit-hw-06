def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return [el.strip() for el in file.readlines()]
    
def load_salary(lines: list[str]) -> list[int]:
    all_salary = []
    for line in lines:
        all_salary.append(int(line.split(',')[1]))
    return all_salary