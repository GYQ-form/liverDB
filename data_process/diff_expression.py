import os
import pandas as pd
import numpy as np

if __name__ == '__main__':
    name_all=set()
    for dir_name in os.listdir("D:/data/biodatabase/2021-12-19"):
        if dir_name.find(".txt") < 0:
            pathi = "D:/data/biodatabase/2021-12-19" + "/" + dir_name
            f = ""
            for file in os.listdir(pathi):
                if len(file) > 20 and file.find(".gz")<0:
                    f = pathi + "/" + file
                    break
            data = pd.read_csv(f, sep='\t',header=None)
            name_all = name_all.union(set(data.iloc[:, 0]))
            break
    name_all=list(name_all)
    all=[]
    length=len(os.listdir("D:/data/biodatabase/2021-12-19"))
    total=0
    for gene in name_all:
        data=[]
        for dir_name in os.listdir("D:/data/biodatabase/2021-12-19"):
            if dir_name.find(".txt") < 0:
                pathi = "D:/data/biodatabase/2021-12-19" + "/" + dir_name
                f = ""
                for file in os.listdir(pathi):
                    if len(file) > 20 and file.find(".gz") < 0:
                        f = pathi + "/" + file
                        break
                df = pd.read_csv(f, sep='\t', header=None)
                name_list=np.array(df.iloc[:,0])
                value=df.iloc[:, 1][np.where(name_list==gene)[0][0]]
                data.append(value)
        data=np.array(data)
        sd=np.std(data, ddof=1)
        cv=sd/np.mean(data)
        tmp=[gene,cv,sd]
        all.append(tmp)
        total+=1
        if total%10==0:
            print(str(total)+"/"+str(length))
            change=[]
            change=all
            all = np.array(all)
            all = all[np.argsort(all[:, 1])[::-1]]
            head = ["gene-name", "cv", "sd"]
            data = pd.DataFrame(all)
            data.to_csv("D:/data/biodatabase/transcript/diff_expression.csv", index=True, header=head)
            all=change
#%%






