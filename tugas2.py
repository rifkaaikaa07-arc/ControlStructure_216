#menentukan angka terbesar
no1 = float(input("Masukkan angka pertama: "))
no2 = float(input("Masukkan angka kedua: "))
no3 = float(input("Masukkan angka ketiga: "))

if no1 >= no2 and no1 >= no3:
    terbesar = no1
elif no2 >= no1 and no2 >= no3:
    terbesar = no2
else:
    terbesar = no3
 
print("Yang terbesar adalah:", terbesar)