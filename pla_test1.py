import numpy as np
from math import *
from random import *
from icecream import ic


def alphabet_index(text):
    letter_text = [i for i in text]  # ['я', ' ', 'б', 'о', 'т', 'а', 'ю', ' ', 'л', 'а', 'б', 'у']
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя 1'  # наш алфавит из 33 букв + пробела + 1 (можно закастомить до произвольного алфавита)
    indecies = [i for i in range(0, 35)]  # [0, 1, ..., 33, 34]
    alpha_indecies = list(zip(alphabet, indecies))
    
    indexed_text = []
    # сопоставление букв сообщения и индексов нашего алфавита
    for bukva in letter_text:
        for cifra in alpha_indecies:
            if bukva == cifra[0]:  
                indexed_text.append(cifra)
    return indexed_text


def devide4x4(letters):
    msg = alphabet_index(letters)
    
    indecies = []
    for i in msg:
        indecies.append(i[1])
    messages_by_num = [indecies[0:4], indecies[4:8], indecies[8:12]]  # [[32, 33, 1, 15], [19, 0, 31, 33], [12, 0, 1, 20]]
    
    
    encrypted = []
    K_matrix = np.array(test_random4x4)
    
    for msg_4 in messages_by_num:
        P_matrix = np.array(msg_4)
        multiplication = np.dot(K_matrix, P_matrix)
        encrypted.append(multiplication)
    return encrypted


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


text = 'я делаю лабу'
test_random4x4 = [[1, 3, 5, 6], [8, 11, 13, 7], [1, 2, 4, 3], [5, 1, 0, 2]]
ic(devide4x4(text))