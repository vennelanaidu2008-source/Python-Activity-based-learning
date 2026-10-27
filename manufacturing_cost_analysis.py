#ALGORITHM 
1. Start the program.
2. Input the product name, number of units produced, material cost per unit, labour cost per unit, wastage percentage, total machine cost, selling price per unit, and target profit percentage.
3. Validate all inputs to ensure costs and quantities are valid.
4. Calculate the total material cost.
5. Calculate the wastage cost based on the material cost and wastage percentage.
6. Calculate the total labour cost.
7. Add machine operating costs.
8. Calculate total manufacturing cost:
   
   Total Cost = Material Cost + Wastage Cost + Labour Cost + Machine Cost
9. Calculate the total selling revenue:
   
   Revenue = Selling Price per Unit × Number of Units Sold
10. Calculate profit or loss:
    
    Profit = Revenue − Total Manufacturing Cost
11. Calculate the profit percentage relative to total manufacturing cost.
12. Compare the profit percentage with the specified target.
13. Display the complete cost statement and indicate whether the target is achieved.
14. Stop the program.

#FLOWCHART

                    START
                      |
                      v
              Enter Product Details
                      |
                      v
           Input Material, Labour, Wastage,
           Machine Cost and Selling Price
                      |
                      v
                Validate Inputs
                      |
                      v
                Inputs Valid?
                /           \
              No             Yes
              |               |
              v               v
        Display Error    Calculate Material Cost
                              |
                              v
                       Calculate Wastage Cost
                              |
                              v
                        Calculate Labour Cost
                              |
                              v
                        Add Machine Cost
                              |
                              v
                     Calculate Total Cost
                              |
                              v
                    Calculate Sales Revenue
                              |
                              v
                      Calculate Profit
                              |
                              v
                  Calculate Profit Percentage
                              |
                              v
                    Profit Target Achieved?
                       /            \
                     Yes             No
                      |               |
                      v               v
                Target Met       Target Not Met
                      |               |
                      +-------+-------+
                              |
                              v
                    Display Cost Analysis
                              |
                              v
                             STOP

                             #CODE

                             
# File name: manufacturing_cost_analysis.py

def main():
    print("=== MANUFACTURING COST AND PROFITABILITY ANALYSIS ===")

    try:
        product = input("Enter product name: ")
        quantity = int(input("Enter number of units produced: "))

        material_per_unit = float(
            input("Enter material cost per unit (Rs.): ")
        )
        labour_per_unit = float(
            input("Enter labour cost per unit (Rs.): ")
        )
        wastage_percent = float(
            input("Enter wastage percentage: ")
        )
        machine_cost = float(
            input("Enter total machine cost (Rs.): ")
        )
        selling_price = float(
            input("Enter selling price per unit (Rs.): ")
        )
        target_profit = float(
            input("Enter target profit percentage: ")
        )

        if (quantity <= 0 or material_per_unit < 0
                or labour_per_unit < 0 or machine_cost < 0
                or selling_price < 0 or not 0 <= wastage_percent <= 100
                or target_profit < 0):
            print("Error: Invalid input values.")
            return

        # Calculate production costs
        material_cost = material_per_unit * quantity
        wastage_cost = material_cost * wastage_percent / 100
        labour_cost = labour_per_unit * quantity

        total_cost = (
            material_cost + wastage_cost
            + labour_cost + machine_cost
        )

        # Assume all produced units are sold
        revenue = selling_price * quantity
        profit = revenue - total_cost

        if total_cost > 0:
            profit_percent = (profit / total_cost) * 100
        else:
            profit_percent = 0 if revenue == 0 else float("inf")

        target_met = profit_percent >= target_profit

        print("\n========== COST AND PROFIT STATEMENT ==========")
        print("Product Name          :", product)
        print("Units Produced        :", quantity)
        print(f"Material Cost         : Rs. {material_cost:.2f}")
        print(f"Wastage Cost          : Rs. {wastage_cost:.2f}")
        print(f"Labour Cost           : Rs. {labour_cost:.2f}")
        print(f"Machine Cost          : Rs. {machine_cost:.2f}")
        print("-----------------------------------------------")
        print(f"Total Production Cost : Rs. {total_cost:.2f}")
        print(f"Total Sales Revenue   : Rs. {revenue:.2f}")

        if profit >= 0:
            print(f"Profit                : Rs. {profit:.2f}")
        else:
            print(f"Loss                  : Rs. {-profit:.2f}")

        if profit_percent == float("inf"):
            print("Profit Percentage     : Not defined (zero cost)")
        else:
            print(f"Profit Percentage     : {profit_percent:.2f}%")

        print(f"Target Profit         : {target_profit:.2f}%")
        print("Target Status         :",
              "TARGET ACHIEVED" if target_met else "TARGET NOT ACHIEVED")
        print("================================================")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()

#OUTPUT
========== COST AND PROFIT STATEMENT ==========
Product Name          : Chair
Units Produced        : 100
Material Cost         : Rs. 30000.00
Wastage Cost          : Rs. 1500.00
Labour Cost           : Rs. 10000.00
Machine Cost          : Rs. 5000.00
-----------------------------------------------
Total Production Cost : Rs. 46500.00
Total Sales Revenue   : Rs. 55000.00
Profit                : Rs. 8500.00
Profit Percentage     : 18.28%
Target Profit         : 20.00%
Target Status         : TARGET NOT ACHIEVED
================================================