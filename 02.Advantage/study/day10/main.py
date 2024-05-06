import pandas as pd
# Tạo một DataFrame về thông tin nhân viên
data = {
'ID': [1, 2, 3, 4, 5],
'Tên nhân viên': ['An', 'Bình', 'Chi', 'Dũng', 'Hạnh'],
'Tuổi': [30, 25, 35, 40, 28],
'Giới tính': ['Nam', 'Nam', 'Nữ', 'Nam', 'Nữ'],
'Phòng ban': ['Kế toán', 'Kinh doanh', 'Nhân sự', 'Kỹ thuật', 'Marketing'],
'Lương (USD)': [3000, 3500, 4000, 4500, 3200]
}
df = pd.DataFrame(data)
print("DataFrame về thông tin nhân viên:")
print(df)

#=================================================================================

# 1) 

employeesover30 = df[df['Tuổi'] > 30]['Tên nhân viên']
print("Nhân viên có tuổi lớn hơn 30:", list(employeesover30))

 

hse = df[df['Lương (USD)'] == df['Lương (USD)'].max()]['Tên nhân viên'].values[0]
lse = df[df['Lương (USD)'] == df['Lương (USD)'].min()]['Tên nhân viên'].values[0]
print("Nhân viên có mức lương cao nhất:", hse)
print("Nhân viên có mức lương thấp nhất:", lse)

# 4)

gendercounts = df['Giới tính'].value_counts()
print("Số lượng nhân viên nam và nữ trong công ty:")
print(gendercounts)

# 5)

employees_in_sales_department = df[df['Phòng ban'] == 'Kinh doanh']['Tên nhân viên']
print("Nhân viên làm việc trong phòng ban Kinh doanh:", list(employees_in_sales_department))

# 6)

df_sorted_by_age = df.sort_values(by='Tuổi')
print("Sắp xếp theo tuổi tăng dần:")
print(df_sorted_by_age)

# 7)

new = {'ID': 6, 'Tên nhân viên': 'Trung', 'Tuổi': 17, 'Giới tính': 'Nam', 'Phòng ban': 'Kinh doanh', 'Lương (USD)': 90000}
df = pd.concat([df,pd.DataFrame([new])], ignore_index=True)
print("Thêm một nhân viên mới:")
print(df)

# 8)

df = df[df['ID'] != 3]
print("Xoá nhân viên có ID là 3:")
print(df)

# 9)

averangeunder30 = df[df['Tuổi'] < 30]['Lương (USD)'].mean()
print("Mức lương trung bình của những nhân viên có tuổi dưới 30:", averangeunder30)

# 10)

stats = df.groupby('Phòng ban')['Lương (USD)'].sum()
hsd = stats.idxmax()
lsd = stats.idxmin()
print("Phòng ban có tổng mức lương cao nhất:", hsd)
print("Phòng ban có tổng mức lương thấp nhất:", lsd)