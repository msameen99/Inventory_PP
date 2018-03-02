# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:54:31 2018

@author: msaservice
"""

import pandas as pd
from datetime import *

Path = 'L:\\_Cloud\\Dropbox\\_Taacis_Working_Folder\\_DataScience\\_Eviva\\_SellerCloud\\_Inventory_PredictedPurchase\\'
NewLinaExcelFile = Path + 'PO containers in the water_25Feb18.xlsx'
PrevLinaExcelFile = Path + '21Jan18\\PO containers in the water_21Jan18.xlsx'

#-----------------------------------------------------------------------------
#Import the PREVIOUS Excel file
try:
    dfPrevLina = pd.read_excel(PrevLinaExcelFile, sheetname = 'Sheet1')
    print(dfPrevLina.shape)
    dfPrevLina[15:18]
except:
    print('ERROR: File NOT found')
    
#Import the NEW Excel file
try:
    dfNewLina = pd.read_excel(NewLinaExcelFile, sheetname = 'Sheet1')
    print(dfNewLina.shape)
    dfNewLina[0:5]
except:
    print('ERROR: File NOT found')
 
#-----------------------------------------------------------------------------
#Compare No of Columns and Columns Names in New & Prev Lina's File

#1st Check the #No of Columns in both file
NewRowCnt, NewColCnt =  dfNewLina.shape
PrevRowCnt, PrevColCnt = dfPrevLina.shape
print(NewRowCnt, NewColCnt,PrevRowCnt, PrevColCnt)
if NewColCnt == PrevColCnt:
    print('OK: Number of Columns are the SAME')
else:
    print('Error: check the Dimension')
        
# 2nd check the Columns NAMEs 
N = [[] for k in range(NewColCnt)]
P = [[] for k in range(NewColCnt)]
for i in range(NewColCnt):
    N[i]=dfNewLina.columns[i]
    P[i]=dfPrevLina.columns[i]

if N == P:
    print('OK: Column Names are the SAME')
else:
    print('Error: Check Columns Names')

#-----------------------------------------------------------------------------

#Understand the Anatomy of your Columns
for i, c in enumerate(dfNewLina.columns): 
    print('{}=>{}<'.format(i,c))

print(dfNewLina.columns)

#-----------------------------------------------------------------------------
#RENAME the Columns with your own Names
NewColNames=('FactoryName','PO_Date_OrderOn','PoNumber','SKU','Qty','ETA','ArrivalDate','PoNumberSC','Cost','AddedToSC','QtyAddedToSC','Comments')

NewOldColNames = {}
for i, c in enumerate(dfNewLina.columns):
    NewOldColNames[NewColNames[i]] = c

dfMyLina=dfNewLina

for col in dfMyLina.columns:
    dfMyLina=dfMyLina.rename(columns={col:list(NewOldColNames.keys())[list(NewOldColNames.values()).index(col)]}) # list(mydict.keys())[list(mydict.values()).index(16)]

print(dfMyLina[15:18])

# Original Index
OrgIndex = dfMyLina.index.tolist()

print(dfMyLina.shape)
print(len(OrgIndex))
dfMyLina[15:18]

#-----------------------------------------------------------------------------
#Delete any ROW with ALL values = NaN
dfNoNaN = dfMyLina.dropna(axis=0, how='all')

OrgNoNaNIndex = dfNoNaN.index.tolist()

print(dfNoNaN.shape)
print(len(OrgNoNaNIndex))
dfNoNaN[15:18]
#OrgNoNaNIndex

#SELECT needed columns ONLY
df01 = dfNoNaN[['SKU','Qty','ETA','ArrivalDate','PO_Date_OrderOn','PoNumber']]
print(df01.shape)
df01.head(5)

#SELECT needed rows ONLY
from datetime import *

df02 = df01[df01['ETA'] > datetime.now()]

print(df02.shape)
df02.head()

FilteredIndex = df02.index.tolist()

print(df02.shape)
print(len(FilteredIndex))
df02[15:18]
#FilteredIndex

#Check & Verify Columns type (for each element)
TypeError = []

# Parameters:-
#           pandas datafram
#           Column Name as String
#           Type(NOT String) : int, datetime, float, pandas._libs.tslib.Timestamp, str
def pdCheckColumType(df, cName, cType):
    flag = True
    for index, row in df.iterrows():
        t = type(row[cName])
        if t is cType: pass
            #print("OK")
        else:
            flag = False
            #print("Err: ", index, "{} Type is: ".format(cName), t)
            TypeError.append([index, NewOldColNames[cName], cType])
    return flag

#Check ALL Cells type (Column by Column)
pdCheckColumType(df02,'PoNumber',str) 
pdCheckColumType(df02,'PO_Date_OrderOn',datetime)
pdCheckColumType(df02,'ArrivalDate',float)
pdCheckColumType(df02,'ETA',pd._libs.tslib.Timestamp)
pdCheckColumType(df02,'Qty',float)
pdCheckColumType(df02,'SKU',str)
    
TypeError

#Access CELL in Datafram
# To access a CELL, use > df01.at[5,'Qty']   OR df01.iat[5,1]

i = 0
a = []
for index, row in df02.iterrows():
    a.append(df02.at[index,'Qty'])
    i += 1
    if i == 6: break
#a = df02.iat[4,1]

a


writer = pd.ExcelWriter( 'C:\\Users\\msaservice\\Documents\\GitHub\\Inventory_PP\\output.xlsx',
                        engine='xlsxwriter',
                        datetime_format='d mmm yyyy hh:mm:ss',
                        date_format='dd mmmm yyyy')
# This is the default
df02.to_excel(writer, sheet_name='Sheet2')
dfNewLina.to_excel(writer,sheet_name='Lina C-P')

# Turn off the default header and skip one row to allow us to insert a user defined header.
df01.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False)  # http://xlsxwriter.readthedocs.io/working_with_pandas.html

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
LinaCP = writer.sheets['Lina C-P']

# Add your format.
format_01 = workbook.add_format({
    'bold': True,
    'text_wrap': False,
    'valign': 'top',
    'font_color': '#9C0006',
    'bg_color':'#FFC7CE',   # light RED background  # http://xlsxwriter.readthedocs.io/format.html
    'border': 13})
format_02 = workbook.add_format({    # http://pbpython.com/improve-pandas-excel-output.html
    'bg_color': '#C6EFCE',           # light GREEN background
    'font_color': '#006100'})

format_03 = workbook.add_format({
    'bg_color': '#FF0000',           # Hard RED background
    'font_color': '#000000'})

# Write the column headers with the defined format.
for col_num, value in enumerate(df01.columns.values):
    worksheet.write(0, col_num + 1, value, format_03)
    

NotIncluded = list(set(OrgIndex) - set(FilteredIndex))
#print(len(OrgIndex), len(FilteredIndex) ,len(NotIncluded))
#NotIncluded


for i in OrgIndex: # range(0, len(dfNewLina))  OR len(dfNewLina.index)  OR  dfNewLina.iterrows()  OR  iterrows()
     if i in NotIncluded:
            for j in range(len(dfNewLina.columns)):
                if pd.isnull(dfNewLina.iat[i,j]): # this will check both NaN and NaT (is pd.np.nan or is pd.NaT)
                    #pass
                    #print(i, j, dfNewLina.iat[i,j])
                    LinaCP.write(i+1, j+1, None ,format_01 )               # http://xlsxwriter.readthedocs.io/worksheet.html
                else:
                    #pass
                    #print(i, j, dfNewLina.iat[i,j])
                    LinaCP.write(i+1, j+1, dfNewLina.iat[i,j],format_01 )
            



for elem in TypeError:
    if pd.isnull(dfNewLina.iat[elem[0],list(dfNewLina.columns).index(elem[1])]):
        LinaCP.write(elem[0]+1, list(dfNewLina.columns).index(elem[1])+1, None ,format_03 )
    else:
        LinaCP.write(elem[0]+1, list(dfNewLina.columns).index(elem[1])+1, dfNewLina.iat[elem[0],list(dfNewLina.columns).index(elem[1])],format_03 )
        

list(dfNewLina.columns).index('ETA')

try:
    writer.save()
except:
    print("Error: Can NOT write the Excel file")
    
