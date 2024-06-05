import pandas as pd
import numpy as np
from scipy.stats import linregress

# 读取 Excel 文件
file_path = '../sheet/od_by_tm1.xlsx'
df = pd.read_excel(file_path)

# 数据分析
price_col = '产品价格'
demand_col = '订单需求量'

min_price = df[price_col].min()
max_price = df[price_col].max()
avg_price = df[price_col].mean()
std_dev_price = df[price_col].std()

slope, intercept, rvalue, _, _ = linregress(df[price_col], df[demand_col])

# 输出结果
print('产品价格统计信息：')
print(f'最小值：{min_price}')
print(f'最大值：{max_price}')
print(f'平均值：{avg_price}')
print(f'标准差：{std_dev_price}')
print('价格与需求量回归分析结果：')
print(f'斜率：{slope}')
print(f'截距：{intercept}')
print(f'相关系数：{rvalue}')