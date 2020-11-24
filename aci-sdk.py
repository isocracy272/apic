#imports
import xlrd
import json

#functions

#Format text from csv
def formatText(text):
	text = str(text)
	text = text.replace("text:u","")
	text = text.replace("'","")
	text = text.lower()

	return text

#Convert Python to JSON and pretty print
def convertPythonToJson(pythonObj):
	jsonObj = json.dumps(pythonObj, sort_keys=True, indent=4)
	
	return jsonObj

#Dump Json into file
def dumpJsonToFile(jsonObj,fileName):
	f = open(fileName, "w")
	f.write(jsonObj)
	f.close()


#Create new BD
def createBd(app,tier,environment,tenant,vrf,gateway):
	bdName = environment + "-" + app + "-" + tier

	bdJson = {
	  "fvBD":{
	    "attributes":{
	      "dn":"uni/tn-" + tenant + "/BD-" + bdName + "",
	      "mac":"00:22:BD:F8:19:FF",
	      "name":"" + bdName + "",
	      "rn":"BD-" + bdName + "",
	      "status":"created"},
	      "children":[{
	        "fvRsCtx":{
	          "attributes":{
	            "tnFvCtxName":"" + vrf + "",
	            "status":"created,modified"
	          },
	        "children":[]
	      }
	    }]
	  }
	}

	return bdJson

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

#create apps

#Define variables
app = appsSheet.cell(1,0)
tier = appsSheet.cell(1,1)
environment = appsSheet.cell(1,2)
gateway = appsSheet.cell(1,3)
tenant = appsSheet.cell(1,4)
vrf = appsSheet.cell(1,5)

#format app vars
app = formatText(app)
tier = formatText(tier)
environment = formatText(environment)
gateway = formatText(gateway)
tenant = formatText(tenant)
vrf = formatText(vrf)

#Test function
bdJson = createBd(app,tier,environment,tenant,vrf,gateway)

#pretty printing and convert from Python Dict into JSON
bdJson = convertPythonToJson(bdJson)

#dump Json into file
fileName = "bd.json"
dumpJsonToFile(bdJson,fileName)

#Open policy
polWorkbook = xlrd.open_workbook("policy.xlsx")
polSheet = polWorkbook.sheet_by_name('policy')

#Start at the top of the logs
polR = 1

#Define number of rows in logs
numpolRows = polSheet.nrows

#create policy

#Xlrd Tests
#app = appsSheet.cell(1,0)
#print app

#source = polSheet.cell(1,0)
#print source

#push to apic








