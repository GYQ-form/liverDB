import os
import gzip
import pandas as pd
import numpy as np

def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    open(f_name, "wb").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    #关闭gzip对象

def transcript(pathi):
    data = pd.read_csv(pathi,sep='\t', header=None)
    expression = np.array(data.iloc[:, 1])
    MRG = np.max(expression)
    TRG = np.sum(expression)
    max_name = data.iloc[:, 0][np.argmax(expression)]
    tmp = [max_name, MRG, TRG]
    return tmp

if __name__ == '__main__':
    all=[]
    total=0
    for name in os.listdir("D:/data/biodatabase/2021-12-19"):
        if name.find(".txt")<0:
            uuid=name
            tmp=[uuid]
            pathi="D:/data/biodatabase/2021-12-19"+"/"+name
            f=""
            for gz in os.listdir(pathi):
                un_gz(pathi+"/"+gz)
                if len(gz)>20:
                    f = pathi+"/"+gz.replace(".gz", "")
            tmp=tmp+transcript(f)
            all.append(tmp)
    data = pd.DataFrame(all)
    head=["uuid","max-read-gene-name","max-read-gene","total-read"]
    data.to_csv("D:/data/biodatabase/transcript/transcript.csv",index=False,header=head)



