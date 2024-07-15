import sys
from pathlib import Path
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def display_directory_structure(directory_path, offset=""):
    try:
        path = Path(directory_path)
        if not path.exists() or not path.is_dir():
            print(f"{Fore.RED}Помилка: Переданий шлях не існує.")
            return

        print(f"{Fore.CYAN}{offset} {path.name}/")

        for item in path.iterdir():
            if item.is_dir():
                display_directory_structure(item, offset + "  ")  # Recursive call
            else:
                print(f"{Fore.GREEN}{offset}   {item.name}")

    except Exception as e:
        print(f"{Fore.RED}Помилка додатку: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python {sys.argv[0]} /шлях/до/вашої/директорії")
    else:
        directory_path = sys.argv[1]
        display_directory_structure(directory_path)
