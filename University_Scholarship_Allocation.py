                
                
                
                #Algorithm

1. Start.
2. Input the number of student applicants.
3. For each applicant, input:
   - Student name and ID.
   - Marks obtained in each subject and maximum marks.
   - Attendance percentage.
   - Annual family income.
4. Calculate the aggregate percentage of each student.
5. Check the eligibility criteria:
   - Aggregate percentage must be at least 75%.
   - Minimum marks in every subject must be at least 40%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
6. If any criterion is not satisfied, mark the student as Not Eligible and record the reason.
7. If all criteria are satisfied, mark the student as Eligible.
8. Rank eligible students using the following rules:
   - Higher aggregate percentage ranks first.
   - If aggregate percentages are equal, higher attendance ranks first.
   - If attendance is also equal, lower annual family income ranks first.
   - If all three are equal, student ID in ascending order ranks first.
9. Allocate scholarships to eligible students according to the available scholarship quota.
10. Display student details, aggregate percentage, eligibility status, rank, and scholarship allocation.
11. Stop.

              #Flowchart

              START
                |
                v
      Set Eligibility Criteria
                |
                v
       Input Number of Students
                |
                v
        Enter Student Details
 (Name, Aggregate, Subject Marks,
   Attendance, Annual Income)
                |
                v
    Check Eligibility Criteria
                |
                v
       Are All Criteria Met?
          /           \
        Yes             No
         |               |
         v               v
 Add to Eligible     Mark as Not
      List             Eligible
         |               |
         +-------+-------+
                 |
                 v
       Are More Students Left?
          /           \
        Yes             No
         |               |
         v               v
  Enter Next Student   Rank Eligible
                       Students
                           |
                           v
                  Apply Tie-Breaking Rules
                           |
                           v
                  Display Rank List
                           |
                           v
                          STOP

             #Code


# File Name: University_Scholarship_Allocation.py

AGGREGATE_MIN = 75
SUBJECT_MIN = 40
ATTENDANCE_MIN = 75
INCOME_MAX = 250000

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nApplicant {i + 1}")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    subjects = int(input("Enter number of subjects: "))
    marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks for subject {j + 1} (out of 100): "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income (Rs.): "))

    percentage = sum(marks) / (subjects * 100) * 100
    reasons = []

    if percentage < AGGREGATE_MIN:
        reasons.append("Aggregate below 75%")

    if any(mark < SUBJECT_MIN for mark in marks):
        reasons.append("Subject marks below 40%")

    if attendance < ATTENDANCE_MIN:
        reasons.append("Attendance below 75%")

    if income > INCOME_MAX:
        reasons.append("Income exceeds Rs. 2,50,000")

    applicants.append({
        "id": student_id,
        "name": name,
        "percentage": percentage,
        "attendance": attendance,
        "income": income,
        "eligible": len(reasons) == 0,
        "reasons": reasons
    })

quota = int(input("\nEnter number of scholarships available: "))

# Rank eligible students using predefined tie-breaking rules.
eligible = [s for s in applicants if s["eligible"]]

eligible.sort(key=lambda s: (
    -s["percentage"],
    -s["attendance"],
    s["income"],
    s["id"]
))

print("\n========== SCHOLARSHIP RESULTS ==========")

for rank, student in enumerate(eligible, start=1):
    status = "Scholarship Awarded" if rank <= quota else "Eligible - Not Allocated"

    print(
        f"Rank: {rank} | ID: {student['id']} | "
        f"Name: {student['name']} | "
        f"Aggregate: {student['percentage']:.2f}% | "
        f"Attendance: {student['attendance']:.1f}% | "
        f"Income: Rs. {student['income']:.0f} | {status}"
    )

for student in applicants:
    if not student["eligible"]:
        print(
            f"ID: {student['id']} | Name: {student['name']} | "
            f"Aggregate: {student['percentage']:.2f}% | "
            f"Not Eligible: {', '.join(student['reasons'])}"
        )

print("\nTotal Applicants:", n)
print("Eligible Applicants:", len(eligible))
print("Scholarships Awarded:", min(quota, len(eligible)))


             #Output

Enter number of applicants: 5

Applicant 1
Enter student ID: S101
Enter student name: Asha
Enter number of subjects: 3
Enter marks for subject 1 (out of 100): 85
Enter marks for subject 2 (out of 100): 78
Enter marks for subject 3 (out of 100): 90
Enter attendance percentage: 92
Enter annual family income (Rs.): 180000

Applicant 2
Enter student ID: S102
Enter student name: Bala
Enter number of subjects: 3
Enter marks for subject 1 (out of 100): 80
Enter marks for subject 2 (out of 100): 75
Enter marks for subject 3 (out of 100): 82
Enter attendance percentage: 88
Enter annual family income (Rs.): 200000

Applicant 3
Enter student ID: S103
Enter student name: Charan
Enter number of subjects: 3
Enter marks for subject 1 (out of 100): 90
Enter marks for subject 2 (out of 100): 38
Enter marks for subject 3 (out of 100): 88
Enter attendance percentage: 90
Enter annual family income (Rs.): 150000

Applicant 4
Enter student ID: S104
Enter student name: Divya
Enter number of subjects: 3
Enter marks for subject 1 (out of 100): 80
Enter marks for subject 2 (out of 100): 80
Enter marks for subject 3 (out of 100): 77
Enter attendance percentage: 88
Enter annual family income (Rs.): 150000

Applicant 5
Enter student ID: S105
Enter student name: Esha
Enter number of subjects: 3
Enter marks for subject 1 (out of 100): 75
Enter marks for subject 2 (out of 100): 76
Enter marks for subject 3 (out of 100): 80
Enter attendance percentage: 70
Enter annual family income (Rs.): 100000

Enter number of scholarships available: 2

========== SCHOLARSHIP RESULTS ==========

Rank: 1 | ID: S101 | Name: Asha | Aggregate: 84.33% | Attendance: 92.0% | Income: Rs. 180000 | Scholarship Awarded
Rank: 2 | ID: S104 | Name: Divya | Aggregate: 79.00% | Attendance: 88.0% | Income: Rs. 150000 | Scholarship Awarded
Rank: 3 | ID: S102 | Name: Bala | Aggregate: 79.00% | Attendance: 88.0% | Income: Rs. 200000 | Eligible - Not Allocated
ID: S103 | Name: Charan | Aggregate: 72.00% | Not Eligible: Aggregate below 75%, Subject marks below 40%
ID: S105 | Name: Esha | Aggregate: 77.00% | Not Eligible: Attendance below 75%

Total Applicants: 5
Eligible Applicants: 3
Scholarships Awarded: 2
