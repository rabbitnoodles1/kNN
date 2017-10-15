# coding=utf-8
import kNN

group, labels = kNN.creatDataSet()                 # 创建数据集和标签然后打印
print (group)
print (labels)
print (kNN.classify0([1, 0.9], group, labels, 3))  # 传入一个向量（如:[1,0.9], 判断它是属于标签A还是B）


