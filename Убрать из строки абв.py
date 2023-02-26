# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('Введите текст: ')
text = input()
text = text.split()
combination = 'абв'


new_text = []
for i in text:
    if combination not in i:
        new_text.append(i)

new_text_str = ' '.join(new_text)
print(new_text_str)

