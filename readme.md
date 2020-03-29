# Genereate keypair

openssl genrsa -out jetqin.key 2048
openssl rsa -in ./config/jetqin.key -pubout > ./config/jetqin.pub

openssl req -new -key jetqin.key -out jetqin.csr -subj "/CN=jetqin/O=dev"\n
