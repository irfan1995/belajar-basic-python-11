#for in list
buah = ["apel", "jeruk", "semangka", "nanas"]

for b in buah:
    print(b)

#for in range
for x in range(5):
    print(x)    

for x in range(6,10):
    print(x)   

for x in range(2,20,2):
    print(x)     

for x in range(5,10):
    print("Irfan")    

nama = []

jumlah = int(input("Masukkan jumlah yang diinginkan : "))

for a in range(jumlah):
    nama.append(input("Masukkan nama ke {}: ".format(a+1)))

for a in nama:
    print(a)   

i = 1 #start
while i < 6: #stop
    print(i)
    i = i + 1  #step

#infinite loop
#while True:
    #print("I love you")       

#break 
for x in range(7):
    if x == 4:
        break
    print(x)    

#continue 
for x in range(7):
    if x == 4:
        continue
    print(x)