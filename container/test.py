import pandas as pd

result_rf = pd.read_csv('./src/output/result.csv')
print(result_rf.Exited.value_counts())

print('*'*79)

result_gb = pd.read_csv('./src/output_gb/result.csv')
print(result_gb.Exited.value_counts())