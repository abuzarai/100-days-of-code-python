import pandas

students = {
    "student": ["Angela", "Mark", "James", "Lily"],
    "score": [43, 56, 78, 21]
}

students_df = pandas.DataFrame(students)

#Loop through rows of dataframe
for (index, row) in students_df.iterrows():
    if row.student == "Angela":
        print(row)

