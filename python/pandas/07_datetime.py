"""Work with date and time values in pandas."""

import pandas as pd


def main():
    data = {
        "event": ["Login", "Purchase", "Logout"],
        "date_time": [
            "2026-01-05 09:30:00",
            "2026-01-05 12:15:00",
            "2026-01-06 17:45:00",
        ],
    }
    df = pd.DataFrame(data)

    # Convert strings to datetime values.
    df["date_time"] = pd.to_datetime(df["date_time"])

    print("Converted date-time values:")
    print(df)
    print("\nYear:", df["date_time"].dt.year.tolist())
    print("Month:", df["date_time"].dt.month.tolist())
    print("Day of the week:", df["date_time"].dt.day_name().tolist())

    # Filter rows for one day.
    selected_date = pd.Timestamp("2026-01-05")
    filtered = df[df["date_time"].dt.date == selected_date.date()]
    print("\nEvents on 2026-01-05:")
    print(filtered)

    # Add a new column using date parts.
    df["date_only"] = df["date_time"].dt.date
    print("\nDate-only column:")
    print(df["date_only"])


if __name__ == "__main__":
    main()
