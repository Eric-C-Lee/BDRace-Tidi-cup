import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import xgboost as xgb

# 读取od_by-tm.xlsx文件
data = pd.read_excel('../sheet/od_by_tm1.xlsx')

# 将销售渠道名称、月头/中/末、节假日/工作日、618/双十一、季节等分类变量转换成虚拟变量
data = pd.get_dummies(data, columns=['销售渠道名称', '月头，月末，月末', '节假日和工作日', '618和双十一', '季节'])

# 将日期列转换成datetime类型，并提取年月日信息
data['日期'] = pd.to_datetime(data['日期'])
data['年'] = data['日期'].dt.year
data['月'] = data['日期'].dt.month
data['日'] = data['日期'].dt.day

# 建立训练集和验证集
train = data.loc[(data['年'] != 2019), :]
valid = data.loc[(data['年'] == 2019), :]

# 提取需求量作为目标变量
target = '订单需求量'

# 建立特征列表
features = ['销售区域代码', '产品编码', '产品大类编码', '产品细分编码',
            '销售渠道名称_offline', '销售渠道名称_online', '产品价格',
            '季节_春', '季节_夏', '季节_秋', '季节_冬',
            '月头，月末，月末_月初', '月头，月末，月末_月中', '月头，月末，月末_月末',
            '节假日和工作日_工作日', '节假日和工作日_节假日',
            '618和双十一_618', '618和双十一_双十一', '618和双十一_其他']

# 建立模型
model = xgb.XGBRegressor(
    n_estimators=100,
    max_depth=8,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    gamma=1,
    seed=42
)

# 拟合模型
model.fit(train[features], train[target])

# 预测需求量
dates = pd.date_range(start='2019-01-01', end='2019-03-31', freq='D')
preds = pd.DataFrame({'日期': dates})
preds['年'] = preds['日期'].dt.year
preds['月'] = preds['日期'].dt.month
preds['日'] = preds['日期'].dt.day
# preds['销售区域代码'] = np.random.choice(valid['销售区域代码'].unique(), size=len(dates))
preds['销售区域代码'] = np.random.choice(valid['销售区域代码'].unique(), size=len(dates)) if len(valid['销售区域代码'].unique()) > 0 else 'default_value'
# preds['产品编码'] = np.random.choice(valid['产品编码'].unique(), size=len(dates))
if len(valid['产品编码'].unique()) > 0:
    preds['产品编码'] = np.random.choice(valid['产品编码'].unique(), size=len(dates))
# preds['产品大类编码'] = np.random.choice(valid['产品大类编码'].unique(), size=len(dates))
if len(valid['产品大类编码'].unique()) > 0:
    preds['产品大类编码'] = np.random.choice(valid['产品大类编码'].unique(), size=len(dates))
if len(valid['产品细分编码'].unique()) > 0:
    preds['产品细分编码'] = np.random.choice(valid['产品细分编码'].unique(), size=len(dates))
preds = pd.get_dummies(preds, columns=['销售区域代码', '产品编码', '产品大类编码',
                                       '产品细分编码'])
preds = preds.fillna(0)
preds[target] = model.predict(preds[features])

# 按天保存预测结果为result1.xlsx
preds.to_excel('result1.xlsx', index=False)

# 按周和月聚合预测结果，并可视化
preds_weekly = preds.resample('W-MON', on='日期').sum();
preds_monthly = preds.resample('MS', on='日期').sum();

#按周和月保存预测结果为result1.xlsx
preds_weekly.to_excel('result1_weekly.xlsx', index=False);
preds_monthly.to_excel('result1_monthly.xlsx', index=False);

#可视化按天的预测结果
import matplotlib.pyplot as plt
plt.plot(preds['日期'], preds[target]);
plt.title('Daily Demand Prediction');
plt.xlabel('Date');
plt.ylabel('Demand');
plt.show()

#可视化按周的预测结果
plt.plot(preds_weekly.index, preds_weekly[target]);
plt.title('Weekly Demand Prediction');
plt.xlabel('Week Starting Date');
plt.ylabel('Demand');
plt.show()

#可视化按月的预测结果
plt.plot(preds_monthly.index, preds_monthly[target]);
plt.title('Monthly Demand Prediction');
plt.xlabel('Month Starting Date');
plt.ylabel('Demand');
plt.show()


