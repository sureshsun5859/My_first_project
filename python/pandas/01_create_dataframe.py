"""Create and inspect pandas Series and DataFrame objects."""

import pandas as pd


def main():
    # A dictionary of columns becomes a DataFrame.
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "London", "Paris"],
        "salary": [50000, 60000, 70000],
    }

    df = pd.DataFrame(data)

    print("DataFrame:")
    print(df)                       #print the entire DataFrame
    print("\nShape:", df.shape)     #print the shape of the DataFrame number of rows and columns (3,4) first number is rows and second number is columns
    print("Columns:", df.columns.tolist())  #print the column names
    print("Data types:\n", df.dtypes) #print the data types of each column

    # A one-dimensional pandas object.
    ages = pd.Series([25, 30, 35], name="age")      #create single column series with name age and values 25,30,35
    print("\nSeries:")
    print(ages)


if __name__ == "__main__":
    main()
