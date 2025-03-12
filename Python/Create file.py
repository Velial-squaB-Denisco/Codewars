from datetime import date

def create_file(n, name, current_time):

    filename = f"{current_time} Kata {n}kyu {name.replace(' ', '_')}.py"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write() 

def main():
    current_time = date.today()
    create_file(6, "Count IP Addresses", current_time)

if __name__ == "__main__":
    main()