import os

import fileinput

path = ''
disease_csv = ''

# 将一个疾病文件中所有的症状提取到一个列表中
symptom = list(map(lambda x:x.strip(), fileinput.FileInput(os.path.join(path, disease_csv))))

# 过滤的所有长度异常的症状名称
symptom = list(filter(lambda x:0<len(x)<100, symptom))