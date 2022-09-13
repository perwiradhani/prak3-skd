import os

def encrypt(text,shift):
    encryption = ("")
    for x in text:
        if x.isupper(): #cek apakah huruf kapital
        # mencari posisi karakter
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
        # melakukan pergeseran
            new_index = (char_index + shift) % 26
        # konversi ke karakter baru
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # menambahkan ke string yang sudah dienkripsi
            encryption = encryption + new_character
        else:
        # karena karakter bukan huruf kapital, biarkan saja
            encryption += x
        
    print("Plain text : ",text)
    print("Cipher Text : ",encryption)


def decrypt(text,shift):
    decryption = ("")
    for x in text:
        if x.isupper():  #cek apakah huruf kapital
        # menemukan posisi dari karakter
            char_unicode = ord(x)
            char_index = char_unicode - ord("A")
        # melakukan pergeseran
            new_index = (char_index - shift) % 26
        # konversi ke karakter baru
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # menambahkan ke string yang sudah didekripsi
            decryption = decryption + new_character
        else:
        # karena karakter bukan huruf kapital, biarkan saja
            decryption += x

    print("Cipher Text: ",text)
    print("Plain Text : ",decryption)


print("==== Caesar Chiper ====")
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")
menu = input("Pilih menu : ")

os.system("cls")

if menu == "1":
    text = input("Enter text: ").upper() # mengubah inputan menjadi huruf kapital
    shift = int(input("Enter key: ")) # memasukkan kunci pergeseran
    encrypt(text,shift)
elif menu == "2":
    text = input("Enter text: ").upper()
    shift = int(input("Enter key: "))
    decrypt(text,shift)
elif menu == "3":
    exit()
else:
    print("Menu tidak tersedia!")