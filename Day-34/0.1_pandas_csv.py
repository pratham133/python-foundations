# ==========================================
# Program 22 - Reading a CSV File
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students)


# ==========================================
# Program 23 - Viewing DataFrame Columns
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.shape)

print(students.columns)

print(students.columns.to_list()) # To Conevrt the Pandas Index object in Normal List

print(students.dtypes)


# ==========================================
# Program 24 - Getting DataFrame Information
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

students.info()


# ==========================================
# Program 25 - Statistical Summary
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.describe())


# ==========================================
# Program 26 - Calculating the Mean
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Marks"].mean())

print(students["Age"].mean())

print(students["Marks"].max())

print(students["Marks"].min())

print(students["Marks"].sum())


# ==========================================
# Program 27 - Calculating the Median
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Marks"].median())

print(students["Age"].median())


# ==========================================
# Program 28 - Calculating Standard Deviation
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Marks"].std())


# ==========================================
# Program 29 - Counting Unique Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Age"].value_counts())

print(students["Marks"].value_counts())


# ==========================================
# Program 30 - Counting Unique Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Marks"].nunique())

print(students["Age"].nunique())


# ==========================================
# Program 31 - Finding Unique Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students["Age"].unique())

print(students["Age"].unique())


# ==========================================
# Program 32 - Checking Missing Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.isnull())


# ==========================================
# Program 33 - Counting Missing Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.isnull().sum())


# ==========================================
# Program 34 - Counting Total Missing Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.isnull().sum().sum())


# ==========================================
# Program 35 - Checking Non-Missing Values
# ==========================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.notnull().sum())


# ===============================================
# Program 36 - Removing Rows With Missing Values
# ===============================================

import pandas as pd

students = pd.read_csv("students.csv")

print(students.dropna())


# ================================================
# Program 37 - Testing dropna() With Missing Data
# ================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, None, 23, 21],
    "Marks": [95, 88, None, 91]
}

students = pd.DataFrame(student_data)

print("Originla DataFrame:")
print(students)

print("\nAfter Dropna()")
print(students.dropna())

print("\nOriginal DataFrame Again:")
print(students)


# ==========================================
# Program 38 - Filling Missing Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, None, 23, 21],
    "Marks": [95, 88, None, 91]
}

students = pd.DataFrame(student_data)

print(students.fillna(0))


# ==============================================
# Program 39 - Filling Missing Values With Mean
# ==============================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, None, 23, 21],
    "Marks": [95, 88, None, 91]
}

students = pd.DataFrame(student_data)

age_mean = students["Age"].mean()

print(students["Age"].fillna(age_mean))


# ==========================================
# Program 40 - Filling Missing Values With Median
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [18, None, 20, 80],
    "Marks": [95, 88, None, 91]
}

students = pd.DataFrame(student_data)

age_median = students["Age"].median()

print(students["Age"].fillna(age_median))


# ==========================================
# Program 41 - Filling Missing Text Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "City": ["Mumbai", None, "Pune", None]
}

students = pd.DataFrame(student_data)

print(students["City"].fillna("Unknown"))


# ==========================================
# Program 42 - Finding the Most Frequent Value
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Mumbai", None]
}

students = pd.DataFrame(student_data)

print(students["City"].mode())


# ==========================================
# Program 43 - Filling Missing City With Mode
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Mumbai", None]
}

students = pd.DataFrame(student_data)

city_mode = students["City"].mode()[0]

students["City"] = students["City"].fillna(city_mode)

print(students)


# ==========================================
# Program 44 - Replacing Inconsistent Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "mumbai", "Mumbai", "Delhi", "MUMBAI", "Delhi"]
}

students = pd.DataFrame(student_data)

students["City"] = students["City"].replace({
    "mumbai" : "Mumbai",
    "MUMBAI" : "Mumbai"
})

print(students)


# ==========================================
# Program 45 - Renaming DataFrame Columns
# ==========================================

import pandas as pd

