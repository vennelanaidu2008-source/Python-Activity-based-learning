#ALGORITHM
1. Start the program.
2. Define consultation charges, diagnostic charges, treatment charges, concession rules, and payment classification limits.
3. Input the patient's name, patient category, consultation fee, diagnostic charges, and treatment charges.
4. Validate the input values. Charges must not be negative.
5. Calculate the total bill by adding consultation, diagnostic, and treatment charges.
6. Apply a 10% concession if the total bill is ₹10,000 or more.
7. Calculate the final bill after deducting the concession.
8. Classify the patient's payment category:
   - Low: Final bill below ₹5,000.
   - Medium: Final bill from ₹5,000 to ₹19,999.99.
   - High: Final bill of ₹20,000 or more.
9. Display the patient's name, total charges, concession, final amount, and payment classification.
10. Stop the program.

#FLOWCHART
                 START
                   |
                   v
       Define Billing and Payment Rules
                   |
                   v
          Enter Patient Details
                   |
                   v
       Enter Consultation Charges,
        Diagnostic and Treatment Fees
                   |
                   v
          Validate Billing Inputs
                   |
                   v
          Are Charges Valid?
             /           \
           No             Yes
           |               |
           v               v
    Display Error     Calculate Total Bill
           |          (Consultation +
           |           Diagnostic +
           |           Treatment)
           |               |
           |               v
           |       Is Bill >= Rs. 10,000?
           |          /           \
           |        Yes            No
           |         |              |
           |         v              v
           |   Apply 10%        No Concession
           |    Concession
           |         |              |
           |         +------+-------+
           |                |
           |                v
           |       Calculate Final Bill
           |                |
           |                v
           |       Classify Payment Amount
           |       Low / Medium / High
           |                |
           |                v
           |       Display Billing Details
           |                |
           |                v
           |               STOP
           |
           +----> Re-enter Patient Details

           #CODE
           
# File name: hospital_billing.py

CONCESSION_LIMIT = 10000
CONCESSION_RATE = 0.10

LOW_LIMIT = 5000
HIGH_LIMIT = 20000


def calculate_bill(consultation, diagnostic, treatment):
    total = consultation + diagnostic + treatment

    if total >= CONCESSION_LIMIT:
        concession = total * CONCESSION_RATE
    else:
        concession = 0

    final_bill = total - concession

    return total, concession, final_bill


def classify_patient(final_bill):
    if final_bill < LOW_LIMIT:
        return "Low Payment Category"
    elif final_bill < HIGH_LIMIT:
        return "Medium Payment Category"
    else:
        return "High Payment Category"


def main():
    print("=== HOSPITAL BILLING SYSTEM ===")

    name = input("Enter patient name: ")

    try:
        consultation = float(
            input("Enter consultation charges (Rs.): ")
        )
        diagnostic = float(
            input("Enter diagnostic charges (Rs.): ")
        )
        treatment = float(
            input("Enter treatment charges (Rs.): ")
        )

        charges = [consultation, diagnostic, treatment]

        if any(charge < 0 for charge in charges):
            print("Error: Charges cannot be negative.")
            return

        total, concession, final_bill = calculate_bill(
            consultation, diagnostic, treatment
        )

        category = classify_patient(final_bill)

        print("\n--- PATIENT BILL DETAILS ---")
        print("Patient Name:", name)
        print(f"Consultation Charges: Rs. {consultation:.2f}")
        print(f"Diagnostic Charges: Rs. {diagnostic:.2f}")
        print(f"Treatment Charges: Rs. {treatment:.2f}")
        print(f"Total Bill: Rs. {total:.2f}")
        print(f"Concession: Rs. {concession:.2f}")
        print(f"Final Bill: Rs. {final_bill:.2f}")
        print("Patient Classification:", category)

    except ValueError:
        print("Error: Please enter valid numeric charges.")


if __name__ == "__main__":
    main()


#OUTPUT
--- PATIENT BILL DETAILS ---
Patient Name: Rahul
Consultation Charges: Rs. 1000.00
Diagnostic Charges: Rs. 4000.00
Treatment Charges: Rs. 8000.00
Total Bill: Rs. 13000.00
Concession: Rs. 1300.00
Final Bill: Rs. 11700.00
Patient Classification: Medium Payment Category