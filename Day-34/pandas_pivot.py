# ==========================================
# Program 96 - Pandas Pivot Table Basics
# ==========================================

import pandas as pd


sales_data = {
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Tablet", "Laptop"],
    "City": ["Mumbai", "Mumbai", "Delhi", "Delhi", "Mumbai", "Delhi"],
    "Sales": [50000, 30000, 45000, 25000, 20000, 55000]
}


sales = pd.DataFrame(sales_data)

pivot_table = sales.pivot_table(
    values="Sales",
    index="Product",
    columns="City",
    aggfunc="sum"
)


print("Original Sales Data:")
print(sales)

print()

print("Sales Pivot Table:")
print(pivot_table)