text1 = open("text1.txt", encoding="utf-8").read().lower()
text2 = open("text2.txt", encoding="utf-8").read().lower()
alf ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#text1 - Лермонтов, text2 - Достоевский

list_of_pair = [x+y for x in alf for y in alf]
#print(list_of_pair)
list1 = [text1.count(para) for para in list_of_pair]
list2 = [text2.count(para) for para in list_of_pair]

chastota1 = [i / len(text1) for i in list1]
chastota2 = [i / len(text2) for i in list2]

dif = 0
for i in range(len(chastota1)):
    dif = dif + abs(chastota1[i] - chastota2[i])
print(dif)