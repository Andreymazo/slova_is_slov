#################### Tinkoff 4 ###################
"""Skuch spisok - v kotorom udalyyaa 1 element ostavliaem ravnoe kolichestvo chlenov, naprimer v spiske
        [1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5] 10, slovar kluch - chislo, value - chislo ego povtorenii v prefixe """


#######################Unikalnie###############
def unik(k):
    lst1 = []
    for i in k:
        if i not in lst1:
            lst1.append(i)
    return (lst1)


############################### Naidem max kol idushih podryad povtorov elementa x v spisle lst ##
def max_povt(x, lst):
    lst1 = []
    lst_fin = []
    index_right = 0
    index_left = 0
    index = 0
    ###########################################
    # while index < len(lst) - index_right:
    #     while index < len(lst) and lst[index] != lst[index + 1]:
    #             index += 1
    #             index_left += 1
    #             lst_fin.append((x, len(lst1), index_right))
    #             lst1 = []
    #             lst = lst[:0] + lst[index:]
    #
    #     index_right += 1
    #     index_left = 0
    #     lst1.append(lst[index])
    #     print(lst1)
    #########################################################33
    # while index < len(lst):
    #     while index < len(lst) and lst[index] != lst[index + 1]:
    #         index += 1
    #
    #     lst[index_left] = lst[index]
    #     lst1.append(lst[index_left])
    #     index_left += 1
    #     index += 1
    #     print(lst1)
    ######################################################333

    #  [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1]
    # for i in lst:
    #     if i == x:
    #         lst1.append(i)
    #         if lst[index + 1] != x:
    #             index += 1
    #             lst_fin.append((x, len(lst1), index))
    #             lst1 = []
    #             print('---------1------index, i, lst1', index, i, lst1)
    #
    #         if lst[index] == x:
    #             index += 1
    #             index_right += 1
    #             index_left = 0
    #             print('--------2-------index, i, lst1', index, i, lst1)
    #
    #     if i != x:
    #         #####################Uslovie kakoe to nuzhno zdes, ne vsegda append dalshe
    #         print('++++++++++++++  i, lst[index], index', i, index)
    #         if index == len(lst) - 1:
    #             lst_fin.append((x, len(lst1), index))
    #             print('lst_fin', lst_fin)
    #             break
    #         if lst[index + 1] == x and index <= len(lst):
    #             lst_fin.append((x, len(lst1), index_right))
    #             print('////////////////lst_fin, x, len(lst1), index, lst1', lst_fin, x, len(lst1), index, lst1)
    #             lst1 = []
    #             index += 1
    #             # index_right = 0
    #
    #         index_left += 1
    #         index += 1
    #         # lst = lst[:0] + lst[index_right + 1:]
    #         # Index uletaet tut naverh
    #
    #         print(' lst ====', lst, ' lst1 ====', lst1, '==== , index,  i', index, i)
    #
    #         # print('index_left===', index_left)
    #     print('lst_fin', lst_fin)

        # if index_left > 1:#S etim pozhe reshim
        #     print('lst do ====== ', lst)
        #     lst=lst[:0]+lst[index_right:]#index_right, lst ==== 5 [3, 3, 4, 3, 3]/[3, 4, 4, 4, 3, 2, 2, 1]
        #     print('index_right, lst ====', index_right, lst)
        #     break
#         print(lst1, index_right)
#     return lst1  # Vernem spisok s kortezhami, (index, dlina)
#
#
# max_povt(3, [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1])


  ############################################################################
    for i in lst:
        if i == x:
            lst1.append((i, index))
            index += 1
            index_right += 1
            index_left = 0
            print('---------------index, i, lst1', index, i, lst1)

        if i != x:
            index += 1
            #####################Uslovie kakoe to nuzhno zdes, ne vsegda append dalshe
            print('++++++++++++++  i, lst[index], index', index, i)
            if index == len(lst)-1:
                lst_fin.append((x, lst1))
                print('lst_fin', lst_fin)
                break
            if lst[index + 1] == x and index <= len(lst):
                lst_fin.append((x, lst1))
                print('//////////////// index, lst1', index, lst1)
                lst1 = []

                index_right = 0
            if lst[index + 1] != x:
                index_left += 1
                print('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ index i', index, i)

                # lst = lst[:0] + lst[index_right + 1:]
                #Index uletaet tut naverh

            print(' lst ====', lst, ' lst1 ====', lst1, '==== , index,  i', index,  i)

                # print('index_left===', index_left)
        print('lst_fin', lst_fin)

        # if index_left > 1:#S etim pozhe reshim
        #     print('lst do ====== ', lst)
        #     lst=lst[:0]+lst[index_right:]#index_right, lst ==== 5 [3, 3, 4, 3, 3]/[3, 4, 4, 4, 3, 2, 2, 1]
        #     print('index_right, lst ====', index_right, lst)
        #     break

    return lst1  # Vernem spisok s kortezhami, (index, dlina)


