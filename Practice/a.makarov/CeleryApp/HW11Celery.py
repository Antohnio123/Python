# Запускать будучи в папке CeleryApp строкой:
# python -m celery -A HW11Celery worker -P gevent
# и в другом окне терминала запустить периодическую задачу:
# celery -A HW11Celery beat

from __future__ import absolute_import, unicode_literals
from celery import Celery
import datetime
from urllib import request as ureq


app = Celery('HW11Celery', broker='amqp://guest@localhost//')
app.conf.CELERY_RESULT_BACKEND='amqp://'
t = 5           # время перепроверки погоды в секундах
web_site = 'https://www.meteoservice.ru/weather/now/nizhniy-novgorod'
# Ресурс, предоставляющий данные о погоде
api_key='551a1edb737d369fc1d85facad27a0eb'
# ключ для получения данных о погоде по API с сайта https://openweathermap.org/city/520555

@app.task
def weather():
    req = ureq.Request(web_site)
    response = ureq.urlopen(req)
    web_page = str(response.read().decode('utf-8'))

    Ind1 = web_page.index('<div class="small-6 medium-6 large-4 columns text-center">') + 113
    Ind1_1 = web_page[Ind1:].index('&deg;</span>') + Ind1
    t1 = web_page[Ind1:Ind1_1]

    Ind2 = web_page.index('<p class="margin-bottom-0">') + 27
    Ind2_1 = web_page[Ind2:].index('</p>') + Ind2
    t2 = web_page[Ind2:Ind2_1]

    # t3 = requests.get(
    #     'https://api.openweathermap.org/data/2.5/weather?q=NizhnyNovgorod,ru&units=metric&lang=ru&appid=551a1edb737d369fc1d85facad27a0eb')

    result = 'В Нижнем Новгороде на ' + str(datetime.datetime.now().ctime()) + \
             ' температура равна: ' + str(t1) + ' по Цельсию. ' + str(t2) + '. (Предоставлено Meteoservice.ru)\n'
    print(result)

    with open ('weatherNNlog.txt', 'a', encoding='utf-8') as log:
        log.write(result)
    return result
#  format(timespec='seconds')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls weather() every t seconds.
    sender.add_periodic_task(t, weather.s(), name='Get weather.')


if __name__ == '__main__':
    # app.start()
    app.worker_main()


