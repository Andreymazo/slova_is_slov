"""Разумный отрезок - сумма равна нулю, нормальный отрезок - в котором есть разумный отрезок,
    надо найти сколько нормальных отрезков"""
"Budem perebirat i smotret skolko razumnih"
"""
- 1 element 3 mozhet s kazhdim drugim elementom dat razumnost, proverili 2 slagaemih (len(k)-1)
- 1 element 3 mozhet s kazhdimi 2mya drugimi elementami dat razumnost, proverili 3 slagaemih (len(k)-2
"""

"""Функция считает количество подотрезков. На входе два индекса в кортеже и список для сравнения"""
lst_to_compare = [-1, 1, 2, -3, 6]  # [3, 5, -8, 9]#[-1, 1, 2, -3, 6]
"""Внимание lst_to_compare костыль, не введете в переменную список, не заработает, простовызвать функцию не поркатит !!!!!!!!!!"""

"""Функция считает два индекса в кортеже. На входе список из вух членов: один первый член, второй список минус перый член и список для сравнения"""


def index_in_tuple(index1, lst_k):
    delta1 = lst_to_compare.index(index1)
    index2_2 = lst_to_compare.index(lst_k[-1])
    delta2 = len(lst_to_compare) - index2_2
    result = (delta1 + delta2)
    return result


def one_perebor(k):  # Delaet vse perebori dlia 1ogo chlena
    lst1 = []
    index = 0
    kk = k.copy()
    while len(k) - 1 >= 1:
        for i in range(len(k) - 1):
            index += 1
            lst1.append((k[0], k[index:], index_in_tuple(k[0], k[
                                                               index:])))  ############################ Dobavim kortezh s indexami (??????????????????/, -index)
        k.pop(-1)
        index = 0
    # kk.pop(-1)
    k = kk
    return lst1, k


def one(k):  # Sobiraem varianti v spisok
    kk = k.copy()
    lst1 = []
    index = 0

    for i in one_perebor(k):
        lst1.append(i)

    k = lst1[1]
    lst1.pop(1)

    while index < len(k) - 1:
        k.pop(
            index)  ## Убираем первый элемент списка и опять делаем все то же самое one_perebor() при этом увеличивается на 1 первый индекс кортежа
        for i in one_perebor(k):
            # print(i)
            lst1.append(i)
        k = lst1[-1]
        lst1.pop(-1)

    return lst1, k


# one([-1, 1, 2, -3, 6])
def sum_tupl(k):  # Summa tupla
    j = k[0]
    jj = k[1]
    res = j + sum(jj)
    return res


def sum_chlen(k):  # Naidem summu chlena
    global lst
    lst = []

    for i in k:
        index = 0

        """k podaetsya uzhe s indexami, nuzhna funkcia preobrazuushaya indexi v kolichestvo podotrzkov """

        while index < len(i):
            lst.append(((sum_tupl(i[index])), i[index][2], i[index]))
            index += 1

    lst_fin = []
    lst_fin_fin = []
    for j in lst:
        if j[0] == 0:
            lst_fin.append(j[2])

    for i in lst_fin:
        index2_2 = lst_to_compare.index(i[1][-1])
        for j in range(len(lst_to_compare) - index2_2):
            lst_fin_fin.append((i[0], i[1], lst_to_compare[-j]))

    print(len(lst_fin_fin))


def norm(n, k):
    lst2 = one(k)[:-1]
    sum_chlen(lst2[0])  # [(3, [5, -8, 9]), (3, [-8, 9]), (3, [9]), (3, [5, -8]), (3, [-8]), (3, [5])]


########################################3
# norm(3, [3, 5, -8, 9, -5])
norm(5, [-1, 1, 2, -3, 6])  # [5, 4, 2, 5, -1, -2, -4, 2, 1, 0, 6, 4, 7, 0, -2, 3, 5, 8, -1, 3]
# [(5, 1), (4, 4), (2, 7), (5, 10), (-1, 5), (-2, 8), (-4, 11), (2, 8), (1, 11), (0, 10), (6, 11), (4, 14), (7, 17), (0, 14), (-2, 17), (3, 16), (5, 17), (8, 20), (-1, 19), (3, 20)]
##########################################
