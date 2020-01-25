import random
osoby1 = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]
# tutaj wasza magia:
print(osoby1)
random.shuffle(osoby1)
for os1, os2 in zip(osoby1, osoby2):
   if os1 == os2:
       random.shuffle(osoby2[os1:])
   else:
       continue
for os1, os2 in zip(osoby1, osoby2):
   print(f"{os1} kupuje prezent {os2}")