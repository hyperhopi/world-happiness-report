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

def plot_graph(subplot_index, x, y, title, xlabel, ylabel, data, palette):
    plt.subplot(3, 3, subplot_index)
    sns.lineplot(x=x, y=y, hue='Country name', data=data, marker='o', palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
    
# 1.Life Ladder
plot_graph(1, 'year', 'Life Ladder', 'Life Ladder Over Years', 'Year', 'Life Ladder', df_prepared, palette)
# 2.Log GDP per capita
plot_graph(2, 'year', 'Log GDP per capita', 'Log GDP per capita Over Years', 'Year', 'Log GDP per capita', df_prepared, palette)
# 3.Social support
plot_graph(3, 'year', 'Social support', 'Social support Over Years', 'Year', 'Social support', df_prepared, palette)
# 4.Freedom to make life choices
plot_graph(4, 'year', 'Freedom to make life choices', 'Freedom to make life choices Over Years', 'Year', 'Freedom to make life choices', df_prepared, palette)
# 5.Generosity
plot_graph(5, 'year', 'Generosity', 'Generosity Over Years', 'Year', 'Generosity', df_prepared, palette)
# 6.Perceptions of corruption
plot_graph(6, 'year', 'Perceptions of corruption', 'Perceptions of corruption Over Years', 'Year', 'Perceptions of corruption', df_prepared, palette)
# 7.Healthy life expectancy at birth
plot_graph(7, 'year', 'Healthy life expectancy at birth', 'Healthy life expectancy at birth Over Years', 'Year', 'Healthy life expectancy at birth', df_prepared, palette)

plt.tight_layout()
plt.show()