alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceasar(input_text,shift_no,direction):
    out_text=""
    if direction=="decode":
        shift_no*=-1
    for char in input_text:
        if char in alphabet:
            pos=alphabet.index(char)
            new_pos=pos+shift_no
            out_text+=alphabet[new_pos]
        else:
            out_text+=char
    print(f"The {direction}d text is {out_text}")
cont='yes'
while cont=="yes":
    command=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text=input("Type your text:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift % 26 #if user enters a greater no.
    ceasar(text,shift,command)
    cont=input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")
    if cont=='no':
        cont='no'
        print("Goodbye!")

#def encrypt(plain_text, shift_no):
#   cipher_text=""
#   for i in plain_text:
#        pos=alphabet.index(i)
#        new_pos=pos+shift_no
#        cipher_text+=alphabet[new_pos]
#   print(f"The encoded text is {cipher_text}")

#def decrypt(cipher_text,shift_no):
#   plain_text=""
#   for i in cipher_text:
#      pos=alphabet.index(i)
#      new_pos=pos-shift_no
#      plain_text+=alphabet[new_pos]
#   print(f"The decoded text is {plain_text}")
#if command=="encode":
#   encrypt(text,shift)
#elif command=="decode":
#    decrypt(text,shift)
#else:
#    print("Invalid command!!")



