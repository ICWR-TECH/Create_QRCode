import requests
import sys

print('''
------------------------------

	Create QR Code

------------------------------

\33[43m\33[30mpython3 create.py "String" "Ukuran" "Nama file"\33[0m
''')

input = str(sys.argv[1])
ukuran = str(sys.argv[2])
namaFile = str(sys.argv[3])

r = requests.get("http://api.qrserver.com/v1/create-qr-code/?data="+input+"&size="+ukuran, allow_redirects=True)

open(namaFile+".png", 'wb').write(r.content)

print("\33[32m\33[1m\33[3mBerhasil mengubah string, nama file = "+namaFile+".png\33[0m\n")
