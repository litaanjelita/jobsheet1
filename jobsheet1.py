import random
from guess import Tebak
tebak=Tebak()
tebak.jawaban = random.randint(1, 10)
tebak.tebakan = int(input('tebak angka 1 s.d 10: '))
if (tebak.cek()):
    print("jawaban kamu benar")
else:
    print("jawaban kamu salah")

