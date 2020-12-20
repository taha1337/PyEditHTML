# PyEditHTML
Launches Avaya CMS scripts to generate text data files, then inserts that data into a local HTML table.

To use this for your organization, follow these instructions:
1. Add the SERVER IP in the acsauto scripts, then change the file path for where the text files will be saved.
2. Edit/delete pyReadBackup.py, updateHD.py/updateSEMS.py/updateSplit.py and change the file paths accordingly
3. Next, run the update*.py script and it will run every x seconds depending on value of x in time.sleep(x) is in update*.py
