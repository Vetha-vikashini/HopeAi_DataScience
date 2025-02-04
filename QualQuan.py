import pandas as pd
import numpy as np
class Univariate():
    def QuanQual(dataset):
        Qual=[]
        Quan=[]
        for cols in dataset.columns:
            if dataset[cols].dtype=="O":
                Qual.append(cols)
            else:
                Quan.append(cols)
        return Qual,Quan
    def descriptive(data,Quan):
        describe=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=Quan)
        for col in Quan:
            describe[col]["Mean"]=data[col].mean()
            describe[col]["Median"]=data[col].median()
            describe[col]["Mode"]=data[col].mode()[0]
            describe[col]["Q1:25%"]=data.describe()[col]["25%"]
            describe[col]["Q2:50%"]=data.describe()[col]["50%"]
            describe[col]["Q3:75%"]=data.describe()[col]["75%"]
            describe[col]["99%"]=np.percentile(data[col],99)
            describe[col]["Q4:100%"]=data.describe()[col]["max"]
            describe[col]["IQR"]=describe[col]["Q3:75%"]-describe[col]["Q1:25%"]
            describe[col]["1.5rule"]=1.5*describe[col]["IQR"]
            describe[col]["Lesser"]=describe[col]["Q1:25%"]-describe[col]["1.5rule"]
            describe[col]["Greater"]=describe[col]["Q3:75%"]+describe[col]["1.5rule"]
            describe[col]["Min"]=data[col].min()
            describe[col]["Max"]=data[col].max()
        return describe
    
    def freqTable(data,col):
        freqTable=pd.DataFrame(columns=["UniqueValues","Frequency","Relative_Frequency","Cum_Frequency"])
        unique_row_count=len(list(data[col].value_counts().index))
        freqTable["UniqueValues"]=data[col].value_counts().index
        freqTable["Frequency"]=data[col].value_counts().values
        freqTable["Relative_Frequency"]=freqTable["Frequency"]/unique_row_count
        freqTable["Cum_Frequency"]=freqTable["Relative_Frequency"].cumsum()

        return freqTable
    
    def Outlier_col(describe,Quan):
        lesser=[]
        greater=[]

        for col in Quan:
            if describe[col]["Min"]<describe[col]["Lesser"]:
                lesser.append(col)
            if describe[col]["Max"]>describe[col]["Greater"]:
                greater.append(col)
        return lesser,greater
    def replce_outlier(data,describe,lesser,greater):
        for col in lesser:
            data[col][data[col]<describe[col]["Lesser"]]= describe[col]["Lesser"]
        for col in greater:
            data[col][data[col]>describe[col]["Greater"]]= describe[col]["Greater"]