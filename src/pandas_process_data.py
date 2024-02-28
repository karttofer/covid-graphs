import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

file_pattern = './covid__history/*.csv'
file_list = glob.glob(file_pattern)

dfs = []

for file in file_list:
    df = pd.read_csv(file, chunksize=1000)
    df.fillna(0, inplace=True)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
combined_df['date'] = pd.to_datetime(combined_df['date'])
combined_df['death'] = pd.to_numeric(combined_df['death'])


# Apply Graphics
sns.set_theme()
df = combined_df
sns.relplot(
    data=df,
    x="date", y="death", 
    hue="death", style="death",
)
plt.yscale('log')
plt.show()