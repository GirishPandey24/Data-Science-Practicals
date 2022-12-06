import sys
import os
import pandas as pd
################################################################
#Base='C:/VKHCG'
sInputFileName='https://media.githubusercontent.com/media/Apress/practical-data-science/master/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad.csv'
sOutputFileName=r'C:\Users\girish.pandey\Desktop\DS Pract\Good-or-Bad-02.csv'
#Company='01-Vermeulen'
################################################################
#Base='C:/VKHCG'
################################################################
print('################################')
#print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileDir=r'C:\Users\girish.pandey\Desktop\DS Pract'
if not os.path.exists(sFileDir):
 os.makedirs(sFileDir)
################################################################
### Import Warehouse
################################################################
sFileName=sInputFileName
print('Loading :',sFileName)
RawData=pd.read_csv(sFileName,header=0)
print('################################') 
print('## Raw Data Values') 
print('################################') 
print(RawData)
print('################################') 
print('## Data Profile') 
print('################################')
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
print('################################')
################################################################
sFileName=sInputFileName
RawData.to_csv(sFileName, index = False)
################################################################
TestData=RawData.dropna(axis=1, how='any')
################################################################
print('################################')
print('## Test Data Values') 
print('################################') 
print(TestData)
print('################################') 
print('## Data Profile') 
print('################################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################################')
################################################################
sFileName=sOutputFileName
TestData.to_csv(sFileName, index = False)
################################################################
print('################################')
print('### Done!! #####################')
print('################################')
################################################################
