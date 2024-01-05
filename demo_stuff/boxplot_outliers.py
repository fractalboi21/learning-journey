import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with some numerical data (including outliers)
data = {'A': [80, 83, 81, 92, 95, 96, 87, 108, 97, 98,105,110,120,86,75,140]}
df = pd.DataFrame(data)

# Create a box plot
plt.boxplot(df.values, labels=df.columns)
plt.title('Box Plot with Outliers')
plt.xlabel('Columns')
plt.ylabel('Values')

# Highlight potential outliers with red color
outliers = dict(markerfacecolor='red', markersize=8, marker='o', linestyle='none')
plt.boxplot(df.values, labels=df.columns, flierprops=outliers)

plt.show()

df_outlier1 = df[df['Length']> 216].copy()
print(Counter(df_outlier1['conterfeit']))

df_outlier2 = df[df['Length']> 215.5].copy()
print(Counter(df_outlier2['conterfeit']))