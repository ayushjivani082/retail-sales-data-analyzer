# retail-sales-data-analyzer

CREAT BY : AYUSH JIVANI

LANGUAGE : PYTHON

REPOSITORIES LINK:https://github.com/ayushjivani082/retail-sales-data-analyzer/tree/f4c07682fc7c14873974e081785974c53eb0e653/Pra_Retail%20sales


Retail Sales Data Analyzer

Project Overview


Project Title: Retail Sales Data Analyzer
The Retail Sales Data Analyzer is a Python-based project that processes, analyzes, and visualizes retail sales data. It uses control structures, arrays, Object-Oriented Programming (OOP), NumPy, Pandas, Matplotlib, and Seaborn to calculate useful sales information and display trends through charts.
Objective
To develop a tool that can load a retail sales CSV file, validate and clean the data, calculate important sales metrics, filter records, and create visualizations that help understand sales performance.
Problem Statement
Build a Retail Sales Data Analyzer application that processes sales data, calculates key metrics, and visualizes trends. The project demonstrates data manipulation, object-oriented programming concepts, numerical calculations, and data visualization using Python libraries.
Features and Functionalities



1. Data Input and Control Structure Logic
Ask the user to provide a CSV file containing retail sales data.
Check the file format and required columns.
Use if-else statements and loops to validate data.
Identify missing or invalid entries.



2. Object-Oriented Programming
Create a RetailAnalyzer class to organize the project functionality.
The class should include these methods:
load_data(self, file_path): Reads the dataset using Pandas.
calculate_metrics(self): Calculates sales metrics such as total sales, average sales, and the most popular product.
filter_data(self): Filters sales records by category or date range.



3. Data Manipulation with NumPy and Pandas
NumPy - Perform numerical operations. - Calculate sales percentages and growth rates where the required data is available. - Use arrays for numerical computations such as average sales.
Pandas - Load and clean the CSV dataset. - Handle missing values. - Aggregate sales by product, category, and date. - Generate additional columns for computed metrics. - Filter and manipulate records.



4. Data Visualization
Create clear charts using Matplotlib and Seaborn:
Bar Chart: Total sales by product category.
Line Graph: Sales trend over time.
Heatmap: Correlation between product prices and quantities sold.
Charts should include suitable titles, axis labels, and legends where needed. Seaborn can be used to improve the visual appearance of the charts.
Dataset Details
Create or use a sample CSV file named retail_sales.csv with these columns:
Column            Description
Date            Sales date in YYYY-MM-DD format Product         Product name Category        Product category Price           Price of one item Quantity Sold   Number of items sold Total Sales     Total sales amount for the record
The Total Sales value can be calculated as:
Total Sales = Price * Quantity Sold
Make sure the CSV column names match the names used in the Python program.
Example Workflow
Input Validation: Ask the user to provide retail_sales.csv and validate its format and structure.
Data Loading: Load the dataset using the load_data() method.
Analysis and Metrics: Calculate total sales, average sales, and the most popular product using calculate_metrics().
Data Filtering: Allow filtering by product category or date range using filter_data().
Visualizations: Generate a category-wise bar chart, a sales-over-time line graph, and a heatmap.
Requirements
Install the required Python libraries before running the project:
pip install pandas numpy matplotlib seaborn
Python should also be installed on the computer.
Project Files
Keep these files together in one project folder:
Retail-Sales-Data-Analyzer/
│
├── retail_analyzer.py
├── retail_sales.csv
└── README.md
retail_analyzer.py --- Main Python program.
retail_sales.csv --- Dataset used for testing.
README.md --- Project description and setup instructions.
How to Run
Keep retail_analyzer.py and retail_sales.csv in the same folder, or provide the correct CSV file path when prompted.
Open a terminal in the project folder.
Install the required libraries.
Run:
python retail_analyzer.py
If you are using Jupyter Notebook, open the notebook and run its cells in order. The practical exam submission instructions shown in the source document specifically ask for a Python script named retail_analyzer.py.
Testing
Test the program with:
The sample retail_sales.csv dataset.
A CSV file containing missing values.
A CSV file with an incorrect or missing column.
Different categories and date ranges.
The program should show clear messages for invalid input and should not continue analysis when the required dataset structure is missing.
Expected Output
The program should display sales analysis results such as:
Total sales.
Average sales.
Most popular product.
Filtered sales records.
It should also generate:
Bar chart of total sales by category.
Line graph showing sales over time.
Heatmap showing the correlation between price and quantity sold.
Actual values and charts depend on the contents of the input CSV file.
Submission Checklist
[ ]
Python script named retail_analyzer.py.
[ ]
Dataset named retail_sales.csv.
[ ]
README file named README.md.
[ ]
Required libraries installed.
[ ]
Program tested with the sample dataset and edge cases.
[ ]
Charts have clear titles and labels.
Conclusion
The Retail Sales Data Analyzer combines Python programming, OOP, NumPy, Pandas, and data visualization. It helps organize retail sales data, calculate important metrics, filter records, and understand sales trends through charts.


A Python-based project to analyze retail sales data, calculate sales
metrics, filter records, and create visual charts.
Project Overview
Retail Sales Data Analyzer reads retail sales information from a CSV
file and performs basic data analysis. It uses Pandas and NumPy
for data handling and calculations, and Matplotlib and Seaborn
to create charts.

If the CSV file does not exist, the program creates a sample dataset
automatically.
Features
- Create a sample retail sales CSV file.
- Load and validate CSV data.
- Clean missing or invalid values.
- Calculate total sales and average sales.
- Find the most popular product.
- Calculate average sales growth.
- Display sales by product, category, and date.
- Filter sales by product category or date range.
- Generate visualizations:
  - Bar chart: Total sales by category
  - Line graph: Daily sales trend
  - Heatmap: Price and quantity correlation
- Save the cleaned dataset as a CSV file.
- Use a menu-driven interface.
Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
Project Structure
Retail-Sales-Data-Analyzer/
│
├── retail_sales_analyzer.py
├── retail_sales.csv          # Created automatically if it does not exist
└── README.md
Installation
Make sure Python is installed on your computer.

Install the required libraries using the terminal:
pip install pandas numpy matplotlib seaborn
How to Run
1. Download or clone this project.
2. Open the project folder in VS Code or another Python editor.
3. Open the terminal in the project folder.
4. Run the Python file:
python retail_sales_analyzer.py
5. Enter a CSV filename when prompted, or press Enter to use the
   default file retail_sales.csv.
6. Use the menu to select the required operation.
Main Menu
  Option   Description
  1        Calculate Sales Metrics
2        Filter Sales Data
3        Display Dataset
4        Create Charts
5        Save Cleaned CSV
6        Exit
Dataset Information
The sample dataset contains these columns:

  Column          Description
  Date            Date of the sale
Product         Product name
Category        Product category
Price           Price of one item
Quantity Sold   Number of items sold
Total Sales     Price multiplied by quantity sold

Total Sales Formula:
Total Sales = Price × Quantity Sold
Charts
The project generates three charts to help understand the sales data:
1. Bar Chart -- compares total sales across product categories.
2. Line Graph -- shows how sales change over different dates.
3. Heatmap -- displays the correlation between price and quantity
   sold.
Concepts Covered
- Python classes and objects
- Functions and methods
- Conditional statements and loops
- File handling
- Exception handling
- CSV data processing
- Pandas DataFrames and grouping
- NumPy arrays and calculations
- Data cleaning and filtering
- Data visualization
