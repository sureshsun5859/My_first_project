"""Perform common string operations with pandas."""

import pandas as pd


def main():
    data = {
        "name": [" alice ", "BOB", "Charlie", "ALICE"],
        "email": [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com",
            "alice@company.com",
        ],
    }
    df = pd.DataFrame(data)

    # Remove surrounding whitespace and convert text to lowercase.
    df["normalized_name"] = df["name"].str.strip().str.lower()
    print("Normalized names:")
    print(df["normalized_name"])

    # Split a string into parts.
    df["email_domain"] = df["email"].str.split("@").str[1]
    print("\nEmail domains:")
    print(df["email_domain"])

    # Search for values containing a substring.
    print("\nRows containing alice:")
    print(df[df["normalized_name"].str.contains("alice")])

    # Add a new column using a regular expression.
    df["username"] = df["email"].str.extract(r"^([^@]+)@", expand=False)
    print("\nUsernames:")
    print(df["username"])


if __name__ == "__main__":
    main()
