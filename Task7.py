# Final project

import csv
from hashlib import sha256

dict_hash = {}
for ramz in range(1000 , 10000):
     hashing_number = sha256(b'%i'% ramz).hexdigest()
     dict_hash[hashing_number] = ramz

with open('tamrin jadi\hash.csv') as f :
    reader = list(csv.reader(f))
    for i in reader:
         for n in i[1:]:
            #   if i[1] in dict_hash:
                   print(f'{i[0]} = {dict_hash[i[1]]}')
