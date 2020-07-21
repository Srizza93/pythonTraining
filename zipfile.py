import os
import sys
import shutil
import zipfile('Backup_22Feb2020.zip')
import traceback


print ('Welcome to USB Backup Utility')
print ('Created by: TheCryptek')
print ('\nWhat directory would you like to back up?')
print ('/Users/martina/Desktop/FOTO')
backUp = raw_input('> ') # Files the user specified to back up
print ('\nWhere would you like to back these files up at?')
print ('/Users/martina/Desktop/Backup')
backDevice = raw_input('> ') # Device the user specified to save the back up on.
print ('\nName of the zip file you prefer?')
print ('Example: Backup.zip')
backZip = raw_input('> ') # The name of the zip file specified by the user
print ('\nBackup started...')

if not os.path.exists(backDevice + '/BackUp'): # If the BackUp folder doesn't exist on the device then
    os.mkdir(backDevice + 'BackUp') # Make the backup folder on usb device

bkZip = zipfile.ZipFile(backZip, 'w') # Not sure what to say for lines 21 - 26
for dirname, subdirs, files in os.walk(backUp):
    bkZip.write(dirname)
    for filename in files:
        bkZip.write(os.path.join(dirname, filename))
    bkZip.close()

#print backZip,backDevice
dest = backDevice + '/BackUp'
#print dest
shutil.move(backZip, dest) # Move the zip files created in working directory to the specified back up device -[ Something is wrong with this can't figure out what ]-
print('Backup finished.')
