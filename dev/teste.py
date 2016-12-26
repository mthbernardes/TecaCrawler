import requests
from lxml import html


def nextpage(page):
    print 'Iniciou'

    print page
    if ',' in page:
        last = int(page.split(',')[1])
    else:
        last = 1
    url = 'http://minhateca.com.br%s' % page
    #print url
    r = requests.get(url)
    tree = html.fromstring(r.content)
    next_page = tree.xpath('//*[@id="galleryView"]/div[1]/div/a/@href')
    if next_page and ',' in next_page[-1]:
        number_next = int(next_page[-1].split(',')[1])
        if number_next > last:
            nextpage(next_page[-1])

nextpage('/dany_alania/Galeria/decoracion/casamento/bolo')
