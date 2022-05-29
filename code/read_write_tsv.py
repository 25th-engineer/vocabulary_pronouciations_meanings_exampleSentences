import csv
import re
import time
import operator

def write_to_tsv(output_path: str, file_columns: list, data: list):
    csv.register_dialect('tsv_dialect', delimiter='\t', quoting=csv.QUOTE_NONE, quotechar=None, escapechar="|")
    wf = open(output_path, 'w', newline='', encoding='utf-8-sig')
    # with open(output_path, 'w', newline='', encoding='utf-8-sig') as wf:
    writer = csv.DictWriter(wf, fieldnames=file_columns, dialect='tsv_dialect')
    writer.writerows(data)
    csv.unregister_dialect('tsv_dialect')
    wf.close()


def read_from_tsv(file_path: str, column_names: list) -> list:
    csv.register_dialect('tsv_dialect', delimiter='\t', quoting=csv.QUOTE_ALL)
    with open(file_path, 'r', encoding = 'utf8') as wf:
        reader = csv.DictReader(wf, fieldnames=column_names, dialect='tsv_dialect')
        data_list = []
        for row in reader:
            data = dict(row)
            data_list.append(data)
    csv.unregister_dialect('tsv_dialect')
    wf.close()
    return data_list


def extract_line_with_pronunciation(file_path: str, file_path_new_1: str, file_path_new_2: str):
    wf = open(file_path, 'r', encoding='utf8')
    nf1 = open(file_path_new_1, 'w+', encoding='utf8')
    nf2 = open(file_path_new_2, 'w+', encoding='utf8')
    line = wf.readline()
    pattern_1 = re.compile('\t美\[')
    pattern_2 = re.compile('\t英\[')
    while line:
        res_1 = pattern_1.search(line)
        res_2 = pattern_2.search(line)
        if res_1 or res_2:
            nf1.write(line)
        else:
            nf2.write(line)
        line = wf.readline()
    nf2.close()
    nf1.close()
    wf.close()


def split_pronunciation_line(file_path: str, column_names: list) -> list:
    data_list = read_from_tsv(file_path, column_names)  # ['WORD_ID', 'SINGLE_WORD', 'WORD_MEANINGS', 'EXAMPLE_SENTENCES']
    pattern_1 = re.compile('美\[.*英.*\][，]')
    pattern_2 = re.compile('英\[.*\][，]')
    pattern_3 = re.compile('美\[.*\][，]')
    set_usa_un = set()
    set_un = set()
    set_usa = set()
    id_pronunciation = dict()
    id_meaning = dict()
    complete_format = []

    for column in data_list:
        pm = column['WORD_MEANINGS']
        res_1 = pattern_1.search(pm)
        res_2 = pattern_2.search(pm)
        res_3 = pattern_3.search(pm)
        id = int(column['WORD_ID'])

        if res_1:
            set_usa_un.add(id)
            id_pronunciation[id] = res_1.group()
            id_meaning[id] = str(pm).replace(res_1.group(), '')
        elif res_2 and (id not in set_usa_un):  # and (id not in set_usa):
            set_un.add(id)
            id_pronunciation[id] = res_2.group()
            id_meaning[id] = str(pm).replace(res_2.group(), '')
        elif res_3 and (id not in set_usa_un):  # and (id not in set_un):
            set_usa.add(id)
            id_pronunciation[id] = res_3.group()
            id_meaning[id] = str(pm).replace(res_3.group(), '')

        if id in set_usa_un:
            item = {'id': id, 'word': column['SINGLE_WORD'], 'pronunciation': id_pronunciation[id],
                    'meaning': id_meaning[id], 'EXAMPLE_sentence': column['EXAMPLE_SENTENCES']}
        elif id in set_un:
            item = {'id': id, 'word': column['SINGLE_WORD'], 'pronunciation': id_pronunciation[id],
                    'meaning': id_meaning[id], 'EXAMPLE_sentence': column['EXAMPLE_SENTENCES']}
        elif id in set_usa:
            item = {'id': id, 'word': column['SINGLE_WORD'], 'pronunciation': id_pronunciation[id],
                    'meaning': id_meaning[id], 'example_sentence': column['EXAMPLE_SENTENCES']}

        complete_format.append(item)

    return complete_format


