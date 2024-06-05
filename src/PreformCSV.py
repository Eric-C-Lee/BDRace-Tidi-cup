import pandas as pd
from sklearn.preprocessing import StandardScaler

# data = pd.read_csv('../sheet/order_train1_washed.csv')
data = pd.read_csv('../sheet/order_train2_washed.csv')
cols_to_scale = ['item_price', 'ord_qty']  # 提取
scaler = StandardScaler()  # 标准化处理
data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])
# data.to_csv('../sheet/order_train1_pre.csv', index=False)
data.to_csv('../sheet/order_train2_pre.csv', index=False)

