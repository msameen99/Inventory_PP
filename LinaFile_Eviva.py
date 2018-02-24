
# coding: utf-8

# # File PATHs الكود الحالي مظبوط على الملف القديم , لو الملف الجديد مشابه للقديم : لا نحتاج تغيير في الكود

# In[1]:


Path = 'L:\\_Cloud\\Dropbox\\_Taacis_Working_Folder\\_DataScience\\_Eviva\\_SellerCloud\\_Inventory_PredictedPurchase\\'
NewLinaExcelFile = Path + 'Lina_12Feb18.xlsx'
PrevLinaExcelFile = Path + '21Jan18\\Lina_21Jan18.xlsx'


# # Import the PREVIOUS Excel file

# In[2]:


import pandas as pd

try:
    dfPrevLina = pd.read_excel(PrevLinaExcelFile, sheetname = 'Sheet1')
    print(dfPrevLina.shape)
except:
    print('ERROR: File NOT found')
    
dfPrevLina[15:18]


# # Import the NEW Excel file

# In[3]:


import pandas as pd

try:
    dfNewLina = pd.read_excel(NewLinaExcelFile, sheetname = 'Sheet1')
    print(dfNewLina.shape)
except:
    print('ERROR: File NOT found')
    
dfNewLina[15:18]


# # Compare #No of Columns and Columns Names in New & Prev Lina's File

# In[4]:


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


# # Understand the Anatomy of your Columns

# In[5]:


i=0
for c in dfNewLina.columns: 
    print('{}=>{}<'.format(i,c))
    i+=1


# In[7]:


dfNewLina.columns


# # RENAME the Columns with your own Names

# In[8]:


NewColNames=('FactoryName','PO_Date_OrderOn','PoNumber','SKU','Qty','ETA','ArrivalDate','PoNumberSC','Cost','AddedToSC','QtyAddedToSC','Comments')

dfMyLina=dfNewLina

i=0
for col in dfMyLina.columns:
    dfMyLina=dfMyLina.rename(columns={col:NewColNames[i]}) #dfMyLina =dfMyLina.rename(columns={dfNewLina.columns[0]:NewColNames[0]})
    i+=1
 
print(dfMyLina.shape)
dfMyLina[15:18]


# # Delete any ROW with ALL values = NaN

# In[9]:


dfNoNaN = dfMyLina.dropna(axis=0, how='all')

print(dfNoNaN.shape)
dfNoNaN[15:18]


# # SELECT needed columns ONLY

# In[10]:


df01 = dfNoNaN[['SKU','Qty','ETA','ArrivalDate','PO_Date_OrderOn','PoNumber']]
df01.head(5)

