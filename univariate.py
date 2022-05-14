class Univariate():
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtype=="O"):
                Qual.append(columnName)
            else:
                Quan.append(columnName)
        return Quan,Qual
    
    def frequencyTable(self,dataset,columnName):
        import pandas as pd
        freq=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumulative_Frequency"])
        freq["Unique_Values"]=dataset[columnName].value_counts().sort_index().index
        freq["Frequency"]=dataset[columnName].value_counts().sort_index().values 
        freq["Relative_Frequency"]=(freq["Frequency"]/len(freq))*100
        freq["Cumulative_Frequency"]=freq["Relative_Frequency"].cumsum()
        return freq
    
    def uniAnalysis(self,dataset,quan):
        import pandas as pd
        import numpy as np
        univari=pd.DataFrame(index=["Mean","Median","Mode","25th","50th","75th","99th","100th","IQR","1.5IQR","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            univari[columnName]["Mean"]=dataset[columnName].mean()
            univari[columnName]["Median"]=dataset[columnName].median()
            univari[columnName]["Mode"]=dataset[columnName].mode()[0]
            univari[columnName]["25th"]=np.percentile(dataset[columnName],25)    
            univari[columnName]["50th"]=np.percentile(dataset[columnName],50)
            univari[columnName]["75th"]=np.percentile(dataset[columnName],75)
            univari[columnName]["99th"]=np.percentile(dataset[columnName],99)
            univari[columnName]["100th"]=np.percentile(dataset[columnName],100)
            univari[columnName]["IQR"]=univari[columnName]["75th"]-univari[columnName]["25th"]
            univari[columnName]["1.5IQR"]=1.5*univari[columnName]["IQR"]
            univari[columnName]["Lesser"]=univari[columnName]["25th"]-univari[columnName]["1.5IQR"]
            univari[columnName]["Greater"]=univari[columnName]["75th"]+univari[columnName]["1.5IQR"]
            univari[columnName]["Min"]=dataset[columnName].min()
            univari[columnName]["Max"]=dataset[columnName].max()
        return univari