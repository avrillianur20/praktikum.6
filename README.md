# praktikum.6
## Nama: Avrillia Nur Hidayah
## NIM: 312210309
## Kelas: TI.22.A3
### Soal

![WhatsApp Image 2022-11-26 at 10 49 23](https://user-images.githubusercontent.com/115686359/204071477-492c3893-309f-490e-8280-91f8ee52ef5f.jpeg)

# Latihan 1
#### Dictionary ditulis dengan dipisahkan koma dalam
```{}```
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
mahasiswa = {}
```
##### 1. Buat program untuk lihat data nya

```
def show():
    if mahasiswa.items():
        print("Daftar Nilai")
        print("=================================================================================")
        print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
        print("=================================================================================")
        i = 0
        for a in mahasiswa.items():
            i += 1
            print("| {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |      {5:6.2f} |"
                  .format(a[0][: 14], a[1][0], a[1][1], a[1][2], a[1][3], a[1][4], no=i))
        print("=================================================================================")

    else:
        print("Daftar Nilai")
        print("=================================================================================")
        print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
        print("=================================================================================")
        print("|                                TIDAK ADA DATA                                 |")
        print("=================================================================================")
```
"else" Digunakan untuk menampilkan jika ada nama yang diketik tidak ada.

##### Outputnya adalah
![Screenshot (622)](https://user-images.githubusercontent.com/115686359/204092088-9cff7aff-9382-4c72-b404-dd8689f4145a.png)

##### 2. Program untuk menambahkan data nya
```
def add():
    print("Tambah Data")
    nama = input("Nama\t : ")
    nim = input("NIM\t : ")
    uts = int(input("Nilai UTS\t : "))
    uas = int(input("Nilai UAS\t : "))
    tugas = int(input("Nilai Tugas\t : "))
    akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
    mahasiswa[nama] = nim, tugas, uts, uas, akhir
```
##### Output nya adalah
![Screenshot (623)](https://user-images.githubusercontent.com/115686359/204093032-459ba695-0640-472d-a479-7073cfaabc0e.png)

![Screenshot (627)](https://user-images.githubusercontent.com/115686359/204094085-d847e2b8-c53c-4a99-befa-69c4686f610b.png)

![Screenshot (628)](https://user-images.githubusercontent.com/115686359/204094179-6b3f0db6-b487-4e80-95a8-0d3a147562dc.png)

##### 3. Buat program untuk menghapus data
```
def delete():
    print("Hapus Data")
    nama = input("Masukkan Nama : ")

    if nama in mahasiswa.keys():
        del mahasiswa[nama]

    else:
        print("Nama tidak ditemukan")
```
##### Outputnya adalah
![Screenshot (625)](https://user-images.githubusercontent.com/115686359/204093404-8585f309-2ee8-4862-bf72-ae27841ed078.png)

Data akan terhapus

![Screenshot (625)](https://user-images.githubusercontent.com/115686359/204093460-6cd5234b-a0c7-43d6-9fad-772884983c0f.png)

##### 4. Program untuk mencari data
```
def search():
    print("Cari Data")
    a = input("Masukkan Nama : ")
    if a in mahasiswa.keys():
        print("===========================================================================")
        print("|      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir   |")
        print("===========================================================================")
        print("| {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |     {5:6.2f} |"
              .format(a, mahasiswa[a][0], mahasiswa[a][1], mahasiswa[a][2], mahasiswa[a][3], mahasiswa[a][4]))
        print("===========================================================================")
 else:
        print("=================================================================================")
        print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
        print("=================================================================================")
        print("|                          DATA TIDAK DITEMUKAN                                 |")
        print("=================================================================================")
```
##### Output yang keluar adalah
![Screenshot (626)](https://user-images.githubusercontent.com/115686359/204094295-ec18da03-d3ce-440a-a0de-a3855c089a8a.png)

program ini untuk mencari data yang di inputkan

##### 5. Program untuk menunya
```
def menu():
    print("\n")
    print("================================")
    print("      Program input nilai       ")
    print("================================\n")

    x = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
    print("\n")

    if x == 'L':
        show()
    elif x == 'T':
        add()
    elif x == 'U':
        update()
    elif x == 'H':
        delete()
    elif x == 'C':
        search()
    elif x == 'K':
        print("==========================================================================")
        print('\n')
        print("> You exit the code                        ")
        print("\n")
        print("==========================================================================")

        exit()

    else:
        print("            KODE YANG ANDA MASUKKAN TIDAK VALID !!!!!!!!!!!")

```
program ini bisa diketik L/T/U/H/C/K, maka akan menjalankan perintah program tersebut.
```show()```, ```add()```, ```update()```, ```delete()```, ```search()```

##### 6. Kode yang akan berjalan menggunakan perintah
```
while True:
    menu()
```
##### Output Keluar
![Screenshot (629)](https://user-images.githubusercontent.com/115686359/204095185-9b3bf7a2-5395-43bc-8964-dbb926c5baab.png)

##### 7. Mengubah data
![Screenshot (630)](https://user-images.githubusercontent.com/115686359/204096728-f9a29c23-28f9-4ae4-94cb-8950fbe656fe.png)

Maka data nya akan otomatis berubah

![Screenshot (630)](https://user-images.githubusercontent.com/115686359/204096780-a9b4ffc8-9e0c-4d9a-abf3-8fcdba0174d8.png)

# Flowchart
