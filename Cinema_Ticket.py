class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, name):
        self.name = name
        self.entry_hall(self)


class Cinema:
    def __init__(self):
        self.__show_list = []
        self.seats = {}

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.seats[id] = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

    def book_seats(self, id, seats_to_book):
        if id in self.seats:
            seat_map = self.seats[id]
            for seat in seats_to_book:
                row, col = seat
                if seat_map[row][col] == 0:
                    seat_map[row][col] = 1

    def view_show_list(self):
        print("List of Shows Today:")
        for show in self.__show_list:
            id, movie_name, time = show
            print(f"Movie Name: {movie_name}({id}), Show ID: {id}, Time: {time}")

    def view_available_seats(self, id):
        if id in self.seats:
            seat_map = self.seats[id]
            print(f"Available seats for show {id}:")
            for row in seat_map:
                print(row)
        else:
            print(f"Show ID: {id} Invalid!")

    def book_ticket(self, id, seats_to_book):
        if id in self.seats:
            seat_map = self.seats[id]
            for row, col in seats_to_book:
                if 0 <= row < len(seat_map) and 0 <= col < len(seat_map[0]):
                    if seat_map[row][col] == 0:
                        self.book_seats(id, [(row, col)])
                        print(f"Seat ({row},{col}) booked for show {id}")
                    else:
                        print(f"Seat ({row},{col}) is already booked.")
                else:
                    print(f"Invalid seat selection for show {id}.")
        else:
            print(f"Show with ID {id} not found.")


restart_program = True
while restart_program:
    cinema = Cinema()
    cinema.entry_show(111, "Jawan", "17/10/2020 11:00 AM")
    cinema.entry_show(333, "Sujon Maji", "17/10/2023 2:00 PM")

    while True:
        print("\nOptions:")
        print("1: View all shows today")
        print("2: View available seats")
        print("3: Book a ticket")
        print("4: Exit")
        choice = input("Enter Option: ")

        if choice == "1":
            cinema.view_show_list()
        elif choice == "2":
            show_id = int(input("Enter show ID to view available seats: "))
            cinema.view_available_seats(show_id)

        elif choice == "3":
            show_id = int(input("Enter show ID to book a seat: "))
            num_seats = int(input("Enter the number of seats to book: "))
            seats_to_book = []
            for _ in range(num_seats):
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
                seats_to_book.append((row, col))
            cinema.book_ticket(show_id, seats_to_book)
        elif choice == "4":
            print("Exiting the current session.")
            break
        else:
            print("Invalid choice! Select a valid option.")

    restart = input("restart the program? (y/n): ")
    if restart.lower() != "y":
        restart_program = False
        print("Program Terminate!")
