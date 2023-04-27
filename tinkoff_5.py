"""Разумный отрезок - сумма равна нулю, нормальный отрезок - в котором есть разумный отрезок,
    надо найти сколько нормальных отрезков"""
"Budem perebirat i smotret skolko razumnih"
"""
- 1 element 3 mozhet s kazhdim drugim elementom dat razumnost, proverili 2 slagaemih (len(k)-1)
- 1 element 3 mozhet s kazhdimi 2mya drugimi elementami dat razumnost, proverili 3 slagaemih (len(k)-2
"""

"""Функция считает количество подотрезков. На входе два индекса в кортеже и список для сравнения"""
lst_to_compare = [3, 5, -8, 9, -5]#[3, 5, -8, 9]#[-1, 1, 2, -3, 6]


"""Функция считает два индекса в кортеже. На входе список из вух членов: один первый член, второй список минус перый член и список для сравнения"""


def index_in_tuple(index1, lst_k):

    print(lst_to_compare)
    print(lst_k)
    print(lst_to_compare.index(lst_k[-1]))
    delta1 = lst_to_compare.index(index1)
    index2_2 = lst_to_compare.index(lst_k[-1])
    delta2 = len(lst_to_compare) - index2_2
    result = (delta1 + delta2)
    print('result, k[0], lst_k, kkk', result, index1, lst_k, lst_to_compare)
    return result

def one_perebor(k):  # Delaet vse perebori dlia 1ogo chlena
    lst1 = []
    index = 0
    kk = k.copy()
    while len(k) - 1 >= 1:
        for i in range(len(k) - 1):
            index += 1
            # print('i', i)
            # print('index', index)     [-1, 1, 2, -3, 6]
            # lst1.append((k[0], k[index:]))#, (0, -index)))  ############################ Dobavim kortezh s indexami (??????????????????/, -index)
            # print(lst1)
            # data_tuple_add_lst1 = [k[0], [k[index:]]]
            # if data_tuple_add_lst1[0] == k[0] and data_tuple_add_lst1[1][-1] == k[-1]:
            # while i == 0 and index < len(k) - 1:
            # print('-------------------')
            lst1.append((k[0], k[index:], index_in_tuple(k[0], k[index:])))  ############################ Dobavim kortezh s indexami (??????????????????/, -index)
            print('i, index lst1', i, index, lst1)
            # index += 1

        k.pop(-1)
        index = 0
    # kk.pop(-1)
    k = kk
    print('k, lst1  =============', k, lst1)
    return lst1, k
    # print('===lst1 === ', lst1, k)  # [(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])]


# ===lst1 ===  [(-1, [1, 2, -3, 6], (-1, -1)), (-1, [2, -3, 6], (-1, -2)), (-1, [-3, 6], (-1, -3)), (-1, [6], (-1, -4)), (-1, [1, 2, -3], (-1, -1)), (-1, [2, -3], (-1, -2)), (-1, [-3], (-1, -3)), (-1, [1, 2], (-1, -1)), (-1, [2], (-1, -2)), (-1, [1], (-1, -1))] [-1, 1, 2, -3, 6]
# ===lst1 ===  [(-1, [1, 2, -3, 6], (0, -1)), (-1, [2, -3, 6], (0, -2)), (-1, [-3, 6], (0, -3)), (-1, [6], (0, -4)), (-1, [1, 2, -3], (0, -1)), (-1, [2, -3], (0, -2)), (-1, [-3], (0, -3)), (-1, [1, 2], (0, -1)), (-1, [2], (0, -2)), (-1, [1], (0, -1))] [-1, 1, 2, -3, 6]

# ===lst1 ===  [(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])] [-1, 1, 2, -3, 6]

# one_perebor([-1, 1, 2, -3, 6])

