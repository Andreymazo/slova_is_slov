import time

#################### Tjnkoff 4 ###################
"""Skuch spisok - v kotorom udalyyaa 1 element ostavliaem ravnoe kolichestvo chlenov, naprimer v spiske
        [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5] 10, slovar kluch - chislo, value - chislo ego povtorenii v prefixe """


#######################Unikalnie###############
def unik(k):
    lst1 = []
    for i in k:
        if i not in lst1:
            lst1.append(i)
    return lst1


############################### Naidem kol idushih podryad povtorov elementa x v spisle lst i index povtora, zanesem v spisok lst_fin##


def povt(x, lst):
    lst1 = []
    lst_fin = []
    index_left = 0
    index = 0

    for i in lst:  # [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 2, 2]

        if i == x:

            lst1.append((i, index))
            index += 1

            if index == len(
                    lst):  ## Zdes ne zahodim kak obichno, obrabativaem cherez if, i poluchaem kak nado, bez index error poslednii element
                if lst[
                    index - 2] != x:  ## Kogda predposlednii element ne raven x, a poslednii raven, uzhe nakidali v lst_fin

                    break
                i = lst[len(lst) - 1]
                if i == x:
                    lst_fin.append((x, lst1))

                    # print('lst_fin', lst_fin)
                    break
                if i != x:
                    lst_fin.append((x, lst1))
                    # print('lst_fin', lst_fin)
                    break

            if index < len(
                    lst):
                if lst[index] != x:
                    if len(lst1) >= 1:
                        lst_fin.append((x, lst1))
                        lst1 = []

        if i != x:
            index += 1
            if index >= len(
                    lst) - 1:  ## Zdes ne zahodim kak obichno, obrabativaem cherez if, i poluchaem kak nado, bez index error poslednii element
                i = lst[len(lst) - 1]
                if i == x:
                    lst1.append((i, index))
                    lst_fin.append((x, lst1))
                    # print('lst_fin', lst_fin)
                    break

                if i != x:
                    if len(lst1) > 1:
                        lst_fin.append((x, lst1))
                    break

            if lst[index] == x and lst1:  ## Budet esli v lst1 chto to est
                ##############Zdes 2ku dobavlyaet index i pustoi spisok za 1 hod do nuznogo ####################
                lst_fin.append((x, lst1))  ## Zabiraem to cto bilo v lst1, esli bilo

                lst1 = []

            if lst[index] != x:
                index_left += 1

    return lst_fin  # Vernem spisok s kortezhami, (index, spisok s indexami)


# povt(3, [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1])#[(3, [(3, 0), (3, 1)]), (3, [(3, 3), (3, 4), (3, 5)])]
# povt(3, [3, 3, 4, 3, 3, 3, 4, 4, 3, 4, 2, 2, 3, 3, 1, 1, 1, 3])
# povt(4, [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1])
# povt(1, [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5])
# [(4, [(4, 2)]), (4, [(4, 6), (4, 7), (4, 8)]), (4, [])]

#########################################Naidem max len v povt()###################################
def povtor_none(kk):  # """Возвращает список повторов с учетом Нана"""
    lst2_counts = []
    index = 0
    for i in kk:

        index += 1
        if index == len(kk):
            if i is None:
                # i = kk.count(kk[index - 2])  ## Zamenim None (on poslednii) na povtori predposlednego elementa,
                lst2_counts.append(kk.count(i))
                break
            if i is not None:
                lst2_counts.append(kk.count(i))
                break

        if i is None:
            f = kk.count(kk[index - 2])
            ff = kk.count(kk[index])
            if ff == f:
                i = ff
        if i is not None:
            lst2_counts.append(kk.count(i))

    return lst2_counts


# povtor_none([1, 2, None, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5])
def max_len(k):
    # print(k)
    lst1 = []
    for i in range(len(k)):
        lst1.append(len(k[i][1]))
    total = max(lst1)
    return total


# max_len([(3, [(3, 0), (3, 1)]), (3, [(3, 3), (3, 4), (3, 5)])])


########### Naidem max paru dlin znacheniya idushego v spiske 1m elementom ##################
def max_para(kk):  # [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]

    ######################## Sformiruem spisok iz kolichestv povtorov i True False - est vozmozhnost skladivat ili net ############
    lst1 = []
    lst_par = []
    index = 0
    # print(kk)
    k = kk
    fin = []
    for i in range(len(kk)):
        x = kk[i]
        # print(i)
        k.pop(i)
        k.insert(i, None)

        for j in unik(povtor_none(kk)):
            fin.append(max_len(povt(j, povtor_none(
                kk))))  # [(3, [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9)])]
        kk[i] = x

        lst_par = max(fin)
    print('Максимальная длина повторов ', lst_par)


start = time.time()

# max_para([1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5])#10
# max_para([1, 2, 4, 2, 3, 1, 3, 9, 15, 23])  # 7
# max_para([3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1])
max_para([1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5, 5, 7, 7])#10
# max_para([11,1,2,4,2,3,1, 3,9, 15,23])
# max_para([1,3,1,2,3,1,2])# [1, 5, 14, 2, 3, 1, 2])  # )
# max_para([1, 5, 14, 2, 3, 1, 2])#5 dolzhno bit 4
# max_para([1,3,1,2,3,1,2])
# max_para([1,2,3,4,5])#5 dolzhno bit
end = time.time()
print('Time for func', end - start)
