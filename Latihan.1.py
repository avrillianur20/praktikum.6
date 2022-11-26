telepon = {
    'ike' : '085783345975',
    'lia' : '081286209858'
}

print(telepon['ike'])

print("\n")

telepon['mala'] = '085664803961'
telepon['sinta'] = '082114241446'

print(telepon.keys())
print(telepon.values())

print("\n")

print("Nama\t| Nomor Telepon ")
print("======================")

for nama,nomor in telepon.items():
    print("%s \t| %s " % (nama,nomor))

print("\n")

del telepon['sinta']

print("Nama\t| Nomor Telepon")
print("======================")
for key,val in telepon.items():
    print("%s \t| %s " % (key,val))