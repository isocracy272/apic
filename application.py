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
	else netBool = False

	return netBool	

#Function to detect duplicate ACI Contract
def detectDuplicateContract(srcNet,dstNet,dstPort):
	#Open the contracts spreadsheet
	conWorkbook = xlrd.open_workbook("logs.xlsx")
	conSheet = conWorkbook.sheet_by_name('Contracts')

	#Start at the top of Contracts
	conR = 1

	#Define number of rows in Contracts
	numConRows = conSheet.nrows

	#Define duplicate Bool to return
	dupBool = False

	while conR != numConRows and dupBool != True:

		#define log vars
		srcNetEx = conSheet(conR,0)
		dstNetEx = conSheet(conR,1)
		dstPortEx = conSheet(conR,2)

		if srcNet == srcNetEx and dstNet == dstNetEx and dstPort == dstPortEx:
			dupBool = True
		
		conR = conR + 1

	return dupBool

#Main Body - Analyse

#Open the logs workbook
logWorkbook = xlrd.open_workbook("logs.xlsx")
logSheet = logWorkbook.sheet_by_name('logs')

#Start at the top of the logs
logR = 1

#Define number of rows in logs
numLogRows = logSheet.nrows

#Open the network workbook
netWorkbook = xlrd.open_workbook("Network.xlsx")
netSheet = netWorkbook.sheet_by_name('Networks')

#Start at the top of the Networks
netR = 1

#Stop when Network is matched onto
netStop = 0

#Define number of rows in Networks
numNetRows = netSheet.nrows

#Open the contracts spreadsheet
conWorkbook = xlwt.workbook("logs.xlsx")
conSheet = conWorkbook.add_sheet('Contracts')

#Save contracts spreadsheet
conWorkbook.save

#Start at the top of Contracts
conR = 1

#Define number of rows in Contracts
numConRows = conSheet.nrows

#Iterate through firewall logs
while logR != numLogRows:

	#define log vars
	srcIpAddr = logSheet(logR,0)
	dstIpAddr = logSheet(logR,1)
	dstPort = logSheet(logR,2)

	#Find network match for source address
	while netR != numNetRows and netStop = 0:
		srcNetEx = netSheet(netR,0)
		srcMaskEx = netSheet(netR,1)

		#Grab the magic number for the subnet mask
		srcMn = getMagicNumber(srcMaskEx)

		#Does source IP belong to this network?
		srcMatchBool = doesAddrResolveToNetwork(srcIpAddr,srcNetEx,srcMn)

		#If source IP address matches network, break out of while loop
		if srcMatchBool == True:
			netStop = 1
			srcNet = srcNetEx
			srcMask = srcMaskEx

		netR = netR + 1

	#Start back at the top of the network spreadsheet	
	netR = 1

	#Reset while loop
	netStop = 0

	#Find network match for destination address
	while netR != numNetRows and netStop = 0:
		dstNetEx = netSheet(netR,0)
		dstMaskEx = netSheet(netR,1)

		#Grab the magic number for the subnet mask
		dstMn = getMagicNumber(dstMaskEx)

		#Does source IP belong to this network?
		dstMatchBool = doesAddrResolveToNetwork(dstIpAddr,dstNetEx,dstMn)

		#If source IP address matches network, break out of while loop
		if dstMatchBool == True:
			netStop = 1
			dstNet = dstNetEx
			dstMask = dstMaskEx

		netR = netR + 1

	#Start back at the top of the network spreadsheet	
	netR = 1

	#Reset while loop
	netStop = 0

	#Detect duplicate ACI Contract
	logDup = detectDuplicateContract(srcNet,dstNet,dstPort)

	#Write contract to contract spreadsheet

	#Main Body - Configure


	logR = logR + 1

#Close Spreadsheets
netWorkbook.close()
logWorkbook.close()


#ToTheEdge
