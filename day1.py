from collections import Counter
#part 1
# Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists for the first and second columns
first_column = []
second_column = []

# Extract the columns
for line in lines:
    columns = line.split()
    if len(columns) >= 2:
        first_column.append(int(columns[0]))
        second_column.append(int(columns[1]))

first_column.sort()
second_column.sort()

distances = []
for i in range(len(first_column)):
    distances.append(abs(first_column[i] - second_column[i]))
print(sum(distances))

#part 2
# Initialize lists for the first and second columns
first_column = []
second_column = []

# Extract the columns
for line in lines:
    columns = line.split()
    if len(columns) >= 2:
        first_column.append(int(columns[0]))
        second_column.append(int(columns[1]))

second_column_counts = Counter(second_column)
print(sum([num * second_column_counts[num] for num in first_column]))