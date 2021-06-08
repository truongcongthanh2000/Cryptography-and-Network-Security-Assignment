# Assignment Cryptography-and-Network-Security Course at HCMUT Semester 202

## Member in Team
|NAME|ID Student|
|---|---|
|Lâm Duy Khang|1812536|
|Trần Xuân Hoàng|1812302|
|Trương Công Thành|1810766|

## Usage
    open terminal and type
    ./bash.sh
    # if your default python is python 2, you need to change code in bash.sh, replace python to python3.
    
## Generate Input 

### input format:
    ciphertext 
    keyCaesar 
    keyRail-fence

### run code
    $ python gen.py > input.txt
    # with small ciphertext: ciphertext = random.choice(list_ciphertext_small)
    # with large ciphertext: ciphertext = random.choice(list_ciphertext)

## Run encrypt, decrypt
    $ python main.py < input.txt > output.txt
    # the result is put into the file output.txt, you can view it.

## Run the decrypt test statistics file.
    $ python static_decrypt.py > result_static_decrypt.txt
    # the result is put into the file result_static_decrypt.txt, you can view it.


