import base64
import hashlib
import hmac
import simplejson as json

from sys  import argv,exit

def usage():
    print("error")
    print("usage jwtparser --simple token")
    print("usage jwtparser --signed token key")
    exit(0)

def base64_url_decode(inp):
    padding_factor = (4 - len(inp) % 4) % 4
    inp += "="*padding_factor 
    return base64.b64decode(str(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))

def parse_signed_request(signed_request, secret):

    l = signed_request.split('.', 2)
    encoded_sig = l[0]
    payload = l[1]

    sig = base64_url_decode(encoded_sig)
    data = json.loads(base64_url_decode(payload))

    if data.get('algorithm').upper() != 'HMAC-SHA256':
        log.error('Unknown algorithm')
        return None
    else:
        expected_sig = hmac.new(secret, msg=payload, digestmod=hashlib.sha256).digest()

    if sig != expected_sig:
        return None
    else:
        log.debug('valid signed request received..')
    return data
if len(argv)==1:
    usage()
   
arg = argv[1]
if arg == "--signed":
     if len(argv)<3:
         usage()
     print(parse_signed_request(argv[2],argv[3]))
     
elif arg == "--simple":
     if len(argv)<2:
        usage()
     print(base64_url_decode(argv[2]))
else:
     usage()
