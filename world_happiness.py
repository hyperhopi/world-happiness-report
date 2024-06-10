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

# plt.subplot(3, 3, 1)
# sns.lineplot(x='year', y='Life Ladder', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Life Ladder Over Years')
# plt.xlabel('Year')
# plt.ylabel('Life Ladder')
# # Format x-axis
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 2.Log GDP per capita
# plt.subplot(3, 3, 2)
# sns.lineplot(x='year', y='Log GDP per capita', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Log GDP per capita Over Years')
# plt.xlabel('Year')
# plt.ylabel('Log GDP per capita')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 3.Social support
# plt.subplot(3, 3, 3)
# sns.lineplot(x='year', y='Social support', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Social support Over Years')
# plt.xlabel('Year')
# plt.ylabel('Social support')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 4.Freedom to make life choices
# plt.subplot(3, 3, 4)
# sns.lineplot(x='year', y='Freedom to make life choices', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Freedom to make life choices Over Years')
# plt.xlabel('Year')
# plt.ylabel('Freedom to make life choices')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 5.Generosity
# plt.subplot(3, 3, 5)
# sns.lineplot(x='year', y='Generosity', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Generosity Over Years')
# plt.xlabel('Year')
# plt.ylabel('Generosity')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 6.Perceptions of corruption
# plt.subplot(3, 3, 6)
# sns.lineplot(x='year', y='Perceptions of corruption', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Perceptions of corruption Over Years')
# plt.xlabel('Year')
# plt.ylabel('Perceptions of corruption')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

# # 7.Healthy life expectancy at birth
# plt.subplot(3, 3, 7)
# sns.lineplot(x='year', y='Healthy life expectancy at birth', hue='Country name', data=df_prepared, marker='o', palette=palette)
# plt.title('Healthy life expectancy at birth Over Years')
# plt.xlabel('Year')
# plt.ylabel('Healthy life expectancy at birth')
# plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

plt.tight_layout()
plt.show()