sorted_dict = {}
# with open('1.txt', 'rt', encoding= 'utf-8') as f1:
#     text_1 = f1.read()
#     lines_1 =text_1.count('\n') + 1
#
# with open('2.txt', 'rt', encoding= 'utf-8') as f2:
#     text_2 = f2.read()
#     lines_2 = text_2.count('\n') + 1
#
# with open('3.txt', 'rt', encoding= 'utf-8') as f3:
#     text_3 = f3.read()
#     lines_3 = text_3.count('\n') + 1
#
# sorted_dict['text_1'] = lines_1
# sorted_dict['text_2'] = lines_2
# sorted_dict['text_3'] = lines_3
#
# sorted_values = sorted(sorted_dict.values())
# dict = {}
#
# for i in sorted_values:
#     for k in sorted_dict.keys():
#         if sorted_dict[k] == i:
#             dict[k] = sorted_dict[k]
#             break
# print(dict)
#
# print('Имя файла = 1.txt','\n''Колличество строк = ', lines_1)
# print('Имя файла = 2.txt','\n''Колличество строк = ', lines_2)
# print('Имя файла = 3.txt','\n''Колличество строк = ', lines_3)


d = {}
for i in range(1, 4):
    name = f'{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        d[name] = [x for x in f.read().splitlines() if x]

with open('final_file.txt', 'w', encoding='utf-8') as file:
    for k, v in sorted(d.items(), key=lambda x: len((x[-1]))):
        file.write(k + '\n')
        file.write(str(len(v)) + '\n')
        file.write('\n'.join(v))
        file.write('\n')