f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

for line in lines:
    words = line.split()
    for word in words:
        if "ё" in word:
            word = word.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")
            print(word)
