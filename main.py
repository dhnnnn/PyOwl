import random

print("====================")
print("=== PyOwl Hunter ===")
print("====================\n")

nama = input("Hai masukan nama kamu : ")

while True: 
    # Membuat array goa
    goa = ["|_|", "|_|", "|_|", "|_|"] 

    # Membuat variable yang menampung angka random
    posisi = random.randint(1, 4)


    # Posisi - 1 dikarenakan random pada posisi 1-4 dan index array dimulai dari 0 
    goa[posisi - 1] = "|🦉|" 

    goa = " ".join(goa)


    print("\nPerhatikan goa di bawah ini : \n\n|_|", "|_|", "|_|", "|_|\n")
    pilih = int(input(f"Hai {nama}, tebak dimanakah owl bersarang [1/2/3/4] : "))

    if pilih == posisi :
        print(f"\n{goa}\n\nSelamat kamu menang")
    elif pilih < 0 or pilih > 4 :
        print("\nPilihan kamu tidak ada")
    else:
        print(f"\n{goa}\n\nHAHAHA kamu kalah")

    mulai_ulang = input("\n\nApakah kamu ingin mengulangi gamenya [y/n] : ")
    
    if mulai_ulang == "y":
        continue
    elif mulai_ulang == "n":
        print(f"\nTerimakasih {nama} telah menggunakan program kami, progam akan di hentikan")
        break        
    else:
        print("\nPilih dengan benar dong, progam akan dihentikan")
        break
