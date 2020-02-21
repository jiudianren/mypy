from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from OpenSSL.crypto import dump_privatekey, dump_publickey,load_privatekey,load_publickey
from cryptography.hazmat.primitives.asymmetric.rsa import *
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM,TYPE_DSA
from cry_l import  *


MY_STRING = "This is my passwd"
pubKey , priKey = get_key()
print(f"pubkey {dump_publickey(FILETYPE_PEM, pubKey)}")
# 从公钥数据中加载公钥
public_key = serialization.load_pem_public_key( dump_publickey(FILETYPE_PEM, pubKey), backend=default_backend())
bytesout = public_key.encrypt(MY_STRING.encode("utf-8"),padding.PKCS1v15())
print(f" data_out：{type(bytesout)} {bytesout}")

# 从私钥数据中加载私钥 这里要注意password是之前在证书里设置得。
private_key = serialization.load_pem_private_key(dump_privatekey(FILETYPE_PEM, priKey), password=None, backend=default_backend())
# 使用私钥对数据进行解密，使用PKCS#1 v1.5的填充方式

if 0:
    out_data = private_key.decrypt(str_out.encode(), padding.PKCS1v15())
    print( f"decrypt:{out_data}")
out_data = private_key.decrypt(bytesout, padding.PKCS1v15())
print( f"decrypt:{out_data}")