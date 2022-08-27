from os import system, name
import io
import time
import sys
import math

def convertTime(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

## function inputs:
##       filePath - path of file to be read
##       myList - the list to store everything in
def readNStore(filePath,myList):
    with open(filePath) as fp:
        line = fp.readline()
        myList.append(line)
        while line:
            line = fp.readline()
            myList.append(line)
    fp.close()

def del_str(myStr,delStr):
    delStr_index = myStr.find(delStr)
    if delStr_index == -1: ## if the string is not found
        return myStr ## just return the string back
    else: ## otherwise,
        temp = myStr[0:delStr_index] #slice it from 0 until the index it found delStr
        return temp ## then return it

AgentGroupReportHD = []         ## List for storing HD data
AgentGroupReportHD_path = "PATH OF TEXT FILE"
AgentGroupReportSEMS = []       ## List for storing SEMS data
AgentGroupReportSEMS_path = "PATH OF TEXT FILE"
SplitReportALL = []
SplitReportALL_path = "PATH OF TEXT FILE"
HTML_path = "PATH OF HTML TEMPLATE FILE"
##################################
#### Extracted data (Agents) #####
##################################
agentNames = []                     ## List for storing Agent Last, First names 
agentNamesSEMS = []
agentExt = []                       ## List for storing Agent Extension
agentExtSEMS = []
agentState = []
agentStateSEMS = []
agentTime = []
agentTimeSEMS = []
agentCount = 0
agentCountSEMS = 0
##################################
#### Extracted data (Splits) #####
##################################
splits = []
splitAgentsStaffed = []
splitCallsWaiting = []
splitOldestCallTime = []
splitACDcalls = []
splitAvgACD = []
splitState = []
##################################
######## Output HTML File ########
##################################
myHTML = []     ## List for storing HTML file

####################################################################################
###################### Code for reading SplitReportALL.txt #########################
####################################################################################
myHTML = []     ## List for storing HTML file
readNStore(SplitReportALL_path, SplitReportALL)
word = str(SplitReportALL[6]).split(' ',5)
for i in range(word.__len__()):
    splitAvgACD.append(word[i])
# Extract Split Names
word = str(SplitReportALL[0]).split(' ',5)
for i in range(word.__len__()):
    splits.append(word[i])
# Extract Split States
word = str(SplitReportALL[1]).split(' ',5)
for i in range(word.__len__()):
    splitState.append(word[i])
# Extract Splits Calls Waiting
word = str(SplitReportALL[2]).split(' ',5)
for i in range(word.__len__()):
    splitCallsWaiting.append(word[i])
# Extract Splits Oldest Call Time Calls
word = str(SplitReportALL[3]).split(' ',5)
for i in range(word.__len__()):
    splitOldestCallTime.append(word[i])
# Extract Splits Agents Staffed Calls
word = str(SplitReportALL[15]).split(' ',5)
for i in range(word.__len__()):
    splitAgentsStaffed.append(word[i])
# Extract Splits ACD Calls
word = str(SplitReportALL[5]).split(' ',5)
for i in range(word.__len__()):
    splitACDcalls.append(word[i])
####################################################################################
###################### Code for reading AgentGroupReportHD.txt #####################
####################################################################################
readNStore(AgentGroupReportHD_path,AgentGroupReportHD)
####################################################################################
###################### Code for reading AgentGroupReportSEMS.txt #####################
####################################################################################
readNStore(AgentGroupReportSEMS_path, AgentGroupReportSEMS)

agentCount = AgentGroupReportHD.__len__() - 2
agentCountSEMS = AgentGroupReportSEMS.__len__() - 2

word = ""
skip = ["POS Qstns  4215922", "ATTENDANT TIMEOUT", "POS from no action", "HELPDESK", "HARD DOWN STORE", "STR SVC Sems", "ALL OTHER PAYROLL", "STR SVC Sems", "SEMS 8009930093X3528", "INT TIMEOUT", "NEW INT STR 4214143", "PAYRLL TIMEOUT" "SALES AUDIT GMG CASH"]
agentAUXReason = [""] * agentCount
agentAUXReasonSEMS = [""] * agentCountSEMS
## Agent Group Report HD ##
for i in range(1,AgentGroupReportHD.__len__()-1): ## filter out the weird VDN
    word = AgentGroupReportHD[i]
    for k in skip:
        word = del_str(word,j)
    if word == "\n":
        continue
    if word == " ":
        continue
    if word == "":
        continue
    agentTime.append(word)
## Agent Group Report SEMS ##
for i in range(1,AgentGroupReportSEMS.__len__()-1): ## filter out the weird VDN
    word = AgentGroupReportSEMS[i]
    for k in skip:
        word = del_str(word,k)
    if word == "\n":
        continue
    if word == " ":
        continue
    if word == "":
        continue
    agentTimeSEMS.append(word)

for i in range(agentTimeSEMS.__len__()):
    word = agentTimeSEMS[i]
    if word == "\n":
        continue
    if word == " ":
        continue
    if word == "":
        continue
    agentTimeSEMS[i] = word.rsplit(' ',2)[1]

for i in range(agentTime.__len__()):
    word = agentTime[i]
    if word == "\n":
        continue
    if word == " ":
        continue
    if word == "":
        continue
    agentTime[i] = word.rsplit(' ',2)[1]

state = ["AUX", "AUXOUT","AVAIL","ACDIN","ACW","RING","OTHER","UNKNOWN","UNSTAFF"]

for i in range(1,AgentGroupReportHD.__len__()):
    word = AgentGroupReportHD[i]
    for k in range(state.__len__()):
        if(word.find(state[k]) != -1):
            agentState.append(word[word.find(state[k]): word.find(state[k]) + state[k].__len__()    ]       )
for i in range(1,AgentGroupReportSEMS.__len__()):
    word = AgentGroupReportSEMS[i]
    for k in range(state.__len__()):
        if(word.find(state[k]) != -1):
            agentStateSEMS.append(word[word.find(state[k]): word.find(state[k]) + state[k].__len__()    ]       )

readNStore(HTML_path, myHTML)

reasons = "HD SHIFTLEAD", "HD 2ND LVL", "HD PROJECT", "HD HOTQUEUE", "HD LUNCH", "HD BREAK", "HD NOT READY", "HD SEMS", "HD POLLING", "HD BATHROOM"

## HD ########
# iterate through list to extract data
for i in range(1,AgentGroupReportHD.__len__()):
    word = AgentGroupReportHD[i]
    # Extract names from .txt file
    agentNames.append(word[2:word.find(" 42")])
    # Extract Extension from .txt file
    agentExt.append(word[9+word.find(" 42"):(word.find(" 42")+17)])
    word = AgentGroupReportHD[i]
    for k in range(reasons.__len__()):
        if word.find(reasons[k]) != -1:
            inde = word.find(reasons[k])
            leng = reasons[k].__len__()
            word = word[inde:inde+leng]
            agentAUXReason[i-1] = word

## SEMS ##########
for i in range(1,AgentGroupReportSEMS.__len__()):
    word = AgentGroupReportSEMS[i]
    # Extract names from .txt file
    agentNamesSEMS.append(word[2:word.find(" 42")])
    # Extract Extension from .txt file
    agentExtSEMS.append(word[9+word.find(" 42"):(word.find(" 42")+17)])
    
    for k in range(reasons.__len__()):
        if word.find(reasons[k]) != -1:
            inde = word.find(reasons[k])
            leng = reasons[k].__len__()
            word = word[inde:inde+leng]
            agentAUXReasonSEMS[i-1] = word

tableRowStart = "<tr>"
cellStart = "<td>"
tableRowEnd = "</tr>"
cellEnd = "</td>"

for i in range(agentCount):
    temp = int(agentTime[i])
    myHTML[42+i] = tableRowStart
    myHTML[42+i] += cellStart + agentNames[i] + cellEnd
    myHTML[42+i] += cellStart + agentExt[i] + cellEnd
    myHTML[42+i] += cellStart + str(agentAUXReason[i]) + cellEnd
    myHTML[42+i] += cellStart + str(agentState[i]) + cellEnd
    myHTML[42+i] += cellStart + convertTime(temp) + cellEnd
    myHTML[42+i] += tableRowEnd

for i in range(6):
    temp2 = float(splitAvgACD[i])
    temp = math.floor(temp2)
    tmp2 = float(splitOldestCallTime[i])
    tmp = math.floor(tmp2)
    myHTML[122+i] = tableRowStart
    myHTML[122+i] += cellStart + splits[i] + cellEnd
    myHTML[122+i] += cellStart + splitState[i] + cellEnd
    myHTML[122+i] += cellStart + splitAgentsStaffed[i] + cellEnd
    myHTML[122+i] += cellStart + str(splitCallsWaiting[i]) + cellEnd
    myHTML[122+i] += cellStart + convertTime(tmp) + cellEnd
    #myHTML[122+i] += cellStart + str(splitOldestCallTime[i]) + cellEnd
    myHTML[122+i] += cellStart + str(splitACDcalls[i]) + cellEnd
    myHTML[122+i] += cellStart + convertTime(temp) + cellEnd
    myHTML[122+i] += tableRowEnd

for i in range(agentCountSEMS):
    temp3 = int(agentTimeSEMS[i])
    myHTML[94+i] = tableRowStart
    myHTML[94+i] += cellStart + agentNamesSEMS[i] + cellEnd
    myHTML[94+i] += cellStart + agentExtSEMS[i] + cellEnd
    myHTML[94+i] += cellStart + str(agentAUXReasonSEMS[i]) + cellEnd
    myHTML[94+i] += cellStart + str(agentStateSEMS[i]) + cellEnd
    myHTML[94+i] += cellStart + convertTime(temp3) + cellEnd
    myHTML[94+i] += tableRowEnd
    if i == agentCountSEMS:
        myHTML[94+i] += "</tbody></table>"

# Write back to HTML    
outF = open("PATH OF WHERE NEW FILE SHOULD BE WRITTEN","w")
for i in range(myHTML.__len__()):
    outF.write(myHTML[i])
outF.close()
print("success!")
