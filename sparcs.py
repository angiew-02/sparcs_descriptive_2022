import pandas as pd

url_nassau = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=500000'
url_suffolk = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Suffolk&$limit=500000'

nassau_df = pd.read_csv(url_nassau)
len(nassau_df)

suffolk_df = pd.read_csv(url_suffolk)
len(suffolk_df)

merged = pd.concat([nassau_df, suffolk_df])

len(merged)

print(merged)

### Loading the Data 
value_counts = merged['length_of_stay'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['age_group'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['gender'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_charges'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_costs'].value_counts() 
print("Value Counts:\n", value_counts)
value_counts = merged['type_of_admission'].value_counts()
print("Value Counts:\n", value_counts)

### Basic Descriptive Statistics 
import numpy as np

# Data 
length_of_stay = np.array([74085, 66479, 49343, 33418, 23726])
total_charges = np.array([9203.04, 15082.10, 17690.10, 14587.88, 15611.25])
total_costs = np.array([2384.85, 1743.66, 1924.39, 4825.86, 3011.89])

# Function to calculate and print basic statistics
def calculate_statistics(data, label):
    print(f"Statistics for {label}:")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    print(f"25th Percentile: {np.percentile(data, 25)}")
    print(f"50th Percentile (Median): {np.percentile(data, 50)}")
    print(f"75th Percentile: {np.percentile(data, 75)}")
    print(f"Quartiles: {np.percentile(data, [25, 50, 75])}")
    print("\n")

# Calculate statistics for each dataset
calculate_statistics(length_of_stay, "Length of Stay")
calculate_statistics(total_charges, "Total Charges")
calculate_statistics(total_costs, "Total Costs")

# Exploring Categorical Variables 

import pandas as pd
import matplotlib.pyplot as plt

# Data for Age Group, Gender, and Type of Admission
data = {
    'Age Group': ['0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older','0 to 17'],
    'Gender': ['M', 'F', 'U','M', 'F', 'U','M', 'F', 'U'],
    'Type of Admission': ['Emergency', 'Elective', 'Newborn', 'Urgent', 'Trauma', 'Not Available']
}

df = pd.DataFrame(data)

# Plot distribution of a categorical variable
def plot_distribution(df, column):
    count = df[column].value_counts()
    count.plot(kind='bar', color='blue')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Plot distributions for Age Group, Gender, and Type of Admission
plot_distribution(df, 'Age Group')
plot_distribution(df, 'Gender')
plot_distribution(df, 'Type of Admission')

### Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data 
data = {
    'Length of Stay': [74085, 66479, 49343, 33418, 23726],
    'Total Charges': [9203.04, 15082.10, 17690.10, 14587.88, 15611.25],
    'Type of Admission': ['Emergency', 'Elective', 'Newborn', 'Urgent', 'Trauma', 'Not Available']
}

df = pd.DataFrame(data)

# 1. Histogram of Length of Stay
plt.figure(figsize=(10,6))
plt.hist(df['Length of Stay'], bins=1000, color='blue', edgecolor='black')
plt.title('Histogram of Length of Stay')
plt.xlabel('Length of Stay (days)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# 2. Boxplot for Total Charges
plt.figure(figsize=(10,6))
sns.boxplot(y=df['Total Charges'], color='green')
plt.title('Boxplot of Total Charges')
plt.ylabel('Total Charges ($)')
plt.grid(axis='y')
plt.show()

# 3. Bar plot for Type of Admission
plt.figure(figsize=(10, 6))
admission_counts = df['Type of Admission'].value_counts()
admission_counts.plot(kind='bar', color='red')
plt.title('Bar Plot of Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

### Handling Missing Data 
data = {
    'Length of Stay': [74085, 66479, 49343, 33418, 23726],
    'Total Charges': [9203.04, 15082.10, 17690.10, 14587.88, 15611.25],
    'Type of Admission': ['Emergency', 'Elective', 'Newborn', 'Urgent', 'Trauma', 'Not Available']
}

df = pd.DataFrame(data)

# Check for missing data
print("Missing data in each column:")
print(df.isnull().sum())

# Drop rows with missing data
df_dropped = df.dropna()
print("\nData after dropping rows with missing data:")
print(df_dropped)

### Summary Report 
# Having trouble creating a box plot as well as other visualizations. Was able to successfully install matplotlib and seaborn however when I went to run the code, it gives me error of 'arrays not being of the same length' so I then adjusted the length but was still giving me the same error message. 
#What is the average length of stay? 
    # The avergae length of stay is 49410.2
#How does the total cost vary by age group or type of admission?
    # The increase in age the lower the cost. The more sereve the type of admission is the higher the cost 
#Any noticeable trends in admissions or charges?
    # As admissions increase charges will increase 