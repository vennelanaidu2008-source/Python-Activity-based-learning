#ALGORITHM
1. Start the program.
2. Define product categories and their tax rates.
3. Define discount rules:
   - Bill amount of ₹5,000 or more: 10% discount.
   - Bill amount of ₹10,000 or more: 15% discount.
   - Maximum discount allowed: ₹2,000.
4. Input the number of products.
5. For each product, input the product name, category, unit price, and quantity.
6. Validate that the price is non-negative, quantity is positive, and category is valid.
7. Calculate each item's subtotal as unit price multiplied by quantity.
8. Calculate the total subtotal for all products.
9. Determine the applicable discount based on the subtotal and limit the discount to ₹2,000.
10. Calculate category-specific taxes on each item's value after allocating the discount proportionally.
11. Calculate the final payable amount by adding the tax to the discounted subtotal.
12. Display the itemized invoice, including product details, subtotal, discount, tax, and final bill.
13. Stop the program.

#FLOWCHART
                                   START
                    |
                    v
          Define Tax and Discount Rules
                    |
                    v
             Input Number of Products
                    |
                    v
          Enter Product Details
      (Name, Category, Price, Quantity)
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
       Display Error    Calculate Item
             |           Subtotals
             |               |
             |               v
             |        Calculate Bill Subtotal
             |               |
             |               v
             |       Check Discount Threshold
             |               |
             |               v
             |       Apply Discount Percentage
             |               |
             |               v
             |       Apply Maximum Discount Limit
             |               |
             |               v
             |       Calculate Category Taxes
             |               |
             |               v
             |       Calculate Final Bill
             |               |
             |               v
             |       Generate Itemized Invoice
             |               |
             |               v
             |              STOP
             |
             +----> Re-enter Product Details

             #CODE

             
# File name: retail_billing.py

TAX_RATES = {
    "food": 0.05,
    "clothing": 0.12,
    "electronics": 0.18
}

DISCOUNT_LIMIT_1 = 5000
DISCOUNT_LIMIT_2 = 10000
DISCOUNT_RATE_1 = 0.10
DISCOUNT_RATE_2 = 0.15
MAX_DISCOUNT = 2000


def calculate_discount(subtotal):
    if subtotal >= DISCOUNT_LIMIT_2:
        rate = DISCOUNT_RATE_2
    elif subtotal >= DISCOUNT_LIMIT_1:
        rate = DISCOUNT_RATE_1
    else:
        rate = 0

    return min(subtotal * rate, MAX_DISCOUNT)


def main():
    print("=== RETAIL BILLING SYSTEM ===")

    try:
        n = int(input("Enter number of products: "))

        if n <= 0:
            print("Error: Number of products must be positive.")
            return

        products = []

        for i in range(n):
            print(f"\nProduct {i + 1}")

            name = input("Enter product name: ")
            category = input(
                "Enter category (food/clothing/electronics): "
            ).strip().lower()

            price = float(input("Enter unit price (Rs.): "))
            quantity = int(input("Enter quantity: "))

            if category not in TAX_RATES:
                print("Error: Invalid product category.")
                return

            if price < 0 or quantity <= 0:
                print("Error: Price cannot be negative; "
                      "quantity must be positive.")
                return

            products.append({
                "name": name,
                "category": category,
                "price": price,
                "quantity": quantity,
                "subtotal": price * quantity
            })

        subtotal = sum(p["subtotal"] for p in products)
        discount = calculate_discount(subtotal)

        # Allocate the discount proportionally to each item.
        total_tax = 0

        for p in products:
            if subtotal > 0:
                item_discount = discount * p["subtotal"] / subtotal
            else:
                item_discount = 0

            taxable_amount = p["subtotal"] - item_discount
            p["discount"] = item_discount
            p["tax"] = taxable_amount * TAX_RATES[p["category"]]
            total_tax += p["tax"]

        final_amount = subtotal - discount + total_tax

        print("\n================ ITEMIZED INVOICE ================")
        print(f"{'Product':<15}{'Category':<14}{'Qty':>4}"
              f"{'Amount':>10}{'Discount':>11}{'Tax':>10}")

        for p in products:
            print(
                f"{p['name']:<15}"
                f"{p['category']:<14}"
                f"{p['quantity']:>4}"
                f"{p['subtotal']:>10.2f}"
                f"{p['discount']:>11.2f}"
                f"{p['tax']:>10.2f}"
            )

        print("-" * 64)
        print(f"Subtotal          : Rs. {subtotal:.2f}")
        print(f"Total Discount    : Rs. {discount:.2f}")
        print(f"Total Tax         : Rs. {total_tax:.2f}")
        print(f"Final Payable     : Rs. {final_amount:.2f}")
        print("==================================================")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()

#OUTPUT
================ ITEMIZED INVOICE ================
Product        Category       Qty    Amount   Discount       Tax
Rice           food            10   1000.00     150.00     42.50
Shirt          clothing         5   4000.00     600.00    408.00
Headphones     electronics      3   6000.00     900.00    918.00
----------------------------------------------------------------
Subtotal          : Rs. 11000.00
Total Discount    : Rs. 1650.00
Total Tax         : Rs. 1368.50
Final Payable     : Rs. 10718.50
==================================================