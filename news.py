import requests
import pprint
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='a1495f8739354ee3af2b3f7748357707')
sources = newsapi.get_sources()
sources_list = sources['sources']

def list_language(): # Получения списка языков
    set_language = set()
    for element  in sources_list:
        set_language.add(element.get('language'))
    print(set_language)

def get_sources_list(): # Проба получения списка источников
    set_sources = set()
    for element  in sources_list:
        set_sources.add(element.get('id'))
    return (set_sources)

def get_category(user_categorys, laguage, page_size, page_number): # Первое задание
    #set_category = set()
    #for element  in sources_list:
    #    set_category.add(element.get('category'))
    #print ('Список категорий: ' + str(set_category))
    user_categorys_list = user_categorys.split(' ')
    user_categorys_list_text = ''
    for element in user_categorys_list:
         user_categorys_list_text += 'category=' + element + '&'
    url = ('https://newsapi.org/v2/top-headlines?' +
       user_categorys_list_text +
       'language=' + laguage + '&' +
       'pageSize=' + page_size + '&' +
       'page=' +  page_number + '&' +
       'apiKey=a1495f8739354ee3af2b3f7748357707'
       )
    print (url)
    response = requests.get(url)
    pprint.pprint (response.json())
def get_key_words(user_key_words, laguage, page_size, page_number): # второе задание задание
    user_key_words_list = user_key_words.split(' ')
    user_key_words_list_text = ''
    for element in  user_key_words_list:
        user_key_words_list_text  += 'q=' + element + '&'
    url = ('https://newsapi.org/v2/top-headlines?' +
       user_key_words_list_text +
       'language=' + laguage + '&' +
       'pageSize=' + page_size + '&' +
       'page=' +  page_number + '&' +
       'apiKey=a1495f8739354ee3af2b3f7748357707'
       )
    print (url)
    response = requests.get(url)
    pprint.pprint (response.json())
def search_publication_in_request (user_request, laguage, page_size, page_number):
    user_request_list = user_request.split(' ')
    user_request_list_text = ''
    for element in  user_request_list:
        user_request_list_text  += 'q=' + element + '&'
    url = ('https://newsapi.org/v2/everything?' +
       user_request_list_text +
       'language=' + laguage + '&' +
       'pageSize=' + page_size + '&' +
       'page=' +  page_number + '&' +
       'apiKey=a1495f8739354ee3af2b3f7748357707'
       )
    print (url)
    response = requests.get(url)
    ansver = response.json()['articles'][0]['title'] + '\n'
    ansver += response.json()['articles'][0]['description']
    ansver += response.json()['articles'][0]['url']
    return ansver

if __name__ == "__main__":
    get_category('science', 'ru', '2', '1')
    get_key_words('Путин', 'ru', '1', '1')
    search_publication_in_request('Путин', 'ru', '1', '1')