from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM
from OpenSSL.crypto import sign, verify
from OpenSSL.crypto import X509


def sign_verify():
    pk = PKey()
    pk.generate_key(TYPE_RSA, 1024)
    signature = sign(pk, b'hello, world!', 'sha1')
    print(signature)

    x509 = X509()
    x509.set_pubkey(pk)
    verify(x509, signature, b'hello, world!', 'sha1')
    if 0:
        verify(x509, signature, b'hello, world!2', 'sha1')


sign_verify()