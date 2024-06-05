import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# 读取数据
# train_data = pd.read_excel('../sheet/order_train1_pre.xlsx') #机筛
train_data = pd.read_excel('../sheet/order_train2_pre.xlsx') #机筛
# train_data = pd.read_excel('../sheet/od_by_tm1.xlsx')  # 人工预筛
# predict_data = pd.read_excel('../sheet/predict_sku1.xlsx')
predict_data = pd.read_excel('../sheet/predict_sku2.xlsx')
train_data['year'] = pd.DatetimeIndex(train_data['日期']).year  # 将日期转换为年份和月份
train_data['month'] = pd.DatetimeIndex(train_data['日期']).month

train_data['销售区域代码'] = train_data['销售区域代码'].astype(str)  # 将编码转换为字符串类型
train_data['产品编码'] = train_data['产品编码'].astype(str)
train_data['产品大类编码'] = train_data['产品大类编码'].astype(str)
train_data['产品细分编码'] = train_data['产品细分编码'].astype(str)
predict_data['销售区域代码'] = predict_data['销售区域代码'].astype(str)
predict_data['产品编码'] = predict_data['产品编码'].astype(str)
predict_data['产品大类编码'] = predict_data['产品大类编码'].astype(str)
predict_data['产品细分编码'] = predict_data['产品细分编码'].astype(str)

# 选择要使用的特征和目标变量
features = ['year', 'month', '销售区域代码', '产品编码', '产品大类编码', '产品细分编码']
target = '订单需求量'

# 拆分训练集和测试集
train = train_data[features + [target]]
train = train.dropna()
X_train = train.drop(target, axis=1)
y_train = train[target]
model = RandomForestRegressor(n_estimators=100, random_state=42)  # 训练随机森林回归模型
model.fit(X_train, y_train)

# 预测
predict_data['year'] = 2019
# predict_data['month'] = 1
# predict_data['prediction_jan'] = model.predict(predict_data[features])
# predict_data['month'] = 2
# predict_data['prediction_feb'] = model.predict(predict_data[features])
# predict_data['month'] = 3
# predict_data['prediction_mar'] = model.predict(predict_data[features])
predict_data['month'] = 4
predict_data['prediction_apr'] = model.predict(predict_data[features])
predict_data['month'] = 5
predict_data['prediction_may'] = model.predict(predict_data[features])
predict_data['month'] = 6
predict_data['prediction_jun'] = model.predict(predict_data[features])
# result = predict_data[['销售区域代码', '产品编码', 'prediction_jan', 'prediction_feb', 'prediction_mar']]  # 保存
result = predict_data[['销售区域代码', '产品编码', 'prediction_apr', 'prediction_may', 'prediction_jun']]  # 保存
# result.to_excel('../sheet/result1.xlsx', index=False)
result.to_excel('../sheet/result2.xlsx', index=False)

# 可视化
# df = pd.read_excel('../sheet/result1.xlsx')
df = pd.read_excel('../sheet/result2.xlsx')
# cols = ['sales_region_code', '2019年1月预测需求量', '2019年2月预测需求量', '2019年3月预测需求量']
cols = ['销售区域代码', 'prediction_apr', 'prediction_may', 'prediction_jun']
df = df[cols]
df.set_index('销售区域代码').plot(kind='bar')
plt.xlabel('Sales Region Code')
plt.ylabel('Demand Forecast')
plt.show()
