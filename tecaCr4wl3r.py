import sys
import argparse
from core.minhateca import minhateca
from core.downloader import download
from core.capivara import LevantaCapivara


def banner():
    print '''           ;               ,
         ,;                 '.
        ;:                   :;
       ::                     ::
       ::                     ::
       ':                     :
        :.                    :
     ;' ::                   ::  '
    .'  ';                   ;'  '.
   ::    :;                 ;:    ::
   ;      :;.             ,;:     ::
   :;      :;:           ,;"      ::
   ::.      ':;  ..,.;  ;:'     ,.;:
    "'"...   '::,::::: ;:   .;.;""'
        '"""....;:::::;,;.;"""
    .:::.....'"':::::::'",...;::::;.
   ;:' '""'"";.,;:::::;.'""""""  ':;
  ::'         ;::;:::;::..         :;
 ::         ,;:::::::::::;:..       ::
 ;'     ,;;:;::::::::::::::;";..    ':.
::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ;
  ;    ::   :::::::  :::::::   :    ;
   '   ::   ::::::....:::::'  ,:   '
    '  ::    :::::::::::::"   ::
       ::     ':::::::::"'    ::
       ':       """""""'      ::
        ::                   ;:
        ':;                 ;:"
-hrr-     ';              ,;'
            "'           '"
              '

'''
    print 'Tool to scrap the site minhateca.com.br'
parser = argparse.ArgumentParser(description = banner())
parser.add_argument('-U', '--username', action = 'store', dest = 'username',required = True, help = 'Minhateca username')
parser.add_argument('-P', '--password', action = 'store', dest = 'password',required = True, help = 'Minhateca password')
parser.add_argument('-u', '--user', action = 'store', dest = 'userquery',required = False, help = 'Give the username to grab all open photos and identify nudity photos')
parser.add_argument('-t', '--txt', action = 'store', dest = 'files', required = False, help = 'Search for txt files')
parser.add_argument('-i', '--image', action = 'store', dest = 'image',required = False, help = 'Search for images')
parser.add_argument('-x', '--image-ext', action = 'store', dest = 'ext', required = False, help= 'Specify image extension')

args = parser.parse_args()
if args.userquery:
    busca = LevantaCapivara()
    busca.user(args.userquery)

elif args.files:
    #Search txt files
    teca = minhateca()
    save = download()

    teca.login(args.username,args.password)
    urls = teca.search(args.files,'txt')
    for url in urls:
        print url
        save.txt(url,url)

elif args.image:
    teca = minhateca()
    save = download()
    if args.ext:
        #Search imgs
        print 'Searching'
        teca.login(args.username,args.password)
        urls = teca.search(args.image,args.ext)
        for url in urls:
            print url
            #save.img(url,url)
else:
    parser.print_help()
