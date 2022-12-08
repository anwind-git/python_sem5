# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = input("Введите текст: ")

del_word = "абв"
text = [i for i in text.split() if del_word not in i]
print(" ".join(text))