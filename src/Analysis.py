import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime

# 分别用，第一个为人工清，第二个为Py清
data = pd.read_excel('../sheet/od_by_tm1.xlsx')
# data = pd.read_excel('../sheet/order_train1_pre.xlsx')

# First.产品的不同价格对需求量的影响
plt.scatter(data['产品价格'], data['订单需求量'])
plt.xlabel('Product Price')
plt.ylabel('Order Demand')
plt.title('Price vs Demand')
plt.show()

# Second.产品所在区域对需求量的影响，以及不同区域的产品需求量有何特性
plt.bar(data['销售区域代码'], data['订单需求量'])
plt.xlabel('Sales Region')
plt.ylabel('Order Demand')
plt.title('Demand in Different Sales Regions')
plt.show()

# Third.不同销售方式（线上和线下）的产品需求量的特性
grouped = data.groupby('销售渠道名称')['订单需求量']
result = grouped.agg(['mean', 'median', 'var'])
result.plot(kind='bar')
plt.show()

# Fourth.不同品类之间的产品需求量有何不同点和共同点
df_product = data.groupby(['产品大类编码', '产品细分编码']).agg(
    {'订单需求量': ['mean', 'sum']}).reset_index()
plt.figure(figsize=(12, 6))
plt.title("Products by Categories", fontsize=14)
plt.xlabel("categories")
plt.ylabel("total sales quantity")
df_product.plot(x=('产品大类编码', ''), y=[('订单需求量', 'mean'), ('订单需求量', 'sum')],
                kind='bar', ax=plt.gca())
plt.legend(["Average Demand Quantity", "Total Sales Quantity"])
plt.xticks(rotation=45)
plt.show()