def split_pronunciation_line_no_pronunciation(file_path: str, column_names: list) -> list:
    data_list = read_from_tsv(file_path, column_names)
    complete_format = []
    for column in data_list:
        if column['WORD_ID'] == '\ufeff9':
            column['WORD_ID'] = '9'
        '''
        # The following item is wrong for 'example_sentences' is not UPPERCASE but lowercase.
        item = {'id': column['WORD_ID'], 'word': column['SINGLE_WORD'], 'pronunciation': '',
                'meaning': column['WORD_MEANINGS'], 'example_sentences': column['EXAMPLE_SENTENCES']}
        '''
        item = {'id': column['WORD_ID'], 'word': column['SINGLE_WORD'], 'pronunciation': '',
                'meaning': column['WORD_MEANINGS'], 'EXAMPLE_SENTENCES': column['EXAMPLE_SENTENCES']}
        complete_format.append(item)
    # print(complete_format)

    # complete_format = [{'id': '9', 'word': 'grimoires', 'pronunciation': '网络释义： 魔法之书；中世纪巫术之书；魔典；',
    #                     'meaning': '', 'EXAMPLE_SENTENCES': ''},
    #                    {'id': '10', 'word': 'subreptitious', 'pronunciation': '网络释义： 隐瞒事实的；',
    #                     'meaning': '', 'EXAMPLE_SENTENCES': ''}]
    return complete_format


def combine_tsv_with_same_headers(file_path_1: str, file_path_2: str, column_names: list) -> list:
    data_list_1 = read_from_tsv(file_path_1, column_names)
    data_list_2 = read_from_tsv(file_path_2, column_names)
    complete_format = []
    for column in data_list_1:
        item = {'id': column['id'], 'word': column['word'], 'pronunciation': column['pronunciation'],
                'meaning': column['meaning'], 'EXAMPLE_SENTENCES': column['EXAMPLE_SENTENCES']}
        complete_format.append(item)
    for column in data_list_2:
        item = {'id': column['id'], 'word': column['word'], 'pronunciation': column['pronunciation'],
                'meaning': column['meaning'], 'EXAMPLE_SENTENCES': column['EXAMPLE_SENTENCES']}
        complete_format.append(item)
    return complete_format


def fun1(file_path_: str):
    data_list = read_from_tsv(file_path_, ['WORD_ID', 'SINGLE_WORD', 'WORD_MEANINGS', 'EXAMPLE_SENTENCES'])
    cnt = 0
    for i in data_list:
        print(i)
        cnt += 1
        if cnt == 100:
            break


def fun2(file_path_origin: str, file_path_new_1: str, file_path_new_2: str):
    '''
    file_path_origin = './TSV_data/origin/unduplicated_word_pronounciations_meanings_example_sentences.tsv'
    file_path_new_1 = './TSV_data/1_yes.tsv'
    file_path_new_2 = './TSV_data/2_no.tsv'
    '''
    time_start = time.time()
    extract_line_with_pronunciation(file_path_origin, file_path_new_1, file_path_new_2)
    time_end = time.time()
    time_sum = time_end - time_start
    print('Time used:\n' + str(time_sum) + ' seconds.')


def fun3(file_path: str, output_path: str, column_names_1: list, column_names_2: list):
    '''
    file_path = './TSV_data/1_yes.tsv'
    output_path = './TSV_data/partly_completed.tsv'
    column_names_1 = ['WORD_ID', 'SINGLE_WORD', 'WORD_MEANINGS', 'EXAMPLE_SENTENCES']
    column_names_2 = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_sentence']
    '''
    complete_format = split_pronunciation_line(file_path, column_names_1)
    write_to_tsv(output_path, column_names_2, complete_format)


def fun4(file_path: str, output_path: str, column_names_1: list, column_names_2: list):
    '''
    file_path = './TSV_data/2_no.tsv'
    output_path = './TSV_data/partly_completed_no.tsv'
    column_names_1 = ['WORD_ID', 'SINGLE_WORD', 'WORD_MEANINGS', 'EXAMPLE_SENTENCES']
    column_names_2 = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_sentences']
    '''
    complete_format = split_pronunciation_line_no_pronunciation(file_path, column_names_1)
    write_to_tsv(output_path, column_names_2, complete_format)


