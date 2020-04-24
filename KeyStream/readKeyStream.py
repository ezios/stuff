import base64
import struct
import sys
import string
import re
from datetime import datetime
"""chall"""
#qwerty 

def usage():
    print("usage : read_key_stream input_file <-b64>")
    sys.exit()

def todic(input_event):
    """format to dict type : dic["key_name"] = keycode from input-events-codes.h
    https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h"""
    with open(input_event,"r") as f:
        inputs = f.readlines()
    for i in range(len(inputs)):
        inputs[i] = inputs[i].replace("#define","")
    keys = {}
    c=[]
    for line in inputs:
        m = re.search("(?P<key_name>^ KEY\w+)",line)
        n = re.search("(?P<code>[0-9][abcdefx0-9 -]*$)",line)
        if n and m:
            m = m.group("key_name").replace("KEY_","")
            keys[n.group('code')] = m.lower()
    return keys

def read_file(fic):
    if len(sys.argv) <= 2:
        with open(fic,'rb') as f:
             stream = f.read()
    else: 
        with open(fic,'r') as f:
            text = f.read()
        text = text.replace("\n","")
        stream = base64.b64decode(text)
    return stream

try :
    input_file = sys.argv[1]
except:
    usage()

bin_stream = read_file(input_file)
data = struct.iter_unpack("4IHHI",bin_stream)
"""
data[0], data [1], data [2] , data[3]  --->  timeval
data[4]  --->  type   , type 1 == key_press
data[5]  --->  key code 
data[6]  ---> value   ( 1-- press , 0 --release , 2 -- long press)"""


rawkeys = []
dtext=[]
keys = todic("input-event-codes.h")
for d in data:
    if d[4] == 1 :
        if d[6] in [1,2]:
            rkey= keys[str(d[5])]
            dtext.append(rkey)
            rawkeys.append('{:>12} \t {} '.format(rkey,datetime.fromtimestamp(d[0])))
           
raw = "\n".join(rawkeys)
dummytext = "".join(dtext)
dummytext = dummytext.replace("tab","\t")
dummytext = dummytext.replace("enter","\n")


with open(input_file+"-raw","w") as f : 
    f.write(raw)
with open(input_file+"-text","w") as f:
    f.write(dummytext)






