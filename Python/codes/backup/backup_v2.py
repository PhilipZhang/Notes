#!/usr/bin/python2.7
# Filename: backup.py
import os
import time

# The files and directories to be backed up are specified in a list.
source = ['~/Dropbox/Notes/Python/codes', '~/Dropbox/Notes/Python/notes']
# The backup must be stored in a main backup directory
target_dir = '~/Dropbox/Notes/Python/backup/'
# The name of the folder is the date
today = target_dir + time.strftime('%Y%m%d')
# The name of the zip archive is the current time
now = time.strftime('%H%M%S') + '.zip'
# Create the subdirectory if it isn't already there
print "today:", today
if not os.path.exists(today):
	os.system("mkdir "+ today)
	print 'Successfully created directory', today
# We use the zip command to put the files into a zip archive
sources = ' '.join(source)
target = today + os.sep + now
zip_command = "zip -qr %s %s" % (target, sources)
print "zip_command: ", zip_command

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'

