from urllib import request
import re

 #нормально работает только для google =)

 #Поиск абсолютных url-путей
def get_absolutely_path(string):
    pattern = '(?:http:\/\/|https:\/\/){1}(?:\w+\.){1,31}(?:[^"]+)'
    return re.findall(pattern, string)


 #Поиск относительных путей
def get_relative_path(string):
    pattern = '(?:href="\/){1}(?:[^"]+)'
    return re.findall(pattern, string)


 #Преобразование путей к абсолютному виду и добавление их к общему списку
def add_path(repl, relative, absolute = None):
    if absolute is None:
        absolute = []
    pattern = 'href="'
    for link in relative:
        link = re.sub(pattern, repl, link)
        absolute.append(link)
    return absolute


 #Отбор рабочих ссылок
def working(links):
    working_links = []
    for link in links:
        if request.urlopen(request.Request(link)).getcode() == 200:
            working_links.append(link)
        else:
            pass
    return working_links


 #чтение страницы
myurl = 'http://google.com'
req = request.Request(myurl)
response = request.urlopen(req)
web_page = str(response.read())

links_a = get_absolutely_path(web_page)
links_r = get_relative_path(web_page)
links = add_path(myurl, links_r, links_a)
working_links = working(links)

 #печать рабочих ссылок для проверки
for link in working_links:
    print(link)






