import json
import matplotlib.pyplot as plt
import os
import numpy as np
def get_file_names(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_names.append(file_path)
    return file_names
def generate_histogram(numbers):
    plt.hist(numbers, bins=100)
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title('Frequency Histogram')
    plt.show()

def read_jsonl(file_path):
    objects = []
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            obj = json.loads(line.strip())
            objects.append(obj)
    return objects
def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data
# 替换为你的 JSONL 文件路径
jsonl_file = '7b1108.jsonl'

# 调用函数读取 JSONL 文件并解析内容为 Python 对象
data = read_jsonl(jsonl_file)
en_count=0
zh_count=0

for obj in data:
    c=obj['output'][0].lower()
    if c >= 'a' and c <= 'z':
        en_count+=1
    else:
        zh_count+=1
print(en_count,zh_count)
print(len(data))

# 打印解析后的对象
en_length=[]
zh_length=[]

for obj in data:
    if len(obj['output'])>0 :
        c=obj['output'][0].lower()
        if c>='a' and c<='z':
            en_length.append(len(obj["output"]))
        else:
            zh_length.append(len(obj["output"]))
length=en_length
print(len(length))
percentiles = np.percentile(length, [25, 50, 75, 90])
print(percentiles)
generate_histogram(length)



'''
en_length_output [25, 50, 75, 90] [ 126.  348.  564. 1079.]
zh_length_output [25, 50, 75, 90] [ 82. 124. 167. 233.]
'''
