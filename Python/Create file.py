import datetime

def create_file(n, name, current_time):

    filename = f"{current_time} Kata {n}kyu {str(name)}.py"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write()

def main():
    current_time = datetime.datetime.today()
    current_time = current_time.strftime("%d-%m-%Y %H-%M-%S") #%Y-%m-%d
    create_file(4, "Matrix Determinant", current_time)

if __name__ == "__main__":
    main()