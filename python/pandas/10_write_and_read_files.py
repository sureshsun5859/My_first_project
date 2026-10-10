"""Read and write common file formats with pandas."""

from pathlib import Path

import pandas as pd


def main():
    output_directory = Path(__file__).resolve().parent / "output"
    output_directory.mkdir(exist_ok=True)

    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "score": [90, 85, 92],
    }
    df = pd.DataFrame(data)

    # Save a CSV file.
    csv_path = output_directory / "results.csv"
    df.to_csv(csv_path, index=False)
    print("Saved CSV:", csv_path)

    # Read the CSV file back.
    loaded_csv = pd.read_csv(csv_path)
    print("\nLoaded CSV:")
    print(loaded_csv)

    # Save and load JSON.
    json_path = output_directory / "results.json"
    df.to_json(json_path, orient="records")
    loaded_json = pd.read_json(json_path)
    print("\nLoaded JSON:")
    print(loaded_json)


if __name__ == "__main__":
    main()