# Five.不同时间段（例如月头、月中、月末等）产品需求量有何特性
data['日期'] = pd.to_datetime(data['日期'])
data['Month'] = data['日期'].dt.month
df_time = data.groupby('Month').agg({'订单需求量': 'sum'}).reset_index()
plt.figure(figsize=(8, 4))
plt.title("Demand Quantity by Month", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Demand Quantity")
plt.plot(df_time['Month'], df_time['订单需求量'], linestyle='-', marker='o')
plt.xticks(df_time['Month'])
plt.show()

# Six.节假日对产品需求量的影响
data['日期'] = pd.to_datetime(data['日期'], format='%Y-%m-%d')


def is_holiday(date):  # 根据日期判断是否为节假日
    if date.weekday() >= 5:  # 判断是否周六周日
        return True
    holidays = [  # 判断是否为节假日
        datetime.date(2015, 1, 1),
        datetime.date(2015, 2, 18),
        datetime.date(2015, 2, 19),
        datetime.date(2015, 2, 20),
        datetime.date(2015, 2, 21),
        datetime.date(2015, 2, 22),
        datetime.date(2015, 2, 23),
        datetime.date(2015, 4, 5),
        datetime.date(2015, 5, 1),
        datetime.date(2015, 6, 20),
        datetime.date(2015, 9, 3),
        datetime.date(2015, 9, 4),
        datetime.date(2015, 9, 5),
        datetime.date(2015, 9, 26),
        datetime.date(2015, 10, 1),
        datetime.date(2015, 10, 2),
        datetime.date(2015, 10, 3),
        datetime.date(2015, 10, 4),
        datetime.date(2015, 10, 5),
        datetime.date(2015, 10, 6),
        datetime.date(2015, 10, 7),
        datetime.date(2015, 10, 10),
        datetime.date(2016, 1, 1),
        datetime.date(2016, 2, 7),
        datetime.date(2016, 2, 8),
        datetime.date(2016, 2, 9),
        datetime.date(2016, 2, 10),
        datetime.date(2016, 2, 11),
        datetime.date(2016, 2, 12),
        datetime.date(2016, 4, 4),
        datetime.date(2016, 5, 1),
        datetime.date(2016, 6, 9),
        datetime.date(2016, 6, 10),
        datetime.date(2016, 6, 11),
        datetime.date(2016, 9, 15),
        datetime.date(2016, 9, 16),
        datetime.date(2016, 9, 17),
        datetime.date(2016, 10, 1),
        datetime.date(2016, 10, 2),
        datetime.date(2016, 10, 3),
        datetime.date(2016, 10, 4),
        datetime.date(2016, 10, 5),
        datetime.date(2016, 10, 6),
        datetime.date(2016, 10, 7),
        datetime.date(2016, 10, 8),
        datetime.date(2017, 1, 1),
        datetime.date(2017, 1, 27),
        datetime.date(2017, 1, 28),
        datetime.date(2017, 1, 29),
        datetime.date(2017, 1, 30),
        datetime.date(2017, 1, 31),
        datetime.date(2017, 2, 1),
        datetime.date(2017, 4, 2),
        datetime.date(2017, 4, 3),
        datetime.date(2017, 4, 4),
        datetime.date(2017, 5, 1),
        datetime.date(2017, 5, 28),
        datetime.date(2017, 5, 29),
        datetime.date(2017, 5, 30),
        datetime.date(2017, 10, 1),
        datetime.date(2017, 10, 2),
        datetime.date(2017, 10, 3),
        datetime.date(2017, 10, 4),
        datetime.date(2017, 10, 5),
        datetime.date(2017, 10, 6),
        datetime.date(2017, 10, 7),
        datetime.date(2017, 10, 8),
        datetime.date(2018, 1, 1),
        datetime.date(2018, 2, 15),
        datetime.date(2018, 2, 16),
        datetime.date(2018, 2, 17),
        datetime.date(2018, 2, 18),
        datetime.date(2018, 2, 19),
        datetime.date(2018, 2, 20),
        datetime.date(2018, 4, 5),
        datetime.date(2018, 4, 6),
        datetime.date(2018, 4, 7),
        datetime.date(2018, 4, 29),
        datetime.date(2018, 4, 30),
        datetime.date(2018, 5, 1),
        datetime.date(2018, 6, 18),
        datetime.date(2018, 9, 24),
        datetime.date(2018, 10, 1),
        datetime.date(2018, 10, 2),
        datetime.date(2018, 10, 3),
        datetime.date(2018, 10, 4),
        datetime.date(2018, 10, 5),
        datetime.date(2018, 10, 6),
        datetime.date(2018, 10, 7),
    ]
    return date.date() in holidays


holiday_data = data[data['日期'].apply(is_holiday)].groupby(['产品编码'], as_index=False)[
    '订单需求量'].sum()  # 计算节假日订单需求量
merged_data = data.merge(holiday_data, on='产品编码', how='left')  # 合并数据集
merged_data['是否为节假日'] = merged_data['日期'].apply(is_holiday)
sns.barplot(x='是否为节假日', y='订单需求量_y',
            data=merged_data[(merged_data['日期'] >= '2015-01-01') & (merged_data['日期'] <= '2018-12-31')])
plt.show()

# Seven.促销（如618、双十一等）对产品需求量的影响
promotions = ['2015-06-18', '2015-11-11', '2016-11-11', '2016-06-18', '2017-11-11', '2017-06-18', '2018-11-11',
              '2018-06-18']
df_promotion = data[data['日期'].isin(promotions)].groupby('日期').agg(
    {'订单需求量': 'sum'}).reset_index()
plt.figure(figsize=(8, 4))
plt.bar(df_promotion['日期'], df_promotion['订单需求量'])
plt.xlabel('Promotion Dates')
plt.ylabel('Demand Quantity')
plt.title('Promotion Demand Quantity')
plt.xticks(rotation=45)
plt.show()

# Eight.季节因素对产品需求量的影响
data['quarter'] = data['日期'].dt.quarter
df_season = data.groupby('quarter').agg({'订单需求量': 'sum'}).reset_index()

plt.figure(figsize=(6, 6))
labels = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
sizes = df_season['订单需求量']  # 这一个给第一个用
# 这一个给第二个用
# sizes = abs(df_season['订单需求量'])
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Seasonal Demand Distribution', fontsize=14)
plt.show()