student_data = {
    "student_name": ["Pratham", "Gojo", "Gun"],
    "student_age": [22, 24, 23],
    "student_marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print("Before Renaming:")
print(students)

students = students.rename(columns={
    "student_name" : "Name",
    "student_age"  : "Age",
    "student_marks": "Marks" 
})

print("\nAfter Renaming:")
print(students)


# ==========================================
# Program 46 - Using inplace=True
# ==========================================

import pandas as pd

student_data = {
    "student_name": ["Pratham", "Gojo", "Gun"],
    "student_age": [22, 24, 23],
    "student_marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print("Before Renaming:")
print(students)

students.rename(
    columns={
        "student_name" : "Name",
        "student_age" : "Age",
        "student_marks" : "Marks"
    },
    inplace=True
)

print("\nAfter Renaming:")
print(students)


# ==========================================
# Program 47 - Adding a New Column
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

students["City"] = ["Mumbai", "Pune", "Mumbai"]
print(students)

students["Passed"] = students["Marks"] >= 70
print(students)

students["BonusMarks"] = students["Marks"] + 5
print(students)


# ==========================================
# Program 48 - Removing a Column
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65],
    "City": ["Mumbai", "Pune", "Mumbai"],
    "Passed": [True, True, False],
    "BonusMarks": [100, 93, 70]
}

students = pd.DataFrame(student_data)

print("Before Removing:")
print(students)

students = students.drop(columns=["BonusMarks"])

print("\nAfter Removing:")
print(students)


# ==========================================
# Program 49 - Removing Multiple Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65],
    "City": ["Mumbai", "Pune", "Mumbai"],
    "Passed": [True, True, False]
}

students = pd.DataFrame(student_data)

print("Before Removing:")
print(students)

students = students.drop(columns=["City", "Passed"])

print("\nAfter Removing:")
print(students)


# ==========================================
# Program 50 - Selecting Multiple Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65],
    "City": ["Mumbai", "Pune", "Mumbai"]
}

students = pd.DataFrame(student_data)

print(students[["Marks", "Name"]])


# ==========================================
# Program 51 - Selecting Rows With iloc
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Row 0:")
print(students.iloc[0])

print("\nRow 1:")
print(students.iloc[1])

print("\nRows 0 to 1:")
print(students.iloc[0:2])


# ==========================================
# Program 52 - Selecting Rows and Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.iloc[1:4, 0:2])

print()

print(students.iloc[0:2, 1:3])


# ==========================================
# Program 53 - Selecting Rows With loc
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Row with label 0:")
print(students.loc[0])

print("\nRow with label 2:")
print(students.loc[2])

print("\nRows with labels 1 to 3:")
print(students.loc[1:3])


# =================================================
# Program 54 - Selecting Rows and Columns With loc
# =================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.loc[1:3, ["Name", "Marks"]])

print(students.loc[0:2, ["Name", "Age"]])

print(students.loc[2:4, ["Marks"]])

print(students.loc[ : , ["Name", "Marks"]])


# ==========================================
# Program 55 - Filtering With loc
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.loc[students["Marks"] >= 90, ["Name", "Marks"]])

print()

print(students.loc[students["Age"] <=22, ["Name", "Age"]])

print()

print(students.loc[students["Marks"] >= 85, ["Name", "Age", "Marks"]])


# ==========================================
# Program 56 - Multiple Conditions With loc
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.loc[
    (students["Age"] <= 22) & (students["Marks"] >= 85),
    ["Name", "Age", "Marks"]
])

print()

print(students.loc[
    (students["Age"] >= 21) & (students["Marks"] >= 90),
    ["Name", "Age", "Marks"]
])

print()

print(students.loc[
    (students["Marks"] >= 90) | (students["Age"] <= 20),
    ["Name", "Age", "Marks"]
])


# ==========================================
# Program 57 - NOT Condition With loc
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.loc[
    ~(students["Marks"] >= 90), 
    ["Name", "Age", "Marks"]
])


