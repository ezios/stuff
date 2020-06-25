from shutil import copyfile
import sys

filepath = sys.argv[1]
destination = sys.argv[2]

def filename(file):
  return file.split("/")[-1]
  
with open(filepath,"r") as f:
	files = f.read().split("\n")

for file in files:
    print('copying '+ file)
    copyfile(file,destination+filename(file))
   
