## Runs avaya script for Splits Report data
## then updates the HTML
import os
import subprocess
import datetime
ctr = 1
while(True):
	t2 = datetime.datetime.now()
	print("###################################")
	print("Time before running SplitReportALL:", t2)
	# update SplitReportALL.txt
	subprocess.call([r"PATH OF Avaya Script.acsauto"], shell=True)
	# then update HTML file
	t1 = datetime.datetime.now()
	diff = t1 - t2

	print("Time after  running SplitReportALL:", t1)
	print("Iteration:\t",ctr)
	print("Duration:\t",(t1 - t2))
	print()
	os.system("cd <FILE PATH for pyReadBackup.py> && python pyReadBackup.py")
	ctr += 1
	#time.sleep(3)