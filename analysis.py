import pandas as pd

# 读取CSV文件
data = pd.read_csv('samples/DWR-932_Pre_best_model.csv', encoding='utf-8')

# 找到最后一列值为1的行
condition1 = data['label'] == 1
rows_with_one1 = data[condition1]

# 找到最后一列值为0的行
condition0 = data['label'] == 0
rows_with_one0 = data[condition0]

# 获取这些行的第一列的名称
column_names1 = rows_with_one1.iloc[:, 0]
column_names0 = rows_with_one0.iloc[:, 0]

# 打印结果
# print("column_names1:", column_names1)
# print("column_names0:", column_names0)
# 将列名转换为集合，去除重复项
unique_column_names1 = set(column_names1)
unique_column_names0 = set(column_names0)

# 打印去重后的列名
print("------------正负样本函数对应的程序-------------")
print("unique_column_names1:", unique_column_names1)
print("unique_column_names0:", unique_column_names0)

# 发现有一样的时候，删除便签为0的
# 找出unique_column_names1中包含在unique_column_names0中的元素
common_elements = set(unique_column_names0).intersection(set(unique_column_names1))

# 删除unique_column_names0中的共同元素
unique_column_names0_modified = [elem for elem in unique_column_names0 if elem not in common_elements]

# 输出结果
print("------------在正样本中出现的程序，在负样本中删除-------------")
print("Pos_samples_list:", unique_column_names1)
print("Pos_samples_len:", len(unique_column_names1))
print("Neg_sample_list (modified):", unique_column_names0_modified)
print("Neg_sample_list_len:", len(unique_column_names0_modified))

# 将输出结果写到文件中d
with open('samples/DWR-932_Pre_best_model_Pos_samples.txt', 'w', encoding='utf-8') as file1:
    file1.write('\n'.join(unique_column_names1))

with open('samples/DWR-932_Pre_best_model_Neg_sample.txt', 'w', encoding='utf-8') as file2:
    file2.write('\n'.join(unique_column_names0_modified))

print("两个列表的内容已经写入到文件中。")

