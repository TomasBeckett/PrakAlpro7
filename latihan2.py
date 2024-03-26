# LATIHAN 2
text = input("Kalimat: ")
print()
target_word = input("Yang dicari: ")

text_lower = text.lower()
target_word_lower = target_word.lower()
word_count = text_lower.count(target_word_lower)

print()
print(f"{target_word} ada {word_count} buah")
