# LATIHAN 4
kalimat = input("Kalimat: ")

kata = kalimat.split()
terpendek = terpanjang = kata[0]

for k in kata:
    if len(k) < len(terpendek):
        terpendek = k
    if len(k) > len(terpanjang):
        terpanjang = k

print(f"terpendek: {terpendek}, terpanjang: {terpanjang}")
