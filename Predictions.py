# 单个文件进行预测
import pandas as pd
import joblib
import numpy as np
from joblib import load
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer
# 加载模型
model = load('joblib_save/The_best_model_final.joblib')

# 读取 CSV 文件
# data = pd.read_csv('samples/Pre/DIR-880_ARM_binary_combined.csv')
data = pd.read_csv('samples/DWR-932_combined.csv')

features = ['src', 'fname', 'funcaddr']
X = data.drop(columns=features) #删除标签列

# 检查数据类型并转换为数值类型
for column in X.columns:   # 此时是包含data中的所有列
    if X[column].dtype == 'object':  # 检查当前列的数据类型是否为object，代指字符串或类别数据。
        X[column] = pd.to_numeric(X[column], errors='coerce')  # 尝试将该列转换为数值类型。

# 处理缺失值，填充为0或者其他策略
X.fillna(0, inplace=True)

# 数据标准化
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# 创建PowerTransformer实例
transformer = PowerTransformer(method='yeo-johnson')
# 拟合数据（计算幂律指数）
X_scaled = transformer.fit_transform(X)

# 导入特征选择模型
# selected_features = load('joblib_save_1/selected_features.joblib')

# 使用缩放后的数据和选择的特征进行预测
predictions = model.predict(X_scaled)

# 打印预测结果
print(predictions)

name_list = []

for i in predictions:
    name_list.append(i)
data["label"] = name_list
# data1.to_csv('Predictions_samples_1.csv',encoding = 'utf-8')
data.to_csv('samples/DWR-932_Pre_best_model.csv', index=False, encoding = 'utf-8')

"""



"""

