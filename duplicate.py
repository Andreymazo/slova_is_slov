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
#[{4: 'g'}, {'g': 1}, {'g': 3}, {2: 'g'}, {'f': 'g'}]