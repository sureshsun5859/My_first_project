"""Load and inspect CSV data with pandas."""

from pathlib import Path

import pandas as pd


def main():
    csv_path = Path(__file__).resolve().parents[1] / "sample_data.csv"

    # A simple CSV load.
    df = pd.read_csv(csv_path)
    print("Loaded data:")
    print(df)

    # Read the same file with a different index and missing-value handling.
    df_with_index = pd.read_csv(
        csv_path,
        index_col=0,
        na_values=["N/A", "NULL"],
    )

    print("\nData with the first column used as the index:")
    print(df_with_index)
    print("\nIndex:", df_with_index.index.tolist())


if __name__ == "__main__":
    main()
