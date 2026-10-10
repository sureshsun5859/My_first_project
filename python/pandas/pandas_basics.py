"""Beginner-friendly pandas lessons.

Run each numbered script separately, or run this file for the main concepts.
"""

import pandas as pd


def main():
    # 1. Create a DataFrame from a dictionary.
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "London", "Paris"],
    }
    df = pd.DataFrame(data)

    # 2. Inspect basic information.
    print("DataFrame shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data types:\n", df.dtypes)

    # 3. Select a column.
    print("\nAge column:")
    print(df["age"])

    # 4. Filter rows.
    adults = df[df["age"] >= 30]
    print("\nAdults:")
    print(adults)

    # 5. Calculate a new column.
    df["age_in_ten_years"] = df["age"] + 10
    print("\nNew column:")
    print(df)


if __name__ == "__main__":
    main()
