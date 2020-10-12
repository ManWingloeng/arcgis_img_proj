import pandas as pd

result = pd.read_csv('result.csv')
result['Name'] = ['ABLE'] * len(result)
result.to_csv('result_name.csv', index=False)
