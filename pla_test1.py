import numpy as np
from math import *
from random import *
from icecream import ic

text = 'я делаю лабу'

myOwnMatrix2x2 = [[25, 2], [1, 3]]
myOwnMatrix3x3 = [[1, 4, 2], [7, 2, 8], [4, 9, 5]]
myOwnMatrix4x4 = [[1, 3, 5, 6], [8, 11, 13, 7], [1, 2, 4, 3], [5, 1, 0, 2]]

# по условию пункта 3 матрицы должны иметь разные определители, быть обратимыми и не иметь общих делителей с n=35
inverted_myOwnMatrix2x2 = np.linalg.inv([[25, 2], [1, 3]])
inverted_myOwnMatrix3x3 = np.linalg.inv([[1, 4, 2], [7, 2, 8], [4, 9, 5]])
inverted_myOwnMatrix4x4 = np.linalg.inv([[1, 3, 5, 6], [8, 11, 13, 7], [1, 2, 4, 3], [5, 1, 0, 2]])


# ic(np.linalg.det(myOwnMatrix2x2))
# ic(np.linalg.det(myOwnMatrix3x3))
# ic(np.linalg.det(myOwnMatrix4x4))
# print()

# ic(inverted_myOwnMatrix2x2)
# ic(inverted_myOwnMatrix3x3)
# ic(inverted_myOwnMatrix4x4)


def alphabet_index(text):
    ''' Выводит список кортежей пар (буква исходного слова; индекс буквы по нашему алфавиту) | 
    str: я делаю лабу  ---> list[tuple]: [('я', 32), ... ,(' ', 33), ('б', 1), ('у', 20)]'''
    letter_text = [i for i in text]  # ['я', ' ', 'б', 'о', 'т', 'а', 'ю', ' ', 'л', 'а', 'б', 'у']
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя 1'  # наш алфавит из 33 букв + пробела + 1 (можно закастомить до произвольного алфавита)
    indecies = [i for i in range(0, 35)]  # [0, 1, ..., 33, 34]
    global alpha_indecies
    alpha_indecies = list(zip(alphabet, indecies))
    
    
    indexed_text = []
    # сопоставление букв сообщения и индексов нашего алфавита
    for bukva in letter_text:
        for cifra in alpha_indecies:
            if bukva == cifra[0]:  
                indexed_text.append(cifra)
    return indexed_text
# ic(alphabet_index(text))  # раскомментируй, чтобы увидеть вывод этой функции



def mod35(multiplication):  
    '''Функция "обрезает" значения матрицы по модулю 35 (мощность нашего алфавита)'''
    return [int(i%35) for i in multiplication]


def encr2(matrix, messages_by_2):
    '''Функция работает по формуле C = KP, где С - зашифрованное слово, К - ключ-матрица, Р - зашифрованное слово. Эта функция берет K=2x2, P=[a,b], где [a,b] - 2 буквы сообщения (происходит разбиение сообщения на куски по 2 символа для умножения на матрицу 2х2)'''
    K2x2_matrix = np.array(matrix)
    encrypted_by_2 = []
    
    for msg in messages_by_2:
        P_matrix = np.array(msg)
        multiplication = np.dot(K2x2_matrix, P_matrix)
        encrypted_by_2.append(mod35(multiplication))
    return encrypted_by_2


def encr3(matrix, messages_by_3):
    '''Функция работает по формуле C = KP, где С - зашифрованное слово, К - ключ-матрица, Р - зашифрованное слово. Эта функция берет K=3x3, P=[a,b,c], где [a,b,c] - 3 буквы сообщения (происходит разбиение сообщения на куски по 3 символа для умножения на матрицу 3х3)'''
    K3x3_matrix = np.array(matrix)
    encrypted_by_3 = []
    
    for msg in messages_by_3:
        P_matrix = np.array(msg)
        multiplication = np.dot(K3x3_matrix, P_matrix)
        encrypted_by_3.append(mod35(multiplication))
    return encrypted_by_3


def encr4(matrix, messages_by_4):
    '''Функция работает по формуле C = KP, где С - зашифрованное слово, К - ключ-матрица, Р - зашифрованное слово. Эта функция берет K=4x4, P=[a,b,c,d], где [a,b,c,d] - 4 буквы сообщения (происходит разбиение сообщения на куски по 4 символа для умножения на матрицу 4х4)'''
    K4x4_matrix = np.array(matrix)
    encrypted_by_4 = []
    
    for msg in messages_by_4:
        P_matrix = np.array(msg)
        multiplication = np.dot(K4x4_matrix, P_matrix)
        encrypted_by_4.append(mod35(multiplication))
    return encrypted_by_4


