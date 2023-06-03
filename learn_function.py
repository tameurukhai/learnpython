# di python function yang ga return nilai dan ga minta params itu disebut prosedur
# kalau yang return nilai itu function

def hitung_luas(panjang1, lebar1):
    hasil = int(panjang1) * int(lebar1)
    return hasil

panjang = input("Masukan panjang: ")
lebar = input("Masukan lebar: ")


print("Hasil panjang x lebar:", hitung_luas(panjang, lebar))