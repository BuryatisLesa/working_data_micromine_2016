import MMpy

def get_data(name_column, name_file):
    """получение данных с столбца любого файла """

    path = MMpy.Project.path() + name_file # создание абсолютного пути до файла
    file = MMpy.File() # создание экземляра для работы с файлом
    file.open(path)

    id_column = file.get_field_id(name_column) # получаем id столбца
    count_records = file.records_count # получаем количество записей в файле

    data = [] # создаем массив для наших данных
    for rec in range(count_records):
        push_data = file.get_str_field_value(id_column, rec+1)
        data.append(push_data)
    file.close()
    return data