import time
import os.path

from settings import *

Functions()

ChangeDate = time.ctime(os.path.getmtime(src + FileName))
print("Ready")

while True:
	NewChangeTime = time.ctime(os.path.getmtime(src + FileName))
	if ChangeDate != NewChangeTime:
		Functions()
		ChangeDate = NewChangeTime

		print('File changed')

