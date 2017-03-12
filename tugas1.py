a = 10;
b = 25;
c = 5;
d = 1;

e = a + b
f = c / d
g = e * f

nama = "Nama : Mochammad Uki Satriana"
npm = "NPM : 1144059"
kelas = "Kelas : D4 TI 3A"

import time
start_time = time.time()
print ("Operasi Aritmatika Lebih dari 1 Operator dan Delta t")
print (nama)
print (npm)
print (kelas)
print ()
print ("Input - (Tiga Lima + Lima Belas) x (Dua / Satu)")
print ("(", a, "+", b,")", "x", "(", c, "/", d,")")
print ("Hasil : ", g)
totalTime = format((time.time() - start_time), '.5f')
print("Delta t : ", totalTime)
print ("Output - Hasil : ", g, " | Delta t : ", totalTime)
