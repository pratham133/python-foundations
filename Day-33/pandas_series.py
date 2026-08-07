# ==========================================
# Program 1 - Introduction to Pandas Series
# ==========================================

import pandas as pd

students = pd.Series([85, 90, 78, 92, 88])

print(students)


# ==========================================
# Program 2 - Accessing Data from a Series
# ==========================================

import pandas as pd

students = pd.Series([85, 90, 72, 98, 88])

print(students[0])

print(students[3])

print(students[4])


# ==========================================
# Program 3 - Creating a Pandas DataFrame
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students)


# ==========================================
# Program 4 - Selecting a Single Column
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students["Marks"])


# ==========================================
# Program 5 - Selecting Multiple Columns
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students[["Age","Marks"]])


# ==========================================
# Program 6 - Accessing Rows Using loc[]
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students.loc[0])

print()

print(students.loc[2])


# ==========================================
# Program 7 - Accessing a Specific Value
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students.loc[0, "Name"])

print(students.loc[1,"Marks"])

print(students.loc[2, "Age"])

print(students.loc[0, "Marks"])

print(students.loc[2,"Name"])

print(students.loc[1, "Age"])


# ==========================================
# Program 8 - Accessing Data Using iloc[]
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun"],
    "Age": [22, 24, 23],
    "Marks": [95, 88, 65]
}

students = pd.DataFrame(student_data)

print(students)

print(students.iloc[0, 0])

print(students.iloc[1, 2])

print(students.iloc[2, 1])


# ==================================================
# Program 9 - Filtering Data Using One Condition
# ==================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

high_marks = students[students["Marks"] > 90]

print(high_marks)


# ==========================================
# Program 10 - Filtering with AND (&)
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

filtered_students = students[
    (students["Marks"] > 80) & 
    (students["Age"] >  21)
]

print(filtered_students)


# ==========================================
# Program 11 - Filtering with OR (|)
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

filtered_students = [
    (students["Marks"] > 90) |
    (students["Age"] > 23)
]

print(filtered_students)


# ==========================================
# Program 12 - Filtering Using Equal To (==)
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[students["Marks"] == 88]

print(result)


# ===============================================
# Program 13 - Filtering Using Not Equal To (!=)
# ===============================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[students["Marks"] != 88]

print(result)


# ===========================================================
# Program 14 - Filtering Using Greater Than or Equal To (>=)
# ===========================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[students["Marks"] >= 90]

print(result)


# =========================================================
# Program 15 - Filtering Using Less Than or Equal To (<=)
# =========================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[students["Marks"] <= 88]

print(result)

print(students[students["Age"] <= 22])

print(students["Marks"] <= 91)


# ==========================================
# Program 16 - Filtering Using isin()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[students["Name"].isin(["Gojo", "Rahul"])]

print(result)

print(students["Marks"].isin([88, 91]))

print(students[students["Age"].isin([22, 23])])


# ==========================================
# Program 17 - Filtering Using between()
# ==========================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

result = students[
    students["Marks"].between(80, 90)
    ]

print(result)

print(students
    [students["Age"].between(22, 24)]
    )

print(students["Marks"].between(90, 95))


# ==============================================
# Program 18 - Sorting Data using sort_values()
# ==============================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul"],
    "Age": [22, 24, 23, 21],
    "Marks": [95, 88, 65, 91]
}

students = pd.DataFrame(student_data)

print(students.sort_values("Marks"))

print(students.sort_values("Age"))

print(students.sort_values("Marks", ascending=False))


# =================================================
# Program 19 - Viewing the First Rows using head()
# =================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.head())

print(students.head(4))


# ================================================
# Program 20 - Viewing the Last Rows using tail()
# ================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.tail())

print(students.tail(4))


# ================================================
# Program 21 - Viewing Random Rows using sample()
# ================================================

import pandas as pd

student_data = {
    "Name": ["Pratham", "Gojo", "Gun", "Rahul", "Naruto", "Luffy"],
    "Age": [22, 24, 23, 21, 20, 19],
    "Marks": [95, 88, 65, 91, 89, 84]
}

students = pd.DataFrame(student_data)

print(students.sample())