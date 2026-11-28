import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Retail Sales Data Analyzer

class RetailAnalyzer:

    def __init__(self):
        self.df = None

    # Create CSV automatically
    def create_csv(self, file_path):

        data = {
            "Date": [
                "2026-01-01", "2026-01-02", "2026-01-03",
                "2026-01-04", "2026-01-05", "2026-01-06",
                "2026-01-07", "2026-01-08", "2026-01-09",
                "2026-01-10", "2026-01-11", "2026-01-12",
                "2026-01-13", "2026-01-14", "2026-01-15",
                "2026-01-16", "2026-01-17", "2026-01-18",
                "2026-01-19", "2026-01-20"
            ],

            "Product": [
                "Laptop", "Mobile", "Mouse", "Keyboard",
                "Laptop", "Mobile", "Headphone", "Mouse",
                "Keyboard", "Laptop", "Mobile", "Headphone",
                "Mouse", "Laptop", "Keyboard", "Mobile",
                "Headphone", "Mouse", "Laptop", "Mobile"
            ],

            "Category": [
                "Electronics", "Electronics", "Accessories",
                "Accessories", "Electronics", "Electronics",
                "Accessories", "Accessories", "Accessories",
                "Electronics", "Electronics", "Accessories",
                "Accessories", "Electronics", "Accessories",
                "Electronics", "Accessories", "Accessories",
                "Electronics", "Electronics"
            ],

            "Price": [
                50000, 20000, 500, 1000, 50000,
                20000, 1500, 500, 1000, 50000,
                20000, 1500, 500, 50000, 1000,
                20000, 1500, 500, 50000, 20000
            ],

            "Quantity Sold": [
                2, 5, 10, 8, 1, 4, 6, 12, 7, 2,
                3, 5, 15, 1, 9, 4, 8, 10, 2, 6
            ]
        }

        df = pd.DataFrame(data)
        df["Total Sales"] = df["Price"] * df["Quantity Sold"]

        df.to_csv(file_path, index=False)

        print("\nCSV file created successfully!")
        print("File Name:", file_path)

    # Load and validate CSV
    def load_data(self, file_path):

        if not file_path.lower().endswith(".csv"):
            print("Invalid file format! Please use CSV.")
            return False

        if not os.path.exists(file_path):
            print("\nCSV file not found.")
            print("Creating sample dataset...")
            self.create_csv(file_path)

        try:
            df = pd.read_csv(file_path)

            required_columns = [
                "Date", "Product", "Category",
                "Price", "Quantity Sold"
            ]

            for column in required_columns:
                if column not in df.columns:
                    print("Missing column:", column)
                    return False

            if df.empty:
                print("CSV file is empty!")
                return False

            # Clean data
            df["Date"] = pd.to_datetime(
                df["Date"], errors="coerce"
            )

            df["Price"] = pd.to_numeric(
                df["Price"], errors="coerce"
            )

            df["Quantity Sold"] = pd.to_numeric(
                df["Quantity Sold"], errors="coerce"
            )

            df["Product"] = df["Product"].fillna("Unknown")
            df["Category"] = df["Category"].fillna("Unknown")

            df["Price"] = df["Price"].fillna(0)
            df["Quantity Sold"] = df["Quantity Sold"].fillna(0)

            # Remove invalid dates and negative values
            df = df.dropna(subset=["Date"])

            df = df[
                (df["Price"] >= 0) &
                (df["Quantity Sold"] >= 0)
            ]

            if df.empty:
                print("No valid records found!")
                return False

            # Create calculated column
            df["Total Sales"] = (
                df["Price"] * df["Quantity Sold"]
            )

            self.df = df

            print("\nDataset loaded successfully!")
            print("Total Records:", len(self.df))

            print("\nDataset Preview:")
            print(self.df.head())

            return True

        except (OSError, pd.errors.ParserError, UnicodeError, ValueError) as e:
            print("Error loading CSV:", e)
            return False

    # Calculate sales metrics
    def calculate_metrics(self):

        if self.df is None or self.df.empty:
            print("No data available!")
            return

        total_sales = self.df["Total Sales"].sum()

        average_sales = self.df["Total Sales"].mean()

        popular_product = (
            self.df.groupby("Product")["Quantity Sold"]
            .sum()
            .idxmax()
        )

        # NumPy operations
        sales_array = np.array(
            self.df["Total Sales"]
        )

        numpy_average = np.mean(sales_array)

        # Daily sales and growth
        daily_sales = (
            self.df.groupby("Date")["Total Sales"]
            .sum()
            .sort_index()
        )

        daily_array = np.array(daily_sales)

        if len(daily_array) > 1:
            previous = daily_array[:-1]
            current = daily_array[1:]

            growth = np.divide(
                current - previous,
                previous,
                out=np.zeros_like(current, dtype=float),
                where=previous != 0
            ) * 100

            average_growth = np.mean(growth)
        else:
            average_growth = 0

        print("\n========== SALES METRICS ==========")

        print("Total Sales:", round(total_sales, 2))
        print("Average Sales:", round(average_sales, 2))
        print("Most Popular Product:", popular_product)
        print("NumPy Average:", round(numpy_average, 2))
        print("Average Sales Growth:", round(average_growth, 2), "%")

        print("\nSales by Product:")
        print(
            self.df.groupby("Product")["Total Sales"].sum()
        )

        print("\nSales by Category:")
        print(
            self.df.groupby("Category")["Total Sales"].sum()
        )

        print("\nSales by Date:")
        print(daily_sales)

    # Filter sales data
    def filter_data(self):

        if self.df is None or self.df.empty:
            print("No data available!")
            return

        print("\n1. Filter by Category")
        print("2. Filter by Date Range")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\nAvailable Categories:")
            print(self.df["Category"].unique())

            category = input("Enter category: ").strip()

            result = self.df[
                self.df["Category"].str.lower()
                == category.lower()
            ]

        elif choice == "2":

            try:
                start = pd.to_datetime(
                    input("Enter Start Date (YYYY-MM-DD): ")
                )

                end = pd.to_datetime(
                    input("Enter End Date (YYYY-MM-DD): ")
                )

                if start > end:
                    print("Start date cannot be after end date!")
                    return

                result = self.df[
                    (self.df["Date"] >= start) &
                    (self.df["Date"] <= end)
                ]

            except (ValueError, TypeError):
                print("Invalid date format!")
                return

        else:
            print("Invalid choice!")
            return

        if result.empty:
            print("No matching records found!")
        else:
            print("\nFiltered Data:")
            print(result.to_string(index=False))

            print("\nFiltered Total Sales:")
            print(result["Total Sales"].sum())

    # Create all charts
    def create_charts(self):

        if self.df is None or self.df.empty:
            print("No data available!")
            return

        sns.set_theme(style="whitegrid")

        # 1. Bar Chart
        category_sales = (
            self.df.groupby("Category")["Total Sales"]
            .sum()
        )

        plt.figure(figsize=(9, 5))

        sns.barplot(
            x=category_sales.index,
            y=category_sales.values
        )

        plt.title("Total Sales by Product Category")
        plt.xlabel("Product Category")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.show()

        # 2. Line Graph
        daily_sales = (
            self.df.groupby("Date")["Total Sales"]
            .sum()
            .sort_index()
        )

        plt.figure(figsize=(10, 5))

        sns.lineplot(
            x=daily_sales.index,
            y=daily_sales.values,
            marker="o",
            label="Daily Sales"
        )

        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 3. Heatmap
        correlation = self.df[
            ["Price", "Quantity Sold"]
        ].corr()

        plt.figure(figsize=(7, 5))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Price and Quantity Correlation")
        plt.tight_layout()
        plt.show()

        print("\nAll charts created successfully!")

    # Save cleaned dataset
    def save_data(self, file_path):

        if self.df is not None:
            self.df.to_csv(file_path, index=False)
            print("\nCleaned CSV saved successfully!")


