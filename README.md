# TecaCrawler
Minhateca.com.br crawler

#Install
<pre>
pip install -r dependencies.txt
</pre>

#Usage
<pre>
#Search for txt files with name senhas
python tecaCr4wl3r.py -U username -P password -t senhas

#Search for images with name foto and file extesion jpg
python tecaCr4wl3r.py -U username -P password -i foto -x jpg

#Scrap user page to grab all open photos and identify nudity photos
python tecaCr4wl3r.py -U username -P password -u usertocrawler
</pre>

#Help
<pre>
           ;               ,
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


Tool to scrap the site minhateca.com.br
usage: tecaCr4wl3r.py [-h] -U USERNAME -P PASSWORD [-u USERQUERY] [-t FILES]
                      [-i IMAGE] [-x EXT]

optional arguments:
  -h, --help            show this help message and exit
  -U USERNAME, --username USERNAME
                        Minhateca username
  -P PASSWORD, --password PASSWORD
                        Minhateca password
  -u USERQUERY, --user USERQUERY
                        Give the username to grab all open photos and identify
                        nudity photos
  -t FILES, --txt FILES
                        Search for txt files
  -i IMAGE, --image IMAGE
                        Search for images
  -x EXT, --image-ext EXT
                        Specify image extension
</pre>

#Disclaimer
<pre>
I am not responsible for the use of this tool
Research pourposes only!
</pre>
