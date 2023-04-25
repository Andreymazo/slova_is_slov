"""Разумный отрезок - сумма равна нулю, нормальный отрезок - в котором есть разумный отрезок,
    надо найти сколько нормальных отрезков"""
"Budem perebirat i smotret skolko razumnih"
"""
- 1 element 3 mozhet s kazhdim drugim elementom dat razumnost, proverili 2 slagaemih (len(k)-1)
- 1 element 3 mozhet s kazhdimi 2mya drugimi elementami dat razumnost, proverili 3 slagaemih (len(k)-2
"""


def one_perebor(k):  # Delaet vse perebori dlia 1ogo chlena
    lst1 = []
    index = 0
    kk = k.copy()
    while len(k) - 1 >= 1:
        for i in range(len(k) - 1):
            index += 1
            # print('i', i)
            # print('index', index)
            lst1.append((k[0], k[index:]))
            # print(lst1)
        k.pop(-1)
        index = 0
    # kk.pop(-1)
    k = kk
    return lst1, k
    # print('===lst1 === ', lst1, k)#[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])]


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

        k.pop(index)
        print('---1----k', k)

        for i in one_perebor(k):
            # print(i)
            lst1.append(i)
        k = lst1[-1]
        lst1.pop(-1)
        print(lst1, k,
              kk)  # [[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []] [6] [-1, 1, 2, -3, 6]
    return lst1, k

# one([-1, 1, 2, -3, 6])
def sum_tupl(k): #Summa tupla
    j = k[0]
    jj = k[1]
    index =0
    # for i in k:
    res = j+sum(jj)
    # print(res)
    return res
# sum_tupl((-1, [1, 2, -3, 6]))

def sum_chlen(k):  # Naidem summu chlena
    global lst
    lst = []
    index = 0
    print('0000000000 len(k), k',len(k),  k)# 0000000000 k ([[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []],)

    for i in k:
        print('+++++++++++++++ i', i)

        while index < len(i):
            while index == len(i):
                index = 0
            lst.append(sum_tupl(i[index]))
            print(lst)
            print(index)
            index += 1
            # if len(lst) == len(i): #Sbros indexa


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

def norm(n, k):
    # for i in one(k):
    lst2 = one(k)[:-1]
    print('00000000-------------------------', lst2[0])#00000000------------------------- ([[(-1, [1, 2, -3, 6]), (-1, [2, -3, 6]), (-1, [-3, 6]), (-1, [6]), (-1, [1, 2, -3]), (-1, [2, -3]), (-1, [-3]), (-1, [1, 2]), (-1, [2]), (-1, [1])], [(1, [2, -3, 6]), (1, [-3, 6]), (1, [6]), (1, [2, -3]), (1, [-3]), (1, [2])], [(2, [-3, 6]), (2, [6]), (2, [-3])], [(-3, [6])], []],)
    print(sum_chlen(lst2[0]))  # [(3, [5, -8, 9]), (3, [-8, 9]), (3, [9]), (3, [5, -8]), (3, [-8]), (3, [5])]

    # k = k[:0]+k[:-1]

    # print(lst1)  # [(3, [5, -8, 9]), (3, [-8, 9]), (3, [9])]

########################################3
# norm(3, [3, 5, -8, 9])
norm(5, [-1, 1, 2, -3, 6])

##########################################
