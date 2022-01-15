import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
%matplotlib inline

data = pd.read_table("D:/data/biodatabase/transcript/expression_all.csv",header = 0,index_col = 0)
data.head()  #查看前5行