# Main Program
def main():

    print("=" * 45)
    print("       RETAIL SALES DATA ANALYZER")
    print("=" * 45)

    analyzer = RetailAnalyzer()

    while True:

        file_path = input(
            "\nEnter CSV file name (Press Enter for default): "
        ).strip()

        if file_path == "":
            file_path = "retail_sales.csv"

        if file_path.lower().endswith(".csv"):
            break

        print("Please enter a valid .csv file name!")

    # Load dataset
    if not analyzer.load_data(file_path):
        return

    # Automatic analysis and charts
    analyzer.calculate_metrics()
    analyzer.create_charts()

    # Menu
    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Calculate Sales Metrics")
        print("2. Filter Sales Data")
        print("3. Display Dataset")
        print("4. Create Charts")
        print("5. Save Cleaned CSV")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            analyzer.calculate_metrics()

        elif choice == "2":

            analyzer.filter_data()

        elif choice == "3":

            print(analyzer.df.to_string(index=False))

        elif choice == "4":

            analyzer.create_charts()

        elif choice == "5":

            analyzer.save_data(file_path)

        elif choice == "6":

            print("\nThank you for using Retail Sales Analyzer!")
            break

        else:

            print("Invalid choice! Please try again.")


# Run program
if __name__ == "__main__":
    main()