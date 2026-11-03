"""Select columns and filter rows with pandas."""

import pandas as pd


def main():
    data = {
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40],
        "city": ["New York", "London", "Paris", "Berlin"],
        "salary": [50000, 60000, 70000, 80000],
    }
    df = pd.DataFrame(data)

    # Select one column.
    print("Single column:")
    print(df["name"])

    # Select multiple columns.
    print("\nSelected columns:")
    print(df[["name", "salary"]])

    # Select rows using one condition.
    adults = df[df["age"] >= 30]
    print("\nAdults:")
    print(adults)

    # Use multiple conditions with & and |.
    high_earning = df[
        (df["age"] >= 30) & (df["salary"] >= 65000)
    ]
    print("\nHigh-earning adults:")
    print(high_earning)

    # Select rows using loc.
    print("\nRows using loc:")
    print(df.loc[1:2])

    # Select columns using loc.
    print("\nColumns using loc:")
    print(df.loc[:, ["name", "city"]])

    # select columns using iloc
    print("\nColumns using iloc:")  
    print(df.iloc[:, 0:2])


if __name__ == "__main__":
    main()
