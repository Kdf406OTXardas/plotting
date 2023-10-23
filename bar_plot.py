import import_file
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

df_work = import_file.df[::]

# подготовка датасета к графику (выбор соотношенеи времени при pyOpenCL/pyCuda)
df_pycuda = df_work.loc[df_work['device'] == 'pyCuda', ['number', 'time']]
df_pyopencl = df_work.loc[df_work['device'] == 'pyOpenCL', ['number', 'time']]

df_pycuda.rename(columns={'time': 'time_pyCuda'}, inplace=True)
df_pyopencl.rename(columns={'time': 'time_pyOpenCL'}, inplace=True)

print(df_pycuda)
print(df_pyopencl)

df_comparison = df_pycuda.merge(df_pyopencl, left_on='number', right_on='number')
df_comparison['number'] = df_comparison['number'].apply(lambda x: round(math.log(x, 10)), 2)

df_comparison['pyOpenCl / pycuda, %'] = (
    round(abs(df_comparison['time_pyCuda'] - df_comparison['time_pyOpenCL']) /
              df_comparison['time_pyCuda'] * 100
          , 2)
)

df_comparison.drop(columns=['time_pyOpenCL', 'time_pyCuda'], inplace=True)
df_comparison.rename(columns={'number': 'log10(number_points)'}, inplace=True)

print(df_comparison)

sns.barplot(data=df_comparison, y='pyOpenCl / pycuda, %', x='log10(number_points)')
plt.show()