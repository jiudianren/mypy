from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from OpenSSL.crypto import dump_privatekey, dump_publickey,load_privatekey,load_publickey
from cryptography.hazmat.primitives.asymmetric.rsa import *
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM,TYPE_DSA
from OpenSSL.crypto import PKey
from OpenSSL.crypto import dump_privatekey, dump_publickey,load_privatekey,load_publickey
from OpenSSL.crypto import sign, verify
import os
import json

import logging
import  base64

# log实例
logger = logging.getLogger("defalut")
# 创建handler 写到控制台，或者日志文件等
hds = logging.StreamHandler()
logger.addHandler(hds)
logger.setLevel(logging.DEBUG)


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
        if  data["type"] ==FILETYPE_PEM:
            priPkey = load_privatekey( FILETYPE_PEM, str.encode(data["pri"]))
            pubPkey = load_publickey(FILETYPE_PEM, str.encode(data["pub"]) )
            #print( f" dump_publickey {dump_publickey(FILETYPE_PEM, pubPkey)}")
            return (pubPkey, priPkey)
        else:
            print("erro")
            return (None, None)




def encrypt( mystr):
    pubKey,priKey = get_key()
    #logger.debug(f"pubkey:{dump_publickey(FILETYPE_PEM, pubKey)}")
    # 从公钥数据中加载公钥
    public_key = serialization.load_pem_public_key( dump_publickey(FILETYPE_PEM, pubKey), backend=default_backend())
    bytesout = public_key.encrypt(mystr.encode("utf8"),padding.PKCS1v15())  # str-->bytes
    logger.debug(f"data_out：{type(bytesout)} {bytesout}")  #  加密成bytes
    strout = str(base64.b32encode(bytesout),encoding="utf8") # base64转化bytes成bytes  再转成str
    logger.debug(f"base64.b32encode str result: {type(strout)} : {strout}")
    return strout


def decrtyp(base64encodstr):
    bytesout = base64.b32decode(base64encodstr)  # str -->解成bytes
    logger.debug(f"base64.b32decode bytes result: {type(bytesout)} : {bytesout}")

    pubKey, priKey = get_key()
    # 从私钥数据中加载私钥 这里要注意password是之前在证书里设置得。
    private_key = serialization.load_pem_private_key(dump_privatekey(FILETYPE_PEM, priKey), password=None, backend=default_backend())
    # 使用私钥对数据进行解密，使用PKCS#1 v1.5的填充方式
    out_data = private_key.decrypt(bytesout, padding.PKCS1v15())
    logger.debug( f"decrypt:{out_data}")
    return out_data



if __name__ == "__main__":
    MY_STRING = "This is my passwd"
    encry_out = encrypt(MY_STRING)
    real_str  = decrtyp(encry_out)
    real_str = str(real_str, encoding="utf8")
    if real_str != MY_STRING:
        logger.error(f"Erro： {MY_STRING}:{real_str}")
    else:
        logger.debug("sucess!!!")