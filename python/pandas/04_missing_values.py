"""Learn to detect, fill, and remove missing values."""

import pandas as pd


def main():
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, None, 35],
        "salary": [50000, 60000, None],
    }
    df = pd.DataFrame(data)

    print("Original data:")
    print(df)
    print("\nMissing values by column:")
    print(df.isna().sum())

    # Fill missing values with a fixed value.
    filled_with_zero = df.fillna(0)
    print("\nFilled with zero:")
    print(filled_with_zero)

    # Fill missing numeric values with the column mean.
    filled_with_mean = df.copy()
    filled_with_mean["age"] = filled_with_mean["age"].fillna(
        filled_with_mean["age"].mean()
    )
    filled_with_mean["salary"] = filled_with_mean["salary"].fillna(
        filled_with_mean["salary"].mean()
    )
    print("\nFilled with column means:")
    print(filled_with_mean)

    # Remove rows containing missing values.
    print("\nRows after removing missing values:")
    print(df.dropna())


if __name__ == "__main__":
    main()
