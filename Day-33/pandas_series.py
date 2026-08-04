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