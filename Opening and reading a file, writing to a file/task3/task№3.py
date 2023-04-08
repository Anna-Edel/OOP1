from operator import itemgetter


def number_of_line(*files):
    list_of_files = []
    text_f = []
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            text_f = file_obj.read().splitlines()
            file_length = len(text_f)
            name_file = file
            list_of_files.append([name_file, file_length, text_f])
            list_of_files.sort(key=itemgetter(1))
    print(list_of_files)
    return list_of_files


number_line = number_of_line('1.txt', '2.txt', '3.txt')


def writing_file(list_of_files):
    with open('all_texts.txt', 'w', encoding='utf-8') as file_obj:
        for file in list_of_files:
            for element in file:
                file_obj.write(f'{element}\n')
    file_path = 'all_texts.txt'
    return file_path


print(writing_file(number_line))
