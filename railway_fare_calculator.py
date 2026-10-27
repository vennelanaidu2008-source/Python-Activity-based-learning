#ALGORITHM
1. Start the program.
2. Define distance-based fare slabs, travel class rates, age-based concession rules, reservation fees, and cancellation penalties.
3. Input the number of passengers.
4. For each passenger, input their name, age, travel distance, and travel class.
5. Validate passenger details and ensure the distance and age are valid.
6. Calculate the basic fare using the distance slabs and selected travel class.
7. Apply the applicable age-based concession:
   - Children below 5 years: free fare.
   - Passengers aged 60 years or above: 20% concession.
   - Other passengers: no concession.
8. Add the reservation fee to the discounted fare.
9. Ask whether the ticket is cancelled.
10. If cancelled, calculate the cancellation penalty and refund amount.
11. Display the passenger-wise fare, concession, reservation fee, penalty, and final payable amount or refund.
12. Stop the program.

#FLOWCHART
                  START
                    |
                    v
          Define Fare and Policy Rules
                    |
                    v
           Input Number of Passengers
                    |
                    v
             Enter Passenger Details
          (Name, Age, Distance, Class)
                    |
                    v
             Validate Input Details
                    |
                    v
               Inputs Valid?
              /            \
            No              Yes
            |                |
            v                v
       Display Error    Calculate Basic Fare
            |           Using Distance Slabs
            |                |
            |                v
            |       Apply Class-Based Rate
            |                |
            |                v
            |       Apply Age Concession
            |                |
            |                v
            |       Add Reservation Fee
            |                |
            |                v
            |        Is Ticket Cancelled?
            |           /          \
            |         Yes           No
            |          |             |
            |          v             v
            |    Calculate Penalty  Calculate Final
            |    and Refund         Payable Fare
            |          |             |
            |          +------+------+
            |                 |
            |                 v
            |       Display Passenger Bill
            |                 |
            |                 v
            |       More Passengers Left?
            |          /            \
            |        Yes             No
            |         |               |
            |         v               v
            |    Enter Next      Display Final
            |     Passenger      Fare Summary
            |                         |
            +-------------------------+
                                      |
                                      v
                                     STOP

                                     #CODE
                                     
# File name: railway_fare_calculator.py

RESERVATION_FEE = 40
SENIOR_AGE = 60
SENIOR_CONCESSION = 0.20
CANCELLATION_RATE = 0.20

CLASS_MULTIPLIERS = {
    "sleeper": 1.0,
    "ac": 2.0,
    "first": 3.0
}


def calculate_basic_fare(distance, travel_class):
    if distance <= 100:
        slab_fare = 100
    elif distance <= 300:
        slab_fare = 250
    else:
        slab_fare = 400

    return slab_fare * CLASS_MULTIPLIERS[travel_class.lower()]


def calculate_ticket(age, distance, travel_class, cancelled):
    if age < 5:
        basic_fare = 0
    else:
        basic_fare = calculate_basic_fare(distance, travel_class)

    if age >= SENIOR_AGE:
        concession = basic_fare * SENIOR_CONCESSION
    else:
        concession = 0

    discounted_fare = basic_fare - concession
    total_fare = discounted_fare + RESERVATION_FEE

    if cancelled:
        penalty = total_fare * CANCELLATION_RATE
        refund = total_fare - penalty
        payable = 0
    else:
        penalty = 0
        refund = 0
        payable = total_fare

    return {
        "basic": basic_fare,
        "concession": concession,
        "reservation": RESERVATION_FEE,
        "total": total_fare,
        "penalty": penalty,
        "refund": refund,
        "payable": payable
    }


def main():
    print("=== RAILWAY FARE AND RESERVATION CALCULATOR ===")

    try:
        count = int(input("Enter number of passengers: "))

        if count <= 0:
            print("Error: Number of passengers must be positive.")
            return

        for i in range(count):
            print(f"\nPassenger {i + 1}")

            name = input("Enter passenger name: ")
            age = int(input("Enter age: "))
            distance = float(input("Enter distance in km: "))
            travel_class = input(
                "Enter class (Sleeper/AC/First): "
            ).strip().lower()

            if age < 0 or distance <= 0:
                print("Error: Age must be non-negative and distance positive.")
                return

            if travel_class not in CLASS_MULTIPLIERS:
                print("Error: Invalid travel class.")
                return

            choice = input(
                "Cancel ticket? (yes/no): "
            ).strip().lower()

            if choice not in ("yes", "no"):
                print("Error: Enter yes or no for cancellation.")
                return

            bill = calculate_ticket(
                age, distance, travel_class, choice == "yes"
            )

            print("\n--- PASSENGER FARE STATEMENT ---")
            print("Passenger Name :", name)
            print("Travel Class   :", travel_class.title())
            print("Distance       :", distance, "km")
            print(f"Basic Fare     : Rs. {bill['basic']:.2f}")
            print(f"Concession     : Rs. {bill['concession']:.2f}")
            print(f"Reservation Fee: Rs. {bill['reservation']:.2f}")
            print(f"Ticket Total   : Rs. {bill['total']:.2f}")

            if choice == "yes":
                print(f"Cancellation Penalty: Rs. {bill['penalty']:.2f}")
                print(f"Refund Amount       : Rs. {bill['refund']:.2f}")
            else:
                print(f"Final Payable  : Rs. {bill['payable']:.2f}")

        print("\nAll passenger fares processed successfully.")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()

#OUTPUT
--- PASSENGER FARE STATEMENT ---
Passenger Name : Ravi
Travel Class   : Sleeper
Distance       : 80.0 km
Basic Fare     : Rs. 100.00
Concession     : Rs. 0.00
Reservation Fee: Rs. 40.00
Ticket Total   : Rs. 140.00
Final Payable  : Rs. 140.00

--- PASSENGER FARE STATEMENT ---
Passenger Name : Lakshmi
Travel Class   : AC
Distance       : 250.0 km
Basic Fare     : Rs. 500.00
Concession     : Rs. 100.00
Reservation Fee: Rs. 40.00
Ticket Total   : Rs. 440.00
Cancellation Penalty: Rs. 88.00
Refund Amount       : Rs. 352.00

--- PASSENGER FARE STATEMENT ---
Passenger Name : Aman
Travel Class   : First
Distance       : 450.0 km
Basic Fare     : Rs. 0.00
Concession     : Rs. 0.00
Reservation Fee: Rs. 40.00
Ticket Total   : Rs. 40.00
Final Payable  : Rs. 40.00

All passenger fares processed successfully.