# ==========================================
# Program 58 - Filtering and Sorting
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.loc[
    students["Marks"] >= 85, 
    ["Name", "Marks"]
].sort_values("Marks", ascending=False))

print()

print(students.loc[
    students["Age"] <= 22,
    ["Name", "Age", "Marks"]
].sort_values("Marks", ascending=True))


# ==========================================
# Program 59 - Sorting by Multiple Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Rahul", "Naruto"],
    "Age": [22, 24, 21, 20],
    "Marks": [90, 90, 85, 90]
}

students = pd.DataFrame(student_data)

print(students.sort_values(
    ["Marks", "Age"],
    ascending=[False, True]
))


# ==========================================
# Program 60 - Top and Bottom Records
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Top 3 Students:")
print(
    students
    .sort_values("Marks", ascending=False)
    .head(3)
)

print()

print("Bottom 2 Students:")
print(
    students
    .sort_values("Marks", ascending=True)
    .head(2)
)

print(students.head(3))

print()

print(
    students
    .sort_values(
        "Age",
        ascending=False
    ).head(2)
)


# ==========================================
# Program 61 - tail() and Sorting
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Last 2 Rows:")
print(students.tail(2))

print()

print("Last 2 After Sorting Marks:")
print(
    students
    .sort_values("Marks", ascending=False)
    .tail(2)
)

print()

print("Last 3 After Ascending Sort:")
print(
    students
    .sort_values("Marks", ascending=True)
    .tail(3)
)


# ==========================================
# Program 62 - Filtering With query()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Students with Marks >= 90:")
print(students.query("Marks >= 90"))

print()

print("Students with Age <= 22:")
print(students.query("Age <= 22"))

print()

print("Students with Age <= 22 AND Marks >= 85:")
print(students.query("Age <= 22 and Marks >= 85"))


# ==========================================
# Program 63 - Counting Filtered Rows
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Students with Marks >= 85:")
print(students[students["Marks"] >= 85].shape[0])

print()

print("Students with Age <= 22:")
print(students[students["Age"] <= 22].shape[0])

print()

print("Students with Marks >= 85 AND Age <= 22:")
print(students[
        (students["Marks"] >= 85) & 
        (students["Age"] <= 22)
    ].shape[0]
)


# ==========================================
# Program 64 - Counting Conditions With sum()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Students with Marks >= 85:")
print((students["Marks"] >= 85).sum())

print()

print("Students with Age <= 22:")
print((students["Age"] <= 22).sum())

print()

print("Students with Marks >= 85 AND Age <= 22:")
print(
    (
        (students["Marks"] >= 85) &
        (students["Age"] <= 22)
    ).sum()
)


# ==========================================
# Program 65 - Introduction to groupby()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students)

print(students.groupby("City")["Marks"].mean())

print(students.groupby("City")["Marks"].sum())

print(students.groupby("City")["Marks"].max())

print(students.groupby("City")["Marks"].count())


# ==========================================
# Program 66 - Multiple Aggregations With agg()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby("City")["Marks"].agg(
    ["mean","min","max", "sum", "count"]
)

print(result)


# ==========================================
# Program 67 - Different Aggregations With agg()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby("City").agg({
    "Marks" : "mean",
    "Age" : "max",
    "Name" : "count"
})

print(result)

print(students.groupby("City").agg({
    "Marks" : "max",
    "Age" : "min",
    "Name" : "count"
}))


# ==========================================
# Program 68 - Named Aggregations
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby("City").agg(
    Average_Marks = ("Marks", "mean"),
    Maximum_Age = ("Age", "max"),
    Student_count = ("Name", "count")
)

print(result)

print(students.groupby("City").agg(
        Highest_Marks = ("Marks", "max"),
        Lowest_Age = ("Age", "min"),
        Total_Marks = ("Marks", "sum") 
))


# ==========================================
# Program 69 - groupby() With Multiple Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby(
    ["City", "Gender"]
)["Marks"].mean()

print(result)

print(students.groupby(["City", "Gender"])["Marks"].sum())

