import datetime

def create_file(n, name, current_date):
    filename = f"{current_date} Kata {n}kyu {str(name)}.py"
    print(filename)
    path = f"{n}kyu"

    with open(f"C:\\Users\\user\\Documents\\GitHub\\Codewars\\Python\\{path}\\{filename}", 'w', encoding='utf-8') as file:
        file.write('""""""')

def main():
    current_date = datetime.datetime.today().strftime("%d-%m-%Y")
    create_file(3, "Alphabetic Anagrams", current_date)

if __name__ == "__main__":
    main()