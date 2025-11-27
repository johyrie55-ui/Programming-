Employees = []

while True:
    print("\n================= PAYROLL SYSTEM =================")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Exit\n")
    
    choice = input("Enter a number (1-4): ")

    if choice == "1":
        print("\n=== Add Employee ===")

        # Keep asking for ID until a unique one is entered
        while True:
            try:
                ID = int(input("Enter ID: "))
            except ValueError:
                print("Error: ID must be a number.")
                continue

            duplicate = False
            for emp in Employees:
                if emp["ID"] == ID:
                    duplicate = True
                    break

            if duplicate:
                print(f"Error: Employee ID {ID} already exists. Please enter a new ID.")
            else:
                break  # Exit the loop once a unique ID is found

        name = input("Enter Name: ")
        position = input("Enter Position: ")

        # Validate Hourly Rate
        while True:
            try:
                Rate = float(input("Enter Hourly Rate: "))
                if Rate < 0:
                    print("Error: Hourly Rate cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number for Hourly Rate.")

        # Validate Hours Worked
        while True:
            try:
                Hours = float(input("Enter Hours Worked: "))
                if Hours < 0:
                    print("Error: Hours Worked cannot be negative. Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number for Hours Worked.")

        salary = Rate * Hours

        dictionary = {
            "ID": ID,
            "Name": name,
            "Position": position,
            "Rate": Rate,
            "Hours Worked": Hours,
            "Salary": salary,
        }

        Employees.append(dictionary)
        print(f"\nEmployee {name} added successfully!")

    elif choice == "2":
        print("\n=== Employee List ===")
        if len(Employees) == 0:
            print("No employees found.")
        else:
            for pos in Employees:
                print("\n-------------------------------------")
                print(f"Employee ID: {pos['ID']}")
                print(f"Name: {pos['Name']}")
                print(f"Position: {pos['Position']}")
                print(f"Hourly Rate: {pos['Rate']:.2f}")
                print(f"Hours Worked: {pos['Hours Worked']}")
                print(f"Total Salary: {pos['Salary']:.2f}")

    elif choice == "3":
        print("\n==== Search Employee ====")
        try:
            search = int(input("Enter Employee ID: "))
        except ValueError:
            print("Error: Please enter a valid numeric ID.")
            continue

        found = False

        for pos in Employees:
            if pos["ID"] == search:
                print("\nEmployee Found!\n")
                print(f"Employee ID: {pos['ID']}")
                print(f"Name: {pos['Name']}")
                print(f"Position: {pos['Position']}")
                print(f"Hourly Rate: {pos['Rate']:.2f}")
                print(f"Hours Worked: {pos['Hours Worked']}")
                print(f"Total Salary: {pos['Salary']:.2f}")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Choice.")