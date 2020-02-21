from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM,TYPE_DSA
from OpenSSL.crypto import dump_privatekey, dump_publickey,load_privatekey,load_publickey
from OpenSSL.crypto import sign, verify
import os
import json
key_dir = "key.json"

def Gen_dsakye():
    pk = PKey()
    print(pk)
    pk.generate_key(TYPE_DSA, 100)
    dpub = dump_publickey(FILETYPE_PEM, pk)  # 生成 pem格式 公钥
    print(dpub)
    dpri = dump_privatekey(FILETYPE_PEM, pk)
    print(dpri)

def gen_ras_key():
    pk = PKey()
    pk.generate_key(TYPE_RSA, 1024)
    dpub = dump_publickey(FILETYPE_PEM, pk)  # 生成 pem格式 公钥
    spub = str(dpub, encoding="utf-8")
    dpri = dump_privatekey(FILETYPE_PEM, pk)
    spri = str(dpri, encoding="utf-8")
    print(dpub)
    if 0:
        print(dpub)
        print(dpri)
        print(spri)
        print(spub)
    info = dict()
    info["type"] = FILETYPE_PEM
    info["pri"] = spri
    info["pub"] = spub
    aj = json.dumps(info)
    fp = open(key_dir, 'w', encoding='utf-8')
    json.dump(aj, fp)
    fp.close()



def get_key():
    if not os.path.exists(key_dir):
        gen_ras_key()
    user_dic = None
    with open(key_dir,"r", encoding="utf-8") as f:
        data = json.loads(json.load(f))

        print(f"{type(data)} data: {data}")
        if  data["type"] ==FILETYPE_PEM:
            priPkey = load_privatekey( FILETYPE_PEM, str.encode(data["pri"]))
            pubPkey = load_publickey(FILETYPE_PEM, str.encode(data["pub"]) )
            print( f" dump_publickey {dump_publickey(FILETYPE_PEM, pubPkey)}")
            return (pubPkey, priPkey)
        else:
            print("erro")
            return (None, None)



MY_STRING = "This is my passwd"

get_key()

