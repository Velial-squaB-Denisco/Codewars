def create_file(n, name):

    filename = f"Kata {n}kyu {name.replace(' ', '_')}.py"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write() 

def main():
    create_file(6, "Count IP Addresses")

if __name__ == "__main__":
    main()