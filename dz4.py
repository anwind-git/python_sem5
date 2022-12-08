# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

import re

def OpenText():
    file = open('source_text.txt', 'r')
    for text in file:
        text
    file.close()
    text = list(text)
    text.append(" ")
    text = "".join(text)
    print(f"Текст из файла: {text}")

    def RleProcessing():
        compression = []
        i = 0
        summ = 0
        while i < (len(text) - 1):
            if text[i] == text[i + 1]:
                summ += 1
            else:
                compression.append(f"{summ + 1}{text[i]}")
                summ = 0
            i += 1
        rle_file = "".join(compression)

        def RleSaveFile():
            file = open('RLE.txt', 'w')
            file.write(str(rle_file))
            file.close()

        RleSaveFile()

    RleProcessing()
        
OpenText()

def RleOpenFile():
    file = open('RLE.txt', 'r')
    for text in file:
        text
    file.close()
    print(f"RLE текст сжатия из файла: {text}")

    def Recovery():
        text_recovery = list(text)
        text_recovery.append(" ")
        text_recovery = "".join(text)
        recovery = []
        letters = re.findall(r'[a-zA-Z]+', text_recovery)
        numbers = re.findall(r'\d+', text_recovery)

        for i in range(len(letters)):
            recovery.append(letters[i] * int(numbers[i]))

        recovery = "".join(recovery)
        print(f"Востановленный RLE текст: {recovery}")

        def RecoverySaveFile():
            file = open('recovery.txt', 'w')
            file.write(str(recovery))
            file.close()

        RecoverySaveFile()

    Recovery()
    
RleOpenFile()