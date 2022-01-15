import pandas as pd
import numpy as np

def r(a):
    b=[]
    for i in range(len(a)):
        b.append(round(float(a[i]),3))
    return b

name_all=["case_id"]+list(pd.read_csv("D:\data\\biodatabase\\2021-12-19\\0b766e80-e81b-46c7-bd2d-567a65735a5c\\f43699d8-3acc-445d-8ab2-9475194ebbc9.FPKM.txt", sep='\t',header=None).iloc[:500,0])

sample = pd.read_csv("D:/data/biodatabase/transcript/clinical_filtered.csv")
case_id = np.array(sample.iloc[:, 0])
case_stage = np.array(sample.iloc[:, 2])

df=pd.read_csv("D:/data/biodatabase/transcript/small_expression_all.csv")
patient=df.loc[:,"case_id"]

sum=[]

all=[]
th4=[]
for i in range(1,len(patient)):
    flag = False
    if case_stage[np.where(patient[i] == case_id)[0][0]] == "4th":
        name_x = df.iloc[i, 0]
        for j in range(len(all)):
            if all[j][0] == name_x:
                flag = True
                break
        if flag == True:
            continue
        all.append([df.iloc[i, 0]] + r(list(df.iloc[i, 1:])))
data = pd.DataFrame(all)
print("finish 4th")
data.to_csv("D:/data/biodatabase/transcript/4th_expression_all.csv", index=False,header=name_all)

all=[]
th5=[]
for i in range(1,len(patient)):
    flag = False
    if case_stage[np.where(patient[i] == case_id)[0][0]] == "5th":
        name_x = df.iloc[i, 0]
        for j in range(len(all)):
            if all[j][0] == name_x:
                flag = True
                break
        if flag == True:
            continue
        all.append([df.iloc[i, 0]] + r(list(df.iloc[i, 1:])))
data = pd.DataFrame(all)
print("finish 5th")
data.to_csv("D:/data/biodatabase/transcript/5th_expression_all.csv", index=False,header=name_all)


all=[]
th6=[]
for i in range(1,len(patient)):
    flag=False
    if case_stage[np.where(patient[i] == case_id)[0][0]]=="6th":
        name_x=df.iloc[i,0]
        for j in range(len(all)):
            if all[j][0]==name_x:
                flag=True
                break
        if flag==True:
            continue
        all.append([df.iloc[i,0]]+r(list(df.iloc[i,1:])))
data = pd.DataFrame(all)
print("finish 6th")
data.to_csv("D:/data/biodatabase/transcript/6th_expression_all.csv", index=False,header=name_all)

all=[]
th7=[]
for i in range(1,len(patient)):
    flag = False
    if case_stage[np.where(patient[i] == case_id)[0][0]] == "7th":
        name_x = df.iloc[i, 0]
        for j in range(len(all)):
            if all[j][0] == name_x:
                flag = True
                break
        if flag == True:
            continue
        all.append([df.iloc[i, 0]] + r(list(df.iloc[i, 1:])))

data = pd.DataFrame(all)
print("finish 7th")
data.to_csv("D:/data/biodatabase/transcript/7th_expression_all.csv", index=False,header=name_all)

