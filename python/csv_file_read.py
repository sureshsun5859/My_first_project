
#file path
import csv


file_path = 'D:\\sures\\Documents\\GitHub\\My_first_project\\python\\sample_data.csv'
# incase of unix file system it would be like this /suresh/Documents/GitHub/My_first_project/python/sample_data.csv

with open(file_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the header row (if present)
    header = next(csv_reader, None)
    if header:
        print(f"Header: {header}")

    # Read and print top 10 row of the CSV file
    count = 0
    for row in csv_reader:
        print(row)
        count += 1
        if count >= 10:
            break

