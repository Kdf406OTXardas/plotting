import import_file
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

df_work = import_file.df[::]

print(df_work)

df_work['time'] = df_work['time'].apply(lambda x: math.log(x, 10))
df_work['number'] = df_work['number'].apply(lambda x: math.log(x, 10))

sns.scatterplot(x='time', y='number', hue='device', data=df_work)

plt.show()