print(students.groupby(
    ["City", "Gender"])
    ["Marks"]
    .count()
)


# ==========================================
# Program 70 - reset_index() After groupby()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby(
    ["City", "Gender"]
)["Marks"].mean()

print("Before reset_index():")
print(result)

print()

result = students.reset_index()

print("After reset_index():")
print(result)

result = students.groupby(
    ["City", "Gender"]
)["Marks"].sum().reset_index()

print(result)


# ==========================================
# Program 71 - groupby() With as_index=False
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby(
    ["City", "Gender"],
    as_index=False
)["Marks"].mean()

print(result)

print(students.groupby(
    "City",
    as_index=False
    )["Marks"].sum()
)


# ==========================================
# Program 72 - groupby() + sort_values()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby(
    "City",
    as_index=False
)["Marks"].mean()

result = result.sort_values(
    "Marks",
    ascending=False
)

print(result)

sum_result = students.groupby(
    "City",
    as_index=False
)["Marks"].sum()

sum_result = sum_result.sort_values(
    "Marks",
    ascending=False
)

print(sum_result)

result_pattern = (
    students
    .groupby("City", as_index=False)["Marks"]
    .mean()
    .sort_values("Marks", ascending=False)
) 

print(result_pattern)


# ==========================================
# Program 73 - groupby() + agg() + sort_values()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

result = students.groupby(
    "City", 
    as_index=False
).agg(
    Average_Marks = ("Marks", "mean"),
    Highest_Marks = ("Marks", "max"),
    Student_Count = ("Name", "count")
)

result = result.sort_values(
    "Average_Marks",
    ascending=False
)

print(result)


# ==========================================
# Program 74 - value_counts()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("City Counts:")
print(students["City"].value_counts())

print()

print("Gender Counts:")
print(students["Gender"].value_counts())

print("Marks Counts:")
print(students["Marks"].value_counts())


# ==========================================
# Program 75 - value_counts(normalize=True)
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

city_percentage = students["City"].value_counts(normalize=True) * 100

print(city_percentage)


# ==========================================
# Program 76 - unique() and nunique()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Pune"],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Male"],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print("Unique Cities:")
print(students["City"].unique())

print()

print("Number of Unique Cities:")
print(students["City"].nunique())

print()

print("Unique Genders:")
print(students["Gender"].unique())

print()

print("Number of Unique Genders:")
print(students["Gender"].nunique())


# ==========================================
# Program 77 - Finding Duplicates
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Pratham"],
    "Age": [22, 24, 23, 21, 22],
    "Marks": [95, 88, 65, 91, 95]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

print()

print("Duplicate Check:")
print(students.duplicated())

print()

print("Duplicate Rows:")
print(students[students.duplicated()])


# ==========================================
# Program 78 - drop_duplicates()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Pratham"],
    "Age": [22, 24, 23, 21, 22],
    "Marks": [95, 88, 65, 91, 95]
}

students = pd.DataFrame(student_data)

print("Before Removing Duplicates:")
print(students)

print()

students = students.drop_duplicates()

print("After Removing Duplicates:")
print(students)


# ==========================================
# Program 79 - drop_duplicates() with subset
# ==========================================

import pandas as pd

customer_data = {
    "Customer_ID": [101, 102, 101, 103],
    "Name": ["Pratham", "Gojo", "Pratham", "Rahul"],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai"],
    "Purchase": [500, 700, 900, 600]
}

customers = pd.DataFrame(customer_data)

print("Original DataFrame:")
print(customers)

print()

clean_customers = customers.drop_duplicates(
    subset="Customer_ID"
)

print("After Removing Duplicate Customer IDs:")
print(clean_customers)


# ==========================================
# Program 80 - keep Parameter
# ==========================================

import pandas as pd

customer_data = {
    "Customer_ID": [101, 102, 101, 103, 101],
    "Name": ["Pratham", "Gojo", "Pratham", "Rahul", "Pratham"],
    "Purchase": [500, 700, 900, 600, 1200]
}