def fun5(output_path_combine: str, file_path_1: str, file_path_2: str, column_names: list):
    '''
    output_path_combine = './TSV_data/combined_version.tsv'
    file_path_yes = './TSV_data/partly_completed_yes.tsv'
    file_path_no = './TSV_data/partly_completed_no.tsv'
    column_names = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES']
    '''
    complete_format = combine_tsv_with_same_headers(file_path_1, file_path_2, column_names)

    # # sorted by id firstly and alphabet secondly.
    # complete_format = sorted(complete_format , key=lambda elem: "%06d %s" %
    #         (int(str(elem['id']).replace('\ufeff', '').replace('"', '')), elem['word']))

    # # sorted by id only.
    complete_format = sorted(complete_format, key=lambda elem: "%06d" %
                               (int(str(elem['id']).replace('\ufeff', '').replace('"', ''))))

    # # sorted by alphabet only.
    # complete_format = sorted(complete_format, key=lambda elem: "%s" % (elem['word']))
    write_to_tsv(output_path_combine, column_names_2, complete_format)


def fun6(file_path_len_field: str, column_names: list):
    '''
    file_path_len_field = './TSV_data/3_combined_version_sorted_by_consecutive_IDs.tsv'
    column_names = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES']
    '''
    complete_format = read_from_tsv(file_path_len_field, column_names)
    maxLen = -1
    filed_name = ''
    maxLen_1 = -1
    maxLen_2 = -1
    maxLen_3 = -1
    maxLen_4 = -1
    maxLen_5 = -1
    for column in complete_format:
        maxLen_1 = max(len(column['id']), maxLen_1)
        maxLen_2 = max(len(column['word']), maxLen_2)
        maxLen_3 = max(len(column['pronunciation']), maxLen_3)
        maxLen_4 = max(len(column['meaning']), maxLen_4)
        maxLen_5 = max(len(column['EXAMPLE_SENTENCES']), maxLen_5)
        for filed in column_names:
            maxLen = max(len(column[filed]), maxLen)
            filed_name = filed
    print(maxLen)
    print(filed_name)
    print('**********')
    print(str(maxLen_1) + ' ' + str(maxLen_2)+ ' ' + str(maxLen_3)+ ' ' + str(maxLen_4)+ ' ' + str(maxLen_5))
    return maxLen


def fun7(file_path_1: str, file_path_2: str, column_names: list):
    '''
    # # origin:
    def fun7(file_path_1: str, file_path_2: str, column_names: list) -> (list, list):
    file_path_1 = './TSV_data/3_combined_version_sorted_by_consecutive_IDs.tsv'
    file_path_2 = './TSV_data/word.csv'
    column_names = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES']
    '''
    complete_format = read_from_tsv(file_path_1, column_names)
    word_list_1 = []
    id_list = []
    for column in complete_format:
        id_list.append(column['id'])
        word_list_1.append(column['word'])
    file_word_data = open(file_path_2, 'r', encoding='utf-8')
    word_data = file_word_data.readline()
    word_list_2 = []
    while word_data:
        word_list_2.append(word_data.strip('\n'))
        word_data = file_word_data.readline()

    word_list_1 = sorted(word_list_1)
    word_list_2 = sorted(word_list_2)
    print(word_list_1[0:90])
    print(word_list_2[0:90])
    print(operator.eq(word_list_1, word_list_2))
    print(str(len(word_list_1)) + ' - ' + str(len(word_list_2)))
    for word in word_list_1:
        if word not in word_list_2:
            print('Found. -- ' + word)
            break
    print('*************************************')
    id_list[0] = 1
    id_list[8] = 9
    id_list = [int(j) for j in id_list]
    # cnt = 0
    # for i in id_list:
    #     id_list[cnt] = int(i)
    #     cnt += 1
    print(id_list[0:20])
    print(len(id_list))
    discrete_id_list = []
    for i in range(1, len(id_list)):
        if id_list[i - 1] != id_list[i] - 1:
            # print(id_list[i])
            discrete_id_list.append(id_list[i] - 1)

    print(len(discrete_id_list))
    print(discrete_id_list)
    print('*************************************')
    # # origin:
    '''return word_list_1, word_list_2'''


