#Imports
import xlrd
import xlwt

#Functions

#Function to derive Magic Number from subnet mask
def getMagicNumber(mask):
	if mask = 30:
		mn = 4
	if mask = 29:
		mn = 8
	if mask = 28:
		mn = 16
	if mask = 27:
		mn = 32
	if mask = 26:
		mn = 64
	if mask = 25:
		mn = 128
	if mask = 24:
		mn = 256
	if mask = 23:
		mn = 512
	if mask = 23:
		mn = 1024

	return mn

#Function to see if an IP address is part of a network
def doesAddrResolveToNetwork(ipAddr,netId,mn):
	broadcatId = netId + mn

	if netId < ipAddr < broadcatId:
		netBool = True

	return netBool	

#Main Body

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

#Iterate through firewall logs
while logR != numLogRows:

	#Find network match for source address
	while netR != numNetRows:
		srcIpLog = logSheet(logR,0)
		srcNet = netSheet(netR,0)
		srcMask = netSheet(netR,1)

		#Grab the magic number for the subnet mask
		srcMn = getMagicNumber(srcMask)

		#Does source IP belong to this network?
		srcMatchBool = doesAddrResolveToNetwork(srcIpLog,srcNet,srcMn)



		netR = netR + 1

	#Start back at the top of the network spreadsheet	
	netR = 1

	#Find network match for destination address
	while netR != numNetRows:
		

		netR = netR + 1




	

	logR = logR + 1



#ToTheEdge
