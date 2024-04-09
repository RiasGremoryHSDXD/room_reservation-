import datetime
import calendar

today_date = datetime.datetime.now()
current_year = today_date.strftime("%Y")
current_month = int(today_date.strftime("%m"))
current_day = int(today_date.strftime("%d"))

reserved_rooms_AVR1 = []
reserved_rooms_AVR2 = []
reserved_rooms_AVR3 = []


def display_option():
    print("------------------------------------------- ")
    print("[1] Reserve Room")
    print("[2] Check Available Room")
    print("[3] Check Reserved Room")
    print("[4] Exit")
    print("------------------------------------------- ")


def choose_room():
    print(" ")
    print("---Available Rooms---")
    print("[1] AVR 1")
    print("[2] AVR 2")
    print("[3] AVR 3")
    print("\n[0] BACK")
    print("----------------------- ")

    choose_room_loop = True
    while choose_room_loop:
        user_choose_room = input("Enter Room#: ")

        if user_choose_room.isalpha():
            print("INVALID INPUT\n")
            continue

        if user_choose_room == "1":
            room_reserved = reserved_room()
            date_sche = sche_room(room_reserved, "1")
            reserved_rooms_AVR1.append(date_sche)
            break
        elif user_choose_room == "2":
            room_reserved = reserved_room()
            date_sche = sche_room(room_reserved, "2")
            reserved_rooms_AVR2.append(date_sche)
            break
        elif user_choose_room == "3":
            room_reserved = reserved_room()
            date_sche = sche_room(room_reserved, "3")
            reserved_rooms_AVR3.append(date_sche)
            break
        elif user_choose_room == "0":
            break
        else:
            print("Room Does not Exist")


def reserved_room():
    reserved_room_loop = True
    while reserved_room_loop:
        print("\n[0] TO GO BACK")
        print("---------------------------")

        user_name = input("Enter last name: ")

        if user_name == "0":
            return choose_room()

        if user_name.isdigit():
            print("INVALID INPUT\n")
            continue

        room_choose_loop = True
        while room_choose_loop:
            print("\n------------------")
            print("[1] COT          |")
            print("[2] CEA          |")
            print("[B] GO BACK      |")
            print("------------------")

            program = input("Enter Program/Course: ").strip()

            if program == "B":
                break

            if program == "1":
                return [user_name, 'COT']
            elif program == "2":
                return [user_name, 'CEA']
            else:
                print("INVALID INPUT ( Please enter 1 or 2 ) or ( B to go back )")


def sche_room(room_reserved, room_choose):
    while True:
        print("- - - - - - - - - - - - - - - - - - -")
        print("Sample Format ||  [2] for Feb")
        print("Enter [B] to go back")
        print("- - - - - - - - - - - - - - - - - - -")

        month = input("Enter a Month: ")

        if month == "B":
            room_reserved = reserved_room()

        if not month.isdigit():
            print("Invalid Input!")
            continue

        month = int(month)
        if month < current_month:
            print("Invalid Input! You can't reserve a past Month")
            continue
        else:
            get_max_day = calendar.monthrange(2024, month)
            get_max_day = get_max_day[1]
            get_month = calendar.month_name[month]
            if month == current_month:
                day_show = current_day
            else:
                day_show = 1
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"All days in {get_month} is {day_show} - {get_max_day}    |")
            print("[B] TO GO BACK                                  |")
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")

            while True:
                day = input("Enter a Day: ")

                if day == "B":
                    break

                if not day.isdigit():
                    print("Invalid Input!")
                    continue

                day = int(day)
                if day > int(get_max_day):
                    print("Invalid Input! Please refer to Sample Format")
                    continue

                if month == current_month:
                    if day < current_day:
                        print("Invalid Input! You can't reserve a past date")
                        continue
                    else:
                        while True:
                            print("\n[B] TO GO BACK")
                            schedule_time = input("Enter (AM / PM): ")
                            print("- - - - - - - - - - - - - - - - - - -\n")

                            if schedule_time == "B":
                                break

                            if schedule_time == "AM" or schedule_time == "PM":
                                date_sche = f"{get_month}, {day} 2024"
                                date_schedule_com = f"{get_month}, {day} 2024 {schedule_time}"
                                return add_room_sche(room_reserved, date_sche, schedule_time, date_schedule_com,
                                                     room_choose, day)
                            else:
                                print("INVALID TIME")
                else:
                    while True:
                        print("\n[B] TO GO BACK")
                        schedule_time = input("Enter (AM / PM): ")
                        print("- - - - - - - - - - - - - - - - - - -\n")

                        if schedule_time == "B":
                            break

                        if schedule_time == "AM" or schedule_time == "PM":
                            date_sche = f"{get_month}, {day} 2024"
                            date_schedule_com = f"{get_month}, {day} 2024 {schedule_time}"
                            return add_room_sche(room_reserved, date_sche, schedule_time, date_schedule_com,
                                                 room_choose, day)
                        else:
                            print("INVALID TIME")


