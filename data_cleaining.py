import pandas as pd

d={
    'id':[1,2,3,None],
    'name':['a','b','c',None]
   }

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns
frameddata=pd.DataFrame(d)
# print(frameddata)
# git feature branch
#master checkout for merge
#feture commit for conflict test


# locate an element
print(frameddata.loc[0]['id'])
filtereddate=frameddata[frameddata['name']=='a']
print(filtereddate)

#To remove none values 
# The inplace parameter in pandas allows you to modify the DataFrame or Series in place, without the need to assign the result to a new variable. 
frameddata['name'].fillna('Phone',inplace=True)
print(frameddata)



# Merge dataframe
d2={
    'id':[1,3,2],
    'mark':[55,33,44]
   }


frameddata2=pd.DataFrame(d2)

merged_date=pd.merge(frameddata,frameddata2,left_on='id',right_on='id',how='inner')

print(merged_date)


# Sorting
merged_date.sort_values(by='mark',ascending=True,inplace=True)
print(merged_date)
