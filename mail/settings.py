# -*- coding: utf-8 -*-

# С какого адреса посылать
from_address = 'mail@sicamp.ru'

# Как зовут отправителя
from_name = 'ЛКЛ'

# Тема письма
subject = 'ЛКЛ 2016'

# В каком поле в csv лежит адрес ученика
email_field = 22

# Какие строки в письмах на какие поля из csv заменить
placeholders = {
    'SURNAME': 0,
    'NAME': 1,
    'PAR': 3
}
