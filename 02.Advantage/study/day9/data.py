import pandas as pd

data = {
    'Tên sản phẩm': ['Sp1', 'Sp2', 'Sp3'],
    'Giá sản phẩm (USD)': [10, 20, 30],
    'Số lượng tồn kho': [50, 30, 45]
}

df = pd.DataFrame(data)
df.to_csv('products.csv', index=False)
df.to_excel('products.xlsx', index=False)

print(df.head())
print(df.dtypes)