import xlrd
import xlwt

#Open the logs workbook
logWorkbook = xlrd.open_workbook(logs.xlsx)
logSheet = logWorkbook.sheet_by_name('logs')

#Start at the top of the logs
logR = 1

#Define number of rows in logs
numLogRows = logSheet.nrows

#Open the network workbook
netWorkbook = xlrd.open_workbook(Network.xlsx)
netSheet = netWorkbook.sheet_by_name('Networks')

#Start at the top of the Networks
netR = 1

#Define number of rows in Networks
numNetRows = netSheet.nrows

#define match variables 
srcNetM = 0
dstNetM = 0

#Iterate through firewall logs
while logR != numLogRows:

	#Find network match for source address
	while srcNetM = 0:
	

	logR = logR + 1



#ToTheEdge