customers = pd.DataFrame(customer_data)

print("Original DataFrame:")
print(customers)

print("\nKeep First:")
print(customers.drop_duplicates(
    subset="Customer_ID",
    keep="first"
))

print("\nKeep Last:")
print(customers.drop_duplicates(
    subset="Customer_ID",
    keep="last"
))

print("\nMark All Duplicates:")
print(customers.drop_duplicates(
    subset="Customer_ID",
    keep=False
))


# ==========================================
# Program 81 - Finding Missing Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto"],
    "Age": [22, 24, None, 21, None],
    "Marks": [95, None, 65, 91, 89],
    "City": ["Mumbai", "Delhi", None, "Delhi", "Mumbai"]
}

students = pd.DataFrame(student_data)

print("DataFrame:")
print(students)

print()

print("Missing Value Check:")
print(students.isnull())

print()

print("Missing Values Per Column:")
print(students.isna().sum())


# ==========================================
# Program 82 - Removing Missing Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto"],
    "Age": [22, 24, None, 21, None],
    "Marks": [95, None, 65, 91, 89],
    "City": ["Mumbai", "Delhi", None, "Delhi", "Mumbai"]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

print()

print("After dropna():")
print(students.dropna())


# ==========================================
# Program 83 - Filling Missing Values
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto"],
    "Age": [22, 24, None, 21, None],
    "Marks": [95, None, 65, 91, 89],
    "City": ["Mumbai", "Delhi", None, "Delhi", "Mumbai"]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

print()

students["Marks"] = students["Marks"].fillna(0)

students["Age"] = students["Age"].fillna(0)

students["City"] = students["City"].fillna('Unknown')

print("After Filling Missing Values:")
print(students)


# ==========================================
# Program 84 - fillna() with Mean and Median
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto"],
    "Marks": [95, 88, None, 91, 89]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)
 
print()

mean_marks = students["Marks"].mean()
median_marks = students["Marks"].median()

print("Mean Marks:", mean_marks)
print("Median Marks:", median_marks)

print()

mean_filled = students.copy()
mean_filled["Marks"] = mean_filled["Marks"].fillna(mean_marks)

print("After Filling with Mean:")
print(mean_filled)

print()

median_filled = students.copy()
median_filled["Marks"] = median_filled["Marks"].fillna(median_marks)

print("After Filling with Median:")
print(median_filled)


# ==========================================
# Program 85 - Forward Fill and Backward Fill
# ==========================================

import pandas as pd

sales_data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"],
    "Sales": [100, None, None, 250, 300]
}

sales = pd.DataFrame(sales_data)

print("Original DataFrame:")
print(sales)

print()

forward_filled = sales.copy()
forward_filled["Sales"] = forward_filled["Sales"].ffill()

print("After Forward Fill:")
print(forward_filled)

print()

backward_filled = sales.copy()
backward_filled["Sales"] = backward_filled["Sales"].bfill()

print("After Backward Fill:")
print(backward_filled)


# ==========================================
# Program 86 - Renaming Columns
# ==========================================

import pandas as pd

sales_data = {
    "Customer Name": ["Pratham", "Gojo", "Rahul"],
    "sales amount": [5000, 7000, 6000],
    "ORDER_DATE": ["2026-01-10", "2026-01-11", "2026-01-12"]
}

sales = pd.DataFrame(sales_data)

print("Original Columns:")
print(sales.columns)

print()

sales = sales.rename(columns={
    "Customer Name": "Customer_Name",
    "sales amount": "Sales_Amount",
    "ORDER_DATE": "Order_Date"
})

print("Renamed DataFrame:")
print(sales)


# ==========================================
# Program 87 - Pandas Merge Basics
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer_ID": [101, 102, 101, 103],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet"],
    "Sales": [50000, 30000, 5000, 25000]
}

orders = pd.DataFrame(orders_data)

print("Customers DataFrame:")
print(customers)

print()

