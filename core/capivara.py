import os
import nude
import requests
from lxml import html
from threading import Thread
from downloader import download

class LevantaCapivara:
    def TaNu(self,path,filename):
        nu = nude.is_nude(os.path.join(path,filename))
        if nu:
            name,ext = os.path.splitext(filename)
            new_name = '[NUDE]'+name+ext
            os.rename(os.path.abspath(os.path.join(path,filename)),os.path.abspath(os.path.join(path,new_name)))

    def findFiles(self,subfolder):
        if ',' in subfolder:
            last = int(subfolder.split(',')[1])
        else:
            last = 1
        url = 'http://minhateca.com.br%s' % subfolder
        r = requests.get(url)
        tree = html.fromstring(r.content)
        files = tree.xpath('//*[@id="galleryView"]/div/ul/li/p/a/@href')
        next_page = tree.xpath('//*[@id="galleryView"]/div[1]/div/a/@href')

        for filename in files:
            print '\t\tArquivo ==> %s' %filename
            if filename.endswith('.jpg'):
                path,filename = self.save.img('http://minhateca.com.br'+filename,filename.replace('/','',1))
                t = Thread(target=self.TaNu, args=(path,filename,))
                t.start()
        if next_page and ',' in next_page[-1]:
            number_next = int(next_page[-1].split(',')[1])
            if number_next > last:
                print next_page[-1]
                self.findFiles(next_page[-1])

    def findFolders(self,folder):
        url = 'http://minhateca.com.br%s' % folder
        r = requests.get(url)
        tree = html.fromstring(r.content)
        subfolders = tree.xpath('//*[@id="foldersList"]/table/tr/td/a/@href')
        for subfolder in subfolders:
            print '\t%s' % subfolder
            self.findFiles(subfolder)
            self.findFolders(subfolder)

    def user(self,username):
        self.save = download()

        self.username = username
        url = 'http://minhateca.com.br/%s' % username
        r = requests.get(url)
        tree = html.fromstring(r.content)
        folders = tree.xpath('//*[@id="Tc_0"]/td[2]/table/tbody/tr/td[2]/a/@href')
        for folder in folders:
            print 'Principal ==> %s' % folder
            self.findFolders(folder)
