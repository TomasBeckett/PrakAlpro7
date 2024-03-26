# LATIHAN 1
kata1 = input("Kata pertama: ")
kata2 = input("Kata bolak-balik: ")

kata1 = kata1.lower().replace(" ", "")
kata2 = kata2.lower().replace(" ", "")

sorted_kata1 = sorted(kata1)
sorted_kata2 = sorted(kata2)

if sorted_kata1 == sorted_kata2:
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")
