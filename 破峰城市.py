import pandas as pd
# 加载Excel文件
file_path = 'C:/Users/文/Desktop/华南大区订单跟进0911.xlsx'
order_tracking_df = pd.read_excel(file_path, sheet_name='订单跟进')
peak_calendar_df = pd.read_excel(file_path, sheet_name='破峰日历')

# 第二步：检查并转换破峰日历表的列名（将数字列转换为日期）
# 假设这些数字列是Excel的日期编码，先将列名转换为数值类型
numeric_columns = pd.to_numeric(peak_calendar_df.columns[3:], errors='coerce')  # 假设第3列开始是日期数字编码

# 将这些数字列转换为日期格式 (Excel 日期从 1899-12-30 开始)
converted_dates = pd.to_datetime(numeric_columns, unit='D', origin='1899-12-30')  # 修正为 'D' 而不是 'd'

# 更新这些列名为日期格式
peak_calendar_df.columns = list(peak_calendar_df.columns[:3]) + list(converted_dates)

# 输出转换后的列名，确认日期转换是否正确
print("转换后的列名：", peak_calendar_df.columns)

# 第三步：确保订单跟进表中的数据列是数值类型
order_tracking_df['绩效K'] = pd.to_numeric(order_tracking_df.iloc[:, 10], errors='coerce')  # K列为每日绩效1
order_tracking_df['绩效L'] = pd.to_numeric(order_tracking_df.iloc[:, 11], errors='coerce')  # L列为每日绩效2
order_tracking_df['23年峰值'] = pd.to_numeric(order_tracking_df.iloc[:, 16], errors='coerce')  # Q列为23年峰值
order_tracking_df['9月目标'] = pd.to_numeric(order_tracking_df.iloc[:, 18], errors='coerce')  # S列为9月目标

# 第四步：检查每日的绩效是否超过23年峰值或9月目标
order_tracking_df['超出目标'] = (order_tracking_df['绩效K'] > order_tracking_df['23年峰值']) | (
            order_tracking_df['绩效L'] > order_tracking_df['9月目标'])

# 筛选出超出目标的城市和日期
exceeded_cities = order_tracking_df[order_tracking_df['超出目标']][['Unnamed: 2', 'T-1']]  # Unnamed: 2 是城市名列, T-1 是日期列

# 第五步：将超出目标的城市写入破峰日历表
for date in exceeded_cities['T-1'].unique():
    cities_for_day = exceeded_cities[exceeded_cities['T-1'] == date]['Unnamed: 2'].tolist()
    cities_str = ', '.join(cities_for_day)

    # 查找日期列并更新该列的数据
    if date in peak_calendar_df.columns:
        peak_calendar_df.loc[:, date] = cities_str

# 保存更新后的破峰日历表
peak_calendar_df.to_excel('更新后的破峰日历1.xlsx', index=False)
print("破峰日历已成功更新，并保存为 '更新后的破峰日历.xlsx' 文件。")