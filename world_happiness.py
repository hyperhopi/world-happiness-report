import pandas as pd

file_path = 'World-happiness-report-v2024.csv'

# READ CSV FILE (OBS! encoding='latin1' is used to read the file correctly)!
df = pd.read_csv(file_path, encoding='latin1')

# print(df.head())

# Filter the data (only SPAIN and SWEDEN)
df_filtered = df[(df['Country name'] == 'Spain') | (df['Country name'] == 'Sweden')]
# Choose explicit columns
df_filtered = df_filtered[['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Freedom to make life choices','Generosity','Perceptions of corruption','Healthy life expectancy at birth']]


# print(df_filtered)

# Save the filtered data to a new CSV file
data = {
    'Country name': df_filtered['Country name'].tolist(),
    'year': df_filtered['year'].tolist(),
    'Life Ladder': df_filtered['Life Ladder'].tolist(),
    'Log GDP per capita': df_filtered['Log GDP per capita'].tolist(),
    'Social support': df_filtered['Social support'].tolist(),
    'Healthy life expectancy at birth': df_filtered['Healthy life expectancy at birth'].tolist()
}

df_prepared = pd.DataFrame(data)
print(df_prepared.head())
