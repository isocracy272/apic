#imports
import xlrd

#functions

#Create new BD

#Create new EPG

#Create new Contracts, Subjects and Filters

#Associate Contract with Consumer

#Associate Contract with Provider

#main body

#Open apps
appsWorkbook = xlrd.open_workbook("apps.xlsx")
appsSheet = appsWorkbook.sheet_by_name('apps')

#Start at the top of the logs
appsR = 1

#Define number of rows in logs
numAppsRows = appsSheet.nrows

#Open policy
polWorkbook = xlrd.open_workbook("policy.xlsx")
polSheet = polWorkbook.sheet_by_name('policy')

#Start at the top of the logs
polR = 1

#Define number of rows in logs
numpolRows = polSheet.nrows

app = appsSheet.cell(1,0)
print app

source = polSheet.cell(1,0)
print source






