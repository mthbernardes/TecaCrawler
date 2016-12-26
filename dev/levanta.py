import os
import requests
from lxml import html

  def findFiles(subfolder):
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

      if next_page and ',' in next_page[-1]:
          number_next = int(next_page[-1].split(',')[1])
          if number_next > last:
              print next_page[-1]
              findFiles(next_page[-1])

  def findFolders(folder):
      url = 'http://minhateca.com.br%s' % folder
      r = requests.get(url)
      tree = html.fromstring(r.content)
      subfolders = tree.xpath('//*[@id="foldersList"]/table/tr/td/a/@href')
      for subfolder in subfolders:
          print '\t%s' % subfolder
          findFiles(subfolder)
          findFolders(subfolder)

  def user(self,username):
      url = 'http://minhateca.com.br/%s' % username
      r = requests.get(url)
      tree = html.fromstring(r.content)
      folders = tree.xpath('//*[@id="Tc_0"]/td[2]/table/tbody/tr/td[2]/a/@href')
      for folder in folders:
          print 'Principal ==> %s' % folder
          findFolders(folder)

user('dany_alania')
