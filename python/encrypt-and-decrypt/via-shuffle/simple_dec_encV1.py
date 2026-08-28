# Criptografia Simples

#setting it up 

import string
import random
import json

print('****')
print('Python Encription Program V1.0 - Read the instructions on the READ.ME file to save your encryptions or to load and decrypt using the program. ')
print('****')

all_str = (string.printable)

possible_strings = list(all_str)
key = possible_strings.copy()

random.shuffle(key)

#print(possible_strings)
print()
#print(key)
print()

#Encrypt

process_of_enc = True

all_encrypts = {'key_of_encryption': key , 'messages': []}


final_message = ''

encryption_counter = 0
while process_of_enc:
    messages = input('type your message: ')
    for message in messages:
        key_indication = possible_strings.index(message)
        encrypted = key[key_indication]
        final_message += encrypted
    print()
    print(final_message)
    all_encrypts['messages'].append(final_message)
    final_message = ''
    #print(all_encrypts)
    
    
    print()
    decision1 = input('encrypt another message? (Y/N): ').lower()
    print()
    if decision1 == 'yes' or decision1 == 'y':
        encryption_counter += 1
        continue
    else:
        process_of_enc = False
           
    
#Decrypt

process_of_dec = True
while process_of_dec:
    json_or_type = input('press 1 to type a code you made now (currenct key). Press 2 to load a json - acording to program instructions: ')
    if json_or_type == '1':
        hidden_message = ''
        print()
        your_message = input('type your encrypted message: ')
        for message in your_message:
            key_indication = key.index(message)
            decrypted = possible_strings[key_indication]
            hidden_message += decrypted
    print()
    print(hidden_message)
    print()
    
    decision1 = input('decrypt another message? (Y/N): ').lower()
    print()
    if decision1 == 'yes' or decision1 == 'y':
        continue
    else:
        process_of_dec = False
        
        
print()
print('thank you for using the program!')
        
    