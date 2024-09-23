# Author = Gerard Keohane
# Purpose = Modular Programming Project

import datetime

today = datetime.date.today()
current_date = today.strftime("%Y_%m_%d")


def login_data():
    # Create an instance of the login_screen class
    list_username = []
    list_pass = []
    with open("Login_data.txt") as logon:
        for line in logon:
            line = line.rstrip()
            login_database = line.split(":")
            list_username.append(login_database[0])
            list_pass.append(login_database[1])
    return list_username, list_pass


list_user, list_password = login_data()


def login(user, password):
    print("Module Record System - Login")
    print("-" * 31)
    username = input("Please enter your username: ")
    while username not in list_user:
        print("Login Failed.\n"
              "Exiting Module Record System.")
        exit()
    password = input("Please enter your password: ")
    if password not in list_password:
        print("Login failed.\n"
              "Exiting Module Record System.")
        exit()
    print(f"Welcome {username}")


def attendance_data():
    list_presents = []
    list_absents = []
    with open("SOFT_6017.txt") as attendance:
        for line in attendance:
            line = line.rstrip()
            attendance_database = line.split(",")
            list_presents.append(int(attendance_database[1]))
            list_absents.append(int(attendance_database[2]))
    return list_presents, list_absents


def attendance_tracker(list_present, list_absent):
    module_options = ("1", "2")
    print("\nModule Record System - Attendance - Choose a Module")
    print("-" * 51)
    print("SOFT_6017\n"
          "SOFT_6018")
    module_choice = input("> ")
    while module_choice not in module_options:
        print("That is not an option, your two options are 1 and 2.")
        module_choice = input("> ")
    if module_choice == "1":
        print()
        print("Module Record System - Attendance - SOFT_6017")
        print("-" * 51)
        with open('SOFT_6017.txt') as f:
            lines = f.readlines()

        num_students = len(lines)
        print(f"There are {num_students} students enrolled.")
        print()

        for i in range(num_students):
            student_data = lines[i].split(',')
            student_name = student_data[0]
            print(f"Student #{i + 1}: {student_name}")
            print("1. Present\n2. Absent")
            attendance_options = ("1", "2")
            attendance_choice = input("> ")
            while attendance_choice not in attendance_options:
                print("That is not an option, your two options are 1 and 2.")
                attendance_choice = input("> ")
            if attendance_choice == "1":
                list_present[i] += 1
                print()
            elif attendance_choice == "2":
                list_absent[i] += 1

            with open("SOFT_6017.txt", "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for j, line in enumerate(lines):
                    attendance_data = line.rstrip().split(",")
                    if attendance_data[0] == student_name:
                        f.write(f"{student_name},{list_present[i]},{list_absent[i]}\n")
                    else:
                        f.write(line)
                f.truncate()

            i += 1

        print("SOFT_6017.txt was updated with the latest attendance records.")

        if module_choice == "2":
            print()
            print("Module Record System - Attendance - SOFT_6018")
            print("-" * 51)
            with open('SOFT_6018.txt') as f:
                lines = f.readlines()

            num_students = len(lines)
            print(f"There are {num_students} students enrolled.")
            print()

            for i in range(num_students):
                student_data = lines[i].split(',')
                student_name = student_data[0]
                print(f"Student #{i + 1}: {student_name}")
                print("1. Present\n2. Absent")
                attendance_options = ("1", "2")
                attendance_choice = input("> ")
                while attendance_choice not in attendance_options:
                    print("That is not an option, your two options are 1 and 2.")
                    attendance_choice = input("> ")
                if attendance_choice == "1":
                    list_present[i] += 1
                    print()
                elif attendance_choice == "2":
                    list_absent[i] += 1

                with open("SOFT_6018.txt", "r+") as f:
                    lines = f.readlines()
                    f.seek(0)
                    for j, line in enumerate(lines):
                        attendance_datas = line.rstrip().split(",")
                        if attendance_datas[0] == student_name:
                            f.write(f"{student_name},{list_present[i]},{list_absent[i]}\n")
                        else:
                            f.write(line)
                    f.truncate()

                i += 1

            print("SOFT_6018.txt was updated with the latest attendance records.")
        input("\nPress Enter to continue...")


def statistics1_data():
    list_avg1 = []
    list_absents1 = []
    with open("SOFT_6017.txt") as statistics1:
        for line in statistics1:
            line = line.rstrip()
            attendance_database = line.split(",")
            list_avg1.append(int(attendance_database[1]))
            list_absents1.append(int(attendance_database[2]))
    return list_avg1, list_absents1


def statistics2_data():
    list_avg2 = []
    list_absents2 = []
    with open("SOFT_6018.txt") as statistics2:
        for line in statistics2:
            line = line.rstrip()
            attendance_database = line.split(",")
            list_avg2.append(int(attendance_database[1]))
            list_absents2.append(int(attendance_database[2]))
    return list_avg2, list_absents2


def generate_stat():
    print("\nModule Record System - Average Attendance Data")
    print("-" * 46)

    list_average1, list_absent1 = statistics1_data()
    list_average2, list_absent2 = statistics2_data()

    average_attendance1 = sum(list_average1) / (sum(list_absent1) + sum(list_average1)) * 100
    average_attendance2 = sum(list_average2) / (sum(list_absent2) + sum(list_average2)) * 100

    print(f"Modular Programming       SOFT_6017   {average_attendance1:.1f}%  {'*' * int(average_attendance1 / 10)}")
    print(f"Programming Fundamentals  SOFT_6018   {average_attendance2:.1f}%  {'*' * int(average_attendance2 / 10)}")

    best_attended = max([(average_attendance1, 'Modular Programming'),
                         (average_attendance2, 'Programming Fundamentals')])

    print(f"\nThe best attended module is {best_attended[1]} with a {best_attended[0]:.1f}% attendance rate.")

    mod_under_40 = [module_name for avg, module_name in
                    [(average_attendance1, 'Modular Programming'),
                     (average_attendance2, 'Programming Fundamentals')]
                    if avg < 40]

    if mod_under_40:
        print(f"There is {len(mod_under_40)} module(s) with attendance under 40%:")
        for module in mod_under_40:
            print(f"   {module}")
    else:
        print("All modules have attendance above 40%.")

    with open(f"Attendance_Stats_{current_date}.txt", "w") as file:
        file.write("Module Record System - Average Attendance Data\n")
        file.write("-" * 46 + "\n")
        file.write(f"Modular Programming       SOFT_6017   {average_attendance1:.1f}%"
                   f"  {'*' * int(average_attendance1 / 10)}\n")
        file.write(f"Programming Fundamentals  SOFT_6018   {average_attendance2:.1f}%"
                   f"  {'*' * int(average_attendance2 / 10)}\n")
        file.write(f"The best attended module is {best_attended[1]} with a {best_attended[0]:.1f}"
                   f"% attendance rate.\n")
        if mod_under_40:
            file.write(f"There is {len(mod_under_40)} module(s) with attendance under 40%:\n")
            for module in mod_under_40:
                file.write(f"   {module}\n")
        else:
            file.write("All modules have attendance above 40%.\n")

    print(f"The above data is also stored at Attendance_Stats_{current_date}.txt.")
    input("\nPress Enter to continue...")


def main():
    login(list_user, list_password)
    list_present, list_absent = attendance_data()
    while True:
        print(f"Module Record System - Options")
        print("-" * 31)
        print("1. Record attendance\n"
              "2. Generate Statistics\n"
              "3. Exit")
        print()
        options_one = ("1", "2", "3")
        system_options = input(">  ")
        while system_options not in options_one:
            print("That is not an option, your three options are 1, 2 and 3.")
            system_options = input("> ")
        if system_options == "1":
            attendance_tracker(list_present, list_absent)
        if system_options == "2":
            generate_stat()
        if system_options == "3":
            print("\nExiting Module Record System.")
            input("\nPress Enter to continue...")
            exit()


if __name__ == '__main__':
    main()
