import pandas as pd
import numpy as np

# Set up the file to write to
filename = "numbers.csv"

# Generate a range of numbers from 1 to 1,000,000,000
numbers = np.arange(1, 1000000001)

# Create a DataFrame and write it to a CSV file
df = pd.DataFrame(numbers, columns=['id'])

# Write the DataFrame to CSV, no index column
df.to_csv(filename, index=False)

print(f"CSV file '{filename}' has been created.")


