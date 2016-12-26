import os
import requests
from lxml import html

class minhateca:
    def search(self,busca,ext,results=1000):
        urls = list()
        for x in range(1,results):
            data = {'IsGallery':'False','FileName':busca,'FileType':'all','SizeFrom':0,'SizeTo':0,'Extension':ext,'Search':'Buscar','ShowAdultContent':'True','Page':str(x)}
            url = 'http://minhateca.com.br/action/SearchFiles'
            headers = {'Referer':'http://minhateca.com.br/action/SearchFiles'}
            r = self.session.post(url,data=data)
            tree = html.fromstring(r.content)
            files = tree.xpath('//*[@class="expanderHeader downloadAction"]/@href')
            if not files:
                break
            print '%d Resultados na pagina %d' % (len(files),x)
            for filename in files:
                url = 'http://minhateca.com.br'+filename
                urls.append(url)
        return urls

    def login(self,user,password):
        url = 'http://minhateca.com.br/action/login/login'
        data = {'Login':user,'Password':password,'Field':0}
        session = requests.Session()
        r = session.post(url,data=data)
        self.session = session
        return r.status_code
