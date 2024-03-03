#1.	Переписать задачи из предыдущего домашнего задания  для байтовых строк (массивов байт).

s = b"The dog barks and growls and runs around the yard after the cat! Why is he in such a hurry to get the cat? Ask where she's running."
count_W = s.count(b'Dog')
count_w = s.count(b'dog')
count_res = count_W + count_w
print('Count: ', count_res)

#2.	Дана байтовая строка. Перевести ее в шестнадцатеричный формат. Проверить результат по таблице ASCII.
m = b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
m_in16 = m.hex()
print(m_in16)

#3.	Необходимо декодировать закодированную с помощью кодировки  cp866 строку:
#b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
#Декодируйте ту же самую строку с помощью кодировки ascii.
#В случае возникновения ошибки, проигнорируйте ее программным способом.

encoded_f = b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
decoded_f = encoded_f.decode('cp866')
print(decoded_f)