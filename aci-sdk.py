#imports
import xlrd
import json
import requests

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
	f = open(fileName, "a")
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
def createEPG(app,tier,environment,tenant,vmm1,vmm2):
	epgName = environment + "-" + app + "-" + tier
	bd = environment + "-" + app + "-" + tier

	epgJson = {
	  "totalCount": "1",
	  "imdata": [
	    {
	      "fvAp": {
	        "attributes": {
	          "annotation": "",
	          "descr": "",
	          "dn": "uni/tn-" + tenant + "/ap-" + app + "",
	          "name": "" + app + "",
	          "nameAlias": "",
	          "ownerKey": "",
	          "ownerTag": "",
	          "prio": "unspecified"
	        },
	        "children": [
	          {
	            "fvAEPg": {
	              "attributes": {
	                "annotation": "",
	                "exceptionTag": "",
	                "floodOnEncap": "disabled",
	                "fwdCtrl": "",
	                "hasMcastSource": "no",
	                "isAttrBasedEPg": "no",
	                "matchT": "AtleastOne",
	                "name": "" + epgName + "",
	                "nameAlias": "",
	                "pcEnfPref": "unenforced",
	                "prefGrMemb": "exclude",
	                "prio": "unspecified",
	                "shutdown": "no"
	              },
	              "children": [
	                {
	                  "fvRsCustQosPol": {
	                    "attributes": {
	                      "annotation": "",
	                      "tnQosCustomPolName": ""
	                    }
	                  }
	                },
	                {
	                  "fvRsBd": {
	                    "attributes": {
	                      "annotation": "",
	                      "tnFvBDName": "" + bd + ""
	                    }
	                  }
	                },
	                {
					  "fvRsDomAtt": {
					    "attributes": {
					      "resImedcy": "immediate",
					      "tDn":"uni/vmm-" + vmm1 + "",
					      "status":"created"
					    },
					  "children":[]
					  }
					},
					{
					  "fvRsDomAtt": {
					    "attributes": {
					      "resImedcy": "immediate",
					      "tDn":"uni/vmm-" + vmm2 + "}",
					      "status":"created"
					    },
					  "children":[]
					  }
					}
	              ]
	            }
	          }
	        ]
	      }
	    }
	  ]
	}

	return epgJson

#Login to APIC
def getCredentialsJson():
	login = { "aaaUser" : { "attributes": {"name":"admin","pwd":"ciscopsdt" } } } 

	return login

#Push to API
def pushJsonToApi():
	login = getCredentialsJson()
	login = convertPythonToJson(login)

	url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
	resp  = requests.post(url=url,json=login)

	return resp

#main body

#Open apps
appsWorkbook = xlrd.open_workbook("apps.xlsx")
appsSheet = appsWorkbook.sheet_by_name('apps')

#Start at the top of the logs
appsR = 1

#Define number of rows in logs
numAppsRows = appsSheet.nrows

#create bds
while appsR != numAppsRows:

	#Define variables
	app = appsSheet.cell(appsR,0)
	tier = appsSheet.cell(appsR,1)
	environment = appsSheet.cell(appsR,2)
	gateway = appsSheet.cell(appsR,3)
	tenant = appsSheet.cell(appsR,4)
	vrf = appsSheet.cell(appsR,5)

	#format app vars
	app = formatText(app)
	tier = formatText(tier)
	environment = formatText(environment)
	gateway = formatText(gateway)
	tenant = formatText(tenant)
	vrf = formatText(vrf)

	#Create BD
	bdJson = createBd(app,tier,environment,tenant,vrf,gateway)

	#pretty printing and convert from Python Dict into JSON
	bdJson = convertPythonToJson(bdJson)

	#dump Json into file
	fileName = "bd.json"
	dumpJsonToFile(bdJson,fileName)

	appsR = appsR + 1

#start back at the top of apps
appsR = 1

#Create new EPG

while appsR != numAppsRows:

	#Define variables
	app = appsSheet.cell(appsR,0)
	tier = appsSheet.cell(appsR,1)
	environment = appsSheet.cell(appsR,2)
	gateway = appsSheet.cell(appsR,3)
	tenant = appsSheet.cell(appsR,4)
	vrf = appsSheet.cell(appsR,5)
	vmm1 = appsSheet.cell(appsR,6)
	vmm2 = appsSheet.cell(appsR,7)

	#format app vars
	app = formatText(app)
	tier = formatText(tier)
	environment = formatText(environment)
	gateway = formatText(gateway)
	tenant = formatText(tenant)
	vrf = formatText(vrf)
	vmm1 = formatText(vmm1)
	vmm2 = formatText(vmm2)
	
	#Create App Profile and EPG
	epgJson = createEPG(app,tier,environment,tenant,vmm1,vmm2)

	#pretty printing and convert from Python Dict into JSON
	epgJson = convertPythonToJson(epgJson)

	#dump Json into file
	fileName = "epg.json"
	dumpJsonToFile(epgJson,fileName)

	appsR = appsR + 1

#Associate VMM Domain with EPG

#Create new Contracts, Subjects and Filters

#Associate Contract with Consumer

#Associate Contract with Provider

#resp = pushJsonToApi()
#print(resp.status_code)
#print(resp.text)

#Open policy
polWorkbook = xlrd.open_workbook("policy.xlsx")
polSheet = polWorkbook.sheet_by_name('policy')

#Start at the top of the logs
polR = 1

#Define number of rows in logs
numpolRows = polSheet.nrows

#create policy

#push to apic








