import pandas as pd
import numpy as np

# Column names matching your Tesla notebook cleaning logic
cols = [
    'Date', 'Year', '_Model_', '_Country_', '_State_', '_Deaths_', 
    '_Tesla Driver_', '_Tesla Occupant_', '_Other Vehicle_', '_Cyclists/ Peds_',
    '_Note_', '_Deceased 1_', '_Deceased 2_', 'Unnamed: 16'
]

# Generate 300 rows of synthetic crash data
np.random.seed(42)
dates = pd.date_range(start='2013-01-01', end='2023-12-31', periods=300)

data = {
    'Date': [d.strftime('%m/%d/%Y') for d in dates],
    'Year': [d.year for d in dates],
    '_Model_': np.random.choice(['3', 'S', 'X', 'Y', 'Other'], 300),
    '_Country_': np.random.choice(['USA', 'Germany', 'China', 'UK', 'Canada'], 300, p=[0.7, 0.1, 0.1, 0.05, 0.05]),
    '_State_': np.random.choice(['CA', 'TX', 'FL', 'NY', 'WA'], 300),
    '_Deaths_': np.random.choice([1, 2, 3], 300, p=[0.8, 0.15, 0.05]),
    '_Tesla Driver_': np.random.choice([0, 1], 300),
    '_Tesla Occupant_': np.random.choice([0, 1], 300),
    '_Other Vehicle_': np.random.choice([0, 1, 2], 300),
    '_Cyclists/ Peds_': np.random.choice([0, 1], 300),
    '_Note_': ['Dummy note' for _ in range(300)],
    '_Deceased 1_': ['Redacted' for _ in range(300)],
    '_Deceased 2_': ['Redacted' for _ in range(300)],
    'Unnamed: 16': [np.nan for _ in range(300)]
}

# Add one extra row at the top because your code does `df.iloc[1:295]`
# This ensures the filtering doesn't cut off actual data
df = pd.DataFrame(data)
empty_row = pd.DataFrame([[np.nan]*len(cols)], columns=cols)
df = pd.concat([empty_row, df], ignore_index=True)

df.to_csv('Tesla-Deaths.csv', index=False, encoding='latin1')
print("File 'Tesla-Deaths.csv' created successfully!")