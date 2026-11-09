import pandas as pd

data = {
    'Name': ['Sarwar', 'Tamim', 'Rupom', 'Munna'],
    'Age': [22, 21, 22, 23],
    'Marks': [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print(df)
print(type(data))
print(type(df))