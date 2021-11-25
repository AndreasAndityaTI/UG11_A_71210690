def calculator():
    print("======== Calculator sederhana ========")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    pil= int(input("Masukkan pilihan: "))
    if pil==1 :
        tambah()
    elif pil==2:
        kurang()
    elif pil==3:
        bagi()
    elif pil==4:
        kali()
    elif pil==5:
        pangkat()
    else :
        print("Maaf input operasi antara 1-5")
    print("")
    return calculator()
 
def tambah():
    bil1=int(input("Masukkan bilangan 1: "))
    bil2=int(input("Masukkan bilangan 2: "))
    hasil=bil1+bil2
    print("Hasilnurutana : ",hasil)

def kurang():
    bil1=int(input("Masukkan bilangan 1: "))
    bil2=int(input("Masukkan bilangan 2: "))
    hasil=bil1-bil2
    print("Hasilnurutana : ",hasil)

def bagi():
    bil1=int(input("Masukkan bilangan 1: "))
    bil2=int(input("Masukkan bilangan 2: "))
    hasil=bil1/bil2
    print("Hasilnurutana : ",hasil)

def kali():
    bil1=int(input("Masukkan bilangan 1: "))
    bil2=int(input("Masukkan bilangan 2: "))
    hasil=bil1*bil2
    print("Hasilnurutana : ",hasil)

def pangkat():
    bil1=int(input("Masukkan bilangan 1: "))
    bil2=int(input("Masukkan bilangan 2: "))
    hasil=bil1**bil2
    print("Hasilnurutana : ",hasil)

calculator() 


