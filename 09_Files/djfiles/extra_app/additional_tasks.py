import os
from _csv import reader, writer
from datetime import datetime
from decimal import Decimal

from djfiles.settings import BASE_DIR
from .models import *


STOP_WORDS = ['Это', 'слово', 'нельзя', 'Использовать']
SAVE_PATH = os.path.join(BASE_DIR, 'save')


def check_stop_words(file):
    file_lines = file.decode('utf-8').split('\n')
    for line in file_lines:
        line_lower = line.lower()
        for word in STOP_WORDS:
            if line_lower.find(word.lower()) > -1:
                return False
    return True


def price_parsing(file, price_file):
    price_str = price_file.decode('utf-8').split('\n')
    if file.content_type == 'application/vnd.ms-excel':
        csv_reader = reader(price_str, delimiter=';', quotechar='"')
        for row in csv_reader:
            try:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            except:
                pass
    elif file.content_type == 'text/plain':
        for row in price_str:
            try:
                code, price = row.split(':')
                Item.objects.filter(code=code).update(price=Decimal(price))
            except:
                pass


def file_write(file, price_file):
    now = datetime.now()
    now_str = now.strftime("%d%m%y-%H-%M-%S")
    file_name = os.path.join(SAVE_PATH, now_str + '_' + file.name)
    with open(file_name, 'w') as save_file:
        writer(save_file)

