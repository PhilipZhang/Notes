#!/usr/bin/python2.7
# Filename: backup.py
import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['~/Dropbox/Notes/Python/codes', '~/Dropbox/Notes/Python/notes']
print "source:", source
# 2. The backup must be stored in a main backup directory
target_dir = '~/Dropbox/Notes/Python/backup/'
print "target_dir:", target_dir
# 3. The files are backed up into a zip file

# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command to put the files into a zip archive
sources = ' '.join(source)
print "sources: ", sources
zip_command = "zip -qr %s %s" % (target, sources)
print "zip_command: ", zip_command

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'

