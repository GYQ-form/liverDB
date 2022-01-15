import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("D:/data/biodatabase/transcript/transcript.csv")
    sample=pd.read_csv("D:/data/biodatabase/transcript/sample.csv")
    name_file=df.iloc[:,0]
    name_file_case=np.array(sample.iloc[:,1])
    name_case=sample.iloc[:,6]
    for i in range(len(name_file)):
        df.iloc[:,0][i]=name_case[np.where(name_file_case==name_file[i])[0][0]]
        print(name_file[i])
    df.to_csv("D:/data/biodatabase/transcript/new_transcript.csv")

