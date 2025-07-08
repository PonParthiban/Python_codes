import random
import string
chars = list(" " + string.punctuation + string.ascii_letters +string.digits)
keys = chars.copy()
random.shuffle(keys)

#encrypt
plain_txt = input("Enter the text to be encrpted: ")
ciper_text = " "
for letters in plain_txt:
    index = chars.index(letters)
    ciper_text += keys[index]
print( f"Encrypted text: {ciper_text}")
print(f"Original text: {plain_txt}")

#dycrypt
ciper_text = input("Enter the text to be dycrpted: ")
plain_txt = " "
for letters in ciper_text:
    index = keys.index(letters)
    plain_txt  += chars[index]
print( f"Encrypted text: {ciper_text}")
print(f"Original text: {plain_txt}")