# User Input

nama = input("Masukkan Nama Anda: ") #default string
umur = input("Masukkan Umur Anda ")


print("Nama Saya Adalah :" + nama)

#Menghitung luas persegi panjang

p = int(input("Masukkan Panjang : "))
l = int(input("Masukkan Lebar : "))

L = p * l
K = (p*l)*2
print("Luas persegi panjang adalah {} cm dan Keliling persegi panjang {} cm".format(L,K))

x = "Indonesia"
y = "AI"
print (x + " " + y)

#String Operation
a = "Hello World"
print(a[1])
print(a[2:6]) #mulai dari 2 sampai 5
print(len(a))

#Condition 
a = 100
b = 20

if b < a:
    print("Nilai b lebih kecil dari a")
elif b==a:
    print("Nilai b sama dengan nilai a")
else:
    print("Nilai b lebih besar dari nilai a")        

nilai = int(input("Masukkan nilai: "))
kkm = 70

if nilai < kkm:
    print("Anda tidak lulus")
else:
    print("Anda Lulus")    

#List 
y = [1, 2, 3, 4, 5] 
print(y[1])   

makanan = ["Soto", "Sate", "Mie Ayam"]
makanan.append("Bakso")
print(makanan)

#mengganti minuman
#minuman = ["teh manis", "kopi", "kopi susu"]

#minuman[0] = input("Minuman pengganti: ")

#print(minuman)
