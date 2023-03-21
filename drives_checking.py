# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:34:20 2022

@author: DELL
"""

import os
import win32com.client
import string
from ctypes import windll
strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk")
for objItem in colItems:
    #xa = []
    #xa.append(objItem.VolumeName)
    #dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    #print(' '.join(map(str, drives)))
    #print(''.join(map(str, objItem.VolumeName)))
    #print(''.join(map(str, objItem.VolumeSerialNumber)))
    print ("Volume Name: ", objItem.VolumeName) 
    #print ("Volume Serial Number: ", objItem.VolumeSerialNumber)
    
                
def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def foo():
    print("New dive introduced")
    print ("Volume Name: ", objItem.VolumeName) 
    print ("Volume Serial Number: ", objItem.VolumeSerialNumber)    


def ham():
    print("Drive disconnected")
    print ("Volume Name: ", objItem.VolumeName) 
    print ("Volume Serial Number: ", objItem.VolumeSerialNumber)
           


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(' '.join(map(str, drives)))

while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        print("New drives:     " + str(x))
        foo()
    x = diff(drives, uncheckeddrives)
    if x:
        print("Removed drives: " + str(x))
        ham()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
