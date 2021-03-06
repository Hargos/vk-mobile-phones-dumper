import datetime

# ------------------------ Файл с настройками дампера ------------------------ #
#																			   #
#            https://github.com/jieggii/vk-mobile-phones-dumper-sql		       #
#																			   #
# ------------------------ Настройки пользователя ---------------------------- #

user = {
    'access_token': 'abcdefg12345'     # Ключ доступа к странице. Можно получить на https://vkhost.github.io/
}



# ------------------------ Настройки подключения к базе данных ------------------------ #
#     (Если вы действовали по инструкции в README.md, то тут менять ничего не надо)

db = {
    'host': 'localhost',                                                                # Хост базы данных
    'db_name': 'vk_dumper',                                                             # Название базы данных
    'table_name': 'vkdump' + datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'),    # Название автоматически создаваемой таблицы. По умолчанию - текущая дата
    'charset': 'utf8mb4',                                                               # Кодировка базы данных
    'login': 'root',                                                                    # Имя пользователя базы данных
    'password': ''                                                                      # Пароль пользователя базы данных
}



# ------------------------ Настройки фильтра ------------------------ #
#     Добавлять записи в фильтр следует только маленькими буквами!!!

filtr = {
    'phone_blacklisted_symbols': [              # Черный список символов, при наличии в номере телефона которых, пользователь не будет записан в бд

        'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x',
        'y', 'z',
             
        'а', 'б', 'в', 'г', 'д', 'е',
        'ё', 'ж', 'з', 'и', 'й', 'к',
        'л', 'м', 'н', 'о', 'п', 'р',
        'с', 'т', 'у', 'ф', 'х', 'ц',
        'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
        'э', 'ю', 'я',
        
        '*', '.', '_',

    ],

    'phone_blacklisted_phones': [           # Черный список номеров. Если номер пользователя равен номеру из списка, пользователь не записывается в бд
        '88005553535',
    ],

    'sex_blacklisted_sex': [                # Черный список полов. Если пол пользователя равен полу из списка, пользователь не записывается в бд
        #'мужской',
        #'женский',
        #'не указан',
    ],

    'city_blacklisted_city': [              # Черный список городов. Если город пользователя равен городу из списка, пользователь не записывается в бд
        #'москва',
        #'санкт-петербург',
        #'не указан',
    ],

    'country_blacklisted_country': [        # Черный список стран. Если страна пользователя равна стране из списка, пользователь не записывается в бд
        #'россия',
        #'украина',
        #'не указана',
    ],

    'bdate_blacklisted_bdate': [            # Черный список дат рождения. Если дата рождения пользователя равна дате рождения из списка, пользователь не записывается в бд
        #'01.01.1999',
        #'12.10.1985',
        #'не указана',
    ]
}
