import os
import pandas as pd
import numpy as np


if __name__ == '__main__':
    sample = pd.read_csv("D:/data/biodatabase/transcript/sample.csv")
    name_file_case = np.array(sample.iloc[:, 1])
    name_case = sample.iloc[:, 6]


    all=[]
    name_all=["case_id"]+list(pd.read_csv("D:\data\\biodatabase\\2021-12-19\\0b766e80-e81b-46c7-bd2d-567a65735a5c\\f43699d8-3acc-445d-8ab2-9475194ebbc9.FPKM.txt", sep='\t',header=None).iloc[:500,0])
    total=0
    length = len(os.listdir("D:/data/biodatabase/2021-12-19"))
    for dir_name in os.listdir("D:/data/biodatabase/2021-12-19"):
        if dir_name.find(".txt") < 0:
            pathi = "D:/data/biodatabase/2021-12-19" + "/" + dir_name
            f = ""
            for file in os.listdir(pathi):
                if len(file) > 20 and file.find(".gz")<0:
                    f = pathi + "/" + file
                    break
            data = pd.read_csv(f, sep='\t',header=None)
            dir_name = name_case[np.where(name_file_case == dir_name)[0][0]]
            all.append([dir_name]+list(data.iloc[:500,1]))
            total+=1
            if (total%10==0):
                print(str(total) + "/" + str(length))

    data = pd.DataFrame(all)
    print("finish")
    data.to_csv("D:/data/biodatabase/transcript/small_expression_all.csv", index=False,header=name_all)

