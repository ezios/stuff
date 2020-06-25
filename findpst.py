import os 
import sys
from subprocess import check_output
import time
def walker(path,searchword=b'!BDN'):
    res=[]
    i=0
    out=""
    for root,dirs,files in os.walk(path):
        for FileName in files:
            
            FilePath = os.path.join(root, FileName)
            
            try:
                out = str(check_output(["file",FilePath]))
            except:
                print("error for "+ FilePath)
            if "Microsoft Outlook email" in out:
                print('[+] '+str(i)+FilePath)
                i+=1
                res.append(FilePath)
    if len(res) == 0:
        return "[-] No "+ searchword + " Found"
    return res

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print('usage findpst <root_directory> <magic_number>')
    print("[+] Running ")
    a = time.time()
    p = walker(path)
    print(p)
    with open("respst.txt","w") as f:
        f.write("\n".join(p))
    print(time.time()-a)
    print("[+] Done")
