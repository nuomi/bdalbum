#!/usr/bin/env python


import os, sys ,errno
import json
import requests
from StringIO import StringIO
from PIL import Image
#from wgety.wgety import Wgety
#import urllib.request


basedir = 'images/'
#w = Wgety()

def list_gen(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            yield os.path.join(root, f)

def download(j):
    folder = basedir+j['imgs'][0]['title'].replace('/','-')+'/'
    try:
        os.makedirs(folder)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(folder):
            pass
        else: raise

    #print('into folder', folder)
    for img in j['imgs']:
        try:
            url = img['imageUrl']
        except:
            #print('imageUrl not found, skip')
            continue

        name = os.path.basename(url)
        if os.path.exists(folder+name):
            #print 'exist, skip', url
            continue
        try:
            print('downloading '+url)


            #urllib.request.urlretrieve(url, folder+name)

            #w.execute(url=url, filename=folder+name, absolute_link=True)

            #r = requests.get(url, timeout=3)
            #i = Image.open(StringIO(r.content))
            #i.save(folder+name)


            #r = requests.get(url, stream=True)
            #if r.status_code == 200:
            #    with open(folder+name, 'wb') as f:
            #        for chunk in r.iter_content():
            #            f.write(chunk)
        except:
            print ('download error!!!!!!!!!!!!!!')


if __name__ == '__main__':
    for f in list_gen('album_data'):
        try:
            j = json.loads(open(f).read().decode('utf-8'))
        except:
            #print('not json file')
            #print('skip:', f)
            continue

        download(j)

