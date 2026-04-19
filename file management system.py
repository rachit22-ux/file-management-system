print("=== File Manager ===")

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Add")
    print("4. Exit")

    ch = input("Choice: ")

    if ch == "1":
        name = input("File name: ")
        data = input("Data: ")

        with open(name + ".txt", "w") as f:
            f.write(data)

        print("File created!")

    elif ch == "2":
        name = input("File name: ")

        try:
            with open(name + ".txt", "r") as f:
                print(f.read())
        except:
            print("File not found!")

    elif ch == "3":
        name = input("File name: ")
        data = input("Add data: ")

        try:
            with open(name + ".txt", "a") as f:
                f.write("\n" + data)

            print("Data added!")
        except:
            print("Error!")

    elif ch == "4":
        break

    else:
        print("Wrong choice!")
