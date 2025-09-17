# -----------------------------------------------------
# Ubuntu-Inspired Data Analysis Assignment 🌍
# Objective:
# - Load and analyze a dataset using pandas
# - Create simple plots with matplotlib
# -----------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -----------------------------------------------------
# Task 1: Load and Explore the Dataset
# -----------------------------------------------------

try:
    # Load the Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # pandas DataFrame

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("First 5 rows of dataset:")
    print(df.head(), "\n")

    # Info about dataset
    print("Dataset Info:")
    print(df.info(), "\n")

    # Check missing values
    print("Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (Iris has no missing values, but let’s show method)
    df = df.dropna()

except FileNotFoundError:
    print("⚠️ File not found. Please check dataset path.")
except Exception as e:
    print("⚠️ An error occurred while loading dataset:", e)


# -----------------------------------------------------
# Task 2: Basic Data Analysis
# -----------------------------------------------------

# Basic statistics
print("Descriptive Statistics:")
print(df.describe(), "\n")

# Group by species and calculate mean of numeric columns
grouped_means = df.groupby("target").mean()
print("Average values per species:")
print(grouped_means, "\n")

# Observations
print("🔎 Observations: Sepal length and petal dimensions differ significantly by species.\n")


# -----------------------------------------------------
# Task 3: Data Visualization
# -----------------------------------------------------

# Set seaborn style
sns.set(style="whitegrid")

# 1. Line Chart (trend of sepal length across samples)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x=df["target"], y=df["petal length (cm)"], ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species (0=setosa,1=versicolor,2=virginica)")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (sepal length vs. petal length)
plt.figure(figsize=(8,5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Scatter Plot: Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

print("✅ Visualizations complete!")
