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


# ==========================================
# Program 97 - Pivot Table Aggregation Functions
# ==========================================

import pandas as pd


sales_data = {
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Laptop"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Sales": [50000, 45000, 30000, 25000, 20000, 55000]
}


sales = pd.DataFrame(sales_data)


sum_table = sales.pivot_table(
    values="Sales",
    index="Product",
    aggfunc="sum"
)

print("Total Sales by Product:")
print(sum_table)

print()


mean_table = sales.pivot_table(
    values="Sales",
    index="Product",
    aggfunc="mean"
)

print("Average Sales by Product:")
print(mean_table)

print()


count_table = sales.pivot_table(
    values="Sales",
    index="Product",
    aggfunc="count"
)

print("Number of Sales Records by Product:")
print(count_table)


# ==========================================
# Program 98 - Multiple Aggregation Functions
# ==========================================

sales_data = {
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Laptop"],
    "Sales": [50000, 45000, 30000, 25000, 20000, 55000]
}

sales = pd.DataFrame(sales_data)

pivot_table = sales.pivot_table(
    values="Sales",
    index="Product",
    aggfunc=["sum", "mean", "count"]
)


print("Sales Analysis by Product:")
print(pivot_table)


# ==========================================
# Program 99 - Multiple Values in Pivot Table
# ==========================================

sales_data = {
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Laptop"],
    "Sales": [50000, 45000, 30000, 25000, 20000, 55000],
    "Profit": [10000, 9000, 6000, 5000, 4000, 11000]
}

sales = pd.DataFrame(sales_data)

pivot_table = sales.pivot_table(
    values=["Sales", "Profit"],
    index="Product",
    aggfunc="sum"
)


print("Sales and Profit Analysis by Product:")
print(pivot_table)


# ==========================================
# Program 100 - Handling Missing Values in Pivot Tables
# ==========================================

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
    aggfunc="sum",
    fill_value=0
)


print("Product Sales by City:")
print(pivot_table)


# ==========================================
# Program 101 - Pivot Table Totals
# ==========================================

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
    aggfunc="sum",
    fill_value=0,
    margins=True
)


print("Product Sales with Totals:")
print(pivot_table)