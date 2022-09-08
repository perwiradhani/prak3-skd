# def encrypt(text,s):
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s) % 26)
#         else:
#             result += chr((ord(char) + s) % 26)
#             return result

# text = ("CEASER CIPHER DEMO")
# s = 4  

# print ("Plain Text : " + text)
# print ("Shift pattern : " + str(s))
# print ("Cipher: " + encrypt(text,s))

def encrypt(text,shift):

    encryption = ("")
    
    
    for c in text:
        if c.isupper():
        # find the position in 0-25
            c_unicode = ord(c)
            c_index = c_unicode - ord("A")
        # perform the shift
            new_index = (c_index + shift) % 26
        # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # append to encrypted string
            encryption = encryption + new_character
        else:
        # since character is not uppercase, leave it as it is
            encryption += c

        

    print("Plain text:",text)
    print("Encrypted text:",encryption)




def decrypt(text,shift):
    decryption = ("")
    for c in text:
        if c.isupper():
        # find the position in 0-25
            c_unicode = ord(c)
            c_index = c_unicode - ord("A")
        # perform the shift
            new_index = (c_index - shift) % 26
        # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # append to encrypted string
            decryption = decryption + new_character
        else:
        # since character is not uppercase, leave it as it is
            decryption += c

    print("Plain text:",text)
    print("Encrypted text:",decryption)


text = input("Enter text: ").upper()
shift = int(input("Enter shift pattern: "))
encrypt(text, shift)