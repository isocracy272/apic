import xlrd
import xlwt

#Open the logs workbook
xl_workbook = xlrd.open_workbook(logs.xlsx)
xl_sheet = xl_workbook.sheet_by_name('logs')

#Start at the top of the logs
logR= 1

#match variables for 
srcNetM = 0
dstNetM = 0

#Iterate through logs and find network
while srcNetM and dstNetM:
	logR = logR + 1



#ToTheEdge
