# Task 1 - Every Other Day

#           0       1           2           3           4           5          6        7
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# even_days = ["sunday", "tuesday", "thursday", "saturday"]
for i, day in enumerate(days):
    if i % 2 == 0:
         print(day)

