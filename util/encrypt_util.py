import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RSAEncryption:

    def __init__(self, private_path, public_path):
        self.private_key_path = private_path
        self.public_key_path = public_path

    def encrypt(self, value):
        with open(self.public_key_path) as secretfile:
            public_key = RSA.import_key(secretfile.read())
            rsa_public_key = PKCS1_OAEP.new(public_key)
            encrypt_text = rsa_public_key.encrypt(value.encode())
            return binascii.hexlify(encrypt_text)

    def decrypt(self, value):
        with open(self.private_key_path) as secretfile:
            private_key = RSA.import_key(secretfile.read())
            rsa_private_key = PKCS1_OAEP.new(private_key)
            return rsa_private_key.decrypt(binascii.unhexlify(value)).decode('utf-8')


if __name__ == '__main__':
    rsa = RSAEncryption('../config/jetqin.key', '../config/jetqin.pub')
    data = rsa.encrypt('dbuser')
    print(data)
    print(rsa.decrypt(data))
