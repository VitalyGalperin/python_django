from .models import Advertisement
import datetime


def fill_db(numbers):
    for i in range(0, numbers):
        new_advertisement = Advertisement(title='Объявление ' + str(i),
                                          description='Текст объявления' + str(i),
                                          price=i,
                                          created_at=datetime.datetime.now(),
                                          update_at=datetime.datetime.now(),
                                          views_count=i,
                                          advertisement_status='Черновик',
                                          advertisement_type='Приму в дар',
                                          )
        new_advertisement.save()


fill_db(500000)
