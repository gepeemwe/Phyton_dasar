#contoh membuat fungsi baru "greeting"

def greeting ():
    nama = input ("Silahkan Masukkan nama Anda : ")
    print ("Selamat datang", nama)
    print ("Mari Mencoba menulis Kode")
#membuat fungsi "hitungtarif"
def hitungtarif (tarif):
    usia = int(input ("silahkan masukan Usia anda: "))
    jumlahbayar = usia * tarif
    print ("Tarif masuk anda adalah sebesar:", jumlahbayar)

greeting ()
hitungtarif(4000)
