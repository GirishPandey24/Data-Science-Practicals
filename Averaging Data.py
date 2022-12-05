import pandas as pd
################################################################
InputFileName='https://media.githubusercontent.com/media/Apress/practical-data-science/master/VKHCG/01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
OutputFileName=r'C:\Users\girish.pandey\Desktop\DS Pract\Retrieve_Router_Location.csv'
print('################################')
print('Working Base :' ' using ')
print('################################')
sFileName=r'https://media.githubusercontent.com/media/Apress/practical-data-science/master/VKHCG/01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
print('Loading :',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,
 usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
AllData=IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
print(AllData)
MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)
