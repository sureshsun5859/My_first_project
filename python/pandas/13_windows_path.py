"""Use portable path handling when working with pandas files."""

from pathlib import Path

import pandas as pd


def main():
    project_directory = Path(__file__).resolve().parents[1]
    data_path = project_directory / "sample_data.csv"

    # The data path works on Windows, macOS, and Linux.
    df = pd.read_csv(data_path)
    print("Loaded file:", data_path)
    print(df)

    # A new output directory can be created automatically.
    output_directory = Path(__file__).resolve().parent / "output"
    output_directory.mkdir(exist_ok=True)
    output_path = output_directory / "sample_copy.csv"

    df.to_csv(output_path, index=False)
    print("Saved file:", output_path)


if __name__ == "__main__":
    main()
