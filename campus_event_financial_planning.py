#ALGORITHM
1. Start.
2. Input the number of participants, registration fee per participant, sponsorship amount, and target budget details.
3. Input venue, equipment, catering, transport, and certificate costs.
4. Calculate total event cost by adding all five expenses.
5. Calculate total registration income by multiplying the expected number of participants by the registration fee.
6. Calculate total available funds by adding registration income and sponsorship.
7. Calculate the sponsorship shortfall, if any, after accounting for the registration income and sponsorship.
8. Calculate the minimum registration count needed to break even after sponsorship.
9. Display total expenses, registration income, sponsorship, funding shortfall or surplus, and minimum registrations required.
10. Stop.

#FLOWCHART

           +------------------+
           |      START       |
           +------------------+
                    |
                    v
           +------------------+
           | Input event costs|
           | and financial    |
           | details          |
           +------------------+
                    |
                    v
           +------------------+
           | Calculate total  |
           | event cost       |
           +------------------+
                    |
                    v
           +------------------+
           | Calculate total  |
           | registration     |
           | income           |
           +------------------+
                    |
                    v
           +------------------+
           | Add sponsorship  |
           | to registration  |
           | income           |
           +------------------+
                    |
                    v
           +------------------+
           | Compare available|
           | funds with total |
           | event cost       |
           +------------------+
                    |
                    v
           +------------------+
           | Calculate funding|
           | shortfall/surplus|
           +------------------+
                    |
                    v
           +------------------+
           | Calculate minimum|
           | registrations to |
           | break even       |
           +------------------+
                    |
                    v
           +------------------+
           | Display financial|
           | report           |
           +------------------+
                    |
                    v
           +------------------+
           |       STOP       |
           +------------------+

           #CODE
           
# Filename: campus_event_financial_planning.py

import math

print("CAMPUS EVENT FINANCIAL PLANNING")

# Input details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering_per_person = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate_per_person = float(input("Enter certificate cost per participant: "))

# Calculate costs
catering = catering_per_person * participants
certificates = certificate_per_person * participants

total_cost = venue + equipment + catering + transport + certificates

# Calculate income
registration_income = participants * registration_fee
total_funds = registration_income + sponsorship

# Funding shortfall or surplus
difference = total_funds - total_cost

if difference < 0:
    shortfall = abs(difference)
    surplus = 0
else:
    shortfall = 0
    surplus = difference

# Minimum registrations needed to break even
# Variable costs are catering and certificates.
variable_cost_per_person = catering_per_person + certificate_per_person
contribution_per_person = registration_fee - variable_cost_per_person

fixed_cost = venue + equipment + transport
amount_to_recover = fixed_cost - sponsorship

if amount_to_recover <= 0:
    minimum_registrations = 0
elif contribution_per_person > 0:
    minimum_registrations = math.ceil(
        amount_to_recover / contribution_per_person
    )
else:
    minimum_registrations = None

# Display report
print("\n----- EVENT FINANCIAL REPORT -----")
print(f"Venue cost:              Rs. {venue:.2f}")
print(f"Equipment cost:          Rs. {equipment:.2f}")
print(f"Catering cost:           Rs. {catering:.2f}")
print(f"Transport cost:          Rs. {transport:.2f}")
print(f"Certificate cost:        Rs. {certificates:.2f}")
print(f"Total event cost:        Rs. {total_cost:.2f}")

print(f"\nRegistration income:     Rs. {registration_income:.2f}")
print(f"Sponsorship:             Rs. {sponsorship:.2f}")
print(f"Total available funds:   Rs. {total_funds:.2f}")

if shortfall > 0:
    print(f"Funding shortfall:       Rs. {shortfall:.2f}")
else:
    print(f"Funding surplus:         Rs. {surplus:.2f}")

if minimum_registrations is None:
    print("Break-even: Not possible with the given registration fee.")
else:
    print("Minimum registrations needed to break even:",
          minimum_registrations)

if difference >= 0:
    print("Event Status: FINANCIALLY FEASIBLE")
else:
    print("Event Status: ADDITIONAL FUNDING REQUIRED")


#OUTPUT
CAMPUS EVENT FINANCIAL PLANNING

----- EVENT FINANCIAL REPORT -----
Venue cost:              Rs. 15000.00
Equipment cost:          Rs. 5000.00
Catering cost:           Rs. 15000.00
Transport cost:          Rs. 4000.00
Certificate cost:        Rs. 2000.00
Total event cost:        Rs. 41000.00

Registration income:     Rs. 50000.00
Sponsorship:             Rs. 10000.00
Total available funds:   Rs. 60000.00
Funding surplus:         Rs. 19000.00
Minimum registrations needed to break even: 35
Event Status: FINANCIALLY FEASIBLE