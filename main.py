#Python 3.8.0
#Make by Lonely Dark

import argparse
import os

parser=argparse.ArgumentParser()

parser.add_argument('-r', '--recursive', help='recursive add files', action='store_true')
parser.add_argument('-d', '--directory', help='directory where the files(or file) are. If file one, input file with full name', required=True)

args=parser.parse_args()

if args.recursive:
	
	os.chdir(args.directory)
	files=os.listdir()
	
	for e in files:
		try:

			file1=open(e,'rb')
			file2=open('backup_'+e, 'wb')
			file2.write(file1.read())
			file1.close()
			file2.close()

		except PermissionError:

			os.chdir(e)
			files=os.listdir()
			for e in files:
				file1=open(e,'rb')
				file2=open('backup_'+e, 'wb')
				file2.write(file1.read())
				file1.close()
				file2.close()
			os.chdir(args.directory)
			continue

else:

	file1=open(args.directory, 'rb')
	file_name=args.directory.split('.')
	file2=open(file_name[0]+'_backup'+'.'+file_name[1], 'wb')
	file2.write(file1.read())
	file1.close()
	file2.close()
