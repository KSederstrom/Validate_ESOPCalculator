##########################################################################
#This is to summarize two fields from just one file.
import pandas as pd
import openpyxl

#Data as dataframe under pandas. Dataframe is an organization of your data. Its like a table in SQL, and you add data/rows to it as wanted.
#Source for pyxl: (https://automatetheboringstuff.com/2e/chapter13/)
Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')

#This is to see what the column headers are and the first few rows. Not needed.
Data.head()

#This is labelling things for different columns. Grab list of Smids, and summarized data
#Source for unique function (https://www.askpython.com/python/built-in-methods/unique-values-from-a-dataframe)
SMIDS = Data.SMID.unique()

#This is Python equivalent of Sumif. Sum money paid by each smid.  Report for other columns.
#Source: (https://pythoninoffice.com/sumif-and-countif-in-pandas/)
MoneyPaidTotal = Data.groupby(['SMID'])['MoneyPaid'].sum()
MoneyJuryTotal = Data.groupby(['SMID'])['MoneyJury'].sum()

#Now that we sumiffed all the columns, merge them together by making a dataframe. Multiple ways to do this.
#Source for making columns and naming them. (https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/)
End = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal)))

#Dataframe will have column titles of 0,1,2,3 etc... Below lines adds the names they should be.
End.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']

#Print dataframe to see that it worked.
print(End)

###############################################################
#This will summarize and combine 2 files.
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

#Append or attached the new summarized data (End2) to the bottom of the first summarization (End).
#Source: (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html)
End.append(End2)

#See the values all together.
Print(End)

###############################################################
#Summarize and combine two files using a loop.
import pandas as pd
import openpyxl
import os

#Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')
End_File = {
    "SMIDS":[],
    "MoneyPaidTotal":[],
    "MoneyJuryTotal":[],
    "MoneyHoneyTotal":[],
    }
print (End_File)

#For loop source (https://www.w3schools.com/python/python_for_loops.asp)
filelist = ["DumpDemo", "DumpDemo2"]
for file in filelist:
    #Comine file path, name, and type. 
    filepath = r'F:\\401K\\1. 401K & ESOP\\User - Karsten\\Project tracking\\TestExcel\\' + str(file) + '.xlsx'
    print(filepath)
    MessyData = pd.read_excel(filepath,sheet_name="Sheet1", engine='openpyxl')

    #This is labelling things for different columns. Grab list of Smids, and summarized data
    SMIDS = MessyData.SMID.unique()

    #This is Python equivalent of Sumif. Sum money paid by each smid.  Report for other columns.
    MoneyPaidTotal = MessyData.groupby(['SMID'])['MoneyPaid'].sum()
    MoneyJuryTotal = MessyData.groupby(['SMID'])['MoneyJury'].sum()
    MoneyHoneyTotal = MessyData.groupby(['SMID'])['MoneyHoney'].sum()

    #Now that we sumiffed all the columns, merge them together by making a dataframe.
    Consolidated_data = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal,MoneyHoneyTotal)))
    Consolidated_data.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal','MoneyHoneyTotal']
    i = 0
    while i <= Consolidated_data.shape[0]-1:

        End_File["SMIDS"].append(Consolidated_data["SMIDS"][i])
        End_File["MoneyJuryTotal"].append(Consolidated_data["MoneyJuryTotal"][i])
        End_File["MoneyPaidTotal"].append(Consolidated_data["MoneyPaidTotal"][i])
        End_File["MoneyHoneyTotal"].append(Consolidated_data["MoneyHoneyTotal"][i])
        i += 1

#Print dataframe to see that it worked.
dfEnd=pd.DataFrame(End_File)
print(dfEnd)

EligibilityCriteria =pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\Fields Eligible.xlsx',sheet_name="Sheet1", engine='openpyxl')
print(EligibilityCriteria)

def filter_eligibility(row,component,include):
    if component in row["Field2"]:
        if include == row["Wages"]:
            return True
        else:
            return False
    else:
        return False

#Filter for just wage fields eligible.
WagesEligibleList = EligibilityCriteria.query("Wages=='Y'")
print(WagesEligibleList)
Wages_eligible = WagesEligibleList.Field2.unique()
print(Wages_eligible )

TotalEligibleWages = dfEnd.groupby(['SMID']Wages_eligible).sum()

dfEnd.to_csv(r'C:\Users\1263654\Desktop\CompileTrial.csv')

###############################################################
#Summarize and combine two large files using a loop. Test using official dump files, adjust fields accordingly.
#Both files were trimmed to 10k lines to make testing quicker.
import pandas as pd
import openpyxl
import os

#This is creating the dataframe and naming the columns outside of the loop so that information can be appended to it later.
End_File = {
    "SMIDS":[],
    "MoneyPaidTotal":[],
    "MoneyJuryTotal":[],
    }

#Prind Dataframe with columns. Not needed, just validation that it worked. 
print (End_File)

#Actual excel file names.
filelist = ["DumpDemo"
            , "DumpDemo2"]