print("Orders DataFrame:")
print(orders)


# ==========================================
# Program 88 - Merging Two DataFrames
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer_ID": [101, 102, 101, 103],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet"],
    "Sales": [50000, 30000, 5000, 25000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID"
)

print("Merged DataFrame:")
print(merged_data)


# ==========================================
# Program 89 - Inner Join
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer_ID": [101, 102, 101, 103],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet"],
    "Sales": [50000, 30000, 5000, 25000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
)

print("Inner Join Result:")
print(merged_data)


# ==========================================
# Program 90 - Left Join
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer_ID": [101, 102, 101, 103],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet"],
    "Sales": [50000, 30000, 5000, 25000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="left"
)

print("Left Join Result:")
print(merged_data)


# ==========================================
# Program 91 - Right Join
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer_ID": [101, 102, 101, 103, 105],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet", "Keyboard"],
    "Sales": [50000, 30000, 5000, 25000, 2000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="right"
)

print("Right Join Result:")
print(merged_data)


# ==========================================
# Program 92 - Outer Join
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["Pratham", "Gojo", "Naruto", "Luffy"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer_ID": [101, 102, 101, 103, 105],
    "Product": ["Laptop", "Phone", "Headphones", "Tablet", "Keyboard"],
    "Sales": [50000, 30000, 5000, 25000, 2000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="outer"
)

print("Outer Join Result:")
print(merged_data)


# ==========================================
# Program 93 - Merge with Different Column Names
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103],
    "Name": ["Pratham", "Gojo", "Naruto"],
    "City": ["Mumbai", "Delhi", "Mumbai"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003],
    "Customer": [101, 102, 103],
    "Product": ["Laptop", "Phone", "Tablet"],
    "Sales": [50000, 30000, 25000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    left_on="Customer_ID",
    right_on="Customer"
)



print("Merged DataFrame:")
print(merged_data)


# ==========================================
# Program 94 - Merge with Suffixes
# ==========================================

import pandas as pd

customers_data = {
    "Customer_ID": [101, 102, 103],
    "Name": ["Pratham", "Gojo", "Naruto"],
    "City": ["Mumbai", "Delhi", "Mumbai"]
}

customers = pd.DataFrame(customers_data)

orders_data = {
    "Order_ID": [1001, 1002, 1003],
    "Customer_ID": [101, 102, 103],
    "City": ["Mumbai", "Delhi", "Pune"],
    "Sales": [50000, 30000, 25000]
}

orders = pd.DataFrame(orders_data)

merged_data = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    suffixes=("_Customer", "_Order")
)

print("Merged DataFrame:")
print(merged_data)


# ==========================================
# Program 95 - Combining DataFrames with concat()
# ==========================================

import pandas as pd

january_data = {
    "Customer_ID": [101, 102],
    "Sales": [5000, 7000]
}

february_data = {
    "Customer_ID": [103, 104],
    "Sales": [6000, 8000]
}

january_sales = pd.DataFrame(january_data)
february_sales = pd.DataFrame(february_data)

combined_sales = pd.concat(
    [january_sales, february_sales],
    ignore_index=True
)

print("January Sales:")
print(january_sales)

print()

print("February Sales:")
print(february_sales)

print()

print("Combined Sales:")
print(combined_sales)


# ==========================================
# Program 96 - Combining DataFrames with axis=1
# ==========================================

import pandas as pd

customer_data = {
    "Customer_ID": [101, 102, 103],
    "Name": ["Pratham", "Gojo", "Naruto"]
}

sales_data = {
    "Sales": [5000, 7000, 6000],
    "Product": ["Laptop", "Phone", "Tablet"]
}

customers = pd.DataFrame(customer_data)
sales = pd.DataFrame(sales_data)

combined_data = pd.concat(
    [customers, sales],
    axis=1
)


print("Customers DataFrame:")
print(customers)

print()

print("Sales DataFrame:")
print(sales)

print()

print("Combined DataFrame:")
print(combined_data)