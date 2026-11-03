## there diffferent file types there like text,csv,json,parquet,excel etc.

# txt and binary files can read direclty in python using open function.
file_path = 'D:\\sures\\Documents\\GitHub\\My_first_project\\python\\pandas\\file_read'
print(f"source file path: {file_path}")
#read the entire text file content using read() method
with open(file_path + '\\data.txt', 'r') as f :
    data = f.read()  # read the entire content of the file
    print(data)      # print the content of the file

print(f"Number of characters in the file: {len(data)}")
print(f"Number of lines in the file: {len(data.splitlines())}")  # count the number of lines in the file

# read the text file line by line using readlines() method
with open(file_path + '\\data.txt', 'r') as f:
    lines = f.readlines()  # read all lines into a list
    print(f"Lines in the file: {lines}")  # print the list of lines

#read the file in binary mode using 'rb' mode
with open(file_path + '\\data.txt', 'rb') as f:
    binary_data = f.read()  # read the entire content of the file in binary mode
    print(f"Binary data: {binary_data}")  # print the binary data

# read the csv file with header using import csv module
import csv
with open(file_path + '\\data.csv', 'r') as f:
    reader = csv.reader(f)  # create a CSV reader object
    header = next(reader)   # read the header row
    print(f"CSV Header: {header}")  # print the header
    for row in reader:      # iterate over the remaining rows
        print(row)          # print each row
        # print(f"id: {row[0]}, name: {row[1]}, age: {row[2]}")  # print specific columns by index
# read json file using json module
import json

with open(file_path + '\\data.json', 'r') as f:
    json_data = json.load(f)  # load the JSON data from the file
    print(f"JSON data: {json_data}")  # print the JSON data