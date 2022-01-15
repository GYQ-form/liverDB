# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

def draw(gene):
    all = []
    df4 = pd.read_csv("D:/data/biodatabase/transcript/4th_expression_all.csv")
    pre_expression4 = np.array(df4.loc[:, gene])
    for i in range(len(pre_expression4)):
        tmp = ["4th", float(pre_expression4[i])]
        all.append(tmp)
    df5 = pd.read_csv("D:/data/biodatabase/transcript/5th_expression_all.csv")
    pre_expression5 = np.array(df5.loc[:, gene])
    for i in range(len(pre_expression5)):
        tmp = ["5th", float(pre_expression5[i])]
        all.append(tmp)
    df6 = pd.read_csv("D:/data/biodatabase/transcript/6th_expression_all.csv")
    pre_expression6 = np.array(df6.loc[:, gene])
    for i in range(len(pre_expression6)):
        tmp = ["6th", float(pre_expression6[i])]
        all.append(tmp)
    df7 = pd.read_csv("D:/data/biodatabase/transcript/7th_expression_all.csv")
    pre_expression7 = np.array(df7.loc[:, gene])
    for i in range(len(pre_expression7)):
        tmp = ["7th", float(pre_expression7[i])]
        all.append(tmp)
    pd.DataFrame(all).to_csv('D:/data/biodatabase/os/' + gene + ".csv", index=False,
                             header=["Tumor_stage", "Expression"])
    os.system("cd D:/R_Language/R-4.1.0/bin")
    os.system("Rscript D:/data/biodatabase/picture.R")
    os.remove('D:/data/biodatabase/os/' + gene + ".csv")

if __name__ == '__main__':
    name_all = list(pd.read_csv("D:/data/biodatabase/transcript/5th_expression_all.csv",header=None).iloc[0, 1:])
    total=0
    length=len(name_all)
    for i in range(len(name_all)):
        draw(name_all[i])
        total+=1
        if total%10==0:
            print(str(total)+"/"+str(length))