def fun8(file_path: str):
    '''
    file_path = './TSV_data/id.csv'
    '''
    file_id_data = open(file_path, 'r', encoding='utf-8')
    id_data = file_id_data.readline()
    id_list = []
    while id_data:
        id_list.append(int(id_data))
        id_data = file_id_data.readline()

    print(len(id_list))
    discrete_id_list = []
    for i in range(1, len(id_list)):
        if id_list[i - 1] != id_list[i] - 1:
            discrete_id_list.append(id_list[i] - 1)
    print(len(discrete_id_list))
    print(discrete_id_list)


def fun9(file_path_1: str, file_path_2: str, column_names: list):
    '''
    file_path_1 = './TSV_data/3_combined_version_sorted_by_consecutive_IDs.tsv'
    file_path_2 = './TSV_data/combined_version_resorted_by_id.tsv'
    column_names = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES']
    '''
    complete_format = read_from_tsv(file_path_1, column_names)
    resort_id_list = []
    for i in range(len(complete_format)):
        # complete_format[i]['id'] = i + 1
        item ={'id': i + 1, 'word': complete_format[i]['word'], 'pronunciation': complete_format[i]['pronunciation'],
               'meaning': complete_format[i]['meaning'], 'EXAMPLE_SENTENCES': complete_format[i]['EXAMPLE_SENTENCES']}
        resort_id_list.append(item)

    for j in range(10):
        print(resort_id_list[j])
    resort_id_list = sorted(resort_id_list, key=lambda elem: "%s" % (elem['word']))
    write_to_tsv(file_path_2, column_names, resort_id_list)


if __name__ == '__main__':
    # # fun1. fun2
    file_path_origin = './TSV_data/origin/unduplicated_word_pronounciations_meanings_example_sentences.tsv'
    file_path_new_1 = './TSV_data/1_yes.tsv'
    file_path_new_2 = './TSV_data/2_no.tsv'

    # # fun3
    file_path_yes = './TSV_data/1_yes.tsv'    # yes
    output_path_yes = './TSV_data/partly_completed_yes.tsv'
    column_names_1 = ['WORD_ID', 'SINGLE_WORD', 'WORD_MEANINGS', 'EXAMPLE_SENTENCES']
    column_names_2 = ['id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES']

    # # fun4
    file_path_no = './TSV_data/2_no.tsv'  # no
    output_path_no = './TSV_data/partly_completed_no.tsv'

    # # fun5
    output_path_combine = './TSV_data/combined_version.tsv'

    # # fun6
    file_path_len_field = './TSV_data/3_combined_version_sorted_by_consecutive_IDs.tsv'

    # # fun7
    file_path_word = './TSV_data/word_nonconsecutive_IDs.csv'

    # # fun8
    file_path_id = './TSV_data/id_nonconsecutive.csv'

    # # fun9
    file_path_to_resort_id = file_path_len_field
    file_path_resorted_id = './TSV_data/5_combined_version_sorted_by_alphabet.tsv'

    '''
    Only one of the following functions can be executed at a time.
    '''
    fun1(file_path_origin)
    # fun2(file_path_origin, file_path_new_1, file_path_new_2)
    # fun3(file_path_yes, output_path_yes, column_names_1, column_names_2)
    # fun4(file_path_no, output_path_no, column_names_1, column_names_2)
    # fun5(output_path_combine, output_path_yes, output_path_no, column_names_2)
    # fun6(file_path_len_field, column_names_2) # max length of field is: 2115, so 2500 may be enough.
    '''The max length of each field is: 6, 31, 74, 375, 2115.('id', 'word', 'pronunciation', 'meaning', 'EXAMPLE_SENTENCES')'''
    # fun7(file_path_len_field, file_path_word, column_names_2)
    # fun8(file_path_id)
    # fun9(file_path_to_resort_id, file_path_resorted_id, column_names_2)
    print('Done.')

