#!/usr/bin/python3

# This file are executable, and it`s require a root permissions

import os
import shutil
from pathlib import Path

def copy():
	parent = Path(os.getcwd()).parent
	if os.path.exists('/root/extboosting'):
		shutil.rmtree('/root/extboosting')
	shutil.copytree(str(parent) , '/root/extboosting/')
	if True:
		print('Sources are copied')

copy()
