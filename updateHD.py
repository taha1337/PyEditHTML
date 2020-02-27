## Runs avaya script for Agent Group Report
## then updates the HTML
import os
import subprocess
import datetime
import time
ctr = 1
while(True):
	
	t2 = datetime.datetime.now()
	print("###################################")
	print("Time before running AgentGroupReportHD:", t2)
    # update AgentGroupReport.txt file
	subprocess.call([r"PATH OF Avaya Script.acsauto"], shell=True)
	# then update HTML file
	t1 = datetime.datetime.now()

	print("Time after  running AgentGroupReportHD:", t1)
	print("Iteration:\t",ctr)
	print("Duration:\t",(t1 - t2))
	print()
	os.system("cd <FILE PATH for pyReadBackup.py> && python pyReadBackup.py")
	ctr += 1
	time.sleep(4)