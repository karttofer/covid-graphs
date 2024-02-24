import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob
plt.style.use('tableau-colorblind10')

file_pattern = './covid__history/*.csv'
file_list = glob.glob(file_pattern)

dfs = []

for file in file_list:
    df = pd.read_csv(file)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

combined_df['date'] = pd.to_datetime(combined_df['date'])

# Create a line plot for specific columns
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='deathConfirmed', data=combined_df, label="Deaths Confirmed")
sns.lineplot(x='date', y='hospitalizedCurrently', data=combined_df, label="Currently Hospitalized")
sns.lineplot(x='date', y='deathProbable', data=combined_df, label="Death Probable")
plt.title('Covid Time Lapse From covidtracking')
plt.xlabel('Date')
plt.ylabel('Results')
plt.legend(title='Legend')
plt.show()