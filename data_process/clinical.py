import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("D:/data/biodatabase/transcript/clinical.csv")
    column=["bcr_patient_barcode","gender","ajcc_staging_edition","age_at_diagnosis","weight_kg_at_diagnosis","height_cm_at_diagnosis"]
    print(df)
    data={}
    for i in column:
        data[i]=df.loc[:,i]
    df_new = pd.DataFrame(data)
    df_new.to_csv("D:/data/biodatabase/transcript/clinical_filtered.csv",index=False)