max_povt(3, [3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 3, 3, 1, 1, 3])
############################################################################

def skuch(lst):
    nov_dicc = {}
    lst1 = []
    lst2 = []  # Prefix
    l = len(nov_dicc)
    index1 = 1  # dlina prefixa
    # index_tek = 0
    # for i in lst:
    #     lst1.append(i)
    #     print([lst1.count(x) for x in lst1], len(lst1)) # Chislo povtorenii elementa i dlina prefixa
    # lst1=[lst.count(x) for x in lst]
    # print(lst1, len(lst1))
    #####################################################
    # lst1 = [lst.count(x) for x in lst]
    # print(lst)
    # print(lst1)
    # new_dicc = dict(zip(lst, lst1))  # Znacheniya i kolichestvo povtorov

    # print(new_dicc)
    #########################################################
    # index2=0
    # for i in range(len(lst)-1):
    #     while len(lst2) <= 1:
    #         lst2.append(lst[index2])
    #         print(lst2)
    #         index2 += 1
    #     lst2_counts = [lst2.count(x) for x in lst2]
    #     print(lst2, lst2_counts, len(lst2_counts))
    lst2_counts = [lst.count(x) for x in lst]  ##[3, 3, 4, 3, 3, 3, 4, 4, 4, 3, 2, 2, 1]
    print(lst2_counts)
    ####################### Naidem maximalnii slice=delta kazhdogo povtora################
    # from itertools import groupby
    # group = groupby(lst2_counts)
    # # print(max(group, key=lambda k: len(list(k[1])))) #(3, <itertools._grouper object at 0x7f39a58abac0>)
    # #####################################################
    # # group = groupby(lst2_counts)
    # result = []
    # index = 0
    # for k, g in group:
    #     length = len(list(g))
    #     result.append((k, length, index))
    #     index += length
    #
    # print(max(result, key=lambda a: a[1]))
    ################################################## Snachala naidem unikalnie elemeti, Potom Naidem max kol povtorov elementa x v spisle lst #################
    # lst.find('x', slice1, slice2) #Nahodit index sovpadeniya
    print('=========Unik==========', unik(lst2_counts))
    index1 = 0
    index2 = 0
    ll = []  # spisok slicov, zanesem v nego kortezhi(index1? index2? dlina)
    ############################333
    # for i in range(len(lst)-1):
    #     while len(lst2) <= 1:
    #         lst2.append(lst[index2])
    #         print(lst2)
    #         index2 += 1
    #     lst2_counts = [lst2.count(x) for x in lst2]
    #     print(lst2, lst2_counts, len(lst2_counts))
    for i in range(len(lst2_counts) - 1):
        while len(lst2_counts) <= 1 and lst2_counts[index2] == lst2_counts[index2 + 1]:
            # if lst2_counts[index2] == lst2_counts[index2+1]:
            index2 += 1  # Uvelichim na 1 slice
            ############################## proverka index2+1 index1-1 (est li vpravo vlevo cherez 1)#################33
            # while lst2_counts[index2+2] == lst2_counts[index2]:
            #     index2 = index2 + 1
            print((index2 - index1), index2, index1)
        l = (index2 - index1) + 1  # dlina slice
        ll.append((index2, index1, l))
        print('spisok slicov,', ll)

        index1 = index2
        index1 += 1
        index2 += 1
        # if lst2_counts[index2] != lst2_counts[index2+1]:
        #     l = (index2 - index1)+1  # dlina slice
        #     ll.append((index2, index1, l))
        #     print('spisok slicov,', ll)
        #
        #     index1 = index2
        #     index1 += 1
        #     index2 += 1
        # Sbros index1
    ######################################33
    # for i in lst2_counts:
    #     if i != lst2_counts[index2+1]:
    #         l = (index2-index1)# dlina slice
    #         ll.append((index2, index1, l))
    #         while index2 <= len(lst2_counts) - 1 and i != lst2_counts[index2]:
    #             index2 += 1
    #             index1 += 1
    #         print('==========index1, index2', index1, index2)
    #         print('spisok slicov,', ll)
    #     index2 += 1
    #     break
    #         index2 += 1
    #         if i == lst2_counts[index2]:
    #             index2 += 1
    #
    #         if i != lst2_counts[index2]:
    #             l = (index2 - index1)
    #             ll.append((i, index2, index1, l))
    #             print('spisok slicov,', ll, 'i', i)
    #             # break
    #             index1 = index2+1
    #         while i != lst2_counts[index2]:
    #                 print("---------------------")
    #                 index2 +=1
    #                 index1 +=1
    #                 break

    # if abs(lst2_counts[index1 - 1] - lst2_counts[index1]) > 1:##Nado tut uslovie uslozhnit - Schitaem kakih povtorov bolshe vsego,
    #     print('Максимальная длина префикса ', sum(lst2_counts))
    #     break

    # print('index2', index2)
    # lst2.append(lst[index2])
    # index2 += 1

    # if i in lst1:
    # index_tek =
    # # if i ==
    # nov_dicc.update({i:})
    # # print(nov_dicc[index])
    #
    # if i in nov_dicc:
    #     print("-----nov_dicc.get(i)----", nov_dicc.get(i))#=nov_dicc.get(i)+1
    # #
    # #     print("AYAYAY")
    # print(nov_dicc)
    # print('nov_dicc, index, nov_dicc[index]', nov_dicc, index, nov_dicc[index])#nov_dicc, index, nov_dicc[index] {1: 1, 2: 1, 3: 1} 3 1
    # print(all(x in lst for x in nov_lst))


