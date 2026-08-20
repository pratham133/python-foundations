# ==========================================
# Program 104 - Converting Text to Datetime
# ==========================================

import pandas as pd


sales_data = {
    "Order_ID": [1001, 1002, 1003],
    "Order_Date": ["2026-01-15", "2026-02-20", "2026-03-10"],
    "Sales": [5000, 7000, 6000]
}


sales = pd.DataFrame(sales_data)


print("Before Datetime Conversion:")
print(sales)

print()

print("Data Types Before Conversion:")
print(sales.dtypes)

print()


sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])

print("After Datetime Conversion:")
print(sales)

print()

print("Data Types After Conversion:")
print(sales.dtypes)


# ==========================================
# Extracting Year, Month, and Day from Datetime
# ==========================================

sales["Year"] = sales["Order_Date"].dt.year
sales["Month"] = sales["Order_Date"].dt.month
sales["Day"] = sales["Order_Date"].dt.day


print("Sales Data with Date Components:")
print(sales)