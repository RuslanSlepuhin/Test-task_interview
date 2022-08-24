
def sort_words(file_name):
    """
    В исходном файле находятся строки с переводом английских слов на русские в формате
    Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur	астурийский ; астурлеонский
    Это значит, что каждое из английских слов (Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur) может переводиться
    как любое русское (астурийский ; астурлеонский)
    Также встречаются простые варианты где в строке 1 английское и русское слово
    Abidjan	Абиджан
    Английские слова отделены от русских переводов символом табуляции
    Функция парсит этот файл и на базе него делает 2 файла - English.txt и Russian txt, где каждой строке на английском
    будет соответствовать строка перевода на русском в другом файле во всех возможных вариантах.
    Пример текста, который должен получиться в файлах, после работы вашего кода:

    English.txt				Russian.txt

    Astur-Leonese				астурийский
    Astur-Leonese				астурлеонский
    Asturian				    астурийский
    Asturian				    астурлеонский
    Asturian-Leonese			астурийский
    Asturian-Leonese			астурлеонский
    ....						....
    :param file_name: передается имя файла (вместе с path), который нужно распарсить
    :return: None
    """

    try:
        with open(file_name, encoding='utf-8', mode='r') as file:
            for line in file:  # читает построчно

                line = line.strip()  # убирает из строки в начале и в конце пробелы, в том числе перевод строк

                if line and line[0:1] != '#':  # если строка не закомментирована и не пустая
                    line_split = line.split(f'\t')  # отделяет английские слова от русских по символу табуляции

                    for eng_word in line_split[0].split(';'):
                        for rus_word in line_split[1].split(';'):

                            with open('English.txt', encoding='utf-8', mode='a') as file_eng:
                                file_eng.writelines(f'{eng_word.strip()}\n')

                            with open('Russian.txt', encoding='utf-8', mode='a') as file_rus:
                                file_rus.writelines(f'{rus_word.strip()}\n')

    except Exception as e:
        print(f'Ошибка чтения файла\n{e}')
        return False

    return True


answer = sort_words(file_name='PythonTest.txt')
if answer:
    print('Код отработал успешно')
else:
    print('Код не отработал, ошибка')
