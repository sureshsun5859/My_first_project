"""Group data and calculate aggregations with pandas."""

import pandas as pd


def main():
    data = {
        "city": ["New York", "New York", "London", "London", "Paris"],
        "department": ["Engineering", "Design", "Engineering", "Sales", "Design"],
        "salary": [50000, 60000, 45000, 55000, 65000],
        "employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    }
    df = pd.DataFrame(data)

    # Calculate the average salary by city.
    average_by_city = df.groupby("city")["salary"].mean()
    print("Average salary by city:")
    print(average_by_city)

    # Calculate several aggregations in one operation.
    summary = (
        df.groupby("city")
        .agg(
            total_salary=("salary", "sum"),
            average_salary=("salary", "mean"),
            employee_count=("employee", "count"),
        )
    )
    print("\nGrouped summary:")
    print(summary)

    # Group by more than one column.
    grouped_by_city_and_department = df.groupby(
        ["city", "department"]
    )["salary"].sum()
    print("\nSalary by city and department:")
    print(grouped_by_city_and_department)


if __name__ == "__main__":
    main()
