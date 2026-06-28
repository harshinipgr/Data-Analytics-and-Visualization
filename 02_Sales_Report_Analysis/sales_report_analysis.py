# Sales Report Analysis

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------
# Create output folder
# -------------------------------------------------

current_folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_folder, "output")
os.makedirs(output_folder, exist_ok=True)
# Read the CSV file from the same folder as this script
csv_path = os.path.join(current_folder, "sales_data.csv")
df = pd.read_csv(csv_path)
# -------------------------------------------------
# Read Dataset
# -------------------------------------------------


print("\nSales Dataset")
print(df)

# -------------------------------------------------
# Calculate Revenue
# -------------------------------------------------

df["Revenue"] = df["Quantity"] * df["Price"]

print("\nUpdated Sales Dataset")
print(df)

# -------------------------------------------------
# Basic Statistics
# -------------------------------------------------

print("\n========== SALES SUMMARY ==========")

print("Total Revenue : Rs.", df["Revenue"].sum())

print("Total Quantity Sold :", df["Quantity"].sum())

print("Average Product Price : Rs.", round(df["Price"].mean(),2))

print("Highest Price :", df["Price"].max())

print("Lowest Price :", df["Price"].min())

# -------------------------------------------------
# Highest Revenue Product
# -------------------------------------------------

highest = df.loc[df["Revenue"].idxmax()]

print("\nHighest Revenue Product")
print("---------------------------")
print("Product :", highest["Product"])
print("Revenue : Rs.", highest["Revenue"])

# -------------------------------------------------
# Revenue by Product
# -------------------------------------------------

product_revenue = df.groupby("Product")["Revenue"].sum()

print("\nRevenue by Product")
print(product_revenue)

# -------------------------------------------------
# Revenue by Month
# -------------------------------------------------

monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue")
print(monthly_revenue)

# -------------------------------------------------
# Revenue by Category
# -------------------------------------------------

category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nCategory Revenue")
print(category_revenue)

# -------------------------------------------------
# Save Report
# -------------------------------------------------

df.to_csv(os.path.join(output_folder, "sales_report.csv"), index=False)

# -------------------------------------------------
# Visualization 1
# Revenue by Product
# -------------------------------------------------

plt.figure(figsize=(8,5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(os.path.join(output_folder,"revenue_bar_chart.png"))

plt.show()
plt.close()

# -------------------------------------------------
# Visualization 2
# Monthly Revenue
# -------------------------------------------------

plt.figure(figsize=(8,5))

monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")

plt.tight_layout()

plt.savefig(os.path.join(output_folder,"monthly_revenue.png"))

plt.show()
plt.close()

# -------------------------------------------------
# Visualization 3
# Category Revenue
# -------------------------------------------------

plt.figure(figsize=(6,6))

category_revenue.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Category Revenue")
plt.ylabel("")

plt.tight_layout()

plt.savefig(os.path.join(output_folder,"category_pie_chart.png"))

plt.show()
plt.close()

print("\nSales report saved successfully!")