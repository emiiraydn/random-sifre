import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu = int(input("Parolanızın uzunluğunuzu giriniz"))

kullsifre = ""

for i in range(parola_uzunlugu):
    kullsifre += random.choice(karakterler)


print("Parolanız:", kullsifre)

