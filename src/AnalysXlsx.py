import pandas as pd
import numpy as np
from scipy.stats import linregress

file_path = '../sheet/od_by_tm1.xlsx'
file_path2 = '../sheet/order_train1_pre.xlsx'
df = pd.read_excel(file_path)
df2 = pd.read_excel(file_path2)
price_col = '产品价格'
demand_col = '订单需求量'
min_price = df[price_col].min()
min_price2 = df2[price_col].min()
max_price = df[price_col].max()
max_price2 = df2[price_col].max()
avg_price = df[price_col].mean()
avg_price2 = df2[price_col].mean()
std_dev_price = df[price_col].std()
std_dev_price2 = df2[price_col].std()
slope, intercept, rvalue, _, _ = linregress(df[price_col], df[demand_col])
slope2, intercept2, rvalue2, _, _ = linregress(df2[price_col], df2[demand_col])
print('基于od_by_tm1.xlsx的产品价格统计信息：')
print(f'最小值：{min_price}')
print(f'最大值：{max_price}')
print(f'平均值：{avg_price}')
print(f'标准差：{std_dev_price}')
print('价格与需求量回归分析结果：')
print(f'斜率：{slope}')
print(f'截距：{intercept}')
print(f'相关系数：{rvalue}')
print('\n基于order_train1_pre.xlsx的产品价格统计信息：')
print(f'最小值：{min_price2}')
print(f'最大值：{max_price2}')
print(f'平均值：{avg_price2}')
print(f'标准差：{std_dev_price2}')
print('价格与需求量回归分析结果：')
print(f'斜率：{slope2}')
print(f'截距：{intercept2}')
print(f'相关系数：{rvalue2}')
