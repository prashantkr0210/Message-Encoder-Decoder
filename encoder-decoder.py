alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def cipher():
  repeat = True
  while repeat == True:   
    direction_given = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    plain_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    cipher_text = ""
    new_shift_amount = shift_amount % len(alphabet)  
  
      
    for a in range(0,len(plain_text)):
      count = 0  
      for b in range(0, len(alphabet)):
        if plain_text[a] == alphabet[b]:
            if direction_given == "encode":
                if b+new_shift_amount < len(alphabet):
                  cipher_text += alphabet[b+new_shift_amount]
                  count += 1
                else:
                  cipher_text += alphabet[(b+new_shift_amount)-len(alphabet)]
                  count += 1
            elif direction_given == "decode":
                if b-new_shift_amount >= 0 and b-new_shift_amount < len(alphabet):
                  cipher_text += alphabet[b-new_shift_amount]
                  count += 1
                else:
                  cipher_text += alphabet[len(alphabet)+(b-new_shift_amount)]
                  count += 1
                
      if count == 0:
            cipher_text += plain_text[a]
    print(f"The {direction_given}d Message is : {cipher_text}")
    ask = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if ask == "no":
        repeat = False

cipher()


    

