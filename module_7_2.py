def custom_write (file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')

    for i, string in enumerate(strings, start=1):
        start_position = file.tell()
        file.write(string + '\n')
        string_position [(i, start_position)] = string

    file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)