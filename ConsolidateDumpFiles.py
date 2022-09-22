###############################################################
#Summarize and combine two large files using a loop. Test using official dump files, adjust fields accordingly.
#Both files were trimmed to 10k lines to make testing quicker.
import pandas as pd
import openpyxl
import os

#This is creating the dataframe and naming the columns outside of the loop so that information can be appended to it later.
End_File = {
    "SMIDS":[],
    "SalaryMWagesT":[],
    "Hourly_WagesT":[],
    }

#Prind Dataframe with columns. Not needed, just validation that it worked. 
print (End_File)

#Actual excel file names.
filelist = ["paymentlogdump_1010000_thru_1032935_03302022"
            , "paymentlogdump_1032942_thru_1083132_03302022"]

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
        End_File["SMIDS"].append(Consolidated_data["SMIDS"][i])
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

#Data = pd.read_excel(r'F:\401K\1. 401K & ESOP\User - Karsten\Project tracking\TestExcel\DumpDemo.xlsx',sheet_name="Sheet1", engine='openpyxl')
End_File = {
    "SMIDS":[],
    "MoneyPaidTotal":[],
    "MoneyJuryTotal":[],
    }
print (End_File)

#For loop source (https://www.w3schools.com/python/python_for_loops.asp)
filelist = ["DumpDemo", "DumpDemo 2"]
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

    #Now that we sumiffed all the columns, merge them together by making a dataframe.
    Consolidated_data = pd.DataFrame(list(zip(SMIDS ,MoneyPaidTotal, MoneyJuryTotal)))
    Consolidated_data.columns = ['SMIDS', 'MoneyPaidTotal', 'MoneyJuryTotal']
    i = 0
    while i <= Consolidated_data.shape[0]-1:

        End_File["SMIDS"].append(Consolidated_data["SMIDS"][i])
        End_File["MoneyJuryTotal"].append(Consolidated_data["MoneyJuryTotal"][i])
        End_File["MoneyPaidTotal"].append(Consolidated_data["MoneyPaidTotal"][i])
        i += 1

#Print dataframe to see that it worked.
dfEnd=pd.DataFrame(End_File)
print(dfEnd)
dfEnd.to_csv(r'C:\Users\1263654\Desktop\CompileTrial.csv')

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
