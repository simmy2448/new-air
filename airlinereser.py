flights = [
    {'flight_no': '001', 'from': 'Delhi', 'to': 'Amritsar'},
    {'flight_no': '002', 'from': 'Delhi', 'to': 'Mumbai'},
    {'flight_no': '003', 'from': 'Amritsar', 'to': 'Canada'},
    {'flight_no': '004', 'from': 'Delhi', 'to': 'Goa'},
    {'flight_no': '005', 'from': 'Bangalore', 'to': 'Kolkata'}
]

bookings=[]

def user_input():
    print ("login first")
    password = input("Enter password: ")
    cpass = input("Confirm password: ")

    if password == cpass:
        print("password matched")
        book_flight()
    else:
        print("password do not match")
        return
    
def view_flight():
    print("available flights")
    for flight in flights:
        print(f"flight:{flight['flight_no']} {flight['from']} to {flight['to']}")

def book_flight():
    print("welcome to book flight page")
    view_flight()

    flight_no=input("enter the flight number you want to book: ")
    selected_flight=None
    for flight in flights:
        if flight['flight_no'] == flight_no:
            selected_flight = flight
       
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    passport = input("Enter your passport number: ")
    contact = input("Enter your contact number: ")
    
    booking = {
        'name': name,
        'age': age,
        'passport': passport,
        'contact': contact,
        'flight': selected_flight

    }
    bookings.append(booking)

    print("flight booked successfully!")
    print("booking confirmation:")
    print(f"passenger: {name}, age:{age},passport:{passport}")
    print(f"flight: {selected_flight['flight_no']} {selected_flight['from']} to {selected_flight['to']}")
    print(f"{contact}")

def cancel_flight():
    if not bookings:
        print("there is no booking to cancel.")
        return
    passport = input("enter your passport number to cancel booking: ")

    for booking in bookings:
        if booking['passport']== passport:
            bookings.remove(booking)
            print("booking cancelled successfully.")
            return
    print("booking is not found with your given passport number.")

def main_menu():    
    print("__________________  Welcome to #ABC Airline __________________")
    print("MENU >>>")
    print("1. Login and Book a Flight")
    print("2. Cancel a Flight")
    print("3. View Available Flights")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        user_input()
    elif choice == '2':
        cancel_flight()
    elif choice == '3':
        view_flight()
    elif choice == '4':
        print("Thank you for using ABC Airline. Goodbye!")
    else:
        print(" Invalid choice. Please try again.")
while True:
    main_menu()
    repeat= input("do you want to perform any other action?  (yes/no): ").lower()
    if repeat=='no':
        print("exiting.have a safe journey!")
        break

    
