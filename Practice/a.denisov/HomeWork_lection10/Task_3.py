import urllib.request

req = urllib.request.Request('http://google.com')
response = urllib.request.urlopen(req)
web_page = response.read()



def url_check(web_page):
    start = 0
    while web_page:
        try:
            url_start = str(web_page).find("://", start)
            url_end = str(web_page).find('"', url_start)
            start = url_end
            finded_url = str(web_page)[url_start:url_end]
            web_url = urllib.request.Request("http"+finded_url, method='HEAD')
            if web_url.unverifiable is True:
                print(f"URL: http{finded_url} is BAD")
            else:
                print(f"URL: http{finded_url} is OK")

        except ValueError:
            break
        except Exception as text:
            print(text)
            pass


url_check(web_page=web_page)
