# Weather Report Analysis

import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------
# Project Folder
# --------------------------------------------

current_folder = os.path.dirname(os.path.abspath(__file__))

output_folder = os.path.join(current_folder, "output")

os.makedirs(output_folder, exist_ok=True)

# --------------------------------------------
# Read CSV
# --------------------------------------------

csv_path = os.path.join(current_folder, "weather_data.csv")

df = pd.read_csv(csv_path)

print("\nWeather Dataset\n")
print(df)

# --------------------------------------------
# Weather Statistics
# --------------------------------------------

print("\n========== WEATHER SUMMARY ==========\n")

print("Average Temperature :", round(df["Temperature"].mean(),2), "°C")

print("Highest Temperature :", df["Temperature"].max(), "°C")

print("Lowest Temperature :", df["Temperature"].min(), "°C")

print("Average Humidity :", round(df["Humidity"].mean(),2), "%")

print("Maximum Rainfall :", df["Rainfall"].max(), "mm")

print("Average Wind Speed :", round(df["WindSpeed"].mean(),2), "km/h")

# --------------------------------------------
# Hottest Day
# --------------------------------------------

hottest = df.loc[df["Temperature"].idxmax()]

print("\nHottest Day")

print("----------------------")

print("Day :", hottest["Day"])

print("Temperature :", hottest["Temperature"], "°C")

# --------------------------------------------
# Coolest Day
# --------------------------------------------

coolest = df.loc[df["Temperature"].idxmin()]

print("\nCoolest Day")

print("----------------------")

print("Day :", coolest["Day"])

print("Temperature :", coolest["Temperature"], "°C")

# --------------------------------------------
# Save Report
# --------------------------------------------

report_path = os.path.join(output_folder, "weather_report.csv")

df.to_csv(report_path, index=False)

# --------------------------------------------
# Graph 1
# Temperature Trend
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(df["Day"], df["Temperature"], marker="o")

plt.title("Temperature Trend")

plt.xlabel("Day")

plt.ylabel("Temperature (°C)")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "temperature_trend.png"))

plt.show()

plt.close()

# --------------------------------------------
# Graph 2
# Humidity
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(df["Day"], df["Humidity"])

plt.title("Humidity Analysis")

plt.xlabel("Day")

plt.ylabel("Humidity (%)")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "humidity_bar_chart.png"))

plt.show()

plt.close()

# --------------------------------------------
# Graph 3
# Rainfall
# --------------------------------------------

plt.figure(figsize=(6,6))

plt.pie(
    df["Rainfall"],
    labels=df["Day"],
    autopct="%1.1f%%"
)

plt.title("Rainfall Distribution")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "rainfall_pie_chart.png"))

plt.show()

plt.close()

# --------------------------------------------
# Graph 4
# Temperature Distribution
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(df["Temperature"], bins=5)

plt.title("Temperature Distribution")

plt.xlabel("Temperature (°C)")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(os.path.join(output_folder, "temperature_histogram.png"))

plt.show()

plt.close()

print("\nWeather report generated successfully!")