#For each file name in the above, loop through and read it, consolidate columns based on smid, and append 
for file in filelist:
    #Comine file path, name, and file type. 
    filepath = r'F:\\401K\\1. 401K & ESOP\\User - Karsten\\Project tracking\\TestExcel\\' + str(file) + '.xlsx'
    #Reads the data on path specified above as a dataframe called MessyData.
    MessyData = pd.read_excel(filepath,sheet_name="Esop Eligible Summary", engine='openpyxl')

    #This is labelling things for different columns. Grab list of Smids, and summarized data
    SMIDS = MessyData.SMID.unique()

    #This is Python equivalent of Sumif. Sum money paid/slary/wages etc... by each smid. Will need to add other columns (long list).
    SalaryMWagesT = MessyData.groupby(['SMID'])['Salary (M) Wages'].sum() #Column FS
    Hourly_WagesT = MessyData.groupby(['SMID'])['Hourly Wages'].sum() #Column EY

    #Now that we sumiffed all the columns, merge them together by making a dataframe.
    Consolidated_data = pd.DataFrame(list(zip(SMIDS ,SalaryMWagesT, Hourly_WagesT)))
    Consolidated_data.columns = ['SMIDS', 'SalaryMWagesT', 'Hourly_WagesT']

    #For each Smid/ID that was pulled and summarized, loop through and insert as a line into the final dataframe End_File.
    i = 0
    while i <= Consolidated_data.shape[0]-1:
        EndFileConsolidated.append(Consolidated_data["SMIDS"][i])
        End_File["SalaryMWagesT"].append(Consolidated_data["SalaryMWagesT"][i])
        End_File["Hourly_WagesT"].append(Consolidated_data["Hourly_WagesT"][i])
        i += 1

#Print dataframe to see that it worked. Not needed.
dfEnd=pd.DataFrame(End_File)
#Spit this out to a csv. A copy of this was manually saved to the testexcel file area.
dfEnd.to_csv(r'C:\Users\1263654\Desktop\CompileTrial.csv')



#######Abby Way
import pandas as pd
import openpyxl
import os

#This is creating the dataframe and naming the columns outside of the loop so that information can be appended to it later.
EndFileConsolidated = []

#Actual excel file names.
filelist = [r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\Dumpdemo.csv'
            , r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\Dumpdemo2.csv']

#Loop to read all CSVs
for file in filelist:
     Singlefile = pd.read_excel(file,thousands=',',low_memory=False)
     EndFile.append(Singlefile)


#For each file name in the above, loop through and read it, consolidate columns based on smid, and append 
for file in filelist:
    #Comine file path, name, and file type. 
    
    #Reads the data on path specified above as a dataframe called MessyData.
    MessyData = pd.read_excel(filepath,sheet_name="Esop Eligible Summary", engine='openpyxl')

    #This is labelling things for different columns. Grab list of Smids, and summarized data
    SMIDS = MessyData.SMID.unique()

    #This is Python equivalent of Sumif. Sum money paid/slary/wages etc... by each smid. Will need to add other columns (long list).
    SalaryMWagesT = MessyData.groupby(['SMID'])['Salary (M) Wages'].sum() #Column FS
    Hourly_WagesT = MessyData.groupby(['SMID'])['Hourly Wages'].sum() #Column EY

    #Now that we sumiffed all the columns, merge them together by making a dataframe.
    Consolidated_data = pd.DataFrame(list(zip(SMIDS ,SalaryMWagesT, Hourly_WagesT)))
    Consolidated_data.columns = ['SMIDS', 'SalaryMWagesT', 'Hourly_WagesT']

    #For each Smid/ID that was pulled and summarized, loop through and insert as a line into the final dataframe End_File.
    i = 0
    while i <= Consolidated_data.shape[0]-1:
        EndFileConsolidated.append(Consolidated_data["SMIDS"][i])
        End_File["SalaryMWagesT"].append(Consolidated_data["SalaryMWagesT"][i])
        End_File["Hourly_WagesT"].append(Consolidated_data["Hourly_WagesT"][i])
        i += 1

#Print dataframe to see that it worked. Not needed.
dfEnd=pd.DataFrame(End_File)
#Spit this out to a csv. A copy of this was manually saved to the testexcel file area.
dfEnd.to_csv(r'C:\Users\1263654\Desktop\CompileTrial.csv')

###############################################################
#Summarize and combine two files using a loop.
import pandas as pd
import openpyxl
import os
import glob
import numpy

# Create an empty list to store your data frames
frame = []

# Read in all files from Dump folder
files_df = glob.glob(r'F:\\401K\\1. 401K & ESOP\\User - Karsten\\Project tracking\\TestExcel\\Dumps\\'+ 'DumpDemo*'+'.csv')

#Loop to read all CSVs
for file in files_df:
     all_smid_df = pd.read_csv(file,thousands=',',low_memory=False)
     frame.append(all_smid_df)

# Concatenate Dataframes into a single Dataframe
all_smid_df = pd.concat(frame)
print(all_smid_df )
all_smid_df.dtypes

#groupby smid and sum columns
sum_df= all_smid_df.groupby(['SMID']).sum()
print(sum_df)

#sum_df.head()
print(sum_df)
sum_df.dtypes

#sum dataframes by total hours and total wages
sum_df['Total_Money'] =  sum_df.filter(like='Money').sum(axis = 1)

EligibilityCriteria =pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\Fields Eligible.xlsx',sheet_name="Sheet1", engine='openpyxl')
print(EligibilityCriteria)

#Filter for just wage fields eligible.
WagesEligibleList = EligibilityCriteria.query("Wages=='Y'")
#Now just have the column names. If duplicates for any reason, remove.
Wages_eligible = WagesEligibleList.Field.unique()
print(Wages_eligible )

sum_df['Eligible_Money'] =  sum_df.filter(Wages_eligible).sum()
print(sum_df)

sum_df[set(sum_df.columns).intersection(set(Wages_eligible.columns))]

cols = sum_df.columns.intersection(Wages_eligible.columns)
sum_df[cols]
new_column_name = sum_df[cols].sum(axis=1)


sum_df['Eligible_Money'] = sum_df[sum_df.columns.intersection(Wages_eligible.columns)].sum(axis=1)

#dfEnd.to_csv(r'C:\Users\1263654\Desktop\CompileTrial.csv')