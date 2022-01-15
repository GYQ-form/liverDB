import numpy as np
import pandas as pd
import random

if __name__ == '__main__':
    df = pd.read_csv("D:/data/biodatabase/transcript/met.csv")
    print(df.head())
    beta=df.iloc[:,1]
    gene=df.iloc[:,5]
    df1=df = pd.read_csv("D:/data/biodatabase/transcript/clinical_filtered.csv")
    case=df1.iloc[:,0]
    all=[]
    for i in range(len(case)):
        x=case[i]
        rand=random.randint(0,len(beta))
        b=beta[rand]
        y=gene[rand]
        y = y.split(";")[0]
        while b<0.5 and y.find(".")>=0:
            rand = random.randint(0, len(beta))
            b = beta[rand]
            y = gene[rand]
            y=y.split(";")[0]

        rand = random.randint(0, len(beta))
        c = beta[rand]
        z = gene[rand]
        z = z.split(";")[0]
        while c>0.5 and z.find(".")>=0:
            rand = random.randint(0, len(beta))
            c = beta[rand]
            z = gene[rand]
            z=z.split(";")[0]
        tmp=[x,y,z]

        while not (x.find('.')<0 and y.find('.')<0 and z.find('.')<0):
            x = case[i]
            rand = random.randint(0, len(beta))
            b = beta[rand]
            y = gene[rand]
            y = y.split(";")[0]
            while b < 0.5 and y.find(".") >= 0:
                rand = random.randint(0, len(beta))
                b = beta[rand]
                y = gene[rand]
                y = y.split(";")[0]

            rand = random.randint(0, len(beta))
            c = beta[rand]
            z = gene[rand]
            z = z.split(";")[0]
            while c > 0.5 and z.find(".") >= 0:
                rand = random.randint(0, len(beta))
                c = beta[rand]
                z = gene[rand]
                z = z.split(";")[0]
            tmp = [x, y, z]
        all.append(tmp)
        print("finish "+x)
    head = ["case-id", "smallest-met", "biggest-met"]
    data = pd.DataFrame(all)
    data.to_csv("D:/data/biodatabase/transcript/met_filtered.csv", index=True, header=head)