def just_indecies(text):
    '''Функция выводит индексы каждого символа сообщения по нашему алфавиту. str: aбвг ---> list: [0, 1, 2, 3]'''
    msg = alphabet_index(text)
    indecies = []
    for i in msg:
        indecies.append(i[1])
    return indecies
# ic(just_indecies(text))  # раскомментируй, чтобы увидеть вывод этой функции

def devide(matrix2, matrix3, matrix4, msg):
    '''Функция разделяет наше сообщение из 12 символов на сообщения по 2, 3 и 4 символа, чтобы умножение на матрицы соответствуещего размера было возможным. str: abcdefghigkl ---> tuple(list, list, list): ([[a, b], ..., [k, l]], [[a, b, c], ..., [g, k, l]], [[a, b, c, d], ..., [i, g, k, l]])'''
    indecies = []
    for i in msg:
        indecies.append(i[1])
    messages_by_2 = [indecies[0:2], indecies[2:4], indecies[4:6], indecies[6:8], indecies[8:10], indecies[10:12]]
    messages_by_3 = [indecies[0:3], indecies[3:6], indecies[6:9], indecies[9:12]]
    messages_by_4 = [indecies[0:4], indecies[4:8], indecies[8:12]]  # [[32, 33, 1, 15], [19, 0, 31, 33], [12, 0, 1, 20]]
    return encr2(matrix2, messages_by_2), encr3(matrix3, messages_by_3), encr4(matrix4, messages_by_4)
# ic(devide(text))  # раскомментируй, чтобы увидеть вывод этой функции

def devide_inv(matrix2, matrix3, matrix4, msg):
    '''Функция разделяет наше сообщение из 12 символов на сообщения по 2, 3 и 4 символа, чтобы умножение на матрицы соответствуещего размера было возможным. str: abcdefghigkl ---> tuple(list, list, list): ([[a, b], ..., [k, l]], [[a, b, c], ..., [g, k, l]], [[a, b, c, d], ..., [i, g, k, l]])'''
    indecies = []
    for i in msg:
        indecies.append(i[1])
    messages_by_2 = [indecies[0:2], indecies[2:4], indecies[4:6], indecies[6:8], indecies[8:10], indecies[10:12]]
    messages_by_3 = [indecies[0:3], indecies[3:6], indecies[6:9], indecies[9:12]]
    messages_by_4 = [indecies[0:4], indecies[4:8], indecies[8:12]]  # [[32, 33, 1, 15], [19, 0, 31, 33], [12, 0, 1, 20]]
    return messages_by_2, messages_by_3, messages_by_4


def coded_troika(matrix2, matrix3, matrix4, tpl):
    return encr2(matrix2, tpl[0]), encr3(matrix3, tpl[1]), encr4(matrix4, tpl[2])
    
def full_split(matrix2, matrix3, matrix4, num, text):
    '''Функция разделяет tuple(list, list, list) в list, list, list, причем, исходные списки - двумерные матрицы, результирующие списки - векторы'''
    encrypted_lists = devide(matrix2, matrix3, matrix4, alphabet_index(text))
    # ic(encrypted_lists)
    if num == 2:
        
        full_split2 = encrypted_lists[0]
        splitted_2 = []
        for i in full_split2:
            splitted_2 = splitted_2 + i
        return splitted_2
    
    if num == 3:
        full_split3 = encrypted_lists[1]
        splitted_3 = []
        for i in full_split3:
            splitted_3 = splitted_3 + i
        return splitted_3
    
    if num == 4:
        full_split4 = encrypted_lists[2]
        splitted_4 = []
        for i in full_split4:
            splitted_4 = splitted_4 + i
        return splitted_4
# ic(full_split(4, text))  # раскомментируй, чтобы увидеть вывод этой функции


def anti_alphabetic_index(matrix2, matrix3, matrix4, num, text):
    '''Функция (вроде как) возвращает из закодированного сообщения текст в соотвествии с индексами его символов'''
    splitted = full_split(matrix2, matrix3, matrix4, num, text)
    # ic(splitted)
    res_msg = []
    
    for index in splitted:
        for bukva in alpha_indecies:
            if index == bukva[1]:
                res_msg.append(bukva[0])
    
    # объединение в одну строку из списка букв
    res_str = ''
    for i in res_msg:
        res_str += i
    
    return res_str
# ic(anti_alphabetic_index(2, text))  # раскомментируй, чтобы увидеть вывод этой функции


