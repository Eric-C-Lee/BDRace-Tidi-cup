import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#读取数据
data = pd.read_excel('../sheet/od_by_tm1.xlsx')

# #First.产品的不同价格对需求量的影响
# plt.scatter(data['产品价格'], data['订单需求量'])
# plt.xlabel('Product Price')
# plt.ylabel('Order Demand')
# plt.title('Price vs Demand')
# plt.show()
#
# #Second.产品所在区域对需求量的影响，以及不同区域的产品需求量有何特性
# plt.bar(data['销售区域代码'], data['订单需求量'])
# plt.xlabel('Sales Region')
# plt.ylabel('Order Demand')
# plt.title('Demand in Different Sales Regions')
# plt.show()

# #Third.不同销售方式（线上和线下）的产品需求量的特性
# # 按销售渠道名称分组并计算统计量
# grouped = data.groupby('销售渠道名称')['订单需求量']
# result = grouped.agg(['mean', 'median', 'var'])
#
# # 可视化结果
# result.plot(kind='bar')
# plt.show()

# #Fourth.不同品类之间的产品需求量有何不同点和共同点
# df_product = data.groupby(['产品大类编码','产品细分编码']).agg(
#     {'订单需求量': ['mean', 'sum']}).reset_index()

# # 绘制分类汇总的条形图
# plt.figure(figsize=(12,6))
# plt.title("Products by Categories", fontsize=14)
# plt.xlabel("categories")
# plt.ylabel("total sales quantity")
# df_product.plot(x=('产品大类编码', ''), y=[('订单需求量', 'mean'), ('订单需求量', 'sum')],
#                 kind='bar', ax=plt.gca())
# plt.legend(["Average Demand Quantity", "Total Sales Quantity"])
# plt.xticks(rotation=45)
# plt.show()

# #Five.不同时间段（例如月头、月中、月末等）产品需求量有何特性
# data['日期'] = pd.to_datetime(data['日期'])
# data['Month'] = data['日期'].dt.month
# df_time = data.groupby('Month').agg({'订单需求量':'sum'}).reset_index()
#
# # 绘制月份和订单需求量的线图
# plt.figure(figsize=(8,4))
# plt.title("Demand Quantity by Month", fontsize=14)
# plt.xlabel("Month")
# plt.ylabel("Demand Quantity")
# plt.plot(df_time['Month'], df_time['订单需求量'], linestyle='-', marker='o')
# plt.xticks(df_time['Month'])
# plt.show()

# #Six.节假日对产品需求量的影响
# # 根据“节假日和工作日”这一列来筛选出值为“节假日”的行，并统计每个产品的订单需求量总数
# holiday_data = data[data['节假日和工作日'] == '节假日'].groupby(['产品编码'], as_index=False)['订单需求量'].sum()

# # 合并原始数据集和节假日订单需求量数据集
# merged_data = data.merge(holiday_data, on='产品编码', how='left')

# # 根据“节假日和工作日”这一列来创建一个新的列，“是否为节假日”，将该列的值设置为true或false
# merged_data['是否为节假日'] = merged_data['节假日和工作日'] == '节假日'

# # 使用seaborn的barplot绘制条形图，展示节假日对于销售产品数的影响。
# sns.barplot(x='是否为节假日', y='订单需求量_y', data=merged_data)

# # 显示图形
# plt.show()


# #Seven.促销（如618、双十一等）对产品需求量的影响
# promotions = ['2015-06-18', '2015-11-11', '2016-11-11', '2016-06-18', '2017-11-11', '2017-06-18', '2018-11-11', '2018-06-18']
# df_promotion = data[data['日期'].isin(promotions)].groupby('日期').agg(
#     {'订单需求量':'sum'}).reset_index()
# # 绘制促销和需求量的柱状图
# plt.figure(figsize=(8,4))
# plt.bar(df_promotion['日期'], df_promotion['订单需求量'])
# plt.xlabel('Promotion Dates')
# plt.ylabel('Demand Quantity')
# plt.title('Promotion Demand Quantity')
# plt.xticks(rotation=45)
# plt.show()

# #Eight.季节因素对产品需求量的影响
# data['quarter'] = data['日期'].dt.quarter
# df_season = data.groupby('quarter').agg({'订单需求量':'sum'}).reset_index()
#
# # 绘制季度和需求量的饼图
# plt.figure(figsize=(6, 6))
# labels = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
# sizes = df_season['订单需求量']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.axis('equal')
# plt.title('Seasonal Demand Distribution', fontsize=14)
# plt.show()