def one(k):  # Sobiraem varianti v spisok
    kk = k.copy()
    lst1 = []
    index = 0
    # print(one_perebor(k))  # Nado ubrat 1 chlen i sdelat vse to zhe samoe dlya 2ogo i td
    # a, b = one_perebor(k)[0], one_perebor(k)[1]
    # print(a, b)
    for i in one_perebor(k):
        lst1.append(i)
    # print(kk)
    # print(lst1)
    k = lst1[1]
    lst1.pop(1)
    # print(lst1)
    # [-1]
    # [-1, 1, 2, -3, 6]
    # [[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]),
    #   (-1, [1, 2]), (-1, [2]), (-1, [1])]]
    while index < len(k) - 1:

        k.pop(index)## Убираем первый элемент списка и опять делаем все то же самое one_perebor() при этом увеличивается на 1 первый индекс кортежа
        print('---1----k', k)

        for i in one_perebor(k):
            # print(i)
            lst1.append(i)
        k = lst1[-1]
        lst1.pop(-1)
        print(lst1, k,
              kk)  # [[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []] [6] [-1, 1, 2, -3, 6]
        # [[(-1, [1, 2, -3, 6], (-1, -1)), (-1, [2, -3, 6], (-1, -2)), (-1, [-3, 6], (-1, -3)), (-1, [6], (-1, -4)),
        #   (-1, [1, 2, -3], (-1, -1)), (-1, [2, -3], (-1, -2)), (-1, [-3], (-1, -3)), (-1, [1, 2], (-1, -1)),
        #   (-1, [2], (-1, -2)), (-1, [1], (-1, -1))],
        #  [(1, [2, -3, 6], (1, -1)), (1, [-3, 6], (1, -2)), (1, [6], (1, -3)), (1, [2, -3], (1, -1)), (1, [-3], (1, -2)),
        #   (1, [2], (1, -1))], [(2, [-3, 6], (2, -1)), (2, [6], (2, -2)), (2, [-3], (2, -1))], [(-3, [6], (-3, -1))],
        # []][6][-1, 1, 2, -3, 6]
    return lst1, k


# one([-1, 1, 2, -3, 6])
def sum_tupl(k):  # Summa tupla
    j = k[0]
    jj = k[1]
    index = 0
    # for i in k:
    res = j + sum(jj)
    # print(res)
    return res


# sum_tupl((-1, [1, 2, -3, 6]))