skuch([1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5])  # 10
# skuch([1, 2, 3, 1, 2, 2, 3, 3, 1, 4, 4, 5]) #
# skuch([2, 4, 2, 3, 1, 3, 9, 15, 23]) #7

################ Tinkoff 3 #######################
# dupl = ([{4: 'g'}, {'g': 1}, {'g': 3}, {2: 'g'}, {'f': 'g'}, {'g': 1}, {2: 'g'}, {4: 'g'}])
# def sublist_in_list(sub, lis):
#     return str(sub).strip('[]') in str(lis).strip('[]')
# print(sublist_in_list(['d', 'f', 'g'], ['d', 'f',  'h', 'j', 'g']))
# lst_a= ['d', 'f', 'g']
# lst_b=['d', 'f',  'h', 'j', 'g']
# print(all(x in lst_b for x in lst_a))
##############################################
# import time
# def podstroka(n, s):#n ne ponyatno zachem podaetsya v funkciu, no takoe uslovie zadaniya
#     """ Podstroka - chast stroki vpodriad,Horoshaya - u kotoroi est vse uchavstvovavshie znaki, Nado naiti dlinu
#     minimalnou horoshey podstroki, u nas 4 simvola a b c d, esli hotya bi 1 net, to uzhe horoshe podstroki ne budet,
#     vivodim -1, v ost variantah vivodim dlinu """
#     # print(len(s))
#     a = ['a', 'b', 'c', 'd']
#     # aa = s.split()
#     aa = list(s)
#     # print(aa)#['a', 'a', 'b', 'b', 'd', 'd', 'c', 'c', 'b', 'a', 'd', 'd']
#     ############################################# 1. Uberem duplikati iz s
#     w = []
#     ww = []
#     www = ''
#     index1 = 0
#     for i in s:
#         if i not in w:
#             # w.append(i)
#             w.append(i)
#     # print(w)  # ['a', 'b', 'd', 'c'] w eto nazhi unicalnie simvoli,# {'b', 'c', 'd', 'a'}
#     # wk = ''.join(w)
#     # print(wk) # abdc  #bcda
#
#         ###########################################################
#         ############ poluchim podstroku ww, v kotoroi vse unikalnie w i ee dlinu, potom sravnim
#         # if len(w) != 4:
#             # print('-1')
#     # def find_podstroka(l):##Prinimaet str vozvrashaet str, len(str), esli vse znaki est ili None
#     ##################### STR #########3
#     # for i in range(len(s)):
#     #     ww = s[0:0] + s[:index1]
#     #     index1 += 1
#     #     print(ww)     # aabbddccbad
#     #     print(index1) # 12
#     def kluch_znach(kk,k, ss):
#
#         index1 = 0
#         dicc = {}
#         for i in ss:
#             # print('kk----------k', kk,k)
#             unik = all(x in kk for x in k)
#             # print(unik)
#             if unik == True:
#
#                 dicc.update({l: kk})
#                 # print(dicc)  # {7: ['a', 'a', 'b', 'b', 'd', 'd', 'c']}
#                 index1 += 1
#                 ss = ss[:0] + ss[index1:]
#                 # print(ss)
#                 # print(index1, ss, kk)
#                 kk = [] ## Sbrasivaem kk
#             kk.append(i)
#             # index1 += 1
#             # print(ww)  # ['a', 'a', 'b', 'b', 'd', 'd', 'c']
#             l = len(kk)
#             # print(l)  # 7
#             #################### Slozhim dlinu i znacheniya v slovar dicc #######
#             #################### Vozmem min znachenie klucha v wlovare dicc ################
#         # return dicc
#         final_lst = []
#         for k in dicc:
#             final_lst.append(k) # Sformiruem spisok znachenii dlin horoshih podstrok
#         if min(final_lst) >= 4:
#             print('Минимальная длина хорошей подстроки', min(final_lst))
#             # print(final_lst)
#         if min(final_lst) < 4:
#             print('-1')
#
#     kluch_znach(ww, w, s)
#
# start = time.time()
# # func('7 4 3 3')
# # # func('7 4 3 1')
# # # func('1 3 6 9')
# podstroka(12, 'aadссdbadd')
# end = time.time()
# print('Time for func', end - start)
###############################
# # ################# Tinkoff 2 ###########################
#
# def proverka(n, m, k):  ## n - djuni, m seniori, k kolichestvo proverok senoirami djunov, skorost 1 djun v 1 minutu
#
#     pass
#     t = n/m*k
#     print(round(t))
#
# proverka(7, 3, 2)## 2 seniora obrabotaut 6 djunov po 2 raza kazhdogo za 6 minut
#
# #####################Tinkoff 1 ########################
# import time
#
#
# def func(l):
#     l = l.split(" ")
#     index1 = 0
#     index2 = 0
#     index3 = 0
#     # while index1 <= len(l)-2:
#     for i in range(len(l) - 1):
#         if l[index1] == l[index1 + 1]:
#             print('YES')##Ia hotel "NO" postavit, no v uslovii zadania pochemu to 'YES' nado postavit pri ravenstve chlenov
#             index1 += 1
#             break
#         if l[index1] > l[index1 + 1]:  # and index <= len(l)-1
#             index1 += 1
#             index2 += 1
#             print('------------', index1, index2, index3)
#
#         # print(l[index1])
#         elif l[index1] < l[index1 + 1]:
#             print('++++++++++++++++', index1)
#             index1 += 1
#             index3 += 1
#
#         elif l[index1] == l[index1 + 1]:
#             print('NO')
#
#     # print(index1, index2, index3)
#
#     if index1 == index2 or index1 == index3:
#         print('YES')
#     # if index1 != index2 and index1 != index3:
#     #         print('NO')
#
#
# start = time.time()
# func('7 4 3 3')
# # func('7 4 3 1')
# # func('1 3 6 9')
# end = time.time()
# print('Time for func', end - start)

