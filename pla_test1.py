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


def devide(letters):
    msg = alphabet_index(letters)
    indecies = []
    for i in msg:
        indecies.append(i[1])
    messages_by_2 = [indecies[0:2], indecies[2:4], indecies[4:6], indecies[6:8], indecies[8:10], indecies[10:12]]
    messages_by_3 = [indecies[0:3], indecies[3:6], indecies[6:9], indecies[9:12]]
    messages_by_4 = [indecies[0:4], indecies[4:8], indecies[8:12]]  # [[32, 33, 1, 15], [19, 0, 31, 33], [12, 0, 1, 20]]
    return encr2(messages_by_2), encr3(messages_by_3), encr4(messages_by_4)



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

test_random2x2 = [[25, 2], [1, 3]]
test_random3x3 = [[1, 4, 2], [7, 2, 8], [4, 9, 5]]
test_random4x4 = [[1, 3, 5, 6], [8, 11, 13, 7], [1, 2, 4, 3], [5, 1, 0, 2]]

for i in devide(text):
    print(f'Результат относительно матриц: {i}')
# ic(devide(text))