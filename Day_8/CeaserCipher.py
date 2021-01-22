alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'en' to Encode and 'de' to Decode the message : \n")
text = input("Enter your text : \n").lower()
shift = int(input("Type the shift number : \n"))

## Prpoer code
def ceaser_txt(in_txt, sh_num, c_dir):
    mod_txt = ""
    sh_num = sh_num % 25
    for i in in_txt:
        if i in in_txt:
            idx = alphabet.index(i)
            if c_dir == 'de':
                sh_num *= -1
            sh_idx = idx + 1 + sh_num
            if sh_idx > 26:
                sh_idx = (idx + 1 + sh_num) % 25
            mod_txt += alphabet[sh_idx - 1]
    print(mod_txt)


## My code with the single function along with some bugs
""" def ceaser_txt(in_txt, sh_num, c_dir):
    mod_txt = ""
    for i in in_txt:
        idx = alphabet.index(i)
        if c_dir == 'en':
            sh_idx = idx + 1 + sh_num
            if sh_idx > 26:
                sh_idx = (idx + 1 + sh_num) % 25
            mod_txt += alphabet[sh_idx - 1]
        elif c_dir == 'de':
            sh_idx = idx + 1 - sh_num
            if sh_idx < 0:
                sh_idx = idx + 1 - sh_num
            mod_txt += alphabet[sh_idx - 1]
        else:
            print("Enter the correct key to proceed ! ")
    print(mod_txt)
"""
ceaser_txt(in_txt = text, sh_num = shift, c_dir = direction)
""""
def encrypt(plain_txt,p_shift):
    cipher_txt=""
    for i in plain_txt:
        idx=alphabet.index(i)
        sh_idx=idx + 1 +p_shift
        if sh_idx > 26:
            sh_idx=(idx+1+p_shift)%25
        cipher_txt+=alphabet[sh_idx-1]
    print(cipher_txt)

def decrypt(plain_txt,p_shift):
    cipher_txt=""
    for i in plain_txt:
        idx = alphabet.index(i)
        sh_idx = idx + 1 - p_shift
        if sh_idx < 0:
            sh_idx = idx + 1 - p_shift
        cipher_txt += alphabet[sh_idx - 1]
    print(cipher_txt)

if direction == 'en':
    encrypt(text,shift)
elif direction == 'de':
    decrypt(text,shift)
else:
    print("Please enter the correct key to operate ! ") """