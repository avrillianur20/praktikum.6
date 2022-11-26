# praktikum.6
## Nama: Avrillia Nur Hidayah
## NIM: 312210309
## Kelas: TI.22.A3
### Soal

![WhatsApp Image 2022-11-26 at 10 49 23](https://user-images.githubusercontent.com/115686359/204071477-492c3893-309f-490e-8280-91f8ee52ef5f.jpeg)

# Latihan 1
#### Dictionary ditulis dengan dipisahkan koma dalam
```
{}
```
```
telepon = {
    'ike' : '085783345975',
    'lia' : '081286209858'
}
```
#### Untuk menampilkan kontak
```
print(telepon['ike'])
```

#### Untuk menambahkan kamus elemen
```
telepon['mala'] = '085664803961'
```

#### Untuk mengubah kamus sama seperti menambahkannya
```
telepon['sinta'] = '082114241446'
```

#### Untuk menampilkan semua nama digunakkan perintah
```
print(telepon.keys())
```

#### Output hasil nya akan seperti ini
![Screenshot (621)](https://user-images.githubusercontent.com/115686359/204073267-156d9744-3253-4c2e-a46a-c377219da27c.png)

#### Kemudian untuk menampilkan suatu nilai semua nomor menggunakan perintah
```
print(telepon.values())
```

#### Output hasilnya adalah
![Screenshot (621)](https://user-images.githubusercontent.com/115686359/204073331-cf39925b-b05e-4c19-b5f3-b72d1f216238.png)

#### Untuk menampilkan daftar nama dan nomor dengan perintah "for"
```
for nama,nomor in telepon.items():
    print("%s \t| %s " % (nama,nomor))
```

#### Output hasilnya adalah
![Screenshot (621)](https://user-images.githubusercontent.com/115686359/204075423-bb4a89a7-e386-4f1e-b1ff-6fe7c34481ba.png)

#### Hapus kontak Sinta menggunakan perintah
```
del telepon['sinta']
```

#### Ouput yang di hasilkan adalah
![Screenshot (621)](https://user-images.githubusercontent.com/115686359/204075500-ff1d93cc-fd60-44d0-8fd1-c3e14eaff9c1.png)

# Tugas Praktikum

#### Buat Dictionary kosong
```