def sum_chlen(k):  # Naidem summu chlena
    global lst
    lst = []
    index = 0

    print('0000000000 len(k), k', len(k),
          k)  # 0000000000 k ([[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []],)
    # 0000000000 len(k), k5[[(-1, [1, 2, -3, 6], (-1, -1)), (-1, [2, -3, 6], (-1, -2)), (-1, [-3, 6], (-1, -3)), (-1, [6], (-1, -4)),
    #    (-1, [1, 2, -3], (-1, -1)), (-1, [2, -3], (-1, -2)), (-1, [-3], (-1, -3)), (-1, [1, 2], (-1, -1)),
    #    (-1, [2], (-1, -2)), (-1, [1], (-1, -1))], [(1, [2, -3, 6], (1, -1)), (1, [-3, 6], (1, -2)), (1, [6], (1, -3)),
    #                                                (1, [2, -3], (1, -1)), (1, [-3], (1, -2)), (1, [2], (1, -1))], [
    #     (2, [-3, 6], (2, -1)), (2, [6], (2, -2)), (2, [-3], (2, -1))], [(-3, [6], (-3, -1))], []]
    for i in k:
        index = 0
        index1 = 0  # Ne sbrasivaetsya index 2 index1???????????????????????????????//
        index2 = 0
        """k podaetsya uzhe s indexami, nuzhna funkcia preobrazuushaya indexi v kolichestvo podotrzkov """
        print('+++++++++++++++ i',
              i)  # +++++++++++++++ i [(1, [2, -3, 6], (0, -1)), (1, [-3, 6], (1, -2)), (1, [6], (2, -3)), (1, [2, -3], (0, -1)), (1, [-3], (1, -2)), (1, [2], (0, -1))]

        while index < len(i):
            # index1 = i[index][2][0] ## 92 - 96 schitaem podotrezki
            # index2 = i[index][2][1]
            # delta1 = index1 - 0
            # delta2 = 0 - index2
            # result_podotrezki = delta1 + delta2  # Kolichestvo podotrezkov pri index1 i index2
            # lst.append((sum_tupl(i[index]), result_podotrezki))
            # lst.append(((sum_tupl(i[index])), i[index][2]))#, podotrezok(i[index][2])))  ## Skladivaem summu varianta i funkciya - podotrezok(i[index][2])) v kortezh

            lst.append(((sum_tupl(i[index])), i[index][2], i[index]))
            # print('lllllllllll', lst)
            # print(index)
            index += 1
            # if len(lst) == len(i): #Sbros indexa
    print('lllllllllll', lst)
    index = 0
    lst_fin = []
    lst_fin_fin = []
    for j in lst:
        print(j[0])
        if j[0] == 0:
            lst_fin.append(j[2])
    print(lst_fin)#[(-1, [1], 4), (1, [2, -3], 3)]
    for i in lst_fin:
        index2_2 = lst_to_compare.index(i[1][-1])
        index = 0
        for j in range(len(lst_to_compare) - index2_2):
            lst_fin_fin.append((i[0],i[1], lst_to_compare[-j]))
    print(lst_fin_fin)
    print(len(lst_fin_fin))


        # index += 1
        # print('index', index, len(i), i)#range(len(k)):#sum(i[0][0][1]
    # index
    # 0
    # 10[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (
    # -1, [1, 2]), (-1, [2]), (-1, [1])]
    # -1
    # index
    # 1
    # 6[(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])]
    # 1
    # index
    # 2
    # 3[(2, [-3, 6]), (2, [6]), (2, [-3])]
    # 2
    # index
    # 3
    # 1[(-3, [6])]
    #     print(i[index][0])
    # lst.append((k[index][0][0][0] + sum(k[index][0][1][1])))#  lst.append((k[index][0][0][0] + sum(k[index][0][1])))
    # index += 1
    # print(lst)
    # print(lst.count(0))
    # return lst.count(0)


# sum_chlen([(3, [5, -8, 9]), (3, [-8, 9]), (3, [9]), (3, [5, -8]), (3, [-8]), (3, [5])])
# sum_chlen([(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])])

# one([3, 5, -8, 9])
## Vozvrashaet podotrezki pri indexah 1, 2

# podotrezok(
#     [(1, [2, -3, 6], (0, -1)), (1, [-3, 6], (1, -2)), (1, [6], (2, -3)), (1, [2, -3], (0, -1)), (1, [-3], (1, -2)),
#      (1, [2], (0, -1))])


def norm(n, k):
    # for i in one(k):
    lst2 = one(k)[:-1]
    print('00000000-------------------------', lst2[
        0])  # 00000000------------------------- ([[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []],)
    print(sum_chlen(lst2[0]))  # [(3, [5, -8, 9]), (3, [-8, 9]), (3, [9]), (3, [5, -8]), (3, [-8]), (3, [5])]

    # k = k[:0]+k[:-1]

    # print(lst1)  # [(3, [5, -8, 9]), (3, [-8, 9]), (3, [9])]


########################################3
norm(3, [3, 5, -8, 9, -5])
# norm(5, [-1, 1, 2, -3, 6])  # [5, 4, 2, 5, -1, -2, -4, 2, 1, 0, 6, 4, 7, 0, -2, 3, 5, 8, -1, 3]
# [(5, 1), (4, 4), (2, 7), (5, 10), (-1, 5), (-2, 8), (-4, 11), (2, 8), (1, 11), (0, 10), (6, 11), (4, 14), (7, 17), (0, 14), (-2, 17), (3, 16), (5, 17), (8, 20), (-1, 19), (3, 20)]
##########################################
