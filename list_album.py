#!/usr/bin/env python

import os, sys
import json
import requests

def list_gen(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.list'):
                yield os.path.join(root, f)


if __name__ == '__main__':

    for l in list_gen('.'):
        try:
            for img in json.loads(open(l).read())['imgs']:
                try:
                    if img['setId'] != '-1':
                        filename = 'album_data/'+img['setId']+'_'+img['photoId']+'.data.json'
                        requests_url = 'http://image.baidu.com/data/albumimgs?sort=0&from=1&cid='+img['photoId']+'&setid='+img['setId']+'&dressid=-1&pn=0&rn=60'
                        print requests_url
                        #print requests.get(requests_url).json()
                        #break
                        #try:
                        #    with open(filename, 'w') as f:
                        #        f.write(requests.get(requests_url).json().encode('utf-8'))
                        #except:
                        #    print >> sys.stderr, 'request error'
                except:
                    print >> sys.stderr, 'error img'
           
        except:
            print >> sys.stderr, l
