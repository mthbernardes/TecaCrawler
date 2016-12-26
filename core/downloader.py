import os
import requests
from lxml import html

class download:
    def save(self,content,path,filename):
        if not os.path.exists(path):
            os.makedirs(path)
        filename = filename.replace('/','_')
        f = open(os.path.join(path,filename),'wb').write(content)

    def img(self,url,filename):
        #Get url to download
        path = None
        r = requests.post(url)
        tree = html.fromstring(r.content)
        url = tree.xpath('//*[@id="fileDetails"]/div[2]/div[1]/img/@src')
        user = tree.xpath('//*[@id="fileDetails"]/div[3]/div[2]/h2/a/text()')[0]
        if url:
            r = requests.get(url[0],stream=True)
            path = os.path.abspath(os.path.join('output','img',user))
            content = r.raw.read()
            self.save(content,path,filename)
        return path,filename.replace('/','_')

    def txt(self,url,filename):
        try:
            #Get url to download
            r = requests.post(url)
            tree = html.fromstring(r.content)
            url = tree.xpath('//*[@class="thumbnailexpander"]/div/div/iframe/@src')[0]
            user = tree.xpath('//*[@id="fileDetails"]/div[3]/div[2]/h2/a/text()')[0]
            #Use download url to get content
            r = requests.get(url)
            tree = html.fromstring(r.content)
            content = tree.xpath('//*[@id="maincontent"]/div[2]/div[1]/pre/text()')[0].encode('utf-8')
            path = os.path.abspath(os.path.join('output','txt',user))
            self.save(content,path,filename)
        except Exception as e:
            print e
            print 'Nao foi manolo'
