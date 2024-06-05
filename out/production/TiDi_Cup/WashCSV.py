import pandas as pd

# 读取csv文件
df = pd.read_csv('../sheet/order_train1.csv')

# 删除缺失值
df.dropna(inplace=True)

# 删除重复值
df.drop_duplicates(inplace=True)

# 去除异常值
df = df[(df['item_price'] > 0) & (df['ord_qty'] > 0)]

# 去除无效数据
df = df[(df['first_cate_code'] != '0000') & (df['second_cate_code'] != '0000')]

# 重置索引
df.reset_index(drop=True, inplace=True)

# 保存清洗后的数据
df.to_csv('../sheet/order_train1_washed.csv', index=False)