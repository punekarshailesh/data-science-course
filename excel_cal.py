import csv

def process_file(file_path, encoding, delimiter):
    total = 0
    with open(file_path, mode='r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            if len(row) == 2:  # Ensure there are two columns
                symbol, value = row
                if symbol in ['‘ OR ’', '“']:  # Check if symbol matches
                    total += float(value)  # Sum up the value
    return total

# Define file paths
file1 = '\q-unicode-data\data1.csv'
file2 = '\q-unicode-data\data2.csv'
file3 = '\q-unicode-data\data3.txt'

# Process each file
sum1 = process_file(file1, 'cp1252', ',')  # CSV with CP-1252 encoding
sum2 = process_file(file2, 'utf-8', ',')   # CSV with UTF-8 encoding
sum3 = process_file(file3, 'utf-16', '\t')  # Tab-separated file with UTF-16 encoding

# Total sum across all files
total_sum = sum1 + sum2 + sum3

print(f"Total sum: {total_sum}")
