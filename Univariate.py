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