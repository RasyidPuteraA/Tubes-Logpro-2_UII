import pandas as pd
import numpy as np
import quick_sort
import partition

# Load the data set from a CSV file
df = pd.read_csv('tourism_with_id.csv')

# Convert the Pandas DataFrame to a NumPy array
data = df.to_numpy()

# Sort the data set using quick sort
quick_sort.quick_sort(data, 0, len(data)-1)

# Create a Pandas DataFrame from the sorted data set
df_sorted = pd.DataFrame(data, columns=['city1', 'city2', 'price', 'distance'])

# Print the first five rows of the sorted data set
print(df_sorted.head(5))

# Calculate the mean, median, and standard deviation of the "price" column
mean = df_sorted['price'].mean()
median = df_sorted['price'].median()
std = df_sorted['price'].std()

# Print the statistical summary
print(f'Mean: {mean:.2f}')
print(f'Median: {median:.2f}')
print(f'Standard deviation: {std:.2f}')

# Save the sorted data set to a CSV file
df_sorted.to_csv('sorted_data.csv', index=False)
