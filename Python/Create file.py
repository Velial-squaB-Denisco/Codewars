import datetime

def create_file(n, name, current_time):

    filename = f"{current_time} Kata {n}kyu {str(name).replace(' ', '_')}.py"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write()

def main():
    current_time = datetime.datetime.today()
    current_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
    create_file(5, "Can you get the loop", current_time)

if __name__ == "__main__":
    main()