import os
import json
import logging
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from OpenSSL.crypto import dump_privatekey, dump_publickey,load_privatekey,load_publickey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM,TYPE_DSA
from OpenSSL.crypto import PKey

#pip install pyopenssl


# log实例
logger = logging.getLogger("defalut")
# 创建handler 写到控制台，或者日志文件等
hds = logging.StreamHandler()
logger.addHandler(hds)
logger.setLevel(logging.DEBUG)

key_dir = "key.json"

def gen_dsa_key():
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
    dpri = dump_privatekey(FILETYPE_PEM, pk)


    spub = str(dpub, encoding="utf-8")
    spri = str(dpri, encoding="utf-8")

    info = dict()
    info["type"] = FILETYPE_PEM
    info["pri"] = spri
    info["pub"] = spub

    aj = json.dumps(info)    # dict 转成 json

    fp = open(key_dir, 'w', encoding='utf-8')
    json.dump(aj, fp, indent=4)
    fp.close()


def get_key():
    if not os.path.exists(key_dir):
        gen_ras_key()

    with open(key_dir,"r", encoding="utf-8") as f:
        data = json.loads(json.load(f)) # load 先读json   loads 将json转成dict

        if data["type"] == FILETYPE_PEM:
            pri_pkey = load_privatekey( FILETYPE_PEM, str.encode(data["pri"]))
            pub_pkey = load_publickey(FILETYPE_PEM, str.encode(data["pub"]) )
            return (pub_pkey, pri_pkey)
        else:
            print("erro!!")
            return (None, None)


def encrypt( pubKey, mystr):
    '''

    :param pubKey: pem格式公钥
    :param mystr:
    :return:
    '''
    #logger.debug(f"pubkey:{dump_publickey(FILETYPE_PEM, pubKey)}")
    # 从pem格式公钥中加载公钥
    public_key = serialization.load_pem_public_key( dump_publickey(FILETYPE_PEM, pubKey), backend=default_backend())
    bytesout = public_key.encrypt(mystr.encode("utf8"), padding.PKCS1v15())  # str-->bytes

    logger.debug(f"data_out：{type(bytesout)} {bytesout}")  #  加密成bytes
    re = str(base64.b32encode(bytesout),encoding="utf8") # base64转化bytes成bytes  再转成str
    logger.debug(f"base64.b32encode str result: {type(re)} : {re}")
    return re


def decrypt(priKey, base64encoded_str):
    '''

    :param priKey:  pem 格式私钥
    :param base64encoded_str:
    :return:
    '''
    bout = base64.b32decode(base64encoded_str)  # str -->解成bytes
    logger.debug(f"base64.b32decode bytes result: {type(bout)} : {bout}")

    # 从私钥数据中加载私钥 这里要注意password是之前在证书里设置得。如果没有设置成None
    private_key = serialization.load_pem_private_key(dump_privatekey(FILETYPE_PEM, priKey), password=None, backend=default_backend())
    # 使用私钥对数据进行解密，使用PKCS#1 v1.5的填充方式
    out_data = private_key.decrypt(bout, padding.PKCS1v15())
    logger.debug( f"decrypt:{out_data}")
    return out_data



if __name__ == "__main__":
    MY_STRING = "This is my passwd"

    pubKey, priKey = get_key()
    encry_out = encrypt(pubKey,MY_STRING)    # encry_out 写到对外发布的地方，别人即使拿到这个也没用
    real_str  = decrypt(priKey,encry_out)
    real_str = str(real_str, encoding="utf8")
    if real_str != MY_STRING:
        logger.error(f"Erro：{MY_STRING}:{real_str}")
    else:
        logger.debug("sucess!!!")