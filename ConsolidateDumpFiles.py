import pandas as pd
import openpyxl

#Data as dataframe under pandas
Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')

#This is to see what the column headers are and the first few rows. Not needed.
Data.head()

#This is labelling things for different columns. Grab list of Smids, and summarized data
SMIDS = Data.SMID.unique()

#This is Python equivalent of Sumif. Sum money paid by each smid.  Report for other columns.
MoneyPaidTotal = Data.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal = Data.groupby(['SMID'])['MoneyJury'].sum()

#Now that we sumiffed all the columns, merge them together by making a dataframe.
End = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal)))

#Dataframe will have column titles of 0,1,2,3 etc... Below lines adds the names they should be. 
End.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']

#Print dataframe to see that it worked.
print(End)


###############################################################
import pandas as pd
import openpyxl

#Data as dataframe under pandas
Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')

#This is to see what the column headers are and the first few rows. Not needed.
Data.head()

#This is labelling things for different columns. Grab list of Smids, and summarized data
SMIDS = Data.SMID.unique()

#This is Python equivalent of Sumif. Sum money paid by each smid.  Report for other columns.
MoneyPaidTotal = Data.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal = Data.groupby(['SMID'])['MoneyJury'].sum()

#Now that we sumifed all the columns, merge them together by making a dataframe.
End = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal)))

#Dataframe will have column titles of 0,1,2,3 etc... Below lines adds the names they should be. 
End.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']

#Print dataframe to see that it worked.
print(End)

#Repeat all of the above but use second source of data.
Data2 = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo 2.xlsx',sheet_name="Sheet1", engine='openpyxl')
Data2.head()
print(Data2)
SMIDS2 = Data2.SMID.unique()

MoneyPaidTotal2 = Data2.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal2 = Data2.groupby(['SMID'])['MoneyJury'].sum()

End2 = pd.DataFrame(list(zip(SMIDS2 ,MoneyPaidTotal2, MoneyJuryTotal2)))
End2.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']
print(End2)

End.append(End2)



###############################################################
import pandas as pd
import openpyxl

#Data as dataframe under pandas
Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')

#This is to see what the column headers are and the first few rows. Not needed.
Data.head()

#This is labelling things for different columns. Grab list of Smids, and summarized data
SMIDS = Data.SMID.unique()

#This is Python equivalent of Sumif. Sum money paid by each smid.  Report for other columns.
MoneyPaidTotal = Data.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal = Data.groupby(['SMID'])['MoneyJury'].sum()

#Now that we sumiffed all the columns, merge them together by making a dataframe.
End = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal)))

#Dataframe will have column titles of 0,1,2,3 etc... Below lines adds the names they should be. 
End.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']

#Print dataframe to see that it worked.
print(End)

#Repeat all of the above but use second source of data.
Data2 = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo 2.xlsx',sheet_name="Sheet1", engine='openpyxl')
Data2.head()
print(Data2)
SMIDS2 = Data2.SMID.unique()

MoneyPaidTotal2 = Data2.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal2 = Data2.groupby(['SMID'])['MoneyJury'].sum()

End2 = pd.DataFrame(list(zip(SMIDS2 ,MoneyPaidTotal2, MoneyJuryTotal2)))
End2.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']
print(End2)

End.append(End2)

