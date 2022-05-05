import numpy
import numpy as np

# a = np.array([0, 1])
# print(a)
#
# b = np.arange(1, 5, 1, dtype='float64')
# print(type(b))
# print(b.dtype)
#
# c = b.astype('float64')
# print(c)
#
# print(c.shape)
#
# d = np.array([np.arange(2), np.arange(2)])
# print(d)
# print(d.shape)
# print(d.ndim)
#
#
# zera = np.zeros((5, 5))
# print(zera)
#
# jedynki = np.ones((5, 5))
# print(jedynki)
#
# pusta = np.empty((2, 2))
# print(pusta)
# print(pusta[1][0])
#
# f = np.arange(1, 5, 0.5)
# print(f)
#
# b = np.linspace(1, 2, 8, endpoint=False)
# print(b)
#
# c, d = np.indices((5, 5))
# print(c)
# print(d)
#
# e = np.indices((3, 3))
# print(e)
# print(e[1][0][1])
#
# f, g = np.mgrid[0:5, 0:5]
# print(f)
# print(g)
#
# b = np.diag([a for a in range(5)], 2)
# print(b)
#
# i = np.fromiter(range(5), dtype='int32')
# print(i)
#
# stanislaw ='stanislaw'
# # stan = np.frombuffer(stanislaw, dtype='S3')
# # print(stan)
# stan_1 = np.array(list(stanislaw))
# # print(stan_1)
# # stan_2 = np.array(list(b'stanislaw'))
# # print(stan_2)
# # stan_3 = np.fromiter(stanislaw, dtype='S3')
# # print(stan_3)
#
# a = np.ones((2, 2))
# b = np.ones((2, 2))
# c = a + b
# print(c)
# d = c - b
# print(d)
#
#
# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)
# print(a[s])
#
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:5])
#
# b = np.arange(25)
# mat = b.reshape((5, 5))
# print(b)
# print(mat)
# print(mat[1:2])
# print(mat[1:, 0:5])
# print("\n")
# print(mat[:, 1])
# print('\n')
# print(mat[2:5, 1:3])
#
# f = np.array([[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(f)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = f[rows, cols]
# print(y)

#Zad1.
#Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.

tab = np.arange(1,16)*3
print(tab)
#Zad2.
#Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię
# przekonwertowaną na typ int64
zmien = np.arange(5, dtype="float")
print(type(zmien[1]))
zmien_2 = zmien.astype('int64')
print(type(zmien_2[1]))

#Zad3.
#Napisz funkcję, która będzie:
#•	Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
#•	Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

def zad_3(n):
    return np.arange(1, n*n + 1)

g = zad_3(5)
print(g)

#Zad4.
#Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania
#oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową
#kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]

def generuj(n, f):
    return np.logspace(1, f, base=n, num=f)

print(generuj(2,4))

#Zad5.
#Napisz funkcję, która:
#•	Na wejściu przyjmuje jeden parametr określający długość wektora
#•	Na podstawie parametru generuj wektor, ale w kolejności odwróconej
#•	Generuj macierz diagonalną z w/w wektorem jako przekątną

def zad_5(n):
    a = np.arange(n, 0, -1)
    return np.diag(a)
print(zad_5(10))

#Zad6.
#Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.


print(np.array([['p', 'a', 'j', 'a', 'k'],
                ['i', 'i', 'a', 'a', 'e'],
                ['v', 'n', 'j', 'k', 'e'],
                ['x', 'a', 'a', 'a', 'e'],
                ['k', 'l', 'a', 't', 'k']]))

# Zad7.
#
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
#
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
#
# Przy założeniach:
#
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i
# umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.


def generuj_macierz(n):
    arr = np.full((n,n),2)
    for x in range(n):
       for y in range(n):
           arr[x][y] = (abs(x-y)+1) *2
    return arr

print(generuj_macierz(5))



# Zadanie 8
#
# Napisz funkcję, która:
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn,
# w zależności od kierunku podziału, nie pozwala na operację)






# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5,
# która będzie zawierała kolejne wartości ciągu Fibonacciego.

pierw = [0, 1]
for i in range(23):
    pierw.append(sum(pierw[-2:]))
print(np.array(pierw).reshape((5,5)))



































