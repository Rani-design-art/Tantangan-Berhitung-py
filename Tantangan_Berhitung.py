import random
import time

operasi = ('+', '-', '*','/')
min_oper = 2
max_oper = 10
jml_soal = 10

def generate_problem():
    kiri = random.randint(min_oper, max_oper)
    kanan = random.randint(min_oper, max_oper)
    tanda_operasi = random.choice(operasi)

    ekspresi = f"{kiri}{tanda_operasi}{kanan}"
    hasil = eval(ekspresi)
    return ekspresi, hasil 

salah = 0
print('===TANTANGAN BERHITUNG!===')
print('')
input('Pencet untuk Memulai!')
print('---------------------')

waktu_start = time.time()

for i in range(jml_soal):
    ekspresi, hasil = generate_problem()
    while True:
        guess = input('Soal #' + str(i+1) + ' = ' + ekspresi + ' = ')
        if float(guess) == hasil:
            break
        salah += 1

waktu_end = time.time()
waktu_total = waktu_end - waktu_start
print('Waktu = ', waktu_total, 'detik')

print('---------------------')
print('Keren!')
