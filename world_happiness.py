import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    'Freedom to make life choices': df_filtered['Freedom to make life choices'].tolist(),
    'Generosity': df_filtered['Generosity'].tolist(),
    'Perceptions of corruption': df_filtered['Perceptions of corruption'].tolist(),
    'Healthy life expectancy at birth': df_filtered['Healthy life expectancy at birth'].tolist()
}

df_prepared = pd.DataFrame(data)

# Save changes to a new CSV file
output_file_path = 'world_happiness_filtered.csv'
df_prepared.to_csv(output_file_path, index=False)

print(df_prepared.head())

# Plotting
plt.figure(figsize=(18, 12))
# Color palette
palette = {"Spain": "#AD1519", "Sweden": "#006AA7"}

# 1. Life Ladder
plt.subplot(3, 3, 1)
sns.lineplot(x='year', y='Life Ladder', hue='Country name', data=df_prepared, marker='o', palette=palette)
plt.title('Life Ladder Over Years')
plt.xlabel('Year')
plt.ylabel('Life Ladder')
# Format x-axis
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

plt.tight_layout()
plt.show()