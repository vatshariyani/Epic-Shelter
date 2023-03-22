# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Thu Apr 28 14:34:20 2022

@author: Vats Hariyani
"""

import shutil
import os
import win32com.client
import string
strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk")
for objItem in colItems:
    print((''.join(map(str, objItem.DeviceID))), (''.join(map(str, objItem.VolumeName))))#, "\nSerial Number: ", (''.join(map(str, objItem.VolumeSerialNumber))))

def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


#dl1 = objItem.DeviceID

dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        print("New drive(s) attached:\n", (''.join(map(str, x))), objItem.VolumeName, "\nSerial Number: ", (''.join(map(str, objItem.VolumeSerialNumber))))
        
    x = diff(drives, uncheckeddrives)
    if x:
        print("Device(s) ejected:\n", (''.join(map(str, x))), objItem.VolumeName, "\nSerial Number: ", (''.join(map(str, objItem.VolumeSerialNumber))))
        
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    break


#def get_details():
while True:
        print("\nSelect The Drive By Writing The Drive Letter")
        selected_drive = str(input())
        selected_drive = (selected_drive.upper()+":")
        if selected_drive in drives:
            print("You have selected", selected_drive, "drive")
            print("Do you want to select or create folder?(yes/no)")
            ans = str(input())
            if ans.lower()=="yes" or ans.lower()=="y":
                print("Type the path to create or select the folder(without drive)")
                folder = str(input())
                folder = (selected_drive+"\\"+folder)
                print(folder)
                if folder==os.path.exists(folder):
                    print("yes")
                    print("Folder " + folder + "already exists!")
                else:
                    os.mkdir(folder)
                    print("Folder " + folder + " created.")
            else:
                print("Type in folder name to backup your data to!")
                folder=input()
                folder=selected_drive+"\\"+folder
                break
            break
        else:        
            print("You have choosen the drive that does not exists.\n"
                  "Try again")
            #get_details()
        
        break
    
#get_details()

while True:
    cans=(str(input("Do you want to copy just a file or whole folder?\n")))
    if cans.lower()=="file":
        print("Put The Path of what you wanna backup: ")
        location=str(input())
        if location and os.path.exists(location):
            print("Backing up from ", location, " to ", folder)
            print("Backing up file...")
            shutil.copy(location, folder)
            break
        else:
            print("Please put the correct path")
            
    elif cans.lower()=="folder":
        print("Put The Path of what you wanna backup: ")
        location=str(input())
        if location and os.path.exists(location):
            print("Backing up from ", location, " to ", folder)
            print("Backing up folder...")
            shutil.copytree(location, folder)           
            break
        else:
            print("Please put the correct path")
    else:
        print("Incorrect option")


print("Backup Completed!!")
