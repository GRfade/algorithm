import math  #数学基本运算
import matplotlib.pyplot as plt #图形显示
import random  #随机数
import numpy as np #矩阵运算库
import pandas as pd #提供高性能易用数据类型和分析工具
import seaborn as sns #绘制数据分布，数据观察函数
from scipy.io import arff #方便导入arff文件数据
import sys #用于表示最大值和最小值

'''
该算法为逻辑回归算法
数据来源：diabetes.arff 糖尿病人的各项数据
数据内容包括：preg（怀孕次数）、plas（葡萄糖浓度）、pres（血压）、skin（皮肤厚度）、insu（胰岛素）、mass（体重）、 pedi（谱系功能）、 age（年龄）、 class(是否为糖尿病人)
前8列为糖尿病人特征特征、最后一列为是否患有糖尿病
'''
