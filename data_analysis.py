import csv

marks = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        marks.append(int(row["Marks"]))

print("Marks:", marks)

# Average
avg = sum(marks) / len(marks)
print("Average Marks:", avg)

# Highest
print("Highest Marks:", max(marks))

# Lowest
print("Lowest Marks:", min(marks))
