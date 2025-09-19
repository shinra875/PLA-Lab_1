import numpy as np
from math import *
from random import *
from icecream import ic


def alphabet_index(text):
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

def anti_alphabetic_index(num, letter):
    splitted = full_split(num, letter)
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

def np_to_int(multiplication):
    return [int(i%35) for i in multiplication]

def encr2(messages_by_2):
    K2x2_matrix = np.array(test_random2x2)
    encrypted_by_2 = []
    
    for msg in messages_by_2:
        P_matrix = np.array(msg)
        multiplication = np.dot(K2x2_matrix, P_matrix)
        encrypted_by_2.append(np_to_int(multiplication))
    return encrypted_by_2

def encr3(messages_by_3):
    K3x3_matrix = np.array(test_random3x3)
    encrypted_by_3 = []
    
    for msg in messages_by_3:
        P_matrix = np.array(msg)
        multiplication = np.dot(K3x3_matrix, P_matrix)
        encrypted_by_3.append(np_to_int(multiplication))
    return encrypted_by_3

def encr4(messages_by_4):
    K4x4_matrix = np.array(test_random4x4)
    encrypted_by_4 = []
    
    for msg in messages_by_4:
        P_matrix = np.array(msg)
        multiplication = np.dot(K4x4_matrix, P_matrix)
        encrypted_by_4.append(np_to_int(multiplication))
    return encrypted_by_4

def just_indecies(text):
    msg = alphabet_index(text)
    indecies = []
    for i in msg:
        indecies.append(i[1])
    return indecies

def devide(letters):
    msg = alphabet_index(letters)
    indecies = []
    for i in msg:
        indecies.append(i[1])
    messages_by_2 = [indecies[0:2], indecies[2:4], indecies[4:6], indecies[6:8], indecies[8:10], indecies[10:12]]
    messages_by_3 = [indecies[0:3], indecies[3:6], indecies[6:9], indecies[9:12]]
    messages_by_4 = [indecies[0:4], indecies[4:8], indecies[8:12]]  # [[32, 33, 1, 15], [19, 0, 31, 33], [12, 0, 1, 20]]
    return encr2(messages_by_2), encr3(messages_by_3), encr4(messages_by_4)

def full_split(num, letters):
    encrypted_lists = devide(letters)
    
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

def task1_4():
    kleshe_matrix = 'Ваша ключ-матрица'
    kleshe_answer = 'Ваше сообщение из 12 символов после кодирования ключем-матрицей'
    
    answ = f'До кодирования: {text}\n\n Ваш текст через индексы вашего алфавита (буква; индекс): {alphabet_index(text)}\n\nВаш текст через индексы вашего алфавита: {just_indecies(text)}\n{kleshe_matrix} размера 2х2: {test_random2x2}\n{kleshe_matrix} размера 3х3: {test_random3x3}\n{kleshe_matrix} размера 4х4: {test_random4x4}\n\n{kleshe_answer}:\n   - 2х2: {anti_alphabetic_index(2, text)}\n   - 3х3: {anti_alphabetic_index(3, text)}\n   - 4х4: {anti_alphabetic_index(4, text)}'''
    return answ

def ri(a, b):
    return randint(a, b)

def random2x2():
    return [[ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35)]]

def random3x3():
    return [[ri(0, 35), ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35)]]

def random4x4():
    return [[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)], [ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35)],[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]]
    # для вывода по строчно, (красиво, но непрактично)
    # return f'{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35)]}\n{[ri(0, 35), ri(0, 35), ri(0, 35), ri(0, 35)]}'


test_random2x2 = [[25, 2], [1, 3]]
test_random3x3 = [[1, 4, 2], [7, 2, 8], [4, 9, 5]]
test_random4x4 = [[1, 3, 5, 6], [8, 11, 13, 7], [1, 2, 4, 3], [5, 1, 0, 2]]
# text = 'я делаю лабу'

text = input('Введите сообщение длинной в 12 символов из алфавита {а-я, "пробела", "1": ')
print(task1_4())