import pandas as pd
from sklearn.preprocessing import StandardScaler

# 读取csv文件
data = pd.read_csv('../sheet/order_train1_washed.csv')

# 将需要进行标准化的列提取出来
cols_to_scale = ['item_price', 'ord_qty']

# 对需要标准化的列进行标准化处理
scaler = StandardScaler()
data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])

# 将处理后的数据保存为csv文件
data.to_csv('../sheet/order_train1_pre.csv', index=False)
