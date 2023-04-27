#contoh membuat fungsi baru "greeting"

def greeting ():
    nama = input ("Silahkan Masukkan nama Anda : ")
    print ("Selamat datang", nama)
    print ("Mari Mencoba menulis Kode")
greeting ()
usia = int(input ("silahkan masukan Usia anda: "))
# fungsi identifikasi kategori usia usia
if usia < 17:
    print ("anda masih anak-anak")
else :
    print ("anda sudah Dewasa")
#membuat fungsi "hitungtarif"
def hitungtarif (tarif):
    jumlahbayar = usia * tarif
    print ("Tarif masuk anda adalah sebesar:", jumlahbayar)

hitungtarif(350)