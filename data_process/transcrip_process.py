import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("D:/data/biodatabase/transcript/expression_all.csv")
    column_name=[column for column in df]
    print("finish reading")
    column_name=column_name[2:]
    all=[]
    total=0
    for gene in column_name:
        data=np.array(df.loc[:,gene])
        data=data.astype(np.float)
        sd = np.std(data, ddof=1)
        cv = sd / np.mean(data)
        tmp=np.array([cv,sd])
        tmp[np.isnan(tmp)]=0
        tmp=list(tmp)
        tmp = [gene]+tmp
        all.append(tmp)
        total += 1
        if total % 10 == 0:
            print(str(total) + "/" + str(len(column_name)-1))
    all = np.array(all)
    all = all[np.argsort(all[:, 1])[::-1]]
    head = ["gene-name", "cv", "sd"]
    data = pd.DataFrame(all)
    data.to_csv("D:/data/biodatabase/transcript/new_diff_expression.csv", index=True, header=head)
