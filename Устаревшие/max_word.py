text = open("in.txt", encoding="utf-8").read().lower()
alf ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
words = [(len([c for c in text if c == x]) / len(text), x) for x in alf]
print(words)