# "Ctrl + F; myOwnMatrix2x2 -> random2x2()" для работы с рандомными матрицами (есть риск не исполнить условие 3; см. комменатрий к блоку функций рандомных матриц внутри этой функции vvv)
def task1_4():
    '''Функция выполняет подпункт 4 задания 1: Зашифровать сообщение в 12 символов тремя ключами-матрицами размеров 2х2, 3х3 и 4х4, представить в виде строчек зашифрованные слова'''
    kleshe_matrix = ' 🗝️  Ключ-матрица'
    kleshe_answer = 'Ваше сообщение из 12 символов после кодирования ключем-матрицей'
    
    # Очень длинная строка вывода всей информации и промежуточных результатов
    answ = f'🤖 До кодирования: {text}\n\nВаш текст через индексы вашего алфавита (буква; индекс): {alphabet_index(text)}\n\nВаш текст через индексы вашего алфавита: {just_indecies(text)}\n{kleshe_matrix} размера 2х2: {myOwnMatrix2x2}\n{kleshe_matrix} размера 3х3: {myOwnMatrix3x3}\n{kleshe_matrix} размера 4х4: {myOwnMatrix4x4}\n\n{kleshe_answer}:\n   📌 2х2: {anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 2, text)}\n   📌 3х3: {anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 3, text)}\n   📌 4х4: {anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 4, text)}'''
    return answ


# блок функций, генерирующих рандомные матрицы 2х2, 3х3 и 4х4 (в общем случае не работают, ведь не соблюдается пункт 3 задания 1: определители матриц-ключей не должны иметь общих делителей с числом n=35 + все определители должны отличаться)
# def ri(a, b):
#     return randint(a, b)

# def random2x2():
#     return [[ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35)]]

# def random3x3():
#     return [[ri(0, 35), ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35)]]

# def random4x4():
    return [[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]]
    # для вывода по строчно, (красиво, но непрактично)
    # return f'{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}'

# ic(task1_4())  # раскомментируй, чтобы увидеть вывод этой функции


# раскомментируйте или отредактируйте готовую строку из 12 символов из нашего алфавита или введите свою строку самостоятельно с помощью input()
text = 'я делаю лабу'
# text = input('Введите сообщение длинной в 12 символов из алфавита {а-я, "пробела", "1": ')
# ic(task1_4())


# добавлены комментарии к разным кускам кода 
# (в основном к функциям). вывод сделан симпатичным



def decode():
    '''Функция берет 3 закодированных строки, умножает каждую на обратную матрицу 2х2, 3х3, 4х4, переводит все к строкам'''
    # закодированные строки
    coded_str2 = anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 2, text)
    coded_str3 = anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 3, text)
    coded_str4 = anti_alphabetic_index(myOwnMatrix2x2, myOwnMatrix3x3, myOwnMatrix4x4, 4, text)
    ic(coded_str2)
    ic(coded_str3)
    ic(coded_str4)

    str2_alphabeted = alphabet_index(coded_str2)
    str3_alphabeted = alphabet_index(coded_str3)
    str4_alphabeted = alphabet_index(coded_str4)
    ic(str2_alphabeted)
    ic(str3_alphabeted)
    ic(str4_alphabeted)
    
    # str2_indecies = just_indecies(coded_str2)
    # str3_indecies = just_indecies(coded_str3)
    # str4_indecies = just_indecies(coded_str4)
    # ic(str2_indecies)
    # ic(str3_indecies)
    # ic(str4_indecies)
    
    str2_devided_inv = devide_inv(inverted_myOwnMatrix2x2, inverted_myOwnMatrix3x3, inverted_myOwnMatrix4x4, str2_alphabeted)[0]
    str3_devided_inv = devide_inv(inverted_myOwnMatrix2x2, inverted_myOwnMatrix3x3, inverted_myOwnMatrix4x4, str3_alphabeted)[1]
    str4_devided_inv = devide_inv(inverted_myOwnMatrix2x2, inverted_myOwnMatrix3x3, inverted_myOwnMatrix4x4, str4_alphabeted)[2]
    ic(str2_devided_inv)
    ic(str3_devided_inv)
    ic(str4_devided_inv)
    
    
    # str2_indecies = devide(str2)[0]
    # str3_indecies = devide(str3)[1]
    # str4_indecies = devide(str4)[2]
    # ic(str2_indecies)
    # ic(str3_indecies)
    # ic(str4_indecies)
    
    # str2_decoded = encr2(inverted_myOwnMatrix2x2, str2_indecies)
    # str3_decoded = encr3(inverted_myOwnMatrix3x3, str3_indecies)
    # str4_decoded = encr4(inverted_myOwnMatrix4x4, str4_indecies)
    
    
    # ic(str2_decoded)
    # ic(str3_decoded)
    # ic(str4_decoded)
    
    # ic(str2_full_split)


ic(decode())