######################################################

###Sortiruem spisok slovarey  nums([{'g':1}, {'g':3}, {2:'g'}, {'f':'g'}, {'g':1}, {2:'g'}, {4:'g'}])###################
# def sort_single_file(nums, low, high, nomer):##nomer pozicia, kotoruu sortiruem, naprimer 3ii element kazdogo elmenta nums
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i][nomer] < pivot[nomer]:
#             i += 1
#
#         j -= 1
#         while nums[j][nomer] > pivot[nomer]:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quick_sort(nums, nomer):
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#
#
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = sort_single_file(items, low, high, nomer)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
# dupl = ([{'g': 1}, {'g': 3}, {2: 'g'}, {'f': 'g'}, {'g': 1}, {2: 'g'}, {4: 'g'}])
# quick_sort(dupl)
################################### Soedinyaet duplicati ##########################
# dupl = ([{4: 'g'}, {'g': 1}, {'g': 3}, {2: 'g'}, {'f': 'g'}, {'g': 1}, {2: 'g'}, {4: 'g'}])
#
#
# def sort_dupl_dic(kw):
#     dup = []
#     for i in range(len(kw)):  # and index1 < len(kw)
#         if kw[i] not in dup:
#             dup.append(kw[i])
#         elif kw[i] in dup:
#             nomer = kw.index(kw[i])
#             print(nomer)
#             dup.insert(nomer + 1, kw[i])
#
#     print(dup)
#
#
# sort_dupl_dic(dupl)

###########################################
# dup = []
# for i in range(len(kw)):
#     for k in kw[i]:
#         if k not in dup:
#             dup.append(k)
#         print(dup)
# print(k)
#####################################
# for i in k[1]:
#     print(k[1][i])
# print(k[1].get(1))
#################################


############################

# def dupl(data_2):  ##Ubiraem duplikati v otsortirovannom spiske data_2 (sverhu otsortirovali)
#     index = 0
#     index2 = 0
#     data_finish = []
#     while index < len(data_2):
#         while index < len(data_2) - 1 and data_2[index] == data_2[index + 1]:
#             index += 1
#         print('data_2[index2]) ==', data_2[index2])
#         data_2[index2] = data_2[index]
#         data_finish.append(data_2[index2])
#         index2 += 1
#         index += 1
#         print(data_finish)
#
# dupl([{4: 'g'}, {4: 'g'}, {'g': 1}, {'g': 1}, {'g': 3}, {2: 'g'}, {2: 'g'}, {'f': 'g'}])
# dupl(['g', 'g', 'g', 1, 2, 2, 2])
# return data_finish
# [{4: 'g'}, {'g': 1}, {'g': 3}, {2: 'g'}, {'f': 'g'}]
