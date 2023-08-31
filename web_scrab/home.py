import csv

# Read and print the contents of the CSV file
with open('product_info.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
