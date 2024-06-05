import pandas as pd

# df = pd.read_csv('../sheet/order_train1.csv')
df = pd.read_csv('../sheet/order_train2.csv')
df.dropna(inplace=True)  # 删除缺失值
df.drop_duplicates(inplace=True)  # 删除重复值
df = df[(df['item_price'] > 0) & (df['ord_qty'] > 0)]  # 去除异常值
df = df[(df['first_cate_code'] != '0000') & (df['second_cate_code'] != '0000')]  # 去除无效数据
df.reset_index(drop=True, inplace=True)  # 重置索引
# df.to_csv('../sheet/order_train1_washed.csv', index=False)
df.to_csv('../sheet/order_train2_washed.csv', index=False)