def add_room_sche(room_reserved, date_sche, schedule_time, date_schedule_com, room_choose, day):
    if room_choose == "1":
        check_list_room = reserved_rooms_AVR1
        room_name_reserve = 'AVR 1'
    elif room_choose == "2":
        check_list_room = reserved_rooms_AVR2
        room_name_reserve = 'AVR 2'
    else:
        check_list_room = reserved_rooms_AVR3
        room_name_reserve = 'AVR 3'

    am_booking = any(f"{date_sche} AM" == reservation[5] for reservation in check_list_room)
    pm_booking = any(f"{date_sche} PM" == reservation[5] for reservation in check_list_room)

    if am_booking and pm_booking:
        print(f"Sorry, {date_sche} AM and PM is fully booked. Please choose another day")
        return sche_room(room_reserved, room_choose)

    if date_schedule_com in (reservation[5] for reservation in check_list_room):
        print(f"Sorry, {day} is fully booked at {date_sche} {schedule_time}. Please choose another time")
        return sche_room(room_reserved, room_choose)

    print("Reservation Confirmed!")
    print(f"Last_Name: {room_reserved[0]} | Program/Course: {room_reserved[1]} | "
          f"Schedule: {date_sche} "
          f"| Time: {schedule_time}")

    list_info = (room_name_reserve, room_reserved[0], room_reserved[1], date_sche, schedule_time, date_schedule_com)
    return list_info


current_date = f"{current_day}/{current_month}/{current_year}"
print(current_date)
option_loop = True
while option_loop:
    display_option()
    user_input = input("Enter choice: ").strip()

    if user_input == "1":
        choose_room()
    elif user_input == "2":
        print("Available Rooms")
        print("['AVR1', 'AVR2', 'AVR3']")
    elif user_input == "3":
        print("\n---Available Rooms---")
        print("AVR 1")
        print("AVR 2")
        print("AVR 3")

        while True:
            check_room = input("Enter Room #: ")

            if check_room in ["1", "2", "3"]:
                if check_room == "1":
                    view_list = reserved_rooms_AVR1
                elif check_room == "2":
                    view_list = reserved_rooms_AVR2
                else:
                    view_list = reserved_rooms_AVR3

                if len(view_list) == 0:
                    print("No Reserved Schedules yet\n")
                    break
                else:
                    print("----------------------------")
                    print(f"| RESERVED SCHEDULES FOR AVR {check_room}|")
                    print("----------------------------")
                    for i in range(len(view_list)):
                        print(f"[{view_list[i][0]}| Name: {view_list[i][1]}| Program/Course: {view_list[i][2]}| Schedule: {view_list[i][3]}| Time:{view_list[i][4]}]")
                    print(" ")
                    break
            else:
                print("INVALID INPUT")

    elif user_input == "4":
        exit(0)
    else:
        print("INVALID CHOICE")
