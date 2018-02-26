
# coding: utf-8

# %%html
# <p style="color:red;font-size:20px"> File PATHs الكود الحالي مظبوط على الملف القديم , لو الملف الجديد مشابه للقديم : لا نحتاج تغيير في الكود</p>

# In[326]:


NewLinaExcelFile='L:\\_Cloud\\Dropbox\\_Taacis_Working_Folder\\_DataScience\\_Eviva\\_SellerCloud\\_Inventory_PredictedPurchase\\Lina_12Feb18.xlsx'
PrevLinaExcelFile = 'L:\\_Cloud\\Dropbox\\_Taacis_Working_Folder\\_DataScience\\_Eviva\\_SellerCloud\\_Inventory_PredictedPurchase\\21Jan18\\Lina_21Jan18.xlsx'


# In[327]:


get_ipython().run_cell_magic('html', '', '<p style="color:red;font-size:20px"> Import the PREVIOUS Excel file </p>')


# In[328]:


import pandas as pd

try:
    dfPrevLina = pd.read_excel(PrevLinaExcelFile, sheetname = 'Sheet1')
    print(dfPrevLina.shape)
except:
    print('ERROR: File NOT found')
    
dfPrevLina[15:18]


# In[329]:


get_ipython().run_cell_magic('html', '', '<p style="color:red;font-size:20px"> Import the NEW Excel file </p>')


# In[330]:


import pandas as pd

try:
    dfNewLina = pd.read_excel(NewLinaExcelFile, sheetname = 'Sheet1')
    print(dfNewLina.shape)
except:
    print('ERROR: File NOT found')
    
dfNewLina[15:18]


# In[1]:


get_ipython().run_cell_magic('html', '', '<p style="color:red;font-size:20px"> Compare #No of Columns and Columns Names in New & Prev Lina\'s File </p>')


# In[337]:


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


# In[338]:


get_ipython().run_cell_magic('html', '', '<p style="color:red;font-size:20px"> Understand the Anatomy of your Columns </p>')


# In[339]:


i=0
for c in dfNewLina.columns: 
    print('{}=>{}<'.format(i,c))
    i+=1


# In[340]:


dfNewLina.columns


# In[1]:


get_ipython().run_cell_magic('html', '', '<p style="font-size:20px;color:red"> RENAME the Columns with your own Names </p>')


# In[352]:


NewColNames=('FactoryName','PO_Date_OrderOn','PoNumber','SKU','Qty','ETA','ArrivalDate','PoNumberSC','Cost','AddedToSC','QtyAddedToSC','Comments')

dfMyLina=dfNewLina

i=0
for col in dfMyLina.columns:
    dfMyLina=dfMyLina.rename(columns={col:NewColNames[i]}) #dfMyLina =dfMyLina.rename(columns={dfNewLina.columns[0]:NewColNames[0]})
    i+=1
 
print(dfMyLina.shape)
dfMyLina[15:18]


# In[3]:


get_ipython().run_cell_magic('html', '', '<p style="font-size:20px;color:red"> Delete any ROW with ALL values = NaN </p>')


# In[354]:


dfNoNaN = dfMyLina.dropna(axis=0, how='all')

print(dfNoNaN.shape)
dfNoNaN[15:18]


# In[4]:


get_ipython().run_cell_magic('html', '', '<p style="font-size:20px;color:red"> SELECT needed columns ONLY </p>')


# In[356]:


df01 = dfNoNaN[['SKU','Qty','ETA','ArrivalDate','PO_Date_OrderOn','PoNumber']]
df01.head(5)

