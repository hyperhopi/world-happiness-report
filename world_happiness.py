import pandas as pd

file_path = 'World-happiness-report-v2024.csv'

# READ CSV FILE (OBS! encoding='latin1' is used to read the file correctly)!
df = pd.read_csv(file_path, encoding='latin1')